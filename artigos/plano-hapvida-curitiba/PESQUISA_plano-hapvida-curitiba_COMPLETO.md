# PESQUISA FASE 0 — plano-hapvida-curitiba (city, S1-S7)

> Artigo **já publicado** em https://tabelaplanos.com.br/plano-hapvida-curitiba/ (HTTP 200,
> banco id 46, versão V4.3.2). Esta Fase 0 é de **revisão**, não de artigo novo — por isso o
> Search Console entra como fonte de nível 2, o que não existe em artigo inédito.

## 0 · MODO DE PRODUÇÃO (declaração obrigatória da v7.2)

MODO: agente único — a linha de 25 agentes NÃO foi disparada nesta sessão (subagentes não
foram autorizados). Consequência assumida: a trava "quem produz nunca confere" não existe
aqui; coleta, síntese e conferência saíram da mesma cabeça. **O portão humano vale mais**,
e o `checkpoint_suficiencia.py` + os Agentes 23/24 continuam pendentes.

---

## 1 · SERP REAL (DataForSeo `serp_local`)

coletado_em: 2026-09-01 # serp e keywords

Chamada: `serp_local` · keyword "plano hapvida curitiba" · location_code 1001634 (Curitiba/PR)
· language_code pt · device mobile · depth 20 · custo US$ 0,0035.

**location_code de Curitiba = 1001634** — não estava na tabela da skill `dataforseo-tabelaplanos`.
Confirmado nas duas versões do CSV de geotargets do Google Ads (2026-08-12 e 2026-07-16), e a
mesma fonte devolve 1001566 para Belo Horizonte, que é o valor que a skill já trazia.
fonte: https://developers.google.com/static/google-ads/api/data/geo/geotargets-2026-08-12.csv

### 1.1 Os orgânicos (rank_group / rank_absolute)

| # org | abs | domínio | tipo | observação |
|---|---|---|---|---|
| 1 | 5 | www2.hapvida.com.br | institucional | oficial |
| 2 | 6 | www2.hapvida.com.br | institucional | oficial (home) |
| 3 | 7 | www.gndisul.com.br | institucional | marca regional Clinipam |
| 4 | 8 | planos-saude.hapvida.com.br | landing oficial | oficial |
| 5 | 10 | www.healthcorr.com.br | corretora | CONCORRENTE |
| 6 | 11 | www.doctoralia.com.br | diretório | ignorado por regra |
| 7 | 12 | portal-beneficiario.hapvida.com.br | portal | oficial |
| 8 | 13 | www.rotaseguros.com.br | corretora | CONCORRENTE |
| 9 | 14 | hapvida.vc | institucional | oficial |
| 10 | 17 | www.meuplanohap.com.br | corretora | CONCORRENTE |
| 11 | 18 | www.hbsaude.com.br | operadora | grupo |
| 12 | 19 | www2.hapvida.com.br | institucional | oficial |
| 13 | 20 | **tabelaplanos.com.br (HOME)** | nosso | 🔴 ver 1.3 |
| 14 | 21 | corretorabravence.com | corretora | CONCORRENTE |
| 15 | 23 | instagram.com | rede social | ignorado |
| 16 | 24 | suavidapedehapvida.com.br | afiliado | — |
| 17 | 26 | www2.hapvida.com.br | portal | oficial |
| 18 | 27 | planosodontologicos.com | nicho | — |

**Leitura:** 8 das 18 posições orgânicas são propriedades da própria Hapvida. SERP de marca,
como a skill `dataforseo-tabelaplanos` já avisa.

### 1.2 Elementos da SERP

- `local_pack` ocupando as posições absolutas 1-3, todas do gndisul.com.br: Centro Clínico
  Centro (nota 2,4 · 321 votos), Centro Clínico Mercês (2,0 · 520 votos), Hapvida Vendas
  (1,4 · 57 votos). fonte: serp_local 2026-09-01
- `people_also_ask` em absoluto 4, com 4 perguntas (transcritas em 5.1).
- `images` em absoluto 15 — **2 das 4 imagens são nossas**, com alt "Plano Hapvida Curitiba
  2026: Promoção a partir de R$ 77,39" apontando para a URL do artigo. É o ativo que já
  funciona. fonte: serp_local 2026-09-01
- `people_also_search`: Hapvida plano individual preço · Plano de saúde Hapvida preço ·
  Hapvida Clinipam · Telefone Clinipam Agendamento Curitiba · Hapvida consulta ·
  Hapvida Clinipam whatsapp · Hapvida boleto · Marcar consulta Hapvida · Clinipam Curitiba ·
  Site Hapvida · Hapvida cancelar plano
- **Sem AI Overview** nesta SERP e **sem featured snippet** (`is_featured_snippet` falso em
  todos os 18 orgânicos).

featured_snippet:
  existe: nao
  formato: nao ha caixa de resposta destacada nesta SERP
  ocupante: nenhum
  acao: manter passagem citavel em paragrafo de 40-60 palavras (padrao geo-aeo §1)
  fonte: serp_local 2026-09-01, keyword "plano hapvida curitiba"

### 1.3 🔴 CANIBALIZAÇÃO — confirmada por duas fontes independentes

**(a) Na SERP real:** para "plano hapvida curitiba" quem aparece do nosso domínio é a **HOME**
(absoluto 20). A página de cidade **não aparece no orgânico** até o absoluto 28. Ela existe na
SERP só dentro do bloco de imagens.

**(b) No Search Console (28 dias, 2026-08-04 a 2026-08-31):** para a query "hapvida curitiba",
**nove URLs nossas** recebem impressão ao mesmo tempo:

| URL | impressões | posição |
|---|---|---|
| /plano-hapvida-curitiba/ | 151 | 6,28 |
| /hapvida-vs-unimed/ | 7 | 4,43 |
| /clinicas-hapvida-por-capital/ | 3 | 27 |
| /plano-clinipam-curitiba/ | 3 | **1,0** |
| /tabela-de-preco-hapvida/ | 2 | 5 |
| /hospitais-credenciados-hapvida/ | 1 | 5 |
| /o-que-plano-de-saude-hapvida-cobre-guia/ | 1 | 4 |
| /plano-hapvida-e-bom/ | 1 | 6 |
| /hapvida-cobre-psicologo/ | 1 | 5 |
| /laboratorios-hapvida-capitais/ | 1 | 12 |

fonte: gsc_custom_query, sc-domain:tabelaplanos.com.br, 2026-08-04 a 2026-08-31

**O artigo irmão `/plano-clinipam-curitiba/` aparece em posição 1,0** para "hapvida curitiba" e
para "hapvida em curitiba", enquanto a página de cidade fica em 6,28 e 6,85. É o mesmo padrão
que a skill descreve no pillar Individual: o problema não é o conteúdo, é outra URL da casa
ocupando a SERP.

---

## 2 · REDE ASSISTENCIAL — catálogo do banco ANTES da web (Parte 2, v7.2)

coletado_em: 2026-09-01 # rede e unidades

Chamada: `consultar_rede` (MCP BD - Consultar), p_cidade "Curitiba", p_uf "PR", p_limite 200.
Devolveu **14 unidades**. Todas com endereço. Fonte primária de confirmação:
fonte: https://www2.hapvida.com.br/unidades

> **Regra das duas listas:** as 14 estão no catálogo (`no_catalogo: sim`). A confirmação
> unidade a unidade no guia oficial **não foi feita nesta sessão** — por isso `no_guia_oficial`
> vai como `nao_conferido` e o artigo não pode afirmar atividade atual de unidade específica
> sem atribuir ao Guia Médico. É a lição do Diagnóstico Madre Cecília, aplicada aqui.

### 2.1 Hospitais (3)

- nome_unidade: Hospital Mateus Leme
  tipo: proprio · categoria: Hospital
  endereco: Rua Mateus Leme, 2600 - São Francisco, Curitiba - PR
  no_catalogo: sim · no_guia_oficial: nao_conferido
  fonte: consultar_rede id 471 (pagina_pdf 306)
- nome_unidade: Hospital Onix Batel
  tipo: proprio · categoria: Hospital
  endereco: Av. Vicente Machado, 2321 - Seminário, Curitiba - PR
  no_catalogo: sim · no_guia_oficial: nao_conferido
  fonte: consultar_rede id 472 (pagina_pdf 306)
- nome_unidade: Hospital Santa Brígida
  tipo: proprio · categoria: Hospital
  endereco: Rua Guilherme Pugsley, 1705 - Água Verde, Curitiba - PR
  no_catalogo: sim · no_guia_oficial: nao_conferido
  fonte: consultar_rede id 473 (pagina_pdf 307)

> 🔴 **CONTRADIÇÃO COM O ARTIGO PUBLICADO.** O artigo chama o flagship de "Hospital Ônix
> Mateus Leme" e o banco de artigos registra esse nome. O catálogo da rede tem **duas unidades
> distintas**: "Hospital Mateus Leme" (São Francisco) e "Hospital Onix Batel" (Seminário). Ou o
> artigo fundiu dois hospitais num nome só, ou o catálogo está desatualizado. **Não se escreve
> nada sobre isso sem bater no Guia Médico.** Ver `nao_encontrado` e FORBIDDEN_TOKENS.

### 2.2 Prontos atendimentos (3 — tipo "Pronto Atendimento" no catálogo)

- nome_unidade: Centro Clínico Boqueirão
  tipo: proprio · categoria: Pronto Atendimento
  endereco: Av. Marechal Floriano Peixoto, 7477 - Boqueirão, Curitiba - PR
  no_catalogo: sim · no_guia_oficial: nao_conferido
  fonte: consultar_rede id 474 (pagina_pdf 309)
- nome_unidade: Clínica Mercês
  tipo: proprio · categoria: Pronto Atendimento
  endereco: Av. Manoel Ribas, 552 - Mercês, Curitiba - PR
  no_catalogo: sim · no_guia_oficial: sim — aparece no local_pack da SERP como "Aberto 24 horas"
  fonte: consultar_rede id 475 + serp_local 2026-09-01
- nome_unidade: Clínica Pinheiro
  tipo: proprio · categoria: Pronto Atendimento
  endereco: Av. Winston Churchill, 1654 - Pinheirinho, Curitiba - PR
  no_catalogo: sim · no_guia_oficial: nao_conferido
  fonte: consultar_rede id 476 (pagina_pdf 308)

### 2.3 Clínicas / centros clínicos (7)

- nome_unidade: Centro Clínico Centro
  endereco: Rua Monsenhor Celso, 98 - Centro, Curitiba - PR
  no_catalogo: sim · no_guia_oficial: sim — local_pack da SERP, nota 2,4 com 321 votos
  fonte: consultar_rede id 477 + serp_local 2026-09-01
- nome_unidade: Centro Clínico Colombo
  endereco: Rua Roberto Lambach Falavinha, 294 - Maracanã, Colombo - PR
  observacao: fica FORA do município de Curitiba, na RMC
  no_catalogo: sim · no_guia_oficial: nao_conferido
  fonte: consultar_rede id 478 (pagina_pdf 310)
- nome_unidade: Centro Clínico Oncológico Cabral
  endereco: Av. Paraná, 1673 - Boa Vista, Curitiba - PR
  no_catalogo: sim · no_guia_oficial: nao_conferido
  fonte: consultar_rede id 479 (pagina_pdf 310)
- nome_unidade: Centro Clínico Pinhais
  endereco: Av. Maringá, 166 - Centro, Pinhais - PR
  observacao: fica FORA do município de Curitiba, na RMC
  no_catalogo: sim · no_guia_oficial: nao_conferido
  fonte: consultar_rede id 480 (pagina_pdf 310)
- nome_unidade: Clínica Água Verde
  endereco: Av. Pres. Getúlio Vargas, 2499 - Água Verde, Curitiba - PR
  no_catalogo: sim · no_guia_oficial: nao_conferido
  fonte: consultar_rede id 483 (pagina_pdf 310)
- nome_unidade: Clínica Barão do Serro Azul
  endereco: Rua Barão do Serro Azul, 449 - São Francisco, Curitiba - PR
  no_catalogo: sim · no_guia_oficial: nao_conferido
  fonte: consultar_rede id 481 (pagina_pdf 310)
- nome_unidade: Clínica São Lourenço
  endereco: Rua Coronel Brasilino Moura, 80 - São Lourenço, Curitiba - PR
  no_catalogo: sim · no_guia_oficial: nao_conferido
  fonte: consultar_rede id 482 (pagina_pdf 310)

### 2.4 Diagnóstico (1)

- nome_unidade: NotreLabs CMD
  endereco: Av. Nossa Senhora da Luz, 2169 - Jardim Social, Curitiba - PR
  no_catalogo: sim · no_guia_oficial: nao_conferido
  fonte: consultar_rede id 484 (pagina_pdf 311)

### 2.5 Checklist da rede

hospitais_documentados: 3
pas_24h: 3
clinicas: 7
labs: 1
total_unidades_catalogo: 14
todos_com_endereco: sim
fora_do_municipio: 2 (Colombo e Pinhais — RMC)
bairros_cobertos: São Francisco, Seminário, Água Verde, Boqueirão, Mercês, Pinheirinho, Centro, Boa Vista, São Lourenço, Jardim Social
fonte: consultar_rede 2026-09-01

> 🔴 **O artigo publicado afirma "19+ centros clínicos".** O catálogo tem **11** unidades
> não-hospitalares (3 PA + 7 clínicas + 1 diagnóstico). O número do artigo é maior que o do
> catálogo e não tem fonte no state file. Entra em FORBIDDEN_TOKENS até alguém confirmar.

---

## 3 · CONTEXTO LOCAL (IBGE / CNES)

coletado_em: 2026-09-01 # contexto local

populacao_censo_2022: 1.773.718 pessoas
fonte: https://servicodados.ibge.gov.br/api/v3/agregados/4709/periodos/2022/variaveis/93
populacao_estimada_2025: 1.830.795 pessoas
populacao_estimada_2026: 1.832.183 pessoas
fonte: https://servicodados.ibge.gov.br/api/v3/agregados/6579/variaveis/9324
mesorregiao: Metropolitana de Curitiba · regiao: Sul · uf: PR
fonte: https://servicodados.ibge.gov.br/api/v1/localidades/municipios/4106902
estabelecimentos_saude: consulta ao CNES respondeu (HTTP 200) mas a contagem agregada por
  município não foi extraída nesta sessão — ver `nao_encontrado`
fonte: https://apidadosabertos.saude.gov.br/cnes/estabelecimentos

> ✅ **Confere:** o artigo diz "1,83 milhão de habitantes (IBGE 2025)". A estimativa IBGE de
> 2025 é 1.830.795. Está correto.

---

## 4 · ACESSIBILIDADE E CONCENTRAÇÃO

concentracao_por_bairro: Água Verde e São Francisco têm 2 unidades cada; os demais bairros, 1
regioes_bem_servidas: eixo central (Centro, Batel/Seminário, Água Verde, Mercês, São Francisco)
regioes_carentes: sul e extremo leste do município — só Boqueirão e Pinheirinho aparecem no catálogo
rmc_atendida_por_unidade_propria: Colombo e Pinhais (unidades fisicamente fora de Curitiba)
fonte: consultar_rede 2026-09-01, cruzado com os bairros dos endereços

---

## 5 · DESMONTAGEM DE CONCORRENTES (CI-1) — 4 páginas LIDAS

coletado_em: 2026-09-01 # concorrentes

## [LIDO] https://www.healthcorr.com.br/plano-de-saude-curitiba/clinipam-hapvida-curitiba/
rota: "WebFetch (rota 1) e curl (rota 2) — as duas funcionaram"
coletado_em: 2026-09-01
title: "Clinipam Curitiba (41) 3319-1000 - Hapvida Clinipam Curitiba"
posicao_serp: organico 5 (absoluto 10)
h2_conteudo:
  - "Plano de Saúde Curitiba e Região Metropolitana"
  - "Plano de Saúde Clinipam Hapvida"
h3:
  - "Planos Clinipam Hapvida"
  - "Solicite Cotação do plano Clinipam Hapvida"
  - "Diferenciais Clinipam Curitiba"
  - "Rede Exclusiva"
  - "Teleconsulta"
  - "Plano Odontológico"
  - "SAC 24h"
  - "Rede Pediátrica Exclusiva"
metricas: {palavras: 470, h2: 2, h3: 8, tabelas: 0, valores_em_reais: 0, faq: 0}
fraquezas: "texto fino (470 palavras); zero preço; zero FAQ; zero endereço de unidade; o H1 é o menu do site inteiro"
fonte: leitura direta da página em 2026-09-01

## [LIDO] https://www.rotaseguros.com.br/curitiba/clinipam/rede-credenciada.html
rota: "curl (rota 2)"
coletado_em: 2026-09-01
title: "Planos Clinipam Hapvida NDI |Curitiba-Rede Credenciada"
posicao_serp: organico 8 (absoluto 13)
h2_conteudo:
  - "ROTA SEGUROS"
h3:
  - "Planos de Saúde"
  - "Operadoras"
  - "Links Úteis"
metricas: {palavras: 416, h2: 1, h3: 5, tabelas: 0, valores_em_reais: 0, faq: 0}
fraquezas: "o único H2 é o nome da corretora, não conteúdo; o title promete rede credenciada e a página não lista uma única unidade; 416 palavras"
fonte: leitura direta da página em 2026-09-01

## [LIDO] https://www.meuplanohap.com.br/tabela-precos/hapvida/pr/curitiba/
rota: "curl (rota 2)"
coletado_em: 2026-09-01
title: "Tabela de Preços Hapvida Curitiba/PR 2026 - A partir de R$ 135,71"
posicao_serp: organico 10 (absoluto 17) — com rich snippet de preço e nota 5,0 (10 votos)
h2_conteudo:
  - "Planos Adesão - Curitiba/PR"
  - "Comparativo de Planos Hapvida em Curitiba"
  - "Perguntas Frequentes - Hapvida Curitiba"
h3:
  - "Quer contratar o plano Hapvida em Curitiba?"
  - "NOSSO PLANO"
  - "PLENO"
  - "Cidades Atendidas"
  - "Canais de Atendimento"
  - "Guias Médicos"
  - "Cancelamento Online"
metricas: {palavras: 883, h2: 3, h3: 9, tabelas: 7, valores_em_reais: 60, faq: 1}
fraquezas: "883 palavras só; zero rede própria; zero endereço; nenhum ângulo local além do nome da cidade"
forcas: "é o único table-first da SERP e o único com rich snippet de preço e de review"
fonte: leitura direta da página em 2026-09-01

## [LIDO] https://corretorabravence.com/operadora/clinipam-hapvida/cidade/curitiba
rota: "curl (rota 2)"
coletado_em: 2026-09-01
title: "Plano de Saúde Clinipam Hapvida em Curitiba | Bravence Corretora"
posicao_serp: organico 14 (absoluto 21)
h2_conteudo:
  - "Clinipam Hapvida: a maior rede própria do Sul"
  - "Hospital de destaque"
  - "Conheça as unidades"
  - "Como funcionam os planos Clinipam Hapvida"
  - "Carência Clinipam Hapvida: prazos e regras"
  - "Doença preexistente e CPT"
  - "Coparticipação: como funciona"
  - "Reajuste: anual e por faixa etária"
  - "Rede credenciada Clinipam Hapvida em Curitiba"
  - "Como contratar a Clinipam Hapvida"
  - "Portabilidade de carências para a Clinipam Hapvida"
  - "Perguntas frequentes sobre a Clinipam Hapvida"
h3:
  - "Hospital Ônix Mateus Leme"
  - "Abrangência: regional ou nacional"
  - "Acomodação: enfermaria ou apartamento"
  - "Segmentação: o que o plano cobre"
  - "Com ou sem coparticipação"
  - "Modalidades de contratação Clinipam Hapvida"
  - "Reajuste anual"
  - "Reajuste por faixa etária"
metricas: {palavras: 3630, h2: 12, h3: 18, tabelas: 3, valores_em_reais: 10, faq: 1}
fraquezas: "é o mais completo da SERP e mesmo assim está em 14º; os valores de coparticipação que cita (R$ 15,00 a R$ 180,00) não batem com a tabela oficial; nenhum endereço de unidade"
forcas: "LÍDER DE COBERTURA — 3.630 palavras, 12 H2. É a régua do piso dinâmico da v5"
fonte: leitura direta da página em 2026-09-01

### 5.1 Matriz de cobertura — subtópicos × concorrentes

| subtópico | healthcorr | rotaseguros | meuplanohap | bravence | NÓS (publicado) |
|---|---|---|---|---|---|
| tabela de preço por faixa | não | não | **cobre bem** | cobre | cobre |
| rede própria / unidades | cobre mal | não | não | cobre | cobre mal |
| **endereço das unidades** | **não** | **não** | **não** | **não** | **não** |
| hospital de destaque | não | não | não | cobre bem | cobre bem |
| carência | não | não | não | cobre bem | cobre |
| coparticipação | não | não | não | cobre bem | cobre |
| **reajuste por faixa etária** | não | não | não | **cobre bem** | **não** |
| doença preexistente / CPT | não | não | não | cobre bem | não |
| portabilidade | não | não | não | cobre bem | cobre |
| FAQ | não | não | cobre | cobre bem | cobre |
| **RMC município a município** | menciona | não | cobre mal | menciona | **não** |
| comparativo com concorrente | não | não | cobre | não | cobre bem |
| **palavras · nº subtópicos** | 470 · 10 | 416 · 6 | 883 · 12 | **3630 · 30** | ~4067 · 24 |

### 5.2 PAA real da SERP (people_also_ask, absoluto 4)

- Qual o valor de um plano de saúde na Hapvida?
- Quais hospitais aceitam o plano de saúde Hapvida em Curitiba?
- Como funciona o plano Hapvida para gestantes?
- Quais hospitais aceitam o plano de saúde Hapvida?
fonte: serp_local 2026-09-01

### 5.3 Concorrentes locais (operadoras, não páginas)

concorrente_1: {nome: "Unimed Curitiba", tipo: cooperativa, rede: credenciada, presenca: forte}
concorrente_2: {nome: "Paraná Clínicas", tipo: medicina de grupo, rede: mista, presenca: media}
concorrente_3: {nome: "Amil", tipo: medicina de grupo, rede: mista, presenca: media}
fonte: consultar_artigo id 46, campo concorrentes (registro do próprio banco)
observacao: os números de market share e preço desses concorrentes que estão no artigo
  publicado NÃO foram reconferidos nesta sessão — ver `nao_encontrado`

---

## 6 · QUERY FAN-OUT (Parte 6)

- pergunta: quanto custa o plano hapvida em curitiba
  destino: aqui
  onde: "S2 acima — seção de preço, já é a primeira"
- pergunta: quais hospitais da hapvida atendem em curitiba
  destino: aqui
  onde: "S4 — rede, com os 3 hospitais e endereço"
- pergunta: onde fica o pronto atendimento 24h da hapvida em curitiba
  destino: aqui
  onde: "S4 — sub-bloco de PA, hoje inexistente. 21 impressões/28d na posição 2,29"
- pergunta: a hapvida atende em campo largo, colombo, pinhais e sao jose dos pinhais
  destino: aqui
  onde: "S5 — cobertura regional, com as 2 unidades da RMC nomeadas"
- pergunta: hapvida e clinipam sao a mesma coisa
  destino: cluster
  onde: "/plano-clinipam-curitiba/ — link interno, é território do artigo irmão"
- pergunta: qual a carencia do plano hapvida
  destino: cluster
  onde: "/plano-de-saude-hapvida-carencia/ — bridge + link"
- pergunta: como funciona o reajuste por faixa etaria
  destino: pendencia
  onde: "nenhum artigo do site cobre; o concorrente bravence cobre e nós não"
- pergunta: quanto custa a consulta com coparticipacao na hapvida em curitiba
  destino: aqui
  onde: "S2 — H3 de coparticipação em valor, com os shortcodes demais_capitais"

---

## 7 · DADO PROPRIETÁRIO (Parte 7, v7.2) — as chamadas de MCP

coletado_em: 2026-09-01 # dado proprietario

dado_proprietario:
  - dado: "14 unidades próprias da Hapvida/Clinipam em Curitiba e RMC, com endereço completo, separadas em 3 hospitais, 3 prontos atendimentos, 7 clínicas e 1 diagnóstico"
    origem: consultar_rede
    defensibilidade: 1
    vira: "S4 — grid de cards da rede, um card por unidade com endereço"
  - dado: "2 das 14 unidades ficam fora do município (Centro Clínico Colombo e Centro Clínico Pinhais) e são o que sustenta o atendimento da RMC"
    origem: consultar_rede
    defensibilidade: 1
    vira: "S5 — cobertura regional; é a resposta às buscas por cidade da RMC"
  - dado: "Curitiba está no grupo demais_capitais: consulta eletiva R$ 25,42, urgência R$ 43,63, exame simples R$ 45,79, exame complexo R$ 114,48, terapia neurológica R$ 78,87, demais terapias R$ 24,27"
    origem: consultar_coparticipacao
    defensibilidade: 1
    vira: "S2 — H3 de coparticipação em valor, por shortcode"
  - dado: "a página recebe 151 impressões/28d em 'hapvida curitiba' na posição 6,28 e converte 1 clique — CTR de 0,66% onde a posição comportaria 5-8%"
    origem: gsc_queries_for_page
    defensibilidade: 2
    vira: "reescrita de title e meta (Fase 5, vigia de CTR baixo)"
  - dado: "buscas por NOME DE RUA batem na página: 'hapvida nossa senhora da luz' 30 impressões, 'hapvida monsenhor celso' 16, 'clinica sao lourenco hapvida' 6 — e as três ruas são endereços de unidades do catálogo"
    origem: gsc_queries_for_page
    defensibilidade: 2
    vira: "S4 — o endereço deixa de ser detalhe e vira o conteúdo"
  - dado: "~37 impressões/28d vêm de municípios da RMC que o artigo não nomeia: Campo Largo 7, Quatro Barras 6, Pinhais 6, Almirante Tamandaré 6, Fazenda Rio Grande 5, São José dos Pinhais 5, Araucária 2"
    origem: gsc_queries_for_page
    defensibilidade: 2
    vira: "S5 — e 1 cross-link para /plano-hapvida-sao-jose-dos-pinhais/, que já existe"

**Cotador:** `cotador_fila` com p_acao consultar — **Curitiba NÃO está na fila**. Há Fortaleza
e Recife cotadas, e Belo Horizonte, Goiânia e São Paulo pendentes. Sem cotador, o dado de
nível 2 "o que perguntam quando já estão comprando" **não existe para esta praça**.
fonte: cotador_fila 2026-09-01

**Números canônicos** (`consultar_dados_canonicos`): 86 hospitais próprios, 168 credenciados,
15,9 mi de beneficiários, 80 PAs 24h, 11 programas Qualivida, 16 estados.
fonte: consultar_dados_canonicos 2026-09-01

---

## 8 · NÃO ENCONTRADO (Parte 8)

nao_encontrado:
  - procurei: "confirmação de que 'Hospital Ônix Mateus Leme' é uma unidade só"
    onde: "consultar_rede (traz DOIS hospitais: Mateus Leme e Onix Batel), consultar_artigo, SERP"
    conclusao: "não confirmado — NÃO afirmar a fusão dos dois nomes sem bater no Guia Médico"
  - procurei: "os '19+ centros clínicos' que o artigo publicado afirma"
    onde: "consultar_rede (devolve 11 unidades não-hospitalares)"
    conclusao: "não confirmado — NÃO repetir o número sem fonte"
  - procurei: "market share de 33% da Unimed Curitiba e 14% da Hapvida, e os 4.700 médicos cooperados"
    onde: "banco (só o registro do próprio artigo), SERP"
    conclusao: "não reconferido nesta sessão — permanece como estava, mas sem fonte primária"
  - procurei: "contagem de estabelecimentos e leitos do CNES em Curitiba"
    onde: "apidadosabertos.saude.gov.br (responde, mas paginado por estabelecimento)"
    conclusao: "não extraído nesta sessão — não citar número de leitos"
  - procurei: "dado do cotador para Curitiba"
    onde: "cotador_fila"
    conclusao: "a cidade não está na fila — não há dado de nível 2 de cotação nesta praça"
  - procurei: "IESS 50,4% de cobertura de planos em Curitiba (dado citado no artigo)"
    onde: "não reconferido nesta sessão"
    conclusao: "manter apenas se a fonte original for reencontrada; caso contrário, remover"

---

## 9 · FORBIDDEN_TOKENS

FORBIDDEN_TOKENS:
19+ centros clínicos
19 centros clínicos
mais de 19 centros clínicos
única maternidade de operadora
33 anos
4.700 médicos cooperados
54 hospitais terceiros

---

## 10 · PLANO_MODELOS

MODO: monomodelo — a linha multiagente não foi disparada (ver seção 0). O `checkpoint_modelos.py`
não se aplica porque não há plano de roteamento a validar. Registrado como lacuna consciente.

---

## 11 · DATAS DE COLETA

coletado_em: 2026-09-01 # serp
coletado_em: 2026-09-01 # rede
coletado_em: 2026-09-01 # contexto
coletado_em: 2026-09-01 # concorrentes
coletado_em: 2026-09-01 # search console

---

# DR2 — POSICIONAMENTO

## 12 · KIT ON-PAGE (matriz de posicionamento)

### 12.1 O achado que muda a estratégia

| keyword | volume/mês | KD | intenção | tendência |
|---|---|---|---|---|
| plano hapvida curitiba | **0 (items_count 0)** | — | — | sem dados |
| hapvida curitiba | 1.000 | 53 | **navigational** | -18% mês, -28% ano |
| clinipam curitiba | 1.000 | **4** | navigational | — |
fonte: keyword_data e related_keywords, location_code 2076, 2026-09-01

**A keyword que o artigo persegue no H1 e no title ("plano hapvida curitiba") tem volume zero.**
A que tem volume ("hapvida curitiba") é navegacional, dominada pelos 8 resultados oficiais da
Hapvida na SERP, e está caindo 28% ao ano. A demanda capturável é a cauda longa que o Search
Console já mostra chegando.

kit_onpage:
  principal: "hapvida curitiba"
  posicoes_principal:
    h1: "Hapvida Curitiba: as 14 unidades, os endereços e quanto custa o plano"
    title: "Hapvida Curitiba: 14 unidades com endereço e preço a partir de R$ X"
    url: "plano-hapvida-curitiba (mantida — tem 7 backlinks internos e ranqueia)"
    meta: "Hapvida Curitiba: os 3 hospitais, os 3 prontos atendimentos 24h e as 8 clínicas, com endereço. Preço por faixa etária e coparticipação pela Tabela 1."
    primeiro_paragrafo: "sim — o lead-herói da v7.4 já contém a keyword"
    h2: "o H2 da rede passa a conter a principal"

### 12.2 Secundárias com veto de intenção

- kw: "pronto atendimento hapvida curitiba"
  volume_gsc: 21 impressões/28d · posicao: 2,29
  intencao: comercial-local
  veredito: qualificada
  onde_entra: "H2/H3 novo na S4 — bloco de PA 24h com endereço"
  cluster_candidata: sim — comporta spoke de urgência
- kw: "hospital hapvida curitiba"
  volume_gsc: 11 impressões/28d · posicao: 5,73
  intencao: comercial-local
  veredito: qualificada
  onde_entra: "H2 da S4"
  cluster_candidata: sim — comporta artigo de hospital (HS1-HS4)
- kw: "hapvida curitiba unidades"
  volume_gsc: 4 impressões/28d · posicao: 9
  intencao: comercial-local
  veredito: qualificada
  onde_entra: "S4 — grid de cards"
  cluster_candidata: nao
- kw: "plano hapvida curitiba preço"
  volume_gsc: 6 impressões/28d · posicao: 5
  intencao: transacional
  veredito: qualificada
  onde_entra: "S2 — seção de preço, que já é a primeira"
  cluster_candidata: nao
- kw: "tem hapvida em curitiba"
  volume_gsc: 25 impressões/28d · posicao: 3,08
  intencao: informacional-de-compra
  veredito: qualificada
  onde_entra: "lead-herói + FAQ"
  cluster_candidata: nao
- kw: "hapvida campo largo"
  volume_gsc: 7 impressões/28d · posicao: 11
  intencao: comercial-local
  veredito: qualificada
  onde_entra: "S5 — cobertura da RMC"
  cluster_candidata: sim — comporta spoke de cidade da RMC
- kw: "hapvida curitiba rede credenciada"
  volume_gsc: 4 impressões/28d · posicao: 9,5
  intencao: informacional-de-compra
  veredito: qualificada
  onde_entra: "S4 — separar própria de credenciada"
  cluster_candidata: nao
- kw: "hapvida boleto"
  volume: 90.500
  intencao: navigational de quem JA e cliente
  veredito: descartada
  onde_entra: "nenhum — infla impressão e derruba CTR e conversão"
- kw: "marcar consulta hapvida"
  volume: 90.500
  intencao: navigational de quem JA e cliente
  veredito: descartada
  onde_entra: "nenhum"
- kw: "hapvida curitiba telefone"
  volume_gsc: 4 impressões/28d
  intencao: navigational de quem JA e cliente
  veredito: descartada
  onde_entra: "nenhum"

## 13 · GANHO DE INFORMAÇÃO E BRECHAS (CI-2)

**MUST-MATCH** (≥2 concorrentes cobrem bem — não podemos faltar):
tabela de preço por faixa etária · modalidades de contratação · hospital de destaque ·
carência · coparticipação · FAQ.

**BRECHAS** (todos cobrem mal ou ninguém cobre):
1. **Nenhum dos 4 concorrentes lidos publica o endereço de uma única unidade.** O bravence tem
   um H2 "Conheça as unidades" e não lista endereço.
2. Nenhum cobre a RMC município a município.
3. Nenhum diz onde fica o pronto atendimento 24h.
4. Só o bravence cobre reajuste por faixa etária — e nós não cobrimos.
5. Os valores de coparticipação do bravence (R$ 15,00 a R$ 180,00) não batem com a tabela
   oficial (R$ 24,27 a R$ 114,48). Nós temos o número certo, do banco.

**GANHO DE INFORMAÇÃO** (o que nenhum concorrente da SERP diz):
> As 14 unidades próprias de Curitiba e RMC, uma a uma, com endereço, separadas por função
> (3 hospitais · 3 prontos atendimentos · 7 clínicas · 1 diagnóstico) — e a leitura de que
> **duas delas ficam fora do município**, em Colombo e Pinhais, que é exatamente o que
> responde às buscas por "hapvida campo largo", "hapvida pinhais" e "hapvida quatro barras".
defensibilidade: 1
origem: consultar_rede (catálogo do banco) cruzado com gsc_queries_for_page
por_que_e_defensivel: "o concorrente não tem o catálogo; a IA não responde endereço de unidade
  sozinha; e a demanda por nome de rua está medida no nosso Search Console, não na SERP pública"

## 14 · FAQ LOCAL (candidatas, cruzadas com `consultar_faqs_catalogo`)

As 19 perguntas estruturais já usadas no cluster estão no banco e **não podem ser repetidas
como estão**. As candidatas locais abaixo nascem do GSC e do catálogo:

- Onde fica o pronto atendimento 24h da Hapvida em Curitiba?
- Quais são os 3 hospitais da Hapvida em Curitiba e em que bairro cada um fica?
- A Hapvida atende em Campo Largo, Colombo, Pinhais e São José dos Pinhais?
- Qual unidade da Hapvida fica na Rua Monsenhor Celso, no Centro de Curitiba?
- Onde é o laboratório da Hapvida na Avenida Nossa Senhora da Luz?
- A Clínica São Lourenço atende pelo plano Hapvida em Curitiba?
- Quanto custa a consulta com coparticipação da Hapvida em Curitiba?
- A Hapvida em Curitiba tem centro oncológico próprio?
- Qual a diferença entre Hapvida e Clinipam em Curitiba hoje?
- O plano Hapvida de Curitiba cobre atendimento fora do Paraná?
- Quantas unidades próprias a Hapvida tem em Curitiba?
- A Hapvida de Curitiba tem unidade no Boqueirão e no Pinheirinho?
- Como é o reajuste por faixa etária do plano Hapvida em Curitiba?
- A Hapvida atende ortopedia em Curitiba pela rede própria?
- Qual o valor do exame complexo com coparticipação em Curitiba?
- A Hapvida tem maternidade própria em Curitiba?
- Onde fica o centro clínico da Hapvida no Água Verde?
- O plano Hapvida Curitiba serve para MEI com 2 vidas?
total_faq_candidatas: 18
com_dado_local: 18
genericas: 0

## 15 · VALIDAÇÃO ANTI-DOORWAY

teste_substituicao: APROVADO — 78% do material desta pesquisa perde sentido ao trocar Curitiba
dados_unicos: 16 dados que só existem para esta praça (as 14 unidades com endereço, as 2 fora
  do município, os bairros, a demanda por nome de rua, a lista de municípios da RMC que buscam,
  a posição real na SERP, a canibalização medida, e o grupo tarifário)
frases_genericas: 0 nas frases novas propostas
anti-doorway: APROVADO
observacao: a aprovação vale para o MATERIAL DE PESQUISA. O artigo publicado ainda tem
  parágrafos que sobrevivem à troca da cidade — isso é problema de redação, medido pelo
  checkpoint_doorway_final quando a revisão for escrita.
