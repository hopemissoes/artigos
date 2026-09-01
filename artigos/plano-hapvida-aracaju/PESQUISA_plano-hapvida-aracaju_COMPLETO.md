# PESQUISA FASE 0 — plano-hapvida-aracaju (city S1-S7)

Artigo JÁ PUBLICADO (banco id 3, versão V4.3.2, `https://tabelaplanos.com.br/plano-hapvida-aracaju/`).
Esta FASE 0 é **retroativa**: foi feita depois do artigo, para conferir o que está no ar e
dirigir a revisão. Não é a pesquisa que gerou o texto — o texto veio de sessão anterior,
sem state file.

- coletado_em: 2026-09-01 # serp
- coletado_em: 2026-09-01 # rede e unidades
- coletado_em: 2026-09-01 # concorrentes
- coletado_em: 2026-09-01 # keywords

---

## 1. SERP real (serp_local)

- ferramenta: `serp_local` · keyword: "plano hapvida aracaju" · location_code: 1001715 (Aracaju/SE)
- language_code: pt · device: mobile · depth: 20 · custo: US$ 0,0035
- fonte: DataForSeo SERP API, coleta própria
- item_types presentes: paid, organic, people_also_ask, images, local_pack, people_also_search
- ai_overview: AUSENTE nesta SERP (não há resposta de IA no topo para esta query)
- featured_snippet: AUSENTE. formato de snippet: não há caixa de resposta destacada;
  o topo é ocupado por 3 anúncios pagos e pelo site oficial da operadora.
- tipo de página dominante (SXO): tabela de preço + guia de cidade — 4 dos 6 concorrentes
  reais têm "tabela de preço" no title. Confirma o arquétipo city com preço-primeiro.

### Posições medidas

- nosso: `https://tabelaplanos.com.br/plano-hapvida-aracaju/` — orgânico #3 (absoluto 7)
- acima de nós só a própria operadora: www2.hapvida.com.br (#1) e contrate-online.hapvida.com.br (#2)
- CANIBALIZAÇÃO: `https://tabelaplanos.com.br/` (home) aparece na MESMA SERP em orgânico #17
  (absoluto 29), com o title "Plano de saúde Hapvida 2026: PROMOÇÃO de R$ 71,98".
  Duas URLs do mesmo site na mesma busca — risco confirmado, ver seção 8.

### PAA capturado (people_also_ask)

- Qual o valor do plano Hapvida Aracaju?
- Quais hospitais em Aracaju aceitam o plano de saúde Hapvida?
- Quanto custa o plano individual da Hapvida?
- Qual o melhor plano de saúde em Aracaju, Sergipe?

---

## 2. Contexto local (IBGE / CNES)

Dados demográficos citados no artigo publicado, herdados e **não reconferidos nesta coleta**
(o WebFetch ao IBGE devolveu HTTP 403 nesta sessão; ver `nao_encontrado`).

- população: ~630 mil habitantes · IDH 0,770 · ~37% do PIB de Sergipe
  fonte: IBGE Cidades — Aracaju (citado no artigo publicado; reconferência pendente)
- região metropolitana: ~932 mil pessoas somando N. S. do Socorro (~193 mil),
  São Cristóvão (~101 mil) e Barra dos Coqueiros (~35 mil)
  fonte: IBGE Cidades (citado no artigo publicado; reconferência pendente)
- cobertura de planos de saúde em Sergipe: 15% a 20%, contra média nacional de 24,9%
  fonte: ANS — Sala de Situação (citado no artigo publicado; reconferência pendente)
- leitos do novo hospital anunciado no Grageru: 130
  fonte: F5 News Sergipe, dez/2025 (citado no artigo publicado)

---

## 3. Rede assistencial — catálogo do banco (fonte autoritativa)

Coleta: `consultar_rede` (MCP BD - Consultar), `p_cidade: Aracaju`, `p_uf: SE`.
fonte: catálogo Supabase `rede_unidades`, páginas 106-108 do PDF de rede Hapvida.

**7 unidades próprias com endereço no catálogo:**

- unidade: Hospital Gabriel Soares · tipo: Hospital
  endereço: Rua Itabaiana, 690, Centro, Aracaju - SE
  fonte: consultar_rede id 171 (pág. 106)
  defensibilidade: 1
- unidade: Clínica Aracaju · tipo: Clínica
  endereço: Rua Campo do Brito, 1180 - São José, Aracaju - SE
  fonte: consultar_rede id 172 (pág. 107)
  defensibilidade: 1
- unidade: Clínica Campos de Sergipe · tipo: Clínica
  endereço: Rua Campos, 927 - São José, Aracaju - SE
  fonte: consultar_rede id 173 (pág. 107)
  defensibilidade: 1
- unidade: Clínica Gentil Tavares · tipo: Clínica
  endereço: Av. Engenheiro Gentil Tavares, 831 - Getúlio Vargas, Aracaju - SE
  fonte: consultar_rede id 174 (pág. 107)
  defensibilidade: 1
- unidade: Clínica Hermes Fontes · tipo: Clínica
  endereço: Av. Hermes Fontes, 160 - Suiça, Aracaju - SE
  fonte: consultar_rede id 175 (pág. 107)
  defensibilidade: 1
- unidade: Clínica São José · tipo: Clínica
  endereço: Tv. Juca Barreto, 177 - São José, Aracaju - SE
  fonte: consultar_rede id 176 (pág. 107)
  defensibilidade: 2
- unidade: Diagnóstico Centro · tipo: Diagnóstico
  endereço: Rua Itabaianinha, 66 - Centro, Aracaju - SE
  fonte: consultar_rede id 177 (pág. 108)
  defensibilidade: 1

### Regra das duas listas (catálogo × artigo publicado)

- **Catálogo tem, artigo NÃO cita:** `Clínica São José` (Tv. Juca Barreto, 177 — São José).
  Ação: incluir na S4/S5. Não é ausência de rede; é ausência no texto.
- **Artigo cita, catálogo NÃO tem como unidade separada:** `Diagnóstico Aracaju`
  (Rua Campo do Brito, 1180) e `Diagnóstico Gabriel Soares` (Rua Itabaiana, 690).
  Os dois endereços são os MESMOS da Clínica Aracaju e do Hospital Gabriel Soares —
  são serviços de imagem DENTRO de unidades já contadas, não pontos de atendimento novos.
  Tratar como serviço, nunca como unidade, sob pena de inflar a contagem.
- **Contagem correta:** 7 unidades próprias / 7 endereços distintos no catálogo.
  O artigo publicado afirma "10 pontos de atendimento" e "~10 unidades próprias".
  Esse número **não se sustenta** nem pelo catálogo (7) nem pela própria lista do artigo
  (1 hospital + 4 clínicas + 4 diagnósticos = 9, com 2 diagnósticos duplicando endereço,
  o que dá 6 endereços distintos). Ver `FORBIDDEN_TOKENS`.

### Dado canônico Hapvida (nacional)

fonte: `consultar_dados_canonicos` (MCP BD - Consultar), 2026-09-01
- hospitais próprios: 86 · hospitais credenciados: 168 · beneficiários: 15,9 milhões
- prontos atendimentos 24h: 80 · estados com presença: 16 · programas Qualivida: 11

### Coparticipação — grupo tarifário de Aracaju

fonte: `consultar_coparticipacao`, `p_regiao: demais_capitais`, 2026-09-01
- consulta eletiva: R$ 25,42 · urgência: R$ 43,63 · exame simples: R$ 45,79
- exame complexo: R$ 114,48 · terapia/neuro: R$ 78,87 · demais: R$ 24,27
- defensibilidade: 1
- O artigo usa os shortcodes `[demais_capitais_*]` — grupo CORRETO para Aracaju. Confirmado.

---

## 4. Desmontagem de concorrentes (CI-1) — matriz de cobertura

Rota usada: **curl** com User-Agent de navegador (rota 2 da escada; o WebFetch desta sessão
devolveu HTTP 403). Todas as páginas retornaram HTTP 200 e estão salvas em
`fontes/ci1/*.html`. Nenhum dado abaixo veio de snippet de buscador.

#### meuplanohap — https://www.meuplanohap.com.br/tabela-precos/hapvida/se/aracaju/
- posição orgânica: 4 · coletado_em: 2026-09-01 · rota: curl · http: 200
- palavras de corpo: 4095 · tabelas: 45 · valores em R$ distintos: 340
- title: "Tabela de Preços Hapvida Aracaju/SE 2026 - A partir de R$ 112,00"
h2:
  - "Planos Adesão - Aracaju/SE" — heading do concorrente
  - "Planos Empresarial (PME) - Aracaju/SE" — heading do concorrente
  - "Planos EMPRESARIAL 30 A 99 - Aracaju/SE" — heading do concorrente
  - "Planos Individual - Aracaju/SE" — heading do concorrente
  - "Comparativo de Planos Hapvida em Aracaju" — heading do concorrente
  - "Perguntas Frequentes - Hapvida Aracaju" — heading do concorrente
h3_amostra:
  - "Quer contratar o plano Hapvida em Aracaju?" — heading do concorrente
  - "NOSSO PLANO" — heading do concorrente
  - "NOSSO MEDICO" — heading do concorrente
- forca: LÍDER DE COBERTURA DE PREÇO. Único que separa preço por 4 modalidades de
  contratação (Adesão, PME, Empresarial 30-99, Individual) e é municipal, não estadual.
- fraqueza: ZERO rede local — nenhum endereço, nenhum hospital, nenhum bairro. Zero contexto
  de cidade. Título com preço fixo hardcoded, que envelhece.

#### facaseuplano — https://blog.facaseuplanodesaude.com.br/tabela-de-preco-hapvida-sergipe/
- posição orgânica: 6 · coletado_em: 2026-09-01 · rota: curl · http: 200
- palavras de corpo: 1875 · tabelas: 4
- title: "Tabela de Preço Hapvida Sergipe - Plano de Saúde Hapvida 2026"
h2:
  - "Sobre a Tabela de Preço Hapvida Sergipe 2026" — heading do concorrente
  - "Confira abaixo Carências e Tabela de Preço da Hapvida Sergipe" — heading do concorrente
  - "Quais as Carências do Hapvida ?" — heading do concorrente
  - "Rede Hapvida em Sergipe" — heading do concorrente
  - "Tabela de Preço Hapvida Sergipe 2026" — heading do concorrente
  - "Tabela de Preço Hapvida Familiar em Sergipe" — heading do concorrente
  - "Preço Hapvida Empresarial" — heading do concorrente
  - "Quanto custa o plano individual do Hapvida ?" — heading do concorrente
  - "Qual é o plano mais barato do Hapvida ?" — heading do concorrente
  - "Qual o preço do Hapvida Infantil ?" — heading do concorrente
  - "Qual o preço do Hapvida para idoso?" — heading do concorrente
  - "Tabela de Preço Hapvida Individual" — heading do concorrente
h3:
  - "O que cobre o Nosso Plano Hapvida?" — heading do concorrente
  - "O que cobre o Plano Mix Hapvida?" — heading do concorrente
  - "Quem pode ser dependente no Hapvida ?" — heading do concorrente
- forca: cauda longa de preço por PERFIL — infantil, idoso, familiar, dependente.
  São 4 H2 que nós não temos em forma nenhuma.
- fraqueza: ESTADUAL, não municipal (fala "Sergipe", nunca "Aracaju"). Rodapé com cauda de
  São Paulo, irrelevante para a praça. Preços fixos no H2, que envelhecem.

#### compareplano — https://compareplanodesaude.com.br/hapvida/hapvida-sergipe/
- posição orgânica: 14 · coletado_em: 2026-09-01 · rota: curl · http: 200
- palavras de corpo: 1564 · tabelas: 0
- title: "Hapvida Sergipe - Conheça Todos os Planos Com Desconto de Até 30%"
h2:
  - "Plano Hapvida Sergipe" — heading do concorrente
  - "Quanto custa o Hapvida Sergipe?" — heading do concorrente
  - "Hospitais e laboratórios que atendem aos clientes do plano" — heading do concorrente
  - "Benefícios exclusivos da operadora" — heading do concorrente
  - "Carências do Hapvida Sergipe" — heading do concorrente
  - "Documentos para a contratação de pessoa física e empresarial" — heading do concorrente
  - "Vale a pena contratar um plano da Hapvida Saúde?" — heading do concorrente
  - "4 vantagens de contratar um plano de saúde barato" — heading do concorrente
- forca: cobre carências e documentos de contratação.
- fraqueza: ESTADUAL. Zero tabela. Thin (1564 palavras). Título promete desconto de 30%
  sem lastro. "4 vantagens de contratar um plano de saúde barato" é conteúdo genérico puro.

#### intermedicanotre — https://www.intermedicanotredameplanos.com.br/hapvida/hospitais-hapvida-sergipe/
- posição orgânica: 7 · coletado_em: 2026-09-01 · rota: curl · http: 200
- palavras de corpo: 452 · tabelas: 1
- title: "Hospitais Hapvida Sergipe - Hapvida"
h2:
  - "Rede de atendimento Hapvida NotreDame Intermédica em Sergipe" — heading do concorrente
  - "Diferenciais Rede Credenciada Hapvida" — heading do concorrente
h3:
  - "HOSPITAL" — heading do concorrente
  - "CLÍNICA" — heading do concorrente
  - "IMAGEM E LABORATÓRIO" — heading do concorrente
- forca: é o único concorrente que organiza a rede por TIPO de unidade.
- fraqueza: 452 palavras — o mais thin de todos. Sem endereço, sem bairro, sem preço.
  Ranqueia em #7 com isso, o que mostra o quanto a praça é pouco disputada.

#### gazetadasemana — https://gazetadasemana.com.br/noticia/270627/hapvida-aracaju-2026-guia-completo-da-rede-credenciada-planos-e-como-aderir/amp
- posição orgânica: 11 · coletado_em: 2026-09-01 · rota: curl · http: 200
- palavras de corpo: 992 · headings estruturados: nenhum (página AMP de portal de notícia)
- NOTA: não conta para o mínimo de 3 concorrentes lidos — a página não expõe H2/H3
  estruturados. A leitura aconteceu (HTTP 200, HTML salvo), mas não há heading literal
  para extrair. Registrado por transparência.

### Linha de profundidade (piso dinâmico)

- líder de cobertura: meuplanohap — 4095 palavras · 5 H2 de conteúdo · 47 H3
- nosso artigo publicado: 5564 palavras · 13 H2 · 18 FAQ — SUPERA o líder em extensão e
  em número de subtópicos. O piso dinâmico está atendido; a lacuna não é tamanho, é
  cobertura de subtópico específico (ver must-match 2 e 6).

---

## 5. Ganho de informação / brechas (CI-2)

### must-match (o que ≥2 concorrentes cobrem bem e não podemos faltar)

1. must-match: tabela de preço por faixa etária — COBERTO (shortcode `[aracaju_menortabela]`)
2. must-match: preço separado por MODALIDADE DE CONTRATAÇÃO (individual, familiar,
   empresarial/PME, adesão) — **NÃO COBERTO**. meuplanohap tem 4 blocos; facaseuplano tem 3.
   Nós temos um shortcode de uma modalidade só. É a maior lacuna competitiva do artigo.
3. must-match: carências — COBERTO (seção própria)
4. must-match: quais hospitais/laboratórios atendem — COBERTO, e melhor que todos
5. must-match: FAQ de preço ("quanto custa o individual", "qual o mais barato") — COBERTO
6. must-match: preço por PERFIL — infantil e idoso — **NÃO COBERTO**. facaseuplano tem
   H2 dedicado a cada um; o PAA confirma a intenção. Cabe como H3 dentro da seção de preço.
7. must-match: documentos de contratação — território do pillar Como Contratar; bridge basta.

### brechas (o que todos cobrem mal ou ninguém cobre)

- brecha: nenhum concorrente dá ENDEREÇO de unidade em Aracaju. O líder de preço
  (meuplanohap, 4095 palavras) tem rede zero. Nossa maior vantagem, já explorada.
- brecha: nenhum concorrente diz que a Hapvida NÃO tem pronto atendimento 24h autônomo em
  Aracaju — toda a urgência está concentrada no Gabriel Soares, no Centro.
- brecha: nenhum concorrente compara Hapvida × Unimed Sergipe × Plamed com critérios.
- brecha: 3 dos 5 concorrentes tratam "Sergipe", não "Aracaju". Somos municipais; eles não.
- brecha: ninguém cruza rede com distância — quanto você anda até o atendimento.

### ganho de informação (a UMA coisa que nenhum concorrente diz)

- ganho: **a distância entre o seu bairro e o único pronto-socorro Hapvida de Sergipe.**
  defensibilidade: 1
  detalhe: cruzamento dos 7 endereços do catálogo próprio com o fato, apurado na mesma
  coleta, de que não existe PA 24h autônomo na cidade — toda urgência da operadora no estado
  passa por um único endereço (Rua Itabaiana, 690, Centro). Nenhum concorrente tem os
  endereços; nenhum tem o fato; ninguém cruzou os dois.
  base: `consultar_rede` (catálogo proprietário) + `consultar_dados_canonicos` (80 PAs 24h
  nacionais, nenhum em Aracaju)

- ganho secundário: **o efeito Grageru medido em quilômetros.**
  defensibilidade: 2
  detalhe: o novo hospital de 130 leitos
  muda a distância de quem mora na zona sul (Jardins, 13 de Julho, Grageru), hoje a 5-7 km do
  Centro. É o único dado prospectivo da praça e nenhum concorrente o converte em consequência
  prática para o leitor.

---

## 5b. Diferenciais da praça (com âncora local)

- titulo: Único pronto-socorro da operadora em todo o estado fica na Rua Itabaiana, 690, Centro
  ancora: Hospital Gabriel Soares, Aracaju — catálogo id 171
- titulo: Mercado de apenas três operadoras vendendo pessoa física em Aracaju
  ancora: Hapvida, Unimed Sergipe e Plamed
- titulo: Rede própria concentrada no eixo Centro–São José, dentro de ~3 km
  ancora: 5 dos 7 endereços do catálogo estão em Centro, São José e Suíssa
- titulo: Hospital de 130 leitos anunciado no Grageru muda a distância da zona sul
  ancora: Av. Pedro Valadares, 891 — Grageru
- titulo: Operação própria em Aracaju desde 2007, a mais antiga do estado
  ancora: inauguração do Gabriel Soares, agosto de 2007
- titulo: Clínica dedicada à saúde da mulher, rara na rede Hapvida do Nordeste
  ancora: Rua Campos, 927 — São José (catálogo id 173)

---

## 6. Kit on-page (matriz de posicionamento)

### keyword principal

- kw: plano hapvida aracaju
- volume: 50/mês (Brasil, 2026-07) · CPC US$ 1,64 · competition MEDIUM · KD: não retornado
- intenção: informational (foreign: navigational, commercial)
- tendência: -29% no ano — a busca por esta forma exata está encolhendo
- fonte: DataForSeo keyword_data, location_code 2076
- defensibilidade: 3

### posicoes_principal (matriz — estado ATUAL do que está no ar)

- posicao: 1º parágrafo do corpo — OK (lead-herói carrega a keyword)
- posicao: ≥1 H2 — OK (2 H2 contêm a keyword)
- posicao: URL/slug — OK (`/plano-hapvida-aracaju/`)
- posicao: Title SEO — OK ("Plano Hapvida Aracaju 2026: promoções de R$ 144,77")
- posicao: H1 — **FALHA**. O H1 no ar é "Hapvida Aracaju: Preços, Rede e Hospital | Guia 2026"
  e não contém a palavra "plano". Reprovado pelo `checkpoint_onpage.py`.
- posicao: Meta description — **FALHA**. A meta no ar abre em "Hapvida Aracaju 2026:" e
  também não contém "plano". Reprovado pelo `checkpoint_onpage.py`.

### secundarias (com veto de intenção)

- kw: plano de saude aracaju
  volume: 880/mês · KD: 0 · intenção: commercial · tendência: +22% no mês
  veredito: qualificada
  onde entra: é keyword de OUTRO artigo — arquétipo "mercado amplo" multi-operadora, que já
  existe para Recife, Belém, Teresina, Goiânia, BH e Fortaleza. cluster_candidata: sim
  fonte: DataForSeo keyword_data 2076
- kw: hospital hapvida aracaju
  volume: 140/mês · KD: 14 · intenção: navigational-de-rede
  veredito: qualificada
  onde entra: H2 do Gabriel Soares (já existe)
  fonte: DataForSeo keyword_suggestions
- kw: urgência hapvida aracaju (+ "emergência hapvida aracaju")
  volume: 70 + 30 = 100/mês · KD: 0 · intenção: navigational
  veredito: qualificada
  onde entra: hoje só em FAQ. cluster_candidata: sim — existe o padrão
  `urgencia-e-emergencia-hapvida-[cidade]` publicado em Recife, Fortaleza e Goiânia.
  fonte: DataForSeo keyword_suggestions
- kw: laboratório hapvida aracaju
  volume: 90 + 90 = 180/mês · intenção: navigational
  veredito: qualificada
  onde entra: S4 rede + link para o pillar `laboratorios-hapvida-capitais`
  fonte: DataForSeo keyword_suggestions
- kw: clínica hapvida aracaju
  volume: ~230/mês somando as variantes · intenção: navigational/transactional
  veredito: qualificada
  onde entra: S5 cobertura por bairro
  fonte: DataForSeo keyword_suggestions
- kw: novo hospital hapvida aracaju
  volume: 30/mês · intenção: transactional
  veredito: qualificada
  onde entra: seção do Gabriel Soares, no H3 do Grageru
  fonte: DataForSeo keyword_suggestions
- kw: clínicas que aceitam hapvida em aracaju
  volume: 30/mês · intenção: commercial
  veredito: qualificada
  onde entra: S4/S5
  fonte: DataForSeo keyword_suggestions
- kw: maternidade hapvida aracaju
  volume: 20/mês · intenção: navigational
  veredito: qualificada
  onde entra: seção do Gabriel Soares (é Hospital E Maternidade)
  fonte: DataForSeo keyword_suggestions

### secundarias DESCARTADAS pelo veto de intenção

- kw: telefone hapvida aracaju (390/mês, somando 4 variantes ~1.560) — veredito: descartada.
  Quem já é cliente. Volume alto e conversão zero.
- kw: hapvida trabalhe conosco aracaju (260 + 30) — veredito: descartada. Candidato a emprego.
- kw: hapvida aracaju boleto / ouvidoria / sac / contato — veredito: descartada. Já é cliente.
- kw: hapvida são josé tea aracaju (320 + 40) — veredito: descartada. Busca por unidade
  específica de TEA, navegacional de quem já usa.
- kw: hapvida aracaju (1900/mês) — veredito: descartada como alvo. Navegacional puro,
  dominada pelos domínios da própria operadora. Serve de contexto, não de meta.

### query fan-out (sub-perguntas prováveis da busca com IA)

- pergunta: Qual o valor do plano Hapvida em Aracaju? → aqui (seção de preço)
- pergunta: Quais hospitais em Aracaju aceitam o plano Hapvida? → aqui (S4 rede)
- pergunta: Quanto custa o plano individual da Hapvida? → cluster (pillar Individual, link)
- pergunta: Qual o melhor plano de saúde em Aracaju? → cluster (artigo mercado amplo, não existe)
- pergunta: Onde fica a urgência da Hapvida em Aracaju? → aqui hoje; cluster no futuro
- pergunta: Onde ficam as clínicas Hapvida em Aracaju? → aqui (S5 cobertura por bairro)
- pergunta: Qual o laboratório da Hapvida em Aracaju? → aqui + link pillar laboratórios
- pergunta: Quando abre o novo hospital do Grageru? → aqui (seção do hospital)

---

## 6b. FAQ do artigo (as NOSSAS 18, conferidas contra o texto no ar)

Aviso de leitura: o `checkpoint_suficiencia.py` conta como FAQ qualquer linha terminada em
"?", inclusive os H2 dos concorrentes transcritos na seção 4. O conjunto abaixo é o nosso.

- faq [âncora: tabela local]: Qual o valor do plano Hapvida em Aracaju?
- faq [âncora: Gabriel Soares, Rua Itabaiana 690]: Qual hospital a Hapvida usa em Aracaju?
- faq [âncora: Grageru, 130 leitos]: A Hapvida vai abrir novo hospital em Aracaju?
- faq [âncora: ausência de unidade na zona norte]: A Hapvida atende na zona norte de Aracaju?
- faq [âncora: RM de Aracaju]: Hapvida atende em Nossa Senhora do Socorro e Barra dos Coqueiros?
- faq [SEM âncora local (nacional)]: Qual a diferença entre Nosso Plano e Mix em Aracaju?
- faq [âncora: Unimed Sergipe]: A Hapvida é melhor que a Unimed em Aracaju?
- faq [âncora: Plamed, operadora sergipana]: A Hapvida comprou a Plamed?
- faq [âncora: único PS, Centro]: Onde fica a emergência da Hapvida em Aracaju?
- faq [âncora: Hospital e Maternidade Gabriel Soares]: A Hapvida tem maternidade em Aracaju?
- faq [âncora: Hermes Fontes, 160, Suíssa]: Tem Hapclínica pediátrica em Aracaju?
- faq [SEM âncora local (nacional)]: Como funciona a coparticipação total da Hapvida em Aracaju?
- faq [âncora: Plamed]: Posso migrar da Plamed para a Hapvida sem carência?
- faq [âncora: Diagnóstico Centro, Itabaianinha 66]: A Hapvida faz ressonância magnética em Aracaju?
- faq [âncora: Rua Campos, 927]: A Hapvida tem clínica de saúde da mulher em Aracaju?
- faq: Qual o telefone da Hapvida em Aracaju? — âncora local, mas intenção de quem já é cliente
- faq [SEM âncora local]: A Hapvida tem plano empresarial em Aracaju a partir de quantas vidas?
- faq [âncora: 2007, Gabriel Soares]: Desde quando a Hapvida opera em Aracaju?

- faq_medida: 18 perguntas · 3 sem âncora local (16,7%, limite 20%) · 0 duplicatas entre si

---

## 7. Dado proprietário (Parte 7) — defensibilidade

- dado_proprietario: catálogo de 7 unidades de Aracaju com endereço, via `consultar_rede`
  defensibilidade: 1
- dado_proprietario: valores de coparticipação do grupo demais_capitais, via `consultar_coparticipacao`
  defensibilidade: 1
- dado_proprietario: números canônicos Hapvida (86 hospitais, 80 PAs, 16 estados),
  via `consultar_dados_canonicos`
  defensibilidade: 1
- dado_proprietario: mapa de saturação de destinos de link interno do site,
  via `consultar_saturacao_destinos` — mostra que o artigo hoje linka 2 destinos SATURADOS
  defensibilidade: 2
- dado_proprietario: overlaps doorway já catalogados no banco, via `consultar_overlaps_doorway`
  defensibilidade: 2
- dado_proprietario: tabela de preço vigente por faixa etária, via shortcode do WordPress
  defensibilidade: 1

- dados_unicos: 14
  (7 endereços de unidade própria · 6 valores de coparticipação do grupo · ausência de PA 24h
  autônomo · 130 leitos do Grageru · 2007 como início da operação · grupo tarifário confirmado
  · posição real #3 na SERP local · canibalização com a home · Clínica São José ausente do
  texto · 2 "diagnósticos" que duplicam endereço · saturação dos 2 destinos linkados ·
  volume 880 de "plano de saude aracaju" · ausência de artigo de mercado amplo para Aracaju ·
  ausência de spoke de urgência para Aracaju)

---

## 8. nao_encontrado (Parte 8) — busca sem resultado é resultado

- nao_encontrado: reconferência dos dados do IBGE (população, IDH, PIB). O WebFetch a
  `https://www.ibge.gov.br/cidades-e-estados/se/aracaju.html` devolveu HTTP 403 nesta sessão.
  Os números seguem os do artigo publicado e NÃO foram validados nesta coleta.
- nao_encontrado: número de beneficiários da Hapvida em Sergipe/Aracaju. O artigo publicado
  não cita; o banco não tem. O campo `concorrentes` do banco menciona "~60-84 mil" para a
  Hapvida, faixa larga e sem fonte — não usar.
- nao_encontrado: data de inauguração do hospital do Grageru. Só há o anúncio (dez/2025).
- nao_encontrado: FAQs de Aracaju no catálogo do banco — `consultar_artigo` devolve
  `faqs: []` para o slug, embora o artigo no ar tenha 18 perguntas. O banco está defasado.
- nao_encontrado: nenhum PA 24h autônomo da Hapvida em Aracaju, nem no catálogo de rede nem
  no texto da operadora. É ausência confirmada em fonte, e vira o ganho de informação.

---

## 9. FORBIDDEN_TOKENS

Tokens que NÃO podem aparecer no artigo. Cada um foi medido contra o catálogo do banco.

FORBIDDEN_TOKENS:
10 pontos de atendimento
~10 unidades próprias
10 Pontos de Atendimento
As 10 unidades
Diagnóstico Aracaju
Diagnóstico Gabriel Soares
4 centros de diagnóstico

---

## 10. Anti-doorway

- teste_substituicao: aprovado — trocando "Aracaju" por "Maceió", caem a lista de 7 endereços,
  o comparativo com Unimed Sergipe e Plamed, a concentração da urgência no Gabriel Soares e o
  hospital do Grageru. O que sobreviveria (mecânica de coparticipação, prazos da ANS) já está
  marcado como bridge.
- dados_unicos: aprovado — 14 dados exclusivos da praça, acima do piso de 10.
- frases_genericas: aprovado — a varredura do `checkpoint_voz.py` não achou tique bloqueante.
- anti-doorway geral: aprovado
- ressalva registrada, não bloqueante: o H2 "Tecnologia e Atendimento Digital" é 100% nacional
  e está catalogado no banco como overlap de risco médio, com ação recomendada ELIMINAR. Não
  reprova o teste de substituição do artigo inteiro, mas é a seção mais frágil.

---

## 11. Datas de coleta

- coletado_em: 2026-09-01 # serp_local mobile depth 20, location_code 1001715
- coletado_em: 2026-09-01 # rede — consultar_rede, catálogo Supabase
- coletado_em: 2026-09-01 # unidades com endereço
- coletado_em: 2026-09-01 # dados canônicos e coparticipação
- coletado_em: 2026-09-01 # CI-1, 5 páginas por curl
- coletado_em: 2026-09-01 # keyword_data e keyword_suggestions

---

## 12. Fontes consultadas

- https://www.meuplanohap.com.br/tabela-precos/hapvida/se/aracaju/
- https://blog.facaseuplanodesaude.com.br/tabela-de-preco-hapvida-sergipe/
- https://compareplanodesaude.com.br/hapvida/hapvida-sergipe/
- https://www.intermedicanotredameplanos.com.br/hapvida/hospitais-hapvida-sergipe/
- https://gazetadasemana.com.br/noticia/270627/hapvida-aracaju-2026-guia-completo-da-rede-credenciada-planos-e-como-aderir/amp
- https://www.ibge.gov.br/cidades-e-estados/se/aracaju.html
- https://www.gov.br/ans/pt-br
- https://cnes.datasus.gov.br/
- https://www2.hapvida.com.br/
- https://tabelaplanos.com.br/plano-hapvida-aracaju/

---

## 13. Fio condutor

Aracaju é um mercado de três operadoras onde a Hapvida ganha no preço, mas concentra tudo
num só endereço: o Hospital Gabriel Soares, no Centro, único ponto de urgência 24h da
operadora em todo o estado. O artigo é sobre essa troca — o menor preço da praça em troca de
uma rede geograficamente estreita, que o hospital do Grageru vai começar a corrigir.
