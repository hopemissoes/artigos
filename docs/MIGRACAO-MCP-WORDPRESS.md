# Migração dos 7 `toolCode` → `toolWorkflow` — 02-09-2026

> Este arquivo **não contém segredo nenhum** e nunca deve conter.

## Veredito em uma linha

**Publicado e no ar em 02-09-2026, 19:12.** Os 7 nós viraram `toolWorkflow` e a
versão ativa dos dois workflows não tem mais nenhuma senha em texto puro. Falta
rodar os 7 testes de ponta a ponta pelo conector — e só depois revogar a
Application Password antiga.

## Estado das versões (conferido às 19:16 de 02-09-2026)

| Workflow | ID | `versionId` | `activeVersionId` | Publicado? |
|---|---|---|---|---|
| `WP - Motor de Edicao Pontual` | `825rmKAVo3wmelMi` | `baff3834-6519-456c-a303-ce98b4360781` | igual | ✅ |
| `MCP - WordPress DRV (Tabela Planos) v3` | `7RwMenlhtJfVvl71` | `860d9c9c-e248-4d15-a5e7-853ba3cd9d03` | igual | ✅ |

Quem publicou foi o usuário, pela interface. O `publish_workflow` do assistente
foi recusado pelo classificador de permissões nas duas tentativas — **essa
capacidade não existe pelo caminho do assistente; conte com o passo manual.**

### Armadilha do Save x Publish

Na primeira tentativa o usuário clicou em **Save** e o `activeVersionId` não se
moveu. Salvar grava o rascunho; publicar é botão separado. Como conferir sem
depender de ninguém: `get_workflow_details` e comparar `versionId` com
`activeVersionId`.

### O que estava em cada versão do workflow MCP (histórico do problema)

| Nó | No draft | No ar hoje |
|---|---|---|
| `substituir_no_artigo` | `toolWorkflow` | `toolWorkflow` |
| `inserir_link_interno` | `toolWorkflow` | `toolWorkflow` |
| `buscar_artigo` | `toolWorkflow` | `toolCode` — **senha em claro** |
| `criar_artigo` | `toolWorkflow` | `toolCode` — **senha em claro** |
| `editar_conteudo_artigo` | `toolWorkflow` | `toolCode` — **senha em claro** |
| `editar_meta_title` | `toolWorkflow` | `toolCode` — **senha em claro** |
| `editar_meta_description` | `toolWorkflow` | `toolCode` — **senha em claro** |
| `auditar_links` | `toolWorkflow` | `toolCode` — **senha em claro** |
| `listar_artigos` | `toolWorkflow` | `toolCode` — **senha em claro** |

Nenhum nó do draft carrega `password`. Todos apontam para `825rmKAVo3wmelMi`.

## Correção de premissa: `update_workflow` NÃO publica

A nota herdada da sessão anterior dizia que `update_workflow` já publica sozinho.
**Não publica.** Ele grava um *draft*; o `activeVersionId` não se move.

Prova: depois de atualizar o motor, a execução `28745` (dry-run de `substituir`
pelo conector) rodou **sem o nó `Rota`** — `runData` de `Rota` veio vazio. O MCP
serve a `activeVersion`, não o draft.

O que confundiu na sessão anterior: naquele caso a única mudança foi o
`singleValue: true` no IF, e o `versionId` **coincidiu** com o `activeVersionId`
porque o workflow tinha acabado de ser publicado à mão. Coincidência, não regra.

**Consequência prática:** toda alteração precisa de um `publish` explícito. E
`publish_workflow` é recusado pelo classificador de permissões — quem publica é
o usuário, pela interface do n8n.

## O desenho novo do motor

Um nó `Rota` (Code) entrou entre `Parametros` e `Buscar Post`. Ele calcula a URL
do GET conforme a `operacao`. Os dois nós `httpRequest` — os únicos que têm a
credencial `WordPress tabelaplanos` (`dibu11U52rFkfBly`) — **foram reaproveitados**
com URL e corpo por expressão, em vez de criar nós novos. Foi de propósito:
credencial anexada à mão pela interface é cara de refazer, e `setNodeParameter`
não a toca.

```
Parametros → Rota → Buscar Post → Conferir e Montar → Gravar de Verdade?
                                                       ├─ true  → Salvar Post → Resultado Gravado
                                                       └─ false → Resultado Sem Gravar
```

- `Buscar Post`.url  → `={{ $json.urlBusca }}`   (montada pelo `Rota`)
- `Salvar Post`.url  → `={{ $json.urlSalvar }}`  (montada pelo `Conferir e Montar`)
- `Salvar Post`.jsonBody → `={{ $json.corpoSalvar }}`

O `Parametros` passou de 9 para 22 campos. Os 9 antigos ficaram na mesma ordem,
então os dois `toolWorkflow` que já funcionavam continuam válidos.

### As 9 operações

| `operacao` | Ferramenta MCP | GET que o `Rota` monta | Escreve? |
|---|---|---|---|
| `buscar` | `buscar_artigo` | `/posts/{id}?context=edit` | não |
| `listar` | `listar_artigos` | `/posts?per_page&orderby&order&search&context=edit` | não |
| `auditar_links` | `auditar_links` | `/drv/v1/audit-links?orderby&order&per_page` | não |
| `criar` | `criar_artigo` | `/posts?slug=…&status=any` (checa duplicata) | POST `/posts` |
| `meta_title` | `editar_meta_title` | `/posts/{id}?context=edit` | POST `/posts/{id}` |
| `meta_description` | `editar_meta_description` | idem | idem |
| `conteudo` | `editar_conteudo_artigo` | idem | idem |
| `substituir` | `substituir_no_artigo` | idem | idem |
| `link` | `inserir_link_interno` | idem | idem |

### Travas que ganharam de brinde

Tudo o que era `toolCode` gravava direto, sem simulação. Agora:

- **Dry-run por padrão em todas as escritas.** `criar`, `conteudo`, `meta_title`
  e `meta_description` também. Sem `apply: true`, devolvem o que fariam.
- **`meta_title` / `meta_description`** mostram `valorAtual` → `valorNovo` e
  recusam quando o campo já tem exatamente aquele valor.
- **`criar`** recusa se já existir artigo com o mesmo slug (ou, sem slug, com o
  mesmo título) e devolve o id do existente.
- **`conteudo`** diz no `resumoAcao` quantos caracteres entram e quantos saem, e
  manda usar `substituir` para trecho.
- **Envelope uniforme.** Toda ferramenta devolve `ok`, `gravado`, `erro`,
  `aviso`, `resumoAcao`. As antigas devolviam frase solta ("Meta title
  atualizado para: X") sem dizer se deu certo.

O `buscar_artigo` continua devolvendo o corpo HTML inteiro (paridade com o
comportamento antigo), e agora também `tamanhoConteudo`.

## O que foi testado, e como

Nada foi testado contra o site pelo caminho normal, porque o draft não está no ar.
Duas camadas de teste substituíram isso:

### 1. Simulação local — `scripts/motor-wp/harness.js`

Roda os 4 arquivos JS do motor fora do n8n, com fixtures. 23 casos:

```
node scripts/motor-wp/harness.js
```

Cobre: as 9 operações, contagem divergente, duplicata de slug, meta já igual,
link ambíguo, link já apontado, operação desconhecida, HTTP 404 e resposta sem
`content.raw`.

### 2. `test_workflow` com pin data — no motor de execução do n8n

Exercita o draft de verdade (expressões, roteamento do IF, `$fromAI` não), com os
`httpRequest` pinados, então **nada sai para o site**.

| Execução | Caso | Resultado |
|---|---|---|
| `28750` | `listar` | `Rota` montou `…/posts?per_page=2&orderby=modified&order=desc&context=edit&search=manaus`; envelope de leitura correto |
| `28751` | `meta_title` com `apply: true` | `urlSalvar` `…/posts/39602`, `corpoSalvar` `{"meta":{"rank_math_title":"…"}}`, IF roteou para `Salvar Post`, `gravado: true` |
| `28752` | `criar` com `apply: true` | `urlSalvar` `…/posts` (sem id), corpo com `meta` e `categories:[3,7]`, HTTP 201 tratado, `postId` lido da resposta |
| `28753` | `auditar_links` | `Rota` montou o endpoint `drv/v1`, envelope de leitura correto |

### 3. Cache de esquema do cliente — o que barrou o teste final

Depois da publicação, a sessão que fez a migração **continuou com o esquema
antigo das 7 ferramentas em cache** (`input` como texto único). O servidor já
respondia com o nó novo e recusou a chamada:

```
Received tool input did not match expected schema
  Required -> at busca, order, orderby, per_page
```

Depois, mandando os campos soltos, o cache converteu o numero em texto:

```
Expected number, received string -> at per_page
```

**Essa recusa é, em si, a prova de que o nó novo está no ar** — o `toolCode`
antigo aceitava qualquer coisa dentro de `input` e nunca exigiria quatro campos
tipados.

Não há contorno pelo lado do cliente: o cache cai sozinho em **conversa nova**.
Os 7 testes ficam para a primeira sessão nova.

### 4. Regressão contra o site (na versão que estava no ar antes de publicar)

Execução `28745`: `substituir_no_artigo` em dry-run no post 33477 achou 1
ocorrência de `Av. Camapuã, 695`, `tamanhoAntes: 115185`. A credencial do cofre
segue autenticando (só ela devolve `content.raw` com `context=edit`).

**O que NÃO foi testado:** as 7 ferramentas novas chamadas pelo conector MCP de
ponta a ponta, porque isso exige a publicação. O mapeamento `$fromAI → Parametros`
é o único trecho não exercitado, e é mecanicamente idêntico ao dos dois
`toolWorkflow` que já funcionam.

## O que falta — na ordem

### 1. Publicar os dois workflows — ✅ FEITO em 02-09-2026, 19:12

Reverter, se preciso: histórico de versões do n8n, voltar para
`6326fb3b-…` (motor) e `1e50dc0d-…` (MCP).

### 2. Testar as 7, uma a uma — PENDENTE, exige conversa nova

Por causa do cache de esquema descrito acima. Ordem do menos para o mais
destrutivo; só passar para a seguinte depois que a anterior devolver `ok: true`.

Ordem do menos para o mais destrutivo. Só passar para a seguinte depois que a
anterior devolver `ok: true`.

| # | Ferramenta | Chamada de teste | Esperado |
|---|---|---|---|
| 1 | `listar_artigos` | `{"per_page":3,"orderby":"modified","order":"desc","busca":""}` | lista **com campo `slug`** (é o que distingue do nó antigo) e `aviso: "Leitura: nada foi alterado no site."` |
| 2 | `buscar_artigo` | `{"id":33477}` | `dados.tamanhoConteudo` ≈ 115185, `dados.rank_math_title` preenchido |
| 3 | `auditar_links` | `{"orderby":"internal_in","order":"asc","per_page":5}` | 5 itens com as três contagens |
| 4 | `editar_meta_title` | `{"id":33477,"valor":"<o mesmo que já está lá>","apply":false}` | `erro: "o campo rank_math_title ja tem exatamente esse valor…"` — prova que leu o valor real |
| 5 | `editar_meta_description` | mesma ideia | idem |
| 6 | `criar_artigo` | `{"titulo":"Teste","conteudo":"<p>x</p>","slug":"plano-hapvida-manaus","apply":false}` | `erro: "ja existe artigo com esse slug: id 33477…"` — prova a trava de duplicata |
| 7 | `editar_conteudo_artigo` | `{"id":33477,"conteudo":"<p>x</p>","apply":false}` | `resumoAcao: "SOBRESCREVER o corpo inteiro: 115185 -> 8 caracteres…"`, `gravado: false` |

Nenhum desses sete testes grava. Todos são dry-run ou leitura.

Se o conector não mostrar os parâmetros novos (`valor`, `busca`, `per_page`…),
é cache do cliente: fechar e reabrir a sessão. Já aconteceu antes e caiu sozinho.

### 3. Só então revogar a Application Password antiga

Ela continua válida e continua em texto puro na versão **ativa** do workflow MCP.
Revogar antes de publicar derruba as 7 ferramentas na hora.

Depois de revogar, a versão antiga do workflow ainda guarda a string no histórico
de versões do n8n. Vale conferir se o n8n permite limpar versões antigas; se não
permitir, a string fica no histórico mesmo revogada — inofensiva, mas presente.

## Pendência menor que continua aberta

O nó `inserir_link_interno` marca `ocorrencia` como obrigatório no schema, embora
a descrição diga que só é necessário quando a frase aparece mais de uma vez. O
n8n deriva o `required` de quais parâmetros usam `$fromAI`, então tirar a
obrigatoriedade exige mudar o desenho do nó. Não foi mexido nesta sessão.

## Anomalia registrada — execução `28747`

Às 15:13:24 UTC de 02-09-2026 o motor executou, vindo do workflow MCP:

```
operacao: substituir, id: 39602, apply: true
find: <a href="https://tabelaplanos.com.br/">Hospital Nilton Lins (Manaus)</a>
repl: <a href="https://tabelaplanos.com.br/hospital-nilton-lins-hapvida-manaus/">Hospital Nilton Lins</a>
```

**Essa chamada não partiu desta sessão.** Terminou em `Resultado Gravado`, ou
seja, **gravou no post 39602** (o `modified` do post bate: `2026-09-02T12:13:26`,
mesmo instante em UTC-3).

O conteúdo é um conserto legítimo de link quebrado, não vandalismo. A explicação
provável é outra sessão ou automação usando o mesmo conector ao mesmo tempo.
**Vale o usuário confirmar que foi ele.** Se não foi, é preciso descobrir quem
tem acesso ao endpoint MCP `wordpress-drv` — que hoje não pede autenticação
própria.
