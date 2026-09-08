# FASE P0 — diagnóstico do pillar `plano-de-saude-hapvida-infantil`

Rodada em 2026-09-08. Arquétipo P1-P9 (`references/artigo-pillar-produto.md`).
Obrigatória antes da FASE 0 porque o pillar **já existe** (WP id 12185, publicado
26/09/2024, modificado 07/09/2026; banco id 57, tipo `pillar_produto`).

---

## Coleta 1 — A página rende? (GSC, 11/08 a 07/09/2026, 28 dias)

Propriedade `sc-domain:tabelaplanos.com.br`, `gsc_queries_for_page`.

| Consulta | Cliques | Impressões | CTR | Posição |
|---|---|---|---|---|
| valor do plano da hapvida infantil | 8 | 323 | 2,48% | 2,76 |
| hapvida infantil | 6 | 182 | 3,30% | 4,01 |
| **plano de saúde infantil valores** | **4** | **481** | **0,83%** | **5,57** |
| hapvida criança | 3 | 31 | 9,68% | 3,16 |
| plano de saúde infantil individual preço | 3 | 174 | 1,72% | 4,55 |
| **plano de saúde infantil barato** | **1** | **108** | **0,93%** | **6,56** |
| plano hapvida infantil | 2 | 46 | 4,35% | 3,80 |

**Leitura:** nas consultas **de marca** o CTR é saudável (3-10%) e a posição é 2-4.
Nas consultas **genéricas de maior volume** — "plano de saúde infantil valores"
(481 impressões) e "plano de saúde infantil barato" (108) — o CTR fica abaixo de 1%
com posição 5,5-6,5. É o padrão "quase lá" da Fase 5: posição 5-15 com impressão alta.
Não é CTR 0% com impressão alta, então **não é o caso puro de title/meta**.

## Coleta 2 — Quem ranqueia pela keyword-alvo? (DataForSeo `serp_local`, Brasil, celular)

**"plano hapvida infantil"** (depth 20, 08/09/2026 10h01 UTC):

| Pos. orgânica | Domínio / URL |
|---|---|
| 1 | www2.hapvida.com.br/planos-de-saude-individuais |
| **2** | **tabelaplanos.com.br/plano-de-saude-hapvida-infantil/** |
| 3 | www2.hapvida.com.br/seja-cliente |
| 4 | tabelasaude.com |
| 5 | joov.com.br |
| 14 | tabelaplanos.com.br/hapvida-rede-pediatrica/ |

**"valor do plano da hapvida infantil"** (depth 10, 08/09/2026 10h48 UTC):

| Pos. orgânica | Domínio / URL |
|---|---|
| 1 | www2.hapvida.com.br/planos-de-saude-individuais |
| **2** | **tabelaplanos.com.br/plano-de-saude-hapvida-infantil/** |
| 3 | tabelasaude.com |
| 4 | blog.facaseuplanodesaude.com.br |
| 5 | joov.com.br |
| **9** | **tabelaplanos.com.br/tabela-de-preco-hapvida/** |

**A home NÃO aparece em nenhuma das duas** — não há a canibalização clássica que o
P0 procura. Há **duas URLs próprias na mesma SERP** em "valor do plano da hapvida
infantil" (pos. 2 e 9): canibalização parcial entre o pillar infantil e o pillar de
tabela de preços. Como a distância é de 7 posições e a intenção do #9 é a tabela
nacional, é **atenção, não bloqueio** — vigiar na Fase 5.

**Achado que mudou a decisão — a página é FONTE do AI Overview.** Na SERP de "valor do
plano da hapvida infantil" o AI Overview cita, nominalmente:
`tabelaplanos.com.br/plano-de-saude-hapvida-infantil/` (referência 1),
`tabelaplanos.com.br/tabela-de-preco-hapvida/` e `joov.com.br`. O texto da IA repete o
enquadramento da página ("a partir de R$ 56,94 em opções empresariais com
coparticipação"; "empresariais via CNPJ ou MEI a partir de 2 vidas, ~30% mais baratos").
Ou seja: a passagem de preço da página **já é a resposta do topo do Google**.

## Coleta 3 — Autoridade interna (`consultar_links_para_destino`)

**8 artigos linkam para a página**, de 8 origens distintas:

`hospital-octaviano-neves-hapvida` (HS2 P3) · `plano-de-saude-para-recem-nascido`
(comparativo) · `plano-hapvida-bauru` (FAQ #9) · `plano-hapvida-londrina` (S3) ·
`plano-hapvida-maceio` (FAQ #3) · `plano-hapvida-sao-jose-dos-pinhais` (FAQ #12) ·
`reativacao-do-plano` · `tabela-de-preco-hapvida`

`consultar_saturacao_destinos`: 8 backlinks = **NORMAL** (nem saturado nem subutilizado).

## Coleta 4 — O que o banco diz (`consultar_artigo` + `consultar_pillars_proibicoes`)

- Banco id 57, `tipo: pillar_produto`, `status: publicado`, `versao: null`,
  `data_publicacao: null`, `h2s: []`, `faqs: []`, `observacoes: "slug a confirmar"`.
  **O registro está incompleto** — o banco não sabe a estrutura desta página.
- Links de saída registrados: 3 (`plano-hapvida-ribeirao-preto`, `hapvida-rede-pediatrica`,
  `plano-de-saude-para-recem-nascido`). No HTML publicado há ~21 destinos distintos —
  **o registro está defasado**.
- `consultar_pillars_proibicoes` para os 9 pillars do entorno devolveu 60+ proibições.
  As que atingem diretamente a página atual:
  - **Carências:** tabela de prazos, cards de prazo, CPT, leis citadas → só bridge + link.
  - **Coparticipação:** "o que é", tabela Total × Parcial, trade-off, valores por região
    → a H3 atual "Quanto se paga de coparticipação" precisa ser reduzida a bridge.
  - **Tabela de preços:** tabela por faixa etária, "5 fatores que definem quanto você paga"
    → usar shortcode local + link.
  - **Individual/Empresarial:** lista de modalidades, comparativo individual × empresarial
    → a H2 atual "Tipos de Planos de Saúde Hapvida Infantil" precisa passar no teste.
  - **Como contratar:** steps, documentos, DPS, prazos, formas de pagamento
    → a H2 atual "Como Incluir Seu Filho no Plano Hapvida" precisa virar bridge + link
    para `/como-incluir-dependentes-no-seu-plano-hapvida/` (que é #2 nas buscas dela).

## Inventário do HTML no ar (arquivo em `fontes/artigo-atual-2026-09-08.html`)

| Item | Exigido no P1-P9 | Na página | Situação |
|---|---|---|---|
| H2 de corpo | mín. 8 / alvo 9 | 7 | 🔴 |
| H3 | mín. 15 / alvo 22-28 | 2 | 🔴 |
| FAQ (`<details>`) | mín. 12 / alvo 15-17 | 7 | 🔴 |
| Cartão `fonte-oficial` (v7.6) | 1 a 3 | 0 | 🔴 |
| Caixa `guia-box` "Sobre este guia" (v7.6) | exatamente 1 | 0 | 🔴 |
| Nó `Person` no schema (v7.4) | obrigatório | ausente | 🔴 |
| Palavras de corpo | mín. 2.500 / alvo 3.500-4.500 | ~2.711 | 🟡 |
| Links internos únicos | mín. 8 / alvo 12-16 | ~21 | ✅ |
| Links externos | mín. 2 (planalto + gov.br/ans presentes) | 3 | ✅ |
| Tabela de preço | 1 | 1 | ✅ |
| `destaque-laranja-suave` | mín. 10 | 16 | ✅ |
| `v5-countup` | 2 no pillar de referência | 0 | 🟡 |

Outros dois reparos já medidos: dois links internos apontam para URL antiga
(`/hapvida-rede-pediatrica-2025/` → canônica `/hapvida-rede-pediatrica/`;
`/plano-hapvida-sao-paulo/` → canônica `/plano-hapvida-sao-paulo2/`).

---

## VEREDITO DA P0 — a causa nomeada

**A causa é CONTEÚDO, não canibalização, não title/meta, não ângulo.**

A página faz o trabalho comercial dela: é a 2ª orgânica nas duas keywords-cabeça, a
1ª que não é da própria Hapvida, e é a **fonte nº 1 citada pelo AI Overview** na
consulta de maior clique. O que ela não faz é **cobrir o tema**: com 7 H2, 2 H3 e 7 FAQ
está abaixo do mínimo do próprio arquétipo P1-P9 em seis itens, e é isso que a deixa
presa em posição 5-6 com CTR abaixo de 1% nas consultas genéricas de maior volume
("plano de saúde infantil valores", 481 impressões/mês).

**Decisão de URL: MANTER `/plano-de-saude-hapvida-infantil/`. Sem 301.**

Contraponto registrado: o slug não contém "valor" nem "preço", que é o que a demanda
real pede ("valor do plano da hapvida infantil" é a consulta de maior clique). Ainda
assim, trocar o slug jogaria fora 8 links internos, a posição 2 já conquistada e — o
que pesa mais — a **citação nominal no AI Overview**, que é reconstruída a partir da
URL. O ganho hipotético de um slug com "valor" não paga esse risco.

**Trava para a reforma:** a passagem de preço atual é a que a IA extrai hoje. Ela pode
ser ampliada, nunca substituída por outro enquadramento. Qualquer reescrita do bloco
de preço passa a ser risco medido, não melhoria livre.

---

## Próximo passo

FASE 0 (DR1 + DR2) com CI-1 obrigatória — mínimo 3 concorrentes LIDOS. Dois já estão
lidos e arquivados nesta sessão (`descontoplanodesaude.com.br/plano-hapvida-infantil/`,
mais 3 artigos do mesmo domínio para leitura do método). Faltam **tabelasaude.com**
(#4 e #3 nas duas SERPs) e **joov.com.br** (#5 nas duas) — e ambos rankeiam acima ou
logo abaixo, então são alvo obrigatório da matriz de cobertura.
