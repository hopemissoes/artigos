# PESQUISA plano-hapvida-divinopolis — FASE 0 (state file)

Artigo: city (S1-S7) · slug `plano-hapvida-divinopolis` · URL de destino
https://tabelaplanos.com.br/plano-hapvida-divinopolis/
Skill: hapvida-article-builder-v7 (v7.4 lead-herói · v7.2 multiagente)
Cidade: Divinópolis / MG — Oeste de Minas · região intermediária de Divinópolis
Grupo tarifário de coparticipação: demais_capitais (Divinópolis nao e BH/RMBH)

---

## 1. SERP real (serp_local)

coletado_em: 2026-09-01  # serp
ferramenta: DataForSeo serp_local · keyword "plano hapvida divinopolis" ·
location_code 2076 (Brasil) · language_code pt · device mobile · depth 20
  fonte: DataForSeo SERP API, task 09011453-1890-0139-0000-84815ff60d1e

limitacao declarada: nao foi usado location_code de cidade porque o geotarget
do Google Ads para Divinopolis nao foi confirmado em duas fontes (o CSV oficial
de geotargets devolveu 404 nas tres URLs testadas). A keyword ja carrega a
cidade, entao a SERP nacional e representativa. Registrado como pendencia.

- posicoes_principal: tabelaplanos.com.br aparece em 9º organico (rank_absolute
  13) — e a HOME (https://tabelaplanos.com.br/), nao uma pagina de cidade.
  Nao existe pagina de Divinopolis no site hoje.
  fonte: serp_local 2026-09-01
- featured_snippet: ausente. formato de snippet: nao ha caixa de resposta
  destacada para a keyword principal. AI Overview estatico ausente (os 4 itens
  de people_also_ask trazem expansao assincrona de IA).
  fonte: serp_local 2026-09-01, item_types = local_pack, people_also_ask,
  organic, people_also_search
- tipo de pagina dominante (checagem SXO): PAGINA DE UNIDADE / GUIA MEDICO
  LOCAL. Dos 14 resultados organicos lidos, 8 sao paginas de unidade ou de guia
  medico (hapvida.com.br, gndiminas.com.br, meuplanohap). Guia de cidade
  completo: nenhum. Implicacao para a arquitetura: a S4 (rede, com endereco)
  precisa vir cedo e ser a secao mais forte; a analise de mercado desce.
- local_pack: 2 fichas, as duas do dominio gndiminas.com.br — "Unidade
  Administrativa Minas - Divinopolis" (R. Rio de Janeiro, 101) e "Hospital
  Santa Monica Divinopolis" (R. Pedro F. Amaral, 33).
- people_also_ask (PAA) coletados:
  - Quanto custa o plano individual da Hapvida?
  - Quais hospitais aceitam o plano de saude Hapvida?
  - Como funciona o plano Hapvida para gestantes?
  - O plano Hapvida cobre cirurgia de hernia?
- people_also_search: Hapvida Divinopolis telefone · trabalhe conosco ·
  endereco · whatsapp · WhatsApp do Hospital Santa Monica · Hospital Santa
  Monica Divinopolis · Bioimagem Divinopolis telefone · Hospital Santa Lucia
  Divinopolis · Hapvida Divinopolis rua rio de janeiro
- canibalizacao: a home do tabelaplanos ocupa a SERP da cidade. Ao publicar a
  city page, checar em D+30 se a home cede a posicao. Registrado na secao 8.

URLs concorrentes (organicos, ordem da SERP):
  - https://www.rotaseguros.com.br/divinopolis/intermedica/index.html
  - https://www.meuplanohap.com.br/guia-medico/mg/divinopolis/
  - https://www.hapvidaconvenio.com.br/plano-de-saude/hapvida-na-cidade-de-divinopolis-mg/
  - https://planosdesaudeintermedica.net.br/divinopolis/

---

## 2. Kit on-page [V5]

- principal: kw: plano hapvida divinopolis | volume: sem dado no Labs (cauda
  longa) | variacao-mae medida: "hapvida divinopolis" = 260 buscas/mes,
  keyword_difficulty 0, competition LOW, cpc R$ 1,70, tendencia anual +24%
  fonte: DataForSeo keyword_suggestions/keyword_data, coleta 2026-09-01

- matriz de posicionamento (principal em todas as 6 posicoes):
  H1: Plano Hapvida Divinopolis: rede propria, precos e onde e atendido
  title: Plano Hapvida Divinopolis: toda a rede propria no Padre Liberio
  url: /plano-hapvida-divinopolis/
  meta: Plano Hapvida Divinopolis [ano_atual]: as unidades proprias da cidade,
  com endereco conferido no guia oficial, e valores a partir de R$ por faixa.
  1o paragrafo: sim (lead-heroi v7.4)
  H2 com a principal: sim (H2 de preco e H2 de rede)

- secundarias:
  - kw: hapvida divinopolis | volume: 260 | intencao: informacional-de-compra
    local | veredito: qualificada | onde entra: H2 de rede (S4) e lead
  - kw: plano de saude divinopolis | volume: 70 | intencao: comercial |
    veredito: qualificada | onde entra: H2 de mercado local (S6)
  - kw: plano de saude unimed divinopolis | volume: 20 | intencao: comercial
    comparativa | veredito: qualificada | onde entra: S6 (comparativo local)
  - kw: plano de saude hospital santa monica divinopolis | volume: 10 |
    intencao: comercial (quer o hospital na rede) | veredito: qualificada |
    onde entra: H3 dentro da S4
  - kw: plano de saude notredame divinopolis | volume: 10 | intencao:
    comercial | veredito: qualificada | onde entra: S3 (produtos locais)
  - kw: plano de saude em divinopolis | volume: 10 | intencao: comercial |
    veredito: qualificada | onde entra: S1
  - kw: hospital santa monica divinopolis atende unimed | volume: 10 |
    intencao: comercial comparativa | veredito: qualificada | onde entra: FAQ
  - kw: hospital santa monica divinopolis | volume: 2400 | intencao:
    navegacional | veredito: qualificada como CLUSTER, nao para esta pagina —
    comporta artigo de hospital proprio (HS1-HS4)
    fonte: DataForSeo keyword_suggestions 2026-09-01

- secundarias DESCARTADAS por veto de intencao (trafego de quem ja e cliente
  ou nunca sera): hapvida divinopolis telefone · hapvida divinopolis trabalhe
  conosco · hapvida divinopolis endereco · hospital santa monica divinopolis
  trabalhe conosco · hospital santa monica divinopolis curriculo · bioimagem
  divinopolis resultados · hospital santa monica divinopolis vagas
  fonte: DataForSeo related_keywords 2026-09-01

- cluster_candidatas (viram pendencia de pauta no banco, apos aprovacao):
  - hospital santa monica divinopolis (2400/mes) — artigo de hospital HS1-HS4
  - bioimagem divinopolis (590/mes) — pauta de diagnostico/exames
  - hospital santa monica nova serrana (210/mes) — pauta de cidade vizinha

- query fan-out (sub-perguntas que a busca com IA gera a partir da principal):
  - pergunta: Onde ficam as unidades proprias da Hapvida em Divinopolis?
    classificacao: aqui (S4)
  - pergunta: Quanto custa o plano Hapvida em Divinopolis por faixa etaria?
    classificacao: aqui (S2 de preco)
  - pergunta: O Hospital Santa Monica pertence a Hapvida?
    classificacao: aqui (S4) e cluster (artigo de hospital)
  - pergunta: A rede de Divinopolis atende quem mora no Centro-Oeste mineiro?
    classificacao: aqui (S5)
  - pergunta: Hapvida ou Unimed compensa mais em Divinopolis?
    classificacao: aqui (S6)
  - pergunta: Como funciona a coparticipacao do plano Hapvida em Divinopolis?
    classificacao: cluster (bridge + link para o pillar de coparticipacao)
  - pergunta: Quais sao as carencias do plano Hapvida em Divinopolis?
    classificacao: cluster (bridge + link para o pillar de carencias)

---

## 3. Contexto local (IBGE / CNES / DATASUS)

- populacao: 231.091 habitantes (Censo 2022)
  fonte: IBGE, agregado 4714, variavel 93, municipio 3122306
  https://servicodados.ibge.gov.br/api/v3/agregados/4714/periodos/2022/variaveis/93
- PIB municipal: R$ 8.328.420 mil (2021)
  fonte: IBGE, agregado 5938, variavel 37, municipio 3122306
- posicao regional: sede da regiao intermediaria e da regiao imediata de
  Divinopolis, mesorregiao Oeste de Minas
  fonte: IBGE, API de localidades, municipio 3122306
  https://servicodados.ibge.gov.br/api/v1/localidades/municipios/3122306
- leitos / CNES: a cidade tem hospitais gerais (CNES tipo 5) de perfis
  distintos — Hospital Sao Joao de Deus (Rua do Cobre, 800), Hospital Sao
  Judas Tadeu (Cel. Joao Notini, 150), Hospital Sao Bento Menni (Barao de
  Cocais, 10 — psiquiatrico), Hospital Universitario da UFSJ (Sgt. Henrique
  Loureiro, 550) e o Hospital e Maternidade Santa Monica, CNES 2159376, unico
  hospital geral vinculado a operadora verticalizada.
  fonte: CNES/DataSUS, API de dados abertos, municipio 312230
  https://apidadosabertos.saude.gov.br/cnes/estabelecimentos
- concorrencia local instalada: Unimed com tres pontos proprios no Centro —
  Unimed Nucleo de Atencao a Saude (Getulio Vargas, 808), Nucleo de
  Especialidades Unimed (Getulio Vargas, 1045) e Unimed Divinopolis Medicina
  Ocupacional (Primeiro de Junho, 1063).
  fonte: CNES/DataSUS, municipio 312230, consulta 2026-09-01
- regulacao aplicavel citada no artigo: Lei 9.656/98 e normas da ANS
  fonte: ANS — https://www.gov.br/ans/pt-br

---

## 4. Rede assistencial (consultar_rede ANTES da web)

coletado_em: 2026-09-01  # rede

Regra das duas listas aplicada. Lista A = catalogo proprio (`consultar_rede`,
cidade Divinopolis, UF MG): 2 unidades. Lista B = Guia Medico oficial
(www2.hapvida.com.br e gndiminas.com.br) + CNES: 5 pontos distintos. Ausencia
no catalogo NAO e prova de ausencia na rede — as unidades que so aparecem na
lista B entram no artigo atribuidas ao guia oficial, e o catalogo recebe
pendencia de atualizacao.

### Hospital e Maternidade Santa Monica
  endereco: Rua Pedro Ferreira do Amaral, 33 - Padre Liberio, Divinopolis - MG, CEP 35502-562
  tipo: Hospital proprio, atendimento 24 horas, com maternidade e bloco cirurgico
  fonte: consultar_rede (id 240/239, catalogo do banco) + Guia Medico oficial https://www2.hapvida.com.br/unidades/hospital-e-maternidade-santa-monica + CNES 2159376
  defensibilidade: 1

### Centro Clinico Santa Monica (Ambulatorio)
  endereco: Rua Pedro Ferreira do Amaral, 33 - Padre Liberio, Divinopolis - MG
  tipo: Centro Clinico proprio (consultas eletivas); segunda a quinta das 07h as 18h, sexta ate as 17h
  fonte: Guia Medico oficial Hapvida, pagina da unidade, consulta 2026-09-01
  defensibilidade: 2

### Bioimagem Hospital Santa Monica
  endereco: Rua Pedro Ferreira do Amaral, 33 - Padre Liberio, Divinopolis - MG
  tipo: Imagem e Diagnostico, dentro do complexo hospitalar
  fonte: Guia Medico oficial Hapvida, pagina da unidade, consulta 2026-09-01
  defensibilidade: 2

### Qualivida Santa Monica
  endereco: Avenida Sete de Setembro, 951 - Centro, Divinopolis - MG, CEP 35500-011
  tipo: unidade de medicina preventiva no Centro; consta no catalogo do banco como Centro Clinico Divinopolis, mesmo endereco
  fonte: consultar_rede (id 240) + portal Hapvida NDI Minas https://www.gndiminas.com.br/unidades/qualivida-santa-monica
  defensibilidade: 1

### Ponto Hapvida no Centro — Rua Rio de Janeiro, 101
  endereco: Rua Rio de Janeiro, 101 - Centro, Divinopolis - MG
  tipo: endereco de atendimento presencial e de servico de diagnostico; consta no CNES como BIOIMAGEM, estabelecimento 146250
  fonte: CNES/DataSUS, municipio 312230, consulta 2026-09-01 (perfil oficial gndiminas no local pack indica o mesmo numero)
  defensibilidade: 4
  [VERIFICAR] a natureza atual do atendimento neste endereco (administrativo, coleta, ou os dois). No artigo, citar como endereco de atendimento presencial da operadora na cidade, atribuido ao guia oficial, sem afirmar servico que nao foi confirmado.

Divergencia registrada, e ela e util ao leitor: o proprio site nacional
classifica a Bioimagem Hospital Santa Monica sob o filtro "MG - Uberlandia" e
o Centro Clinico Santa Monica sob "Varzea Paulista", com o endereco correto de
Divinopolis no corpo da pagina. Quem filtra por cidade no portal nacional
perde unidade que existe.
  fonte: www2.hapvida.com.br, paginas das duas unidades, consulta 2026-09-01

Rede credenciada / retaguarda mapeada no guia do concorrente e ainda NAO
confirmada em fonte primaria — tratada como [VERIFICAR], fica fora do artigo
ate confirmacao: INCORD, Centro de Bio Analise, Clinica AmorSaude Divinopolis,
DOM Clinica de Oncologia, Congregacao das Irmas Hospitaleiras (Sao Bento
Menni), Clinica Libelula.
  fonte: guia medico do concorrente meuplanohap, leitura 2026-09-01 — concorrente nao e fonte

---

## 5. Desmontagem de concorrentes [V4 / CI-1]

Escada de rotas: rota 1 (WebFetch) testada e viva; a leitura efetiva foi feita
pela rota 2 (curl com user-agent de navegador), que devolve o HTML inteiro e
permite copiar o heading literal. Nenhum concorrente entrou por indice de
buscador. Arquivos salvos em `artigos/plano-hapvida-divinopolis/fontes/`.

### Concorrente 1 — Rota Seguros, pagina de cidade
- https://www.rotaseguros.com.br/divinopolis/intermedica/index.html
  coletado_em: 2026-09-01
  rota: curl
  palavras: 834
  h2_literais:
    - "Hapvida NDI/GNDI Minas | Divinópolis"
    - "Saiba tudo sobre a fusão das gigantes da saúde, Hapvida e GNDI."
    - "Perguntas e respostas"
  h3_literais:
    - "Como você quer ser atendido?"
    - "Diferenciais Hapvida NDI para você!"
  matriz de cobertura: preco cobre mal · rede cobre mal (so o endereco da
  propria corretora, Av. Getulio Vargas, 1000) · modalidades cobre bem ·
  contratacao cobre bem · mercado local nao cobre · unidade por unidade nao
  cobre · coparticipacao nao cobre
  ponto fraco: a pagina e sobre a fusao Hapvida+GNDI, nao sobre Divinopolis;
  troque a cidade e o texto continua valendo inteiro
  fonte: leitura direta da pagina, arquivo fontes/rota-index.html

### Concorrente 2 — Rota Seguros, pagina de tabela de precos
- https://www.rotaseguros.com.br/divinopolis/intermedica/tabela-de-precos.html
  coletado_em: 2026-09-01
  rota: curl
  palavras: 510
  h2_literais:
    - "Tabela de Preços Hapvida NDI - Divinópolis"
    - "Plano de Saúde Individual (Adesão)"
    - "Planos de Saúde Empresariais"
  h3_literais:
    - "Como você quer ser atendido?"
  matriz de cobertura: preco cobre bem, com 16 valores por faixa etaria de
  R$ 97,05 a R$ 754,50 · rede nao cobre · mercado local nao cobre
  ponto fraco: os valores estao escritos a mao no HTML, sem data de vigencia
  visivel — desatualizam em silencio a cada reajuste. E o unico concorrente que
  entrega numero, e e justamente onde ele fica vulneravel
  fonte: leitura direta da pagina, arquivo fontes/rota-tabela.html

### Concorrente 3 — Meu Plano Hap, guia medico de Divinopolis
- https://www.meuplanohap.com.br/guia-medico/mg/divinopolis/
  coletado_em: 2026-09-01
  rota: curl
  palavras: 1378 (lider de cobertura da SERP)
  h2_literais:
    - "🏥 Endereços em Divinopolis"
    - "Dúvidas Frequentes"
    - "Orçamento Online"
    - "Opinião dos nossos clientes"
    - "Hapvida em cidades vizinhas"
  h3_literais:
    - "Para te ajudar, precisamos saber:"
  matriz de cobertura: rede cobre bem em volume (lista prestadores com endereco
  e especialidade) · preco nao cobre · modalidades nao cobre · mercado local
  nao cobre · coparticipacao nao cobre
  ponto fraco medido: sob o titulo "Enderecos em Divinopolis" a lista traz
  enderecos que nao sao de Divinopolis — Av. Augusto de Lima 1126 (Barro
  Preto), Av. do Contorno 8981 (Gutierrez) e R. Alvares Maciel 356 (Santa
  Efigenia) sao de Belo Horizonte. Alem disso nao separa rede propria de
  credenciada, o que e a distincao que muda a decisao de compra
  fonte: leitura direta da pagina, arquivo fontes/concorrente-meuplanohap.com.br-20260901.html

### Concorrente 4 — Hapvida Convenio
- https://www.hapvidaconvenio.com.br/plano-de-saude/hapvida-na-cidade-de-divinopolis-mg/
  coletado_em: 2026-09-01
  rota: curl
  palavras: 900
  h1_literal: "HAPVIDA NA CIDADE DE DIVINÓPOLIS MG"
  h2_literais:
    - "Fale agora com a equipe de vendas"
    - "Mapa do Site"
    - "Atendimento"
  matriz de cobertura: nao cobre rede · nao cobre preco · nao cobre mercado
  local · cobre mal modalidades · cobre mal telemedicina
  ponto fraco: zero dado verificavel — nenhum endereco, nenhum nome de unidade,
  nenhum numero. Empresa sediada em Ribeirao Preto/SP. O rodape ainda carrega
  links para dominios sem relacao com saude
  fonte: leitura direta da pagina, arquivo fontes/concorrente-hapvidaconvenio.com.br-20260901.html

### Concorrente 5 — Planos de Saude Intermedica
- https://planosdesaudeintermedica.net.br/divinopolis/
  coletado_em: 2026-09-01
  rota: curl
  palavras: 858
  h2_literais:
    - "Acesso Rápido"
    - "Intermédica no seu Estado"
  h3_literais:
    - "Intermédica Saúde Divinópolis"
    - "Intermédica Saúde Individual Divinópolis"
    - "Intermédica Saúde Familiar Divinópolis"
    - "Intermédica Saúde PME Divinópolis"
    - "Intermédica Saúde Empresarial Divinópolis"
    - "Diferenciais Intermédica Saúde Divinópolis"
  matriz de cobertura: nao cobre rede · nao cobre preco · nao cobre mercado
  local · cobre mal modalidades
  ponto fraco: template estadual com o nome da cidade injetado nos H3; o corpo
  fala do GNDI nacional. O rodape cita servico da SulAmerica, sinal de texto
  reaproveitado sem revisao
  fonte: leitura direta da pagina, arquivo fontes/concorrente-planosdesaudeintermedica.net.br-20260901.html

Linha de profundidade (piso dinamico): lider de cobertura = meuplanohap, com
1.378 palavras e 5 subtopicos de conteudo. Nosso piso passa a ser cobrir os
must-match abaixo e superar 5 subtopicos com material local — o piso fixo do
checkpoint_completude (8 H2, 12 FAQ, 1.200 palavras) segue como minimo absoluto.

---

## 6. Ganho de informacao / brechas [V4 / CI-2]

- must-match (o que 2 ou mais concorrentes cobrem e nao podemos faltar):
  tabela de preco por faixa etaria · enderecos da rede na cidade · modalidades
  disponiveis (individual/adesao, PME, empresarial) · como contratar e cotar ·
  FAQ · atendimento por telemedicina.

- brecha: nenhum dos cinco separa REDE PROPRIA de REDE CREDENCIADA. O guia do
  lider mistura as duas e ainda mistura cidade, o que faz o leitor achar que a
  Hapvida tem em Divinopolis uma capilaridade que ela nao tem — e tambem o
  contrario, ignorar o que ela de fato tem.
- brecha: nenhum descreve o mercado de saude de Divinopolis. A cidade e polo
  macrorregional com hospital filantropico de referencia e Unimed com tres
  pontos proprios no Centro; nenhum concorrente cita isso.
- brecha: nenhum trata a abrangencia regional — quem mora em Nova Serrana,
  Claudio, Carmo do Cajuru ou Santo Antonio do Monte e usa Divinopolis como
  polo de saude nao encontra resposta em nenhuma das cinco paginas.
- brecha: o unico que da preco escreve o numero no HTML, sem vigencia. Nossa
  tabela por shortcode e sempre a vigente, e isso pode ser dito.
- brecha: nenhum explica em qual guia medico o cliente de Divinopolis deve
  procurar a rede.

- GANHO DE INFORMACAO (a coisa que nenhum concorrente da SERP diz):
  Em Divinopolis a rede propria da Hapvida e um CAMPUS UNICO — hospital,
  centro clinico e diagnostico no mesmo numero da Rua Pedro Ferreira do
  Amaral, no Padre Liberio — mais um ponto no Centro. Consequencia pratica que
  ninguem escreveu: internacao, consulta eletiva e exame de imagem resolvem no
  mesmo endereco, o que muda o calculo de deslocamento de quem mora longe do
  Padre Liberio; e o guia medico do lider da SERP leva o leitor a tres
  enderecos de Belo Horizonte apresentados como se fossem de Divinopolis.
  dado_proprietario: cruzamento do catalogo de rede da corretora
  (consultar_rede) com o Guia Medico oficial e com o CNES, unidade a unidade
  defensibilidade: 1
  fonte: consultar_rede + www2.hapvida.com.br + CNES 2159376, 2026-09-01

  Segundo eixo, do mesmo cruzamento: a operacao de Divinopolis e servida pelo
  portal Hapvida NDI Minas, e as duas bases oficiais divergem entre si — o
  portal nacional arquiva duas unidades de Divinopolis sob filtros de outras
  cidades. Dizer ao leitor onde consultar a rede e informacao que nenhum
  concorrente da.
  defensibilidade: 2
  fonte: www2.hapvida.com.br e https://www.gndiminas.com.br/unidades/hospital-santa-monica-divinopolis, 2026-09-01

---

## 7. Dado proprietario [V7.2] (consultar_rede · cotador_fila · banco)

- dado_proprietario: catalogo de rede da corretora para Divinopolis, com o
  Hospital Santa Monica marcado como unidade que gera imagem de tabela
  defensibilidade: 1
  fonte: consultar_rede, cidade Divinopolis, UF MG, registros 239 e 240
- dado_proprietario: valores canonicos de coparticipacao do grupo
  demais_capitais, aplicavel a Divinopolis — consulta eletiva, urgencia, exame
  simples, exame complexo, terapia e demais
  defensibilidade: 1
  fonte: consultar_coparticipacao, regiao demais_capitais
- dado_proprietario: numeros canonicos da rede Hapvida — 86 hospitais
  proprios, 80 prontos atendimentos 24h, 16 estados, 11 programas Qualivida
  defensibilidade: 1
  fonte: consultar_dados_canonicos
- dado_proprietario: mapa de saturacao de destinos internos, que decide para
  onde este artigo pode linkar sem inflar pillar ja saturado
  defensibilidade: 2
  fonte: consultar_saturacao_destinos, 2026-09-01
- dado_proprietario: catalogo de FAQs ja usadas, para nao repetir pergunta de
  outro artigo do cluster
  defensibilidade: 2
  fonte: consultar_faqs_catalogo, categoria geografia
- consultar_rede: executado antes de qualquer busca na web, conforme a regra
  das duas listas da secao 4
- cotador_fila: nao consultado nesta rodada. Divinopolis nao estava na fila de
  cotacao no momento da pesquisa; a tabela do artigo sai por shortcode.

---

## 8. Nao encontrado [V7.2]

nao_encontrado:
- geotarget do Google Ads para Divinopolis — onde foi procurado: CSV oficial de
  geotargets do Google (tres URLs, todas 404), busca na web e espelhos em
  repositorio publico. Consequencia: serp_local rodado em location_code 2076.
- pronto atendimento 24h autonomo, fora do complexo hospitalar — onde foi
  procurado: consultar_rede, Guia Medico oficial, portal Hapvida NDI Minas.
  Nao afirmar que existe nem que nao existe.
- numero de beneficiarios da Hapvida em Divinopolis — onde foi procurado:
  consultar_dados_canonicos e portais oficiais. O concorrente meuplanohap cita
  um numero, que nao foi confirmado em fonte primaria e por isso esta na lista
  de tokens proibidos.
- confirmacao de que a rede de Divinopolis atende formalmente Nova Serrana e
  demais cidades da regiao imediata — onde foi procurado: Guia Medico oficial e
  portal NDI Minas. O artigo trata abrangencia regional sem cravar municipio.
- data da entrada da Hapvida em Divinopolis e historico da aquisicao do
  Hospital Santa Monica — onde foi procurado: portais oficiais e relacoes com
  investidores. Sem fonte primaria, fica fora.
- posicao do tabelaplanos em uma SERP geolocalizada em Divinopolis — onde foi
  procurado: DataForSeo, bloqueado pela ausencia do geotarget acima.

---

## 9. FORBIDDEN_TOKENS

FORBIDDEN_TOKENS:
- Hospital Sao Joao de Deus
- Hospital São João de Deus
- Hospital Sao Judas Tadeu
- Hospital São Judas Tadeu
- Hospital Sao Bento Menni
- Hospital São Bento Menni
- Hospital Santa Lucia
- Hospital Santa Lúcia
- Hospital Santa Monica Nova Serrana
- Rua Pedro Ferreira do Amaral, 180
- Av. Augusto de Lima, 1126
- Av. do Contorno, 8981
- Rua Alvares Maciel, 356
- 2.922 beneficiarios
- 150 cirurgioes
- 35 enfermeiros

## 10. PLANO_MODELOS [V7.2]

MODO: multimodelo
- 22 roteador: forte
- 1 SERP e tipo de pagina: medio
- CI-1 desmontagem: forte (travado)
- 2 rede: medio
- 3 contexto local: barato
- 4 keywords e fan-out: barato
- CI-2 ganho de informacao: forte (travado)
- 5 sintese e fio condutor: forte (travado)
- 6 conferente de fatos: forte (travado), modelo distinto do agente 2
- 7 conferente DataForSeo: barato, modelo distinto do agente 4
- 23 juiz de pesquisa P-A: forte (travado), modelo distinto do agente 5
- 24 juiz de pesquisa P-B: forte (travado), modelo distinto do 23
- 8/9/10 redatores dos blocos A/B/C: A forte, B e C medio
- 11 editor-chefe: forte (travado), modelo distinto dos redatores
- 19 voz humana: medio, modelo distinto do agente 11
- 20 imagem da tabela: barato
- 12 veracidade: forte (travado)
- 13 anti-doorway: forte (travado), modelo distinto do agente 5
- 14 requisitos: medio
- 15 citabilidade GEO: forte (travado)
- 16a/16b/16c painel de juizes: forte, em ao menos 2 modelos distintos, com ao
  menos 1 juiz em modelo diferente do editor-chefe
- 21 varredura final anti-doorway: forte (travado), modelo distinto do 13
- 17 schema: medio · 18 registro no banco: barato
Rebaixamentos: nenhum.

## 11. Datas de coleta

coletado_em: 2026-09-01  # serp
coletado_em: 2026-09-01  # rede
coletado_em: 2026-09-01  # concorrentes
coletado_em: 2026-09-01  # banco supabase
coletado_em: 2026-09-01  # ibge e cnes

## 12. FAQ local

- Quais unidades proprias da Hapvida existem hoje em Divinopolis?
- O Hospital e Maternidade Santa Monica faz parte da rede propria da Hapvida?
- O plano Hapvida de Divinopolis tem maternidade e parto na propria cidade?
- Onde faco exame de imagem pela Hapvida sem sair de Divinopolis?
- A Hapvida tem atendimento 24 horas em Divinopolis?
- Qual guia medico devo consultar para ver a rede Hapvida de Divinopolis?
- Quanto custa o plano Hapvida em Divinopolis por faixa etaria?
- O plano contratado em Divinopolis cobre atendimento em Belo Horizonte?
- Quem mora na regiao de Divinopolis pode usar a rede da cidade?
- A Hapvida tem alguma unidade no Centro de Divinopolis?
- Compensa mais Hapvida ou Unimed para quem mora em Divinopolis?
- O plano Hapvida atende no Hospital Universitario da UFSJ em Divinopolis?
- Quais especialidades o Centro Clinico Santa Monica atende em Divinopolis?
- Empresa com CNPJ em Divinopolis pode contratar o plano empresarial?
- O programa Qualivida funciona em Divinopolis e onde fica?
- Quanto se paga de coparticipacao por consulta em Divinopolis?
- A Hapvida cobre psiquiatria e saude mental em Divinopolis?
- Preciso ir ate o Padre Liberio para tudo ou resolvo consulta no Centro?

## 13. Anti-doorway

- teste_substituicao: aplicado secao a secao trocando Divinopolis por Uberaba e
  por Betim. As sete secoes previstas perdem sentido na troca: a S4 depende do
  campus unico do Padre Liberio, a S5 depende da regiao imediata de
  Divinopolis, a S6 depende da Unimed local e do perfil de polo macrorregional,
  a S2 depende do grupo tarifario demais_capitais aplicado a esta praca.
- dados_unicos: 14 dados que so valem em Divinopolis, listados a seguir
  1. Hospital e Maternidade Santa Monica, Rua Pedro Ferreira do Amaral, 33, Padre Liberio
  2. Centro Clinico Santa Monica no mesmo endereco, com horario de segunda a sexta
  3. Bioimagem Hospital Santa Monica no mesmo complexo
  4. Qualivida Santa Monica na Avenida Sete de Setembro, 951, Centro
  5. ponto de atendimento na Rua Rio de Janeiro, 101, Centro
  6. CNES 2159376 do Hospital Santa Monica
  7. populacao de 231.091 habitantes pelo Censo 2022
  8. PIB municipal de R$ 8.328.420 mil em 2021
  9. condicao de sede da regiao intermediaria e imediata de Divinopolis
  10. Unimed com tres pontos proprios no Centro, com endereco
  11. presenca do Hospital Universitario da UFSJ na cidade
  12. divergencia de catalogo do portal nacional para duas unidades da cidade
  13. o guia medico do lider da SERP mistura tres enderecos de Belo Horizonte
  14. a busca local por hospital santa monica divinopolis vale 2.400 por mes,
      quase dez vezes a busca por hapvida divinopolis
- frases_genericas: zero previstas. Discurso de operadora (modelo
  verticalizado, rede propria sempre que possivel, custo competitivo,
  atendimento humanizado) e conteudo nacional (mecanica de coparticipacao,
  prazos de carencia, passos de contratacao, lista de documentos) sai por
  bridge de 1 a 2 frases com link para o pillar, nunca como paragrafo.
- FAQ cruzada com consultar_faqs_catalogo, categoria geografia: nenhuma
  pergunta do catalogo entra em forma reaproveitada. As perguntas de
  abrangencia regional e de atendimento em outra cidade sao reescritas com
  ancora em Divinopolis e na regiao imediata.
- anti-doorway: APROVADO

## 14. Fio condutor

Divinopolis nao tem rede espalhada: tem um campus. Hospital, centro clinico e
diagnostico da Hapvida ficam no mesmo numero da Rua Pedro Ferreira do Amaral,
no Padre Liberio, mais um ponto no Centro — e e isso que decide se o plano
serve para voce, porque muda o deslocamento, nao a mensalidade. O artigo
inteiro responde a uma pergunta pratica: onde voce vai ser atendido, de fato,
nesta cidade — e por que o guia medico que aparece primeiro no Google leva
voce a enderecos de Belo Horizonte.
