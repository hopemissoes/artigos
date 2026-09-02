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
  `setNodeParameter`, sem tocar nas credenciais dos outros nós; depois dele
  `versionId == activeVersionId == 6326fb3b-f118-4d8b-9fff-9ab8c0189d71`.
  ⚠️ **A conclusão tirada daqui — "o `update_workflow` já publica" — está errada**;
  foi coincidência. Ver a correção de premissa na seção da segunda sessão.

- ✅ **Gravação validada.** O `apply: true` pelo conector foi recusado pelo
  classificador de permissões da sessão (trava do cliente, não do motor); o usuário
  executou o sub-workflow direto no n8n e o motor gravou: `statusCode: 200`,
  `modified: 2026-09-02T11:57:27`, revisão guardada pelo WordPress. O endereço do
  PA Cidade Nova está correto no ar e a alteração foi registrada no banco
  (`registrar_atualizacao`, id 46).

**Falta:**

- ~~Publicar os dois workflows.~~ ✅ **Feito pelo usuário em 02-09-2026, 19:12.**
  A versão ativa dos dois já é a nova; **nenhum nó no ar carrega senha.**
  O `publish_workflow` do assistente foi recusado pelo classificador nas duas
  tentativas — publicar é sempre passo manual.
- ~~Rodar os 7 testes de ponta a ponta.~~ ✅ **Feito em 02-09-2026, em sessão
  nova** — o cache de esquema caiu sozinho, como esperado. **Os 7 passaram**
  (o `auditar_links` só depois do conserto abaixo).
  Nenhum teste gravou. Saídas coladas em `docs/MIGRACAO-MCP-WORDPRESS.md`,
  seção 2.
- ~~Corrigir o `auditar_links`.~~ ✅ **Feito, publicado e reconferido em
  02-09-2026.** A rota do site é `/drv/v1/links-audit` (não `audit-links`) e o
  `orderby` de lá é `incoming_links | internal_links | external_links | date`,
  com `order` em maiúsculo. Depois de o usuário publicar
  (`activeVersionId 47b1c6f9-…`), o teste 3 passou: 169 artigos, 5 por página,
  com as três contagens. Nunca foi credencial — o 404 vinha antes da
  autenticação. **Os 7 testes passaram.**
- **Ajuste menor no schema.** O nó `inserir_link_interno` do workflow MCP marca
  `ocorrencia` como obrigatório, embora a descrição diga que só é necessário quando
  a frase aparece mais de uma vez.
- ~~Só depois de publicar e testar revogar a Application Password antiga.~~
  ✅ **Liberado.** Nenhuma das 7 ferramentas usa mais a senha em texto puro; todas
  falam com o site pela credencial `WordPress tabelaplanos` (`dibu11U52rFkfBly`).
  A senha antiga **pode ser revogada** — o `auditar_links` continua quebrado antes
  e depois, por outro motivo. Lembrando que, mesmo revogada, a string segue no
  histórico de versões do n8n.

## Estado em 02-09-2026 (segunda sessão) — migração dos 7

**Feito, no draft dos dois workflows:**

- Motor `WP - Motor de Edicao Pontual` (`825rmKAVo3wmelMi`) estendido de 2 para
  **9 operações**: as antigas `substituir` e `link` mais `buscar`, `listar`,
  `criar`, `conteudo`, `meta_title`, `meta_description` e `auditar_links`.
  Entrou um nó `Rota` que monta a URL do GET; os dois `httpRequest` com a
  credencial do cofre foram **reaproveitados** (URL e corpo por expressão), então
  o vínculo de credencial não foi tocado.
- Os **7 `toolCode` viraram `toolWorkflow`** apontando para o motor. Conferido
  campo a campo: **nenhum nó do draft carrega `password`.**
- Todas as escritas ganharam **dry-run por padrão** — inclusive `criar`,
  `conteudo` e os dois campos de meta, que antes gravavam direto.

**Testado:**

- 23 casos em simulação local (`scripts/motor-wp/harness.js`);
- 4 execuções `test_workflow` com pin data, dentro do n8n, sem tocar no site
  (`28750` listar, `28751` meta_title, `28752` criar, `28753` auditar_links);
- regressão do `substituir` contra o site, na versão ativa (`28745`) — a
  credencial do cofre segue autenticando.

**Não testado:** as 7 ferramentas chamadas de ponta a ponta pelo conector MCP.
Isso depende da publicação. Roteiro de teste, uma a uma, em
`docs/MIGRACAO-MCP-WORDPRESS.md`.

**Correção de premissa importante:** `update_workflow` **não publica sozinho**.
Ele grava draft; o `activeVersionId` não se move. A execução `28745` provou:
rodou sem o nó `Rota`, que só existe no draft. A nota anterior desta página
estava errada — o que houve foi coincidência de `versionId` logo após uma
publicação manual.

**Detalhe completo, tabela de versões, roteiro de publicação e de teste, e uma
anomalia registrada (execução `28747`, gravação no post 39602 que não partiu da
sessão): `docs/MIGRACAO-MCP-WORDPRESS.md`.**

## Regra que fica

Segredo **nunca** dentro de `jsCode`, de arquivo do repositório ou de conversa.
Sempre no cofre de credenciais do n8n, ou como variável de ambiente — referenciado,
nunca copiado.

Corolário aprendido aqui: `@n8n/n8n-nodes-langchain.toolCode` **não tem campo de
credenciais**. Ferramenta de MCP que precise de autenticação tem que ser
`toolWorkflow` chamando um sub-workflow com nós `httpRequest`. Não é preferência
de estilo — é o que separa segredo referenciado de segredo copiado.
