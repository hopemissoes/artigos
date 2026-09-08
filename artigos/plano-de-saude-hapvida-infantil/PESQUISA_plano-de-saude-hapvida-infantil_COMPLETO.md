# PESQUISA plano-de-saude-hapvida-infantil — FASE 0 (state file)

Tipo: **pillar de produto (P1-P9)** · Reformulação de página publicada (WP id 12185, banco id 57).
FASE P0 já rodada — ver `FASE-P0.md`. Causa: conteúdo. URL: manter, sem 301.

## 1. SERP real (serp_local)

coletado_em: 2026-09-08  # serp

- posicoes_principal:
  - "plano hapvida infantil" (Brasil, mobile, depth 20): **#2 orgânico** (rank_absolute 5) —
    https://tabelaplanos.com.br/plano-de-saude-hapvida-infantil/ · acima só www2.hapvida.com.br
    (#1). Segunda URL nossa: /hapvida-rede-pediatrica/ em #14.
  - "valor do plano da hapvida infantil" (Brasil, mobile, depth 10): **#2 orgânico**
    (rank_absolute 4) · /tabela-de-preco-hapvida/ em #9 → canibalização parcial, vigiar.
- featured_snippet / formato de snippet: **não há featured snippet** em nenhuma das duas
  keywords. O topo é **AI Overview** (asynchronous_ai_overview) seguido de bloco de imagens
  e "as pessoas também perguntam". Formato da resposta da IA: **parágrafo curto com faixa de
  preço + lista de fatores**. A passagem citável deve seguir esse formato (parágrafo com o
  valor + lista dos fatores), não tabela solta.
- **AI Overview cita a nossa página como fonte nº 1** em "valor do plano da hapvida infantil",
  ao lado de /tabela-de-preco-hapvida/ e joov.com.br. Texto que a IA extraiu: "a partir de
  R$ 56,94 em opções empresariais com coparticipação" e "empresariais via CNPJ ou MEI a partir
  de 2 vidas, cerca de 30% mais baratos". **Ampliar essa passagem, nunca substituir.**
- tipo de página dominante (SXO): guia comercial de produto com tabela de preço — é o que
  ranqueia nas duas SERPs (tabelasaude, joov, facaseuplanodesaude, garantiaseg). Confere com
  o arquétipo P1-P9. Não mudar o tipo.
- URLs concorrentes:
  - https://descontoplanodesaude.com.br/plano-hapvida-infantil/
  - https://tabelasaude.com/plano-de-saude-infantil/hapvida/
  - https://joov.com.br/qual-o-valor-do-plano-da-hapvida-infantil/
  - https://blog.facaseuplanodesaude.com.br/tabela-preco-hapvida-2023/
  - https://www.garantiaseg.com.br/plano-de-saude/plano-de-saude-hapvida-tabela-de-precos/

## 2. Kit on-page [V5]

- principal: kw: plano de saúde hapvida infantil | volume: 140/mês | dificuldade: 2 |
  intenção: comercial. Casa com a URL, com o H1 e com o title. As variantes de marca
  ("hapvida infantil" 320 · "valor do plano da hapvida infantil" 320 · "plano de saude
  hapvida infantil" 140 · "plano de saúde infantil hapvida" 40) somam **860/mês** no
  mesmo campo semântico.
- secundarias:
  - kw: valor do plano da hapvida infantil | volume: 320 | KD 0 | intencao: commercial | veredito: qualificada | onde entra: H2 de preço + FAQ | cluster_candidata: não (é a mesma intenção da página)
  - kw: plano de saude infantil valores | volume: 880 | KD 0 | intencao: informational-de-compra | veredito: qualificada | onde entra: H2 de preço + passagem citável | cluster_candidata: não
  - kw: plano de saude infantil individual | volume: 590 | KD 6 | intencao: informational-de-compra | veredito: qualificada | onde entra: H2 de modalidades | cluster_candidata: sim — spoke "plano de saúde infantil individual"
  - kw: plano de saude infantil individual preço | volume: 210 | KD 0 | intencao: commercial | veredito: qualificada | onde entra: H3 dentro do H2 de preço | cluster_candidata: não
  - kw: plano de saude infantil barato | volume: 140 | KD 0 | intencao: commercial | veredito: qualificada | onde entra: H2 do eixo (por que o preço muda) | cluster_candidata: não
  - kw: plano de saude infantil sem carencia | volume: 30 | intencao: informational-de-compra | veredito: qualificada | onde entra: H3 recém-nascido 30 dias + FAQ | cluster_candidata: não
  - kw: melhor plano de saude infantil | volume: 50 | intencao: commercial | veredito: qualificada | onde entra: P9 (vale a pena / não compensa) | cluster_candidata: não
  - kw: hapvida infantil | volume: 320 | KD 0 | intencao: informational | veredito: qualificada | onde entra: H1/lead | cluster_candidata: não
- secundarias DESCARTADAS pelo veto de intenção (volume sem cliente):
  - "emergência infantil hapvida" (390) · "urgência e emergência hapvida infantil" (320) ·
    "hapvida emergência infantil" (320) — quem busca isso **já tem o plano** e quer o endereço
    agora. Território de `/urgencia-e-emergencia-hapvida/` e `/hapvida-rede-pediatrica/`:
    vira **link**, nunca seção.
  - "hospital infantil hapvida manaus/fortaleza/recife" (90/50/40) — navegacional de unidade;
    território dos artigos de hospital.
  - "hapvida consulta" (165.000) · "boleto hapvida individual" (8.100) · "hapvida telefone
    4004" (5.400) — cliente existente. Não perseguir.
- matriz de posicionamento:
  | Posição | Conteúdo |
  |---|---|
  | H1 | contém "plano de saúde hapvida infantil" |
  | title | abre com a principal + o gancho de preço da secundária de maior clique |
  | URL | /plano-de-saude-hapvida-infantil/ (já contém a principal — manter) |
  | meta description | principal 1× + faixa de preço |
  | 1º parágrafo (lead-herói) | principal + valor a partir de (shortcode) |
  | ≥1 H2 | principal ou variação natural |
  | ≥2 H2 com secundária | H2 de preço ("valores") + H2 de modalidades ("individual") |
- query fan-out (mínimo 5) — sub-perguntas que a busca com IA gera a partir da keyword-alvo:
  - pergunta: quanto custa um plano de saúde infantil hoje → AQUI (H2 de preço)
  - pergunta: o preço muda conforme a idade da criança → AQUI (H3 do eixo — a faixa 0-18 é uma só)
  - pergunta: dá para fazer plano só para a criança, sem os pais → AQUI (H2 de modalidades)
  - pergunta: o recém-nascido entra sem carência → AQUI (H3) + link /plano-de-saude-para-recem-nascido/
  - pergunta: quais carências valem para a criança → CLUSTER → link /plano-de-saude-hapvida-carencia/
  - pergunta: o plano infantil cobre fono, terapia ocupacional e psicologia → AQUI (FAQ) + link /hapvida-cobre-fisioterapia/ e /hapvida-cobre-psicologo/
  - pergunta: para onde levar a criança em uma emergência → CLUSTER → link /urgencia-e-emergencia-hapvida/
  - pergunta: como incluir o filho como dependente → CLUSTER → link /como-incluir-dependentes-no-seu-plano-hapvida/
  - pergunta: o Hapvida infantil é melhor que o da Unimed ou da Amil → PENDÊNCIA de pauta (spoke comparativo); hoje só link /hapvida-vs-amil-comparativo/

## 3. Contexto local (IBGE / CNES / DATASUS)

**Não se aplica: pillar de produto é nacional.** A skill proíbe descer a detalhe de cidade
no pillar (`artigo-pillar-produto.md` → "Pillar não desce a detalhe de cidade"). O contexto
geográfico entra só como **âmbito nacional + link** para os artigos de cidade.
- populacao: n/a — pillar nacional
- leitos / CNES: n/a — pillar nacional
- Fontes oficiais que o artigo vai citar e linkar (cartão "Fonte oficial" da v7.6 — máx. 3):
  - Lei 9.656/1998, art. 12, III, "b" (inclusão do recém-nascido em 30 dias) —
    https://www.planalto.gov.br/ccivil_03/leis/l9656.htm — fonte: Planalto — [VERIFICAR resposta 200 antes de publicar]
  - RN 566/2022 (prazos máximos de atendimento; consulta pediátrica em até 7 dias úteis) —
    https://www.gov.br/ans/pt-br/assuntos/consumidor/prazos-maximos-de-atendimento — fonte: ANS — [VERIFICAR resposta 200 antes de publicar]
  - Painel "Confira alguns de nossos números" —
    https://www2.hapvida.com.br/institucional/sobre-o-grupo — fonte: site oficial Hapvida, conferido em 06/09/2026
  - Registro da operadora na ANS (nº 359017) — https://www.ans.gov.br/ — fonte: ANS

## 4. Rede assistencial (consultar_rede ANTES da web)

coletado_em: 2026-09-08  # rede

**Mínimo de unidades para pillar = 0** — a rede por unidade é território do artigo de cidade
e do artigo de hospital. Aqui entram só os números nacionais canônicos (seção 7) e o link
para `/hapvida-rede-pediatrica/`, que é o dono do tema.

### Hospital Mandacaru — Recife (PE)
- endereço: já publicado em artigo próprio — https://tabelaplanos.com.br/hospital-mandacaru-hapvida-recife/
- tipo: hospital próprio com atendimento pediátrico
- fonte: artigo próprio publicado + banco (`consultar_artigo`)
- defensibilidade: 1
- uso no artigo: **nomear e linkar** — é a entidade que o concorrente cita sem ter página.

### Hospital Layr Maia — Belém (PA)
- endereço: já publicado em artigo próprio — https://tabelaplanos.com.br/hospital-layr-maia-hapvida/
- tipo: maternidade e hospital infantil da rede própria
- fonte: artigo próprio publicado (título: "a Maternidade e o Hospital Infantil da Hapvida em Belém")
- defensibilidade: 1
- uso no artigo: nomear e linkar.

## 5. Desmontagem de concorrentes [V4 / CI-1]

**Escada de rotas — tentativas registradas em 08/09/2026:** rota 1 `WebFetch` ❌
(`EGRESS_BLOCKED`) · rota 2 `curl` ❌ (`connect_rejected` no proxy) · **rota 4 `n8n` ✅**
(workflow `NUUZmP5y4AtFb2jL`, roda fora do contêiner). Páginas baixadas inteiras e
arquivadas em `fontes/`. Nenhum dado abaixo veio de trecho de buscador.

### descontoplanodesaude.com.br — https://descontoplanodesaude.com.br/plano-hapvida-infantil/
- coletado_em: 2026-09-08
- rota: n8n
- palavras: 4692 | subtopicos: 27
h2_conteudo:
  - "O que é o plano Hapvida infantil e como funciona a cobertura"
  - "Rede pediátrica: hospitais, UTI neonatal e pronto atendimento infantil"
  - "Carência do plano Hapvida infantil"
  - "Emergência pediátrica 24 horas"
  - "Programa de acompanhamento preventivo infantil"
  - "Odontopediatria: cuidado bucal desde cedo"
  - "Quanto custa o plano Hapvida infantil"
  - "Individual, familiar ou empresarial: qual escolher"
  - "Como incluir seu filho no plano"
  - "Crianças com condições de saúde específicas"
  - "Acompanhamento do desenvolvimento nos primeiros anos"
  - "Documentos para o dia a dia do plano infantil"
  - "Viajando com o plano Hapvida infantil"
  - "Reembolso para atendimento pediátrico fora da rede"
  - "Especialidades pediátricas disponíveis"
  - "Plano Hapvida infantil para adolescentes"
  - "Check-ups e exames de rotina por faixa etária"
  - "Sazonalidade: épocas do ano com maior procura pediátrica"
  - "Plano Hapvida infantil x outras operadoras"
  - "Incluindo mais de um filho no plano"
  - "Erros comuns na hora de contratar plano para os filhos"
  - "Vale a pena investir no plano Hapvida infantil"
  - "Perguntas frequentes sobre o plano Hapvida infantil"
h3_conteudo:
  - "Segmentação hospitalar: o que garante internação e cirurgia"
  - "A rede pediátrica começa antes do nascimento"
  - "Inclusão do recém-nascido em até 30 dias sem carência"
  - "Nutricionista e psicólogo infantil"
  - "Terapias multidisciplinares"
  - "Saúde mental na infância e adolescência"
  - "Triagem neonatal: os primeiros exames do bebê"
  - "Gêmeos e partos múltiplos"
- H2 de CTA descontados da contagem: "CORRETORA OFICIAL", "Quer um Plano Hapvida com Condições Exclusivas?", repetição do H1.
- dados citados: preço só em faixa ("em torno de R$ 150 a R$ 160" individual; "em torno de R$ 100" empresarial) · tabela de carência com 5 linhas · 3 hospitais pediátricos nomeados · "UTI neonatal em cerca de 15 capitais".
- estrutura: 3 cartões "Fonte oficial" (planalto + ANS) · 1 caixa "Sobre este guia" · autor nomeado + tempo de leitura · FAQ com 15 perguntas · schema BlogPosting+Person · 15 links internos · 36 ocorrências de "costuma".
- fraqueza: nenhum valor por cidade; um terço das seções é genérico de plano de saúde (sazonalidade, kit de viagem, marcos do desenvolvimento) e não tem vantagem informacional; "Vale a pena" só com o lado positivo.
- método confirmado como TEMPLATE em outros 3 artigos do mesmo domínio (carência, cirurgias, psicólogo), lidos pela mesma rota: 22-27 H2, exatamente 3 "Fonte oficial", exatamente 1 "Sobre este guia", exatamente 15 FAQ, "Leitura de 18/19 minutos".

### tabelasaude.com — https://tabelasaude.com/plano-de-saude-infantil/hapvida/
- coletado_em: 2026-09-08
- rota: n8n
- palavras: 2749 | subtopicos: 12
h2_conteudo:
  - "Quanto custa o plano Hapvida infantil? Valores de setembro/2026"
  - "Quanto custa o Hapvida infantil por cidade?"
  - "Modalidades do Hapvida para crianças"
  - "Enfermaria ou apartamento? Coparticipação total ou parcial?"
  - "Rede própria: o diferencial da Hapvida"
  - "Como funciona para o seu filho na Hapvida"
  - "Tabela de carências do Hapvida"
  - "Dúvidas frequentes sobre o Hapvida infantil"
h3_conteudo:
  - "Valores por acomodação (faixa 0 a 18 anos)"
  - "Ambulatorial"
  - "Nosso Plano · Enfermaria"
  - "Nosso Plano · Apartamento"
  - "Mix"
  - "Acomodação"
  - "Coparticipação"
  - "Hospitais próprios"
  - "PAs infantis 24h"
  - "Laboratórios próprios"
  - "Onde é mais forte"
  - "Recém-nascido"
  - "Dependente"
  - "Titular criança"
- dados citados: 53 valores em R$ · 33 linhas de tabela · preço por cidade dentro da FAQ (Belo Horizonte R$ 115,42 empresarial / R$ 185,56 individual · Fortaleza R$ 158,09 / R$ 237,45 · Recife R$ 186,32 / R$ 264 · Salvador R$ 209,64 / R$ 323,67 · Manaus R$ 185,20 / R$ 309,09 · Goiânia R$ 121,18 / R$ 147,39 · Belém R$ 145,80 / R$ 263,05) · tabela de carência completa.
- **É o concorrente mais forte e o benchmark real** — ocupa #4 e #3 nas duas SERPs medidas.
- fraqueza: publica "referência ANS", valor mais alto que o praticado (BH R$ 115,42 contra o nosso a partir de R$ 71,98 no mesmo recorte empresarial 0-18); não liga coparticipação ao preço; sem autor; rede descrita de forma genérica; preço por cidade espalhado em 8 FAQs, sem comparação lado a lado.

### joov.com.br — https://joov.com.br/qual-o-valor-do-plano-da-hapvida-infantil/
- coletado_em: 2026-09-08
- rota: n8n
- palavras: 985 | subtopicos: 6
h2_conteudo:
  - "Quanto custa o plano de saúde infantil da Hapvida?"
  - "Benefícios do Plano Infantil da Hapvida"
  - "A rede exclusiva da Hapvida"
  - "Como funciona o agendamento de Consultas e Exames?"
  - "Cobertura para Urgência e Emergência"
  - "Por que escolher o Plano Infantil da Hapvida?"
- dados citados: "Ambulatório: A partir de 168,43 · Enfermaria: A partir de 286,61 · Apartamento: A partir de 417,99" — **última atualização Oct 24, 2024**.
- fraqueza: conteúdo raso de 2024 ranqueando em #5 nas duas keywords — prova de que a SERP está fraca e que cobertura + recência ganham aqui.

### Matriz de cobertura (subtópico x concorrente)

| Subtópico | desconto | tabelasaude | joov | nós hoje |
|---|---|---|---|---|
| Preço 0-18 com valor | faixa | sim, por cidade | sim (2024) | sim, 4 cidades x 4 modalidades |
| Preço não muda com a idade | não | sim (FAQ) | não | não |
| Modalidades (amb x completo) | sim | sim | parcial | sim |
| Coparticipação total x parcial no preço | não | não | não | sim |
| Individual só para a criança | não | sim | não | parcial |
| Recém-nascido 30 dias sem carência | sim | sim | não | sim |
| Carência do infantil | tabela | tabela | não | link para o pillar |
| Rede pediátrica nomeada | 3 hospitais | genérica | não | não (só o número 86) |
| Terapias (fono/TO/psicologia) | sim | não | não | sim (FAQ) |
| Odontopediatria | sim | não | sim | sim (sem link) |
| Comparação com outras operadoras | sim | não | não | não |
| Vale a pena / não compensa | só o lado bom | não | não | não |
| Fonte oficial linkada | 3 cartões | não | não | 2 links, sem cartão |
| Autor visível | sim | não | não | não |
| **palavras / subtópicos** | **4.692 / 27** | **2.749 / 12** | **985 / 6** | **2.711 / 7** |

Líder de cobertura: descontoplanodesaude (27 subtópicos). **Piso dinâmico da v5: superar 27
subtópicos cobertos, com conteúdo que passe no teste de substituição por produto.**

## 6. Ganho de informação / brechas [V4 / CI-2]

> **Ganho de informação — defensibilidade: 1** (proprietário). Enunciado completo no fim
> desta seção; sai da tabela vigente por cidade, não de fonte pública.

- must-match (todo concorrente cobre; não podemos faltar):
  - valor da faixa 0-18 com número em tela
  - o que muda entre ambulatorial e cobertura completa
  - recém-nascido incluído em até 30 dias entra sem carência
  - dá para contratar só para a criança
  - onde a criança é atendida (rede própria, PA infantil)
  - carência do infantil (aqui: bridge + link, é território do pillar de carências)
- brecha (todos cobrem mal ou ninguém cobre):
  - **coparticipação total × parcial dentro do preço infantil** — nenhum dos três explica que
    a escolha muda a mensalidade da criança; nós já temos as 4 colunas.
  - **o valor por cidade comparado lado a lado** — o tabelasaude tem os valores, mas
    escondidos em 8 FAQs separadas; ninguém monta o comparativo.
  - **para quem NÃO compensa** — nenhum dos três admite um cenário ruim (P9 da skill).
  - **quanto custa usar** (coparticipação por consulta/exame da criança) — ninguém publica.
- GANHO DE INFORMAÇÃO (o que nenhum concorrente diz):
  > **O preço do plano infantil não muda com a idade da criança — muda com o CEP.** Na faixa
  > 0 a 18 anos o valor é o mesmo do recém-nascido ao adolescente (a primeira troca de faixa
  > da ANS é aos 19), mas entre a cidade mais barata e a mais cara da nossa tabela a mesma
  > modalidade varia quase **90%**. Quem escolhe plano infantil não está escolhendo idade:
  > está escolhendo praça e modalidade.
  - defensibilidade: 1 — nível 1 (proprietário): sai da tabela vigente da corretora (shortcodes por cidade),
    não de fonte pública. O concorrente que tem preço por cidade publica valores de
    "referência ANS" mais altos e não faz a comparação.
  - teste do eixo: o concorrente **não** consegue escrever isso com 20 minutos de Google —
    precisaria da tabela vendida, por cidade, na mesma modalidade e no mesmo mês.

## 7. Dado proprietário [V7.2] (consultar_rede · cotador_fila · banco)

- dado_proprietario: tabela vigente por cidade e modalidade na faixa 0-18 (Fortaleza, Belo
  Horizonte, São Paulo, Belém × Ambulatorial/Nosso Plano × copart. total/parcial) —
  defensibilidade: 1 — fonte: shortcodes do site, mesma origem da imagem da tabela
- dado_proprietario: coparticipação por categoria e região (`consultar_coparticipacao`,
  08/09/2026) — sp_bh: consulta eletiva R$ 43,63 · exame simples R$ 51,52 · exame complexo
  R$ 125,93 · terapia neurológica R$ 78,87 · urgência R$ 61,82 · demais R$ 42,47 —
  demais_capitais: consulta eletiva R$ 25,42 · exame simples R$ 45,79 · exame complexo
  R$ 114,48 · terapia neurológica R$ 78,87 · urgência R$ 43,63 · demais R$ 24,27 —
  defensibilidade: 1 — fonte: banco Supabase (`consultar_coparticipacao`)
- dado_proprietario: números canônicos (`consultar_dados_canonicos`, 08/09/2026) —
  86 hospitais próprios · 168 credenciados · 80 PAs 24h · 365 clínicas · 301 unidades de
  diagnóstico · 15,9 mi de beneficiários · 16 estados · 11 programas Qualivida —
  defensibilidade: 1-2 — fonte: banco + painel oficial www2.hapvida.com.br
- dado_proprietario: autoridade interna da página — 8 artigos linkam para ela
  (`consultar_links_para_destino`, 08/09/2026); saturação NORMAL — defensibilidade: 1 —
  fonte: banco Supabase
- dado_proprietario: desempenho real da página no GSC (28 dias, 11/08-07/09/2026) —
  "plano de saúde infantil valores" 481 impressões, posição 5,57, CTR 0,83% —
  defensibilidade: 1 — fonte: Search Console via MCP

## 8. Não encontrado [V7.2]

nao_encontrado:
- número de capitais com UTI neonatal na rede própria — onde foi procurado: `consultar_dados_canonicos` (não existe a chave), banco de rede. O concorrente afirma "cerca de 15 capitais"; **não confirmado** → não publicar.
- lista oficial de hospitais 100% pediátricos da rede — onde foi procurado: banco (`consultar_artigo`, artigos de hospital publicados). Confirmados por artigo próprio: Mandacaru (Recife) e Layr Maia (Belém). "Rio Solimões" e "Infantil Intermédica" vêm só do concorrente → não publicar.
- taxa de resolução da teleconsulta ("aproximadamente 77%", presente no artigo atual) — onde foi procurado: `consultar_dados_canonicos` (não há a chave). Manter fora até confirmar em `hapvida-data` ou fonte oficial.
- idade-limite do dependente (21/24 anos, presente na FAQ atual) — onde foi procurado: dados canônicos. É regra contratual, varia por contrato → tratar com atribuição ("conforme o contrato"), nunca como número cravado.

## 9. FORBIDDEN_TOKENS

FORBIDDEN_TOKENS:
- 88 hospitais
- 10 anos
- mais de 10 anos
- Rio Solimões
- Infantil Intermédica
- 15 capitais
- R$ 103
- R$ 157,76
- R$ 115,42
- R$ 185,56
- R$ 168,43
- R$ 286,61
- R$ 417,99
- Diamante

## 10. PLANO_MODELOS [V7.2]

**MODO: monomodelo** — declarado. Esta sessão roda em um único modelo; a linha de 25 agentes
não foi disparada. O que se perde: a separação de ponto cego entre produtor e conferente
(travas T2/T3). O que compensa, conforme a própria skill: **o portão humano passa a valer
mais** e nenhuma trava mecânica é dispensada. As travas de arquivo (`checkpoint_fase0`,
`checkpoint_suficiencia`, `checkpoint_completude`, `checkpoint_verificar`,
`checkpoint_preco_primeiro`, `checkpoint_voz`, `checkpoint_doorway_final`) continuam
obrigatórias e são o que sustenta a qualidade neste regime.

## 11. Datas de coleta

coletado_em: 2026-09-08  # serp
coletado_em: 2026-09-08  # rede
coletado_em: 2026-09-08  # concorrentes
coletado_em: 2026-09-08  # keywords
coletado_em: 2026-09-07  # gsc (janela 11/08 a 07/09/2026)

## 12. FAQ local

- Quanto custa o plano de saúde Hapvida infantil hoje?
- O valor do plano infantil muda conforme a idade da criança?
- Por que o mesmo plano infantil custa mais em uma cidade do que em outra?
- Dá para contratar o plano infantil só para a criança, sem os pais?
- Qual a diferença entre coparticipação total e parcial no plano infantil?
- Quanto se paga de coparticipação por consulta e exame no plano infantil?
- O que muda entre o plano infantil ambulatorial e o plano infantil completo?
- O recém-nascido entra no plano infantil sem cumprir carência?
- O que acontece com o plano infantil se eu perder o prazo de 30 dias do recém-nascido?
- O plano infantil da Hapvida cobre fonoaudiologia, terapia ocupacional e psicologia?
- O plano infantil cobre atendimento odontológico da criança?
- Onde a criança do plano infantil é atendida em uma urgência pediátrica?
- Quem tem MEI consegue contratar o plano infantil empresarial?
- Até que idade o filho fica como dependente no plano infantil?
- Posso incluir enteado ou filho adotivo no plano infantil?
- Como incluir mais de um filho no mesmo plano infantil?
- O plano infantil da Hapvida cobre cirurgia?
- Para quem o plano infantil da Hapvida pode não compensar?
- O plano infantil da Hapvida cobre as vacinas do calendário do bebê?
- O plano infantil tem carência para consulta com pediatra?

## 13. Anti-doorway

- teste_substituicao: **por PRODUTO** (regra do pillar, não por cidade). Trocar "plano
  infantil" por "plano individual" ou "Plano Mix" em cada seção. Seções que sobrevivem à
  troca: reescrever ou virar bridge. O eixo (preço muda com o CEP, não com a idade) só é
  válido para o infantil — é a faixa 0-18 que não tem degrau de idade. Aprovado.
- dados_unicos: 12
  1. valor 0-18 em Fortaleza, BH, São Paulo e Belém, nas 4 modalidades (16 células)
  2. variação de ~90% entre a praça mais barata e a mais cara na mesma modalidade
  3. a faixa 0-18 não tem degrau de preço — a primeira troca da ANS é aos 19
  4. coparticipação por categoria nas duas regiões tarifárias (12 valores)
  5. internação e cirurgia isentas de coparticipação em todas as modalidades
  6. 86 hospitais próprios · 80 PAs 24h · 365 clínicas · 301 unidades de diagnóstico
  7. Hospital Mandacaru (Recife) e Hospital Layr Maia (Belém) nomeados, com página própria
  8. Programa Bebê Hap e o prazo de 30 dias com o artigo de lei (art. 12, III, "b")
  9. prazo máximo de 7 dias úteis para consulta pediátrica (RN 566/2022)
  10. registro ANS da operadora nº 359017
  11. modalidade empresarial a partir de 2 vidas, inclusive MEI
  12. desempenho real da própria página (o que a IA já cita hoje)
- frases_genericas: 0 toleradas. Caça-clichê obrigatório em "modelo verticalizado", "rede
  própria sempre que possível", "custo competitivo", "atendimento de qualidade",
  "tranquilidade para a família", "cobertura total".
- anti-doorway: **APROVADO** — o teste de substituição por produto foi aplicado ao esqueleto
  P1-P9 e as seções nacionais de carência, coparticipação-conceito, documentos e steps de
  contratação estão marcadas como bridge + link, conforme as 60+ proibições devolvidas por
  `consultar_pillars_proibicoes` em 08/09/2026.

## 14. Diferenciais (rotulados)

- titulo: O preço do plano infantil não muda com a idade, muda com a praça — ancora: tabela vigente por cidade na faixa 0-18, 16 células (defensibilidade: 1)
- titulo: Quanto custa USAR o plano infantil — ancora: coparticipação por categoria nas duas regiões tarifárias, 12 valores do banco (defensibilidade: 1)
- titulo: No plano infantil, internação e cirurgia da criança são isentas de coparticipação — ancora: regra de produto confirmada no banco de coparticipação (defensibilidade: 1)
- titulo: Para quem o plano infantil NÃO compensa — ancora: P9 de dupla lista; nenhum dos 3 concorrentes lidos publica o lado ruim (defensibilidade: 2)
- titulo: Os hospitais da rede infantil que já têm página própria no site — ancora: Mandacaru (Recife) e Layr Maia (Belém), artigos publicados (defensibilidade: 1)

## 15. Fio condutor

**Escolher plano infantil não é escolher idade — é escolher praça e modalidade.** Dos 0 aos
18 anos o preço é o mesmo; o que faz a mensalidade dobrar é a cidade, a acomodação e a
coparticipação. O guia mostra o número de cada combinação, diz quanto custa usar e admite
para quem não compensa.
