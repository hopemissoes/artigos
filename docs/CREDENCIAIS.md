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

## Regra que fica

Segredo **nunca** dentro de `jsCode`, de arquivo do repositório ou de conversa.
Sempre no cofre de credenciais do n8n, ou como variável de ambiente — referenciado,
nunca copiado.
