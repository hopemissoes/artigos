# Migração dos 7 `toolCode` → `toolWorkflow` — 02-09-2026

> Este arquivo **não contém segredo nenhum** e nunca deve conter.

## Veredito em uma linha

**Publicado, testado e no ar em 02-09-2026.** Os 7 nós viraram `toolWorkflow` e a
versão ativa dos dois workflows não tem mais nenhuma senha em texto puro. Os 7
testes de ponta a ponta pelo conector foram rodados: **6 passaram; só o
`auditar_links` falhou**, por URL e enum errados no nó `Rota` — defeito de rota,
não de credencial. **A Application Password antiga já pode ser revogada**; o
`auditar_links` está quebrado do mesmo jeito antes e depois disso.

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

### 2. Testar as 7, uma a uma — ✅ RODADO em 02-09-2026, sessão nova — **6 de 7 passaram**

O cache de esquema caiu sozinho, como previsto: em conversa nova as 7 ferramentas
chegaram na forma nova (campos soltos e tipados, `slug` no `listar_artigos`,
envelope `ok`/`gravado`/`aviso`). Nenhum teste gravou — todos leitura ou
`apply: false`.

| # | Ferramenta | Resultado | O que provou |
|---|---|---|---|
| 1 | `listar_artigos` | ✅ passou | 3 itens **com `slug`**, `total: 3`, `aviso` de leitura |
| 2 | `buscar_artigo` | ✅ passou | `tamanhoConteudo: 115185`, metas do Rank Math preenchidas |
| 3 | `auditar_links` | ❌ **falhou** | HTTP 404 `rest_no_route` — o motor monta a URL errada (ver diagnóstico) |
| 4 | `editar_meta_title` | ✅ passou | recusou por valor idêntico, lendo o valor real do site |
| 5 | `editar_meta_description` | ✅ passou | idem |
| 6 | `criar_artigo` | ✅ passou | trava de duplicata de slug; nada criado |
| 7 | `editar_conteudo_artigo` | ✅ passou | `gravado: false`, `115185 -> 8 caracteres` |

#### Teste 1 — `listar_artigos` `{"per_page":3,"orderby":"modified","order":"desc","busca":""}`

```json
{
  "gravado": false, "ok": true, "erro": null, "operacao": "listar",
  "dados": [
    {"id": 39602, "titulo": "Hapclínica Duque de Caxias (Manaus): endereço, horário e como marcar consulta",
     "slug": "hapclinica-duque-de-caxias-manaus",
     "link": "https://tabelaplanos.com.br/hapclinica-duque-de-caxias-manaus/",
     "status": "publish", "data": "2026-09-02T10:21:08", "modificado": "2026-09-02T12:13:26"},
    {"id": 33477, "titulo": "Plano Hapvida Manaus [ano_atual]: Preços, Rede Própria e Pediatria 24h",
     "slug": "plano-hapvida-manaus",
     "link": "https://tabelaplanos.com.br/plano-hapvida-manaus/",
     "status": "publish", "data": "2025-12-24T15:39:20", "modificado": "2026-09-02T11:57:27"},
    {"id": 39474, "titulo": "Hospital Nilton Lins Hapvida Manaus: Guia Completo [ano_atual]",
     "slug": "hospital-nilton-lins-hapvida-manaus",
     "link": "https://tabelaplanos.com.br/hospital-nilton-lins-hapvida-manaus/",
     "status": "publish", "data": "2026-08-26T11:39:00", "modificado": "2026-09-02T10:40:18"}
  ],
  "total": 3,
  "aviso": "Leitura: nada foi alterado no site."
}
```

#### Teste 2 — `buscar_artigo` `{"id":33477}`

Envelope (o `conteudo`, de 115.185 caracteres, foi omitido aqui):

```json
{
  "gravado": false, "ok": true, "erro": null,
  "postId": 33477, "slug": "plano-hapvida-manaus", "operacao": "buscar",
  "aviso": "Leitura: nada foi alterado no site.",
  "dados": {
    "id": 33477,
    "titulo": "Plano Hapvida Manaus [ano_atual]: Preços, Rede Própria e Pediatria 24h",
    "slug": "plano-hapvida-manaus",
    "link": "https://tabelaplanos.com.br/plano-hapvida-manaus/",
    "status": "publish",
    "data": "2025-12-24T15:39:20", "modificado": "2026-09-02T11:57:27",
    "rank_math_title": "Plano Hapvida Manaus Promoção [ano_atual]: a partir de [manaus_menorvalor]",
    "rank_math_description": "Plano Hapvida em Manaus a partir de [manaus_menorvalor]. Consulte a tabela de preços [ano_atual], rede credenciada, carências e tipos de planos. Cotação grátis!",
    "tamanhoConteudo": 115185,
    "conteudo": "<115185 caracteres>"
  }
}
```

`content.raw` com `context=edit` só volta autenticado — **a credencial do cofre
está funcionando pelo caminho do conector.**

#### Teste 3 — `auditar_links` `{"orderby":"internal_in","order":"asc","per_page":5}` — ❌ FALHOU

```json
{
  "gravado": false, "ok": false,
  "erro": "HTTP 404 ao consultar https://tabelaplanos.com.br/wp-json/drv/v1/audit-links?orderby=internal_in&order=asc&per_page=5",
  "detalhe": "{\"code\":\"rest_no_route\",\"message\":\"Nenhuma rota foi encontrada que corresponde com o URL e o método de requisição.\",\"data\":{\"status\":404}}",
  "aviso": "Nada foi alterado."
}
```

**Diagnóstico — é o motor, não o site, e não é a credencial.** O namespace
`drv/v1` existe e responde. A rota real tem o nome **invertido** e outro enum de
ordenação. Conferido em `GET https://tabelaplanos.com.br/wp-json/drv/v1`:

| | O que o nó `Rota` monta | O que o site expõe |
|---|---|---|
| Rota | `/drv/v1/audit-links` | **`/drv/v1/links-audit`** |
| `orderby` | `internal_in`, `internal_out`, `external_out` | **`internal_links`, `incoming_links`, `external_links`, `date`** |
| `order` | `asc` / `desc` | **`ASC` / `DESC`** (enum, maiúsculo) |

O site aceita ainda `post_type`, `page`, `category`, `internal_links_max` e
`incoming_links_max`. O 404 vem antes da checagem de autenticação, então esse
teste não diz nada sobre credencial — e os outros seis já provaram que ela
autentica.

**Conserto — feito no draft em 02-09-2026, falta publicar.**

- Nó `Rota` do motor `825rmKAVo3wmelMi`: a URL passou a ser
  `/wp-json/drv/v1/links-audit`; `order` sai em maiúsculo; e entrou um mapa que
  traduz o vocabulário antigo para o do site, aceitando os dois:
  `internal_in → incoming_links`, `internal_out → internal_links`,
  `external_out → external_links`, `date → date`. Valor desconhecido cai em
  `incoming_links`. Mesmo código em `scripts/motor-wp/rota.js`.
- Nó `auditar_links` do workflow MCP `7RwMenlhtJfVvl71`: a descrição e o
  `$fromAI` do `orderby` passaram a nomear os valores do site.

Validado em duas camadas, sem tocar no site:

- `node scripts/motor-wp/harness.js` — o caso `auditar_links` monta
  `…/drv/v1/links-audit?orderby=incoming_links&order=ASC&per_page=3`;
- execução **`28914`** (`test_workflow` com pin data, no draft do motor):
  entrada `orderby: internal_in, order: asc, per_page: 5` →
  `urlBusca: https://tabelaplanos.com.br/wp-json/drv/v1/links-audit?orderby=incoming_links&order=ASC&per_page=5`,
  envelope de leitura correto, `aviso: "Leitura: nada foi alterado no site."`

**Falta o passo manual:** publicar os dois workflows pela interface do n8n
(`update_workflow` só grava draft; `publish_workflow` é recusado pelo
classificador). Depois disso, re-rodar o teste 3.

Os campos de saída passam a ser os do site — `incoming_links`, `internal_links`
e `external_links` —, não os `internal_in`/`internal_out`/`external_out` que esta
página previa; a expectativa do roteiro é que estava errada, não o site.

#### Teste 4 — `editar_meta_title` com o valor atual, `apply: false`

```json
{
  "gravado": false, "ok": false,
  "erro": "o campo rank_math_title ja tem exatamente esse valor. Nada a fazer.",
  "postId": 33477, "slug": "plano-hapvida-manaus", "campo": "rank_math_title",
  "valorAtual": "Plano Hapvida Manaus Promoção [ano_atual]: a partir de [manaus_menorvalor]",
  "aviso": "Nada foi alterado."
}
```

#### Teste 5 — `editar_meta_description` com o valor atual, `apply: false`

```json
{
  "gravado": false, "ok": false,
  "erro": "o campo rank_math_description ja tem exatamente esse valor. Nada a fazer.",
  "postId": 33477, "slug": "plano-hapvida-manaus", "campo": "rank_math_description",
  "valorAtual": "Plano Hapvida em Manaus a partir de [manaus_menorvalor]. Consulte a tabela de preços [ano_atual], rede credenciada, carências e tipos de planos. Cotação grátis!",
  "aviso": "Nada foi alterado."
}
```

#### Teste 6 — `criar_artigo` com slug existente, `apply: false`

```json
{
  "gravado": false, "ok": false,
  "erro": "ja existe artigo com esse slug: id 33477 (status publish). Nada foi criado.",
  "dados": [
    {"id": 33477, "slug": "plano-hapvida-manaus", "status": "publish",
     "link": "https://tabelaplanos.com.br/plano-hapvida-manaus/"}
  ],
  "aviso": "Nada foi alterado."
}
```

#### Teste 7 — `editar_conteudo_artigo` `{"id":33477,"conteudo":"<p>x</p>","apply":false}`

```json
{
  "gravado": false, "ok": true, "erro": null,
  "postId": 33477, "slug": "plano-hapvida-manaus", "operacao": "conteudo",
  "resumoAcao": "SOBRESCREVER o corpo inteiro: 115185 -> 8 caracteres. Para trocar um trecho, use substituir.",
  "tamanhoAntes": 115185, "tamanhoDepois": 8,
  "aviso": "SIMULACAO: nada foi gravado. Reenvie com apply true para valer."
}
```

A trava mais importante da migração está de pé: a ferramenta que antes gravava
direto agora simula por padrão e diz, em caracteres, o tamanho do estrago.

### 3. Revogar a Application Password antiga — LIBERADO em 02-09-2026

Nenhuma das 7 ferramentas usa mais a senha em texto puro: todas passaram a
`toolWorkflow` e falam com o site pela credencial do cofre
(`WordPress tabelaplanos`, `dibu11U52rFkfBly`). Os testes 2, 4, 5, 6 e 7 leram
`content.raw` com `context=edit`, o que só sai autenticado — prova de que a
credencial do cofre está no caminho. **Pode revogar.** A falha do `auditar_links`
é de URL, não de autenticação, e independe da revogação.

Contexto de por que a ordem era esta:
Revogar antes de publicar derruba as 7 ferramentas na hora.

Depois de revogar, a versão antiga do workflow ainda guarda a string no histórico
de versões do n8n. Vale conferir se o n8n permite limpar versões antigas; se não
permitir, a string fica no histórico mesmo revogada — inofensiva, mas presente.

## Pendências menores que continuam abertas

**1. `auditar_links` chama uma rota que não existe.** Detalhe e correção no
diagnóstico do teste 3, acima. É a única das 9 operações do motor que não
funciona.

**2.** O nó `inserir_link_interno` marca `ocorrencia` como obrigatório no schema, embora
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
