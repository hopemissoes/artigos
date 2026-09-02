# Credenciais — achado de 02-09-2026 e como consertar

> Este arquivo **não contém segredo nenhum** e nunca deve conter.

## O que foi encontrado

Ao habilitar o acesso MCP no workflow **`MCP - WordPress DRV (Tabela Planos) v3`**
(`7RwMenlhtJfVvl71`) para acrescentar ferramentas de edição pontual, ficou visível
que a **Application Password do WordPress está escrita em texto puro nos 7 nós**
do workflow:

```
auth: { username: 'hopemissoes', password: '<em claro no jsCode>' }
```

Nós afetados: `buscar_artigo`, `criar_artigo`, `editar_conteudo_artigo`,
`editar_meta_title`, `editar_meta_description`, `auditar_links`, `listar_artigos`.

O workflow **não usa o cofre de credenciais do n8n** — por isso a lista de
credenciais não tinha nenhuma do tipo `wordpressApi`, só duas `httpBasicAuth`
que pertencem a outra coisa.

### Por que importa

- Qualquer leitor do workflow (pessoa ou integração com escopo `workflow:read`)
  lê a senha. Foi assim que ela entrou na transcrição da sessão de 02-09-2026.
- É a chave do site inteiro: permite criar, editar e despublicar qualquer post
  de `tabelaplanos.com.br` pela REST API, de qualquer lugar.

### Por que estava assim

Não foi descuido. O tipo de nó usado, `@n8n/n8n-nodes-langchain.toolCode`
(Code Tool), **não expõe campo de credenciais** — confirmado na definição de
tipo. Escrever inline era o único caminho naquele desenho.

## Como consertar — ordem que não deixa o site sem automação

A ordem importa: revogar primeiro quebraria as 7 ferramentas na hora. A revogação
é o **último** passo.

1. **Criar** uma Application Password nova no WordPress
   (Usuários → Perfil do `hopemissoes` → Senhas de aplicativo).
   **Não revogar a antiga ainda.**
2. **Guardar no n8n**, sem passar por ninguém:
   - Credentials → New → **Basic Auth** → usuário `hopemissoes` + a senha nova; e/ou
   - Variables → `WP_APP_PASSWORD` e `WP_USER`.
3. **Não colar a senha em conversa com o assistente.** O desenho novo existe
   justamente para que ela nunca precise ser vista — o assistente referencia a
   credencial pelo ID, que ele descobre sozinho com `list_credentials`.
4. **Migrar o workflow.** Como `toolCode` não aceita credencial, há dois caminhos:
   - **`$vars`** — trocar a string literal por `$vars.WP_APP_PASSWORD` nos 7 nós.
     Mudança mínima, baixo risco. Depende de o Code Tool avaliar `$vars` e de o
     plano do n8n ter Variables. **Testar primeiro.**
   - **`toolWorkflow` + sub-workflow** — as ferramentas passam a chamar um
     sub-workflow com nós `httpRequest`, que **têm** campo de credenciais.
     É o mecanismo próprio do n8n; custa uma reescrita maior.
5. **Testar** as 7 ferramentas migradas + as 2 novas.
6. **Só então revogar** a Application Password antiga no WordPress.

## Ferramentas a acrescentar na mesma edição

Motivo original da mexida: a `editar_conteudo_artigo` sobrescreve o corpo inteiro
do post, o que inviabiliza corrigir 3 caracteres numa página de 300 mil e
inviabiliza automatizar linkagem interna.

- `substituir_no_artigo(id, find, repl, esperado, apply)`
- `inserir_link_interno(id, frase, destino, apply)`

Travas já escritas e testadas em `scripts/wp.py` (ver `docs/EDICAO-WORDPRESS.md`),
a portar para os nós novos: dry-run por padrão, guarda de contagem, máscara de
texto seguro, recusa de `<a>` aninhado, um link por destino.

## Estado em 02-09-2026

**Feito:**

- Credencial `WordPress tabelaplanos` (`dibu11U52rFkfBly`, tipo `httpBasicAuth`)
  criada no cofre do n8n. O valor **nunca passou pelo assistente** — ele só
  descobriu o nome e o ID via `list_credentials`.
- Criado o sub-workflow **`WP - Motor de Edicao Pontual`** (`825rmKAVo3wmelMi`),
  com nós `httpRequest` — os únicos que aceitam credencial do cofre. Toda a
  lógica das travas mora nele; ele é o único lugar que fala com o WordPress.
- Acrescentadas duas ferramentas ao `MCP - WordPress DRV (Tabela Planos) v3`,
  como `toolWorkflow` (não `toolCode`), apontando para o motor:
  `substituir_no_artigo` e `inserir_link_interno`. **Sem segredo nelas.**
- Workflow MCP publicado.

**Confirmado no teste de 02-09-2026 (sessão seguinte):**

- ✅ **A credencial ficou anexada.** O motor leu `content.raw` do post 33477 com
  `context=edit` — o que só a credencial válida permite. A leitura via API não
  mostrar o campo `credentials` era redação, não ausência. A mensagem *"a resposta
  nao trouxe content.raw"* nunca apareceu.
- ✅ **As duas ferramentas apareceram** na lista do conector. O cache era mesmo do
  lado do cliente.
- ✅ **Três das travas foram exercitadas contra dados reais e passaram**: dry-run
  por padrão, guarda de contagem e um-link-por-destino. Saídas coladas em
  `docs/EDICAO-WORDPRESS.md`.
- ✅ **Bug encontrado e corrigido.** O nó IF `Gravar de Verdade?` usava operadores
  booleanos unários sem `singleValue: true`, então o n8n validava o `rightValue`
  vazio contra tipo boolean em modo `strict` e abortava **toda** chamada — dry-run
  inclusive. As duas ferramentas estavam inoperantes. Corrigido via
  `setNodeParameter`, sem tocar nas credenciais dos outros nós; o `update_workflow`
  já publicou (`versionId == activeVersionId == 6326fb3b-f118-4d8b-9fff-9ab8c0189d71`).

- ✅ **Gravação validada.** O `apply: true` pelo conector foi recusado pelo
  classificador de permissões da sessão (trava do cliente, não do motor); o usuário
  executou o sub-workflow direto no n8n e o motor gravou: `statusCode: 200`,
  `modified: 2026-09-02T11:57:27`, revisão guardada pelo WordPress. O endereço do
  PA Cidade Nova está correto no ar e a alteração foi registrada no banco
  (`registrar_atualizacao`, id 46).

**Falta:**

- **Ajuste menor no schema.** O nó `inserir_link_interno` do workflow MCP marca
  `ocorrencia` como obrigatório, embora a descrição diga que só é necessário quando
  a frase aparece mais de uma vez.
- Migrar os 7 `toolCode` antigos, que **continuam com a senha em texto puro**.
- **Só depois disso** revogar a Application Password antiga no WordPress.

### Ordem para a migração dos 7

O motor já aceita `operacao`; basta acrescentar os casos (`buscar`, `listar`,
`criar`, `meta_title`, `meta_description`, `auditar_links`) e trocar cada
`toolCode` por um `toolWorkflow`. Um nó por vez, testando, para não derrubar o
que funciona hoje.

## Regra que fica

Segredo **nunca** dentro de `jsCode`, de arquivo do repositório ou de conversa.
Sempre no cofre de credenciais do n8n, ou como variável de ambiente — referenciado,
nunca copiado.

Corolário aprendido aqui: `@n8n/n8n-nodes-langchain.toolCode` **não tem campo de
credenciais**. Ferramenta de MCP que precise de autenticação tem que ser
`toolWorkflow` chamando um sub-workflow com nós `httpRequest`. Não é preferência
de estilo — é o que separa segredo referenciado de segredo copiado.
