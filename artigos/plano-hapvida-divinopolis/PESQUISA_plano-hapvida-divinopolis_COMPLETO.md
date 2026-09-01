# PESQUISA plano-hapvida-divinopolis — FASE 0 (state file)

Artigo: city (S1-S7) · slug `plano-hapvida-divinopolis` · URL de destino
https://tabelaplanos.com.br/plano-hapvida-divinopolis/
Skill: hapvida-article-builder-v7 (v7.4 lead-herói · v7.2 multiagente)
Cidade: Divinópolis / MG — Oeste de Minas · região intermediária de Divinópolis
Grupo tarifario de coparticipacao: demais_capitais.
Regra de mapeamento, colada da ferramenta consultar_coparticipacao: so existem
dois valores de regiao — "sp_bh" (Sao Paulo, Rio de Janeiro, Belo Horizonte,
RMBH e Betim) e "demais_capitais" (todas as outras cidades). Divinopolis nao
esta na lista fechada do primeiro grupo, entao cai no segundo por definicao da
propria regra, nao por deducao. Shortcodes: [demais_capitais_*].

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
- people_also_ask (PAA) coletados, e a adaptacao local de cada um (a PAA e
  nacional; o que entra na FAQ e a versao ancorada em Divinopolis):
  - PAA "Quanto custa o plano individual da Hapvida" -> vira a FAQ de valor de
    entrada da secao 12, ancorada em Divinopolis
  - PAA "Quais hospitais aceitam o plano de saude Hapvida" -> vira a FAQ de
    unidades proprias da secao 12, ancorada em Divinopolis
  - PAA "Como funciona o plano Hapvida para gestantes" -> vira a FAQ de
    maternidade e parto da secao 12, ancorada em Divinopolis
  - PAA "O plano Hapvida cobre cirurgia de hernia" -> vira a FAQ de cirurgia
    eletiva da secao 12, ancorada em Divinopolis
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
  - pergunta: Onde ficam as unidades proprias da Hapvida em Divinopolis (sub-consulta)
    classificacao: aqui (S4)
  - pergunta: Quanto custa o plano Hapvida em Divinopolis por faixa etaria (sub-consulta)
    classificacao: aqui (S2 de preco)
  - pergunta: O Hospital Santa Monica pertence a Hapvida (sub-consulta)
    classificacao: aqui (S4) e cluster (artigo de hospital)
  - pergunta: A rede de Divinopolis atende quem mora no Centro-Oeste mineiro (sub-consulta)
    classificacao: aqui (S5)
  - pergunta: Hapvida ou Unimed compensa mais em Divinopolis (sub-consulta)
    classificacao: aqui (S6)
  - pergunta: Como funciona a coparticipacao do plano Hapvida em Divinopolis (sub-consulta)
    classificacao: cluster (bridge + link para o pillar de coparticipacao)
  - pergunta: Quais sao as carencias do plano Hapvida em Divinopolis (sub-consulta)
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
- bairros de Divinopolis com estabelecimento de saude registrado: 57 bairros
  distintos no CNES. Os maiores concentradores sao Centro, Santa Clara, Niteroi,
  Sao Jose, Bom Pastor, Catalao, Padre Liberio, Liberdade, Jardim Nova America,
  Afonso Pena, Tiete, Sidil, Sagrada Familia, Realengo, Interlagos, Ponte Funda,
  Santa Rosa, Icarai, Esplanada e Serra Verde. E a materia-prima da S5.
  fonte: CNES/DataSUS, municipio 312230, coleta paginada de 2026-09-01
- ressalva do PIB: o dado de 2021 e o mais recente publicado no agregado 5938
  do IBGE consultado. Se o artigo for revisado depois de nova divulgacao, o
  numero muda — nao deixar o ano implicito no texto.
- regulacao aplicavel citada no artigo: Lei 9.656/98 e normas da ANS
  fonte: ANS — https://www.gov.br/ans/pt-br

---

## 4. Rede assistencial (consultar_rede ANTES da web)

coletado_em: 2026-09-01  # rede

ESTADO DAS PAGINAS OFICIAIS LIDAS (achado do juiz P-A, resolvido): as paginas
de unidade do www2.hapvida.com.br e do gndiminas.com.br sao aplicacoes de
pagina unica. O HTML servido traz, no mesmo arquivo, um bloco de erro
("Parece que esta pagina nao faz mais parte do nosso site") E os dados reais da
unidade. Conferido em 2026-09-01: as tres URLs respondem HTTP 200. Duas paginas
do portal Minas trazem "Razao Social: Teste", o que e placeholder do CMS.
CONSEQUENCIA PARA A REDACAO, INEGOCIAVEL: nunca escrever "opera hoje",
"funciona hoje" ou "atende hoje". A formula e "consta no Guia Medico oficial da
Hapvida em 01/09/2026" ou "registrado no CNES sob o codigo X".

Regra das duas listas, aplicada UNIDADE A UNIDADE (nao em prosa).
Lista A = catalogo proprio da corretora (consultar_rede, cidade Divinopolis,
UF MG): 2 registros, ids 239 e 240. Lista B = Guia Medico oficial + CNES.
Ausencia no catalogo NAO e prova de ausencia na rede.

### Hospital e Maternidade Santa Monica
  endereco: Rua Pedro Ferreira do Amaral, 33 - Padre Liberio, Divinopolis - MG, CEP 35502-562
  tipo: Hospital geral proprio (CNES tipo 5)
  no_catalogo: sim (consultar_rede id 239)
  no_guia_oficial: sim
  cnes: 2159376 | CNPJ 23.772.726/0001-48 | sem motivo de desabilitacao
  turno CNES: ATENDIMENTO CONTINUO DE 24 HORAS/DIA, plantao inclusive sabados, domingos e feriados
  centro cirurgico (CNES): sim
  centro obstetrico (CNES): NAO | centro neonatal (CNES): NAO
  telefone oficial: (37) 2102-5600 (bate com o CNES: 37 21025600)
  fonte: consultar_rede id 239 + Guia Medico oficial https://www2.hapvida.com.br/unidades/hospital-e-maternidade-santa-monica + CNES 2159376, artefato salvo em fontes/cnes-2159376.json
  defensibilidade: 1

### Centro Clinico Santa Monica (Ambulatorio)
  endereco: Rua Pedro Ferreira do Amaral, 33 - Padre Liberio, Divinopolis - MG
  tipo: Centro Clinico proprio, consultas eletivas; segunda a quinta das 07h as 18h, sexta ate as 17h
  no_catalogo: nao | no_guia_oficial: sim
  fonte: Guia Medico oficial, pagina da unidade, leitura de 2026-09-01
  defensibilidade: 2
  pendencia de catalogo: incluir no consultar_rede

### Bioimagem Hospital Santa Monica
  endereco: Rua Pedro Ferreira do Amaral, 33 - Padre Liberio, Divinopolis - MG
  tipo: Imagem e diagnostico, dentro do complexo hospitalar
  no_catalogo: nao | no_guia_oficial: sim
  fonte: Guia Medico oficial, pagina da unidade, leitura de 2026-09-01
  defensibilidade: 2
  pendencia de catalogo: incluir no consultar_rede

### Qualivida Santa Monica
  endereco: Avenida Sete de Setembro, 951 - Centro, Divinopolis - MG, CEP 35500-011
  tipo: unidade de medicina preventiva, fora do complexo, no Centro
  no_catalogo: sim, com OUTRO NOME (consultar_rede id 240 registra "Centro Clinico
  Divinopolis" no mesmo endereco) | no_guia_oficial: sim, como "Qualivida Santa Monica"
  divergencia de nome entre as duas listas: NAO RESOLVIDA. Tratar o NOME como
  [VERIFICAR]; o endereco esta confirmado nas duas listas. No artigo, citar pelo
  endereco e pela funcao, sem cravar o nome comercial.
  fonte: consultar_rede id 240 + portal Hapvida NDI Minas https://www.gndiminas.com.br/unidades/qualivida-santa-monica
  defensibilidade: 1

### Unidade administrativa da operadora — Rua Rio de Janeiro, 101
  endereco: Rua Rio de Janeiro, 101 - Centro, Divinopolis - MG
  tipo: ATENDIMENTO ADMINISTRATIVO E PRESENCIAL — NAO E REDE ASSISTENCIAL.
  Nao entra na contagem de rede propria nem na S4. Cabe na S7, como o endereco
  presencial da operadora na cidade.
  no_catalogo: nao | no_guia_oficial: nao (nao ha pagina de unidade)
  fonte: perfil oficial do Google da operadora, dominio gndiminas.com.br, ficha
  "Unidade Administrativa Minas - Divinopolis", coletada via serp_local em 2026-09-01
  defensibilidade: 4
  ACHADO QUE MUDA A REDACAO: o CNES 146250 (BIOIMAGEM, CNPJ 07.367.674/0002-59)
  registrado NESTE MESMO endereco esta DESABILITADO (motivo 04). Ou seja, o
  servico de diagnostico que ja existiu na Rua Rio de Janeiro, 101 nao esta
  ativo no CNES. E PROIBIDO apresentar este endereco como ponto de exame,
  coleta ou atendimento assistencial. O endereco entra na secao 9 justamente
  para impedir isso.
  fonte: CNES 146250, artefato salvo em fontes/cnes-146250.json

CONTAGEM HONESTA: a rede ASSISTENCIAL propria confirmada em Divinopolis tem
QUATRO unidades — tres no mesmo numero da Rua Pedro Ferreira do Amaral e uma na
Avenida Sete de Setembro. A quinta linha acima e administrativa. Isso fica
ABAIXO do piso de 5 unidades que o checkpoint_fase0 pede para artigo de cidade,
e e material para decisao do usuario, nao para maquiagem: ou o artigo sai com a
excecao declarada, ou a cidade nao comporta o pillar completo. Ver secao 15.

Rede credenciada / retaguarda: mapeada no guia do concorrente e NAO confirmada
em fonte primaria — fica integralmente fora do artigo. Nomes descartados estao
na secao 9.
  fonte: guia medico do concorrente meuplanohap, leitura 2026-09-01 — concorrente nao e fonte

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
    - "Como você quer ser atendido?" (rotulo de formulario, nao e conteudo)
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
    - "Como você quer ser atendido?" (rotulo de formulario, nao e conteudo)
  matriz de cobertura: preco cobre bem, com 16 valores por faixa etaria de
  R$ 97,05 a R$ 754,50 · rede nao cobre · mercado local nao cobre
  ponto fraco: os valores estao escritos a mao no HTML e a pagina declara
  "AS TABELAS DE PRECOS PODEM SOFRER ALTERACAO SEM AVISO PREVIO. ALTERADO EM
  31/03/25" — ou seja, a data existe e e de marco de 2025, mais de um ano antes
  desta coleta. E o unico concorrente que entrega numero, e a fragilidade e a
  idade da tabela, nao a ausencia de data. Nao afirmar que ele "nao diz quando
  atualizou": e falso e o leitor confere com um Ctrl+F.
  fonte: leitura direta da pagina, trecho literal em fontes/rota-tabela.txt
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
    - "Para te ajudar, precisamos saber:" (rotulo de formulario, nao e conteudo)
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

ganho de informacao — nivel de defensibilidade: 2. Rebaixado de 1 para 2 pelo
juiz P-B, com razao: a materia-prima do "campus unico" (tres unidades no mesmo
numero da Rua Pedro Ferreira do Amaral) ja esta publicada no guia do
meuplanohap, que esta na SERP. Descobrir o endereco compartilhado nao e o
ganho. O ganho e o CRUZAMENTO — catalogo proprio da corretora (consultar_rede)
x Guia Medico oficial x CNES — que produz duas coisas que nenhum concorrente
tem: a CORRECAO do erro do lider (ele mistura tres enderecos de Belo Horizonte
dentro de "Enderecos em Divinopolis") e a divergencia de filtro dentro do
proprio site oficial da Hapvida. E dai que sai a frase de venda, nao do
endereco em si.

- LACUNA ACEITA DE PROPOSITO (decisao declarada, nao esquecimento): o lider da
  SERP nomeia cerca de 30 prestadores credenciados de Divinopolis com endereco.
  A nossa pesquisa deixa TODOS de fora porque nenhum foi confirmado em fonte
  primaria — e o guia dele mistura enderecos de Belo Horizonte, o que mostra o
  custo de publicar volume sem conferir. A troca e consciente: menos volume de
  rede credenciada, mais precisao na rede propria. O artigo diz ao leitor que a
  rede credenciada existe e manda ele ao Guia Medico oficial, em vez de listar
  o que nao conferiu. Fica pendencia de verificacao da rede credenciada para a
  proxima atualizacao.

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
- brecha: nenhum trata a abrangencia regional. A regiao imediata de Divinopolis
  (codigo IBGE 310065) tem 20 municipios: Araujos, Camacho, Carmo da Mata,
  Carmo do Cajuru, Claudio, Conceicao do Para, Divinopolis, Itapecerica,
  Itatiaiuca, Itauna, Japaraiba, Lagoa da Prata, Leandro Ferreira, Nova
  Serrana, Pedra do Indaia, Perdigao, Pitangui, Santo Antonio do Monte, Sao
  Goncalo do Para e Sao Sebastiao do Oeste. Nenhuma das cinco paginas responde
  a quem mora neles e usa Divinopolis como polo de saude. O unico que chega
  perto e o meuplanohap, que lista "Hapvida em cidades vizinhas" comecando por
  Nova Serrana.
  fonte: IBGE, API de localidades, regiao imediata 310065
  https://servicodados.ibge.gov.br/api/v1/localidades/regioes-imediatas/310065/municipios
  ATENCAO AO REDATOR: citar municipio da regiao imediata e citar geografia, NAO
  cobertura. A pesquisa NAO confirmou que a rede de Divinopolis atende
  formalmente nenhum deles (ver secao 8). Escrever "polo regional de saude",
  nunca "atende Nova Serrana".
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

  Segundo eixo, reduzido ao que a evidencia sustenta (o juiz P-A mostrou que a
  alegacao original ia longe demais): a Bioimagem Hospital Santa Monica, cujo
  endereco no corpo da pagina e Divinopolis, aparece no filtro do portal
  nacional sob "MG - Uberlandia". Ja o Centro Clinico Santa Monica traz DOIS
  rotulos na mesma pagina — "MG - Divinopolis" e "Varzea Paulista" —, entao
  dele NAO se pode dizer que some do filtro. A alegacao publicavel e sobre a
  Bioimagem, e a licao para o leitor e a mesma: consultar a rede pelo portal
  Hapvida NDI Minas, que atende Minas, e nao so pelo filtro de cidade do portal
  nacional. Nenhum concorrente diz isso.
  defensibilidade: 2
  fonte: www2.hapvida.com.br e https://www.gndiminas.com.br/unidades/hospital-santa-monica-divinopolis, 2026-09-01

- diferenciais unicos de Divinopolis (rotulados para a trava):
  titulo: em Divinopolis hospital, centro clinico e diagnostico da Hapvida ficam no mesmo endereco do Padre Liberio
  titulo: a unica unidade da Hapvida fora do complexo em Divinopolis fica no Centro, na Avenida Sete de Setembro
  titulo: o guia medico que lidera a SERP de Divinopolis mistura tres enderecos de Belo Horizonte
  titulo: Divinopolis e sede de regiao intermediaria, e a rede da cidade e a referencia de quem mora no Oeste de Minas
  titulo: a Unimed concorre em Divinopolis com tres pontos proprios no Centro, todos com endereco no CNES

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
- PARTO E OBSTETRICIA na cidade — onde foi procurado: CNES 2159376 (registra
  centro obstetrico = 0 e centro neonatal = 0), texto oficial da unidade (lista
  o bloco cirurgico em clinica medica, pediatria, ortopedia, ginecologia,
  neurologia, urologia, bucomaxilo, cirurgia geral e plastica, SEM obstetricia)
  e guia do concorrente (tambem sem GO para o hospital). O nome da unidade diz
  "Maternidade", o registro publico nao confirma centro obstetrico.
  E PROIBIDO afirmar que o plano cobre parto em Divinopolis. A FAQ sobre parto
  foi reescrita para a pergunta que a fonte sustenta.
- PRODUTOS COMERCIAIS vendidos em Divinopolis (Nosso Plano, Mix, Pleno, Smart,
  NotreLife, linha regional de Minas) — onde foi procurado: consultar_rede,
  consultar_dados_canonicos, Guia Medico oficial, portal NDI Minas e as cinco
  paginas de concorrente. Nenhuma fonte nomeia produto disponivel na praca. O
  unico nome de produto lido em qualquer fonte e do concorrente ("Adapt 300
  Estadual"), e concorrente nao e fonte. A S3 nao pode ser escrita como a skill
  a especifica: ISTO E DADO PROPRIETARIO DA CORRETORA e tem de vir do usuario.
- ABRANGENCIA CONTRATUAL por produto (municipal, estadual ou nacional) — onde
  foi procurado: Guia Medico oficial, portal NDI Minas, banco. Sem ela nao se
  responde se o plano contratado em Divinopolis atende em Belo Horizonte nem se
  a rede da cidade serve a regiao imediata.
- VALOR DE ENTRADA vigente da tabela de Divinopolis — onde foi procurado:
  cotador_fila (a cidade nao esta na fila; so BH, Fortaleza, Goiania, Recife e
  Sao Paulo). O unico preco existente no dossie e o do concorrente, que esta
  proibido na secao 9. Sem o valor, o lead-heroi da v7.4 nao pode ser escrito.
- LEITOS E CAPACIDADE do Hospital Santa Monica — onde foi procurado: API de
  dados abertos do CNES (nao expoe endpoint de leitos por estabelecimento).
  A skill ja proibe contagem de leitos no texto, entao isso so afeta a S4, que
  perde os paragrafos de capacidade.
- HISTORICO E MARCOS do Hospital Santa Monica (aquisicao, reformas) — onde foi
  procurado: portais oficiais e relacoes com investidores. A linha do tempo que
  a S4 pede NAO tem materia-prima. Substituir por outro recurso visual.
- SEGUNDO CONCORRENTE LOCAL com dado proprio para a S6 — onde foi procurado:
  CNES (so a Unimed aparece com pontos proprios em Divinopolis). A tabela
  comparativa da S6 sai com uma operadora, nao duas.

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
- R PEDRO FERREIRA DO AMARAL 180
- Av. Augusto de Lima, 1126
- AV AUGUSTO DE LIMA 1126
- Av. do Contorno, 8981
- AV DO CONTORNO 8981
- Rua Alvares Maciel, 356
- R ALVARES MACIEL 356
- R BELGICA 50
- R BELGICA 515
- 2.922 beneficiarios
- 2.922 beneficiários
- 150 cirurgioes
- 150 cirurgiões
- 35 enfermeiros
- INCORD
- Centro de Bio Analise
- CENTRO DE BIO ANALISE
- AmorSaude
- AMORSAUDE
- DOM Clinica de Oncologia
- Congregacao das Irmas Hospitaleiras
- Clinica Libelula
- CLINICA LIBELULA
- Centro de Oftalmologia Brasil
- Adapt 300 Estadual
- 493.080/22-1
- 493.081/22-9
- (37) 2102-8100
- 37 2102-8100
- 87 hospitais
- 77 pronto atendimentos
- 318 centro clinicos
- 18 estados
- 15 milhões de clientes
- 280 mil beneficiarios
- 96%
- R$ 97,05
- R$ 125,74
- R$ 131,01
- R$ 154,83
- R$ 169,74
- R$ 183,89
- R$ 200,60
- R$ 238,25
- R$ 239,06
- R$ 309,73
- R$ 310,78
- R$ 402,65
- R$ 404,01
- R$ 523,45
- R$ 582,34
- R$ 754,50
- Rua Rio de Janeiro, 101
- RUA RIO DE JANEIRO 101
- R. Rio de Janeiro, 101

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
- O Hospital Santa Monica de Divinopolis atende gestante pela Hapvida?
  (RESPOSTA LIMITADA: o CNES 2159376 registra centro obstetrico 0 e centro
  neonatal 0, e a lista oficial de especialidades do bloco cirurgico nao traz
  obstetricia. NAO afirmar cobertura de parto na cidade; dizer o que a fonte
  sustenta e mandar o leitor confirmar no Guia Medico)
- Onde faco exame de imagem pela Hapvida sem sair de Divinopolis?
- A Hapvida tem atendimento 24 horas em Divinopolis?
  (RESPOSTA LIMITADA AO CONFIRMADO: 24h so no Hospital e Maternidade Santa
  Monica. NAO generalizar para "a rede atende 24h" — nao ha pronto atendimento
  autonomo confirmado, ver secao 8)
- Qual guia medico devo consultar para ver a rede Hapvida de Divinopolis?
- Qual e o valor de entrada do plano Hapvida para quem mora em Divinopolis?
- O plano contratado em Divinopolis cobre atendimento em Belo Horizonte?
  (BRIDGE: 1-2 frases + link, o mecanismo de abrangencia e do pillar)
- Quem mora na regiao de Divinopolis pode usar a rede da cidade?
  (SEM ABRANGENCIA CONFIRMADA: responder pela geografia — Divinopolis e sede da
  regiao imediata — e mandar conferir a abrangencia do contrato. NAO afirmar
  que a rede atende municipio X)
- A Hapvida tem alguma unidade no Centro de Divinopolis?
- A Unimed de Divinopolis tem rede propria como a do Padre Liberio?
- Cirurgia eletiva pelo plano Hapvida e feita em Divinopolis ou fora dela?
  (o CNES confirma centro cirurgico no Hospital Santa Monica; a lista oficial
  de especialidades do bloco e a fonte. NAO extrapolar para o que nao esta na
  lista)
- Quais especialidades o Centro Clinico Santa Monica atende em Divinopolis?
- Empresa com CNPJ em Divinopolis pode contratar o plano empresarial?
  (BRIDGE: 1-2 frases + link. Ancorar no perfil economico da cidade — polo
  industrial e comercial do Oeste de Minas — ou nao entra)
- O programa Qualivida funciona em Divinopolis e onde fica?
- Quanto se paga de coparticipacao por consulta em Divinopolis?
  (o valor e do grupo tarifario demais_capitais, que Divinopolis divide com
  outros municipios — nao apresentar como preco exclusivo da cidade)
- A Hapvida cobre psiquiatria e saude mental em Divinopolis?
  (BRIDGE: 1-2 frases + link. NAO nomear hospital psiquiatrico: o unico
  candidato da cidade esta em FORBIDDEN_TOKENS por nao ter confirmacao de rede)
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
  13. o guia medico do lider da SERP lista pelo menos cinco enderecos de Belo
      Horizonte sob o titulo "Enderecos em Divinopolis" — um deles, o Centro de
      Oftalmologia Brasil da Av. Augusto de Lima, esta registrado no NOSSO banco
      como retaguarda do artigo de Belo Horizonte
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

## 15. O que trava a redacao e depende do usuario

Rodada 1 de refino do portao de pesquisa concluida. Os dois juizes bloquearam;
os achados que dependiam de coleta foram resolvidos com fonte primaria. Sobram
tres, e nenhum se resolve com mais pesquisa aberta — os tres sao dado que a
corretora tem e a web nao:

1. PRODUTOS COMERCIAIS DA PRACA. Nenhuma fonte publica nomeia o que a Hapvida
   vende em Divinopolis. Sem isso a S3 nao existe e o artigo perde uma das sete
   secoes. E dado de nivel 1: a corretora sabe.
2. VALOR DE ENTRADA E PREFIXO DO SHORTCODE. O artigo e preco-primeiro e abre por
   uma faixa com o preco em 34px. Sem o prefixo cadastrado no plugin e sem o
   valor vigente, nao ha primeira tela.
3. ABRANGENCIA CONTRATUAL POR PRODUTO. Decide tres FAQs e o tratamento da
   regiao imediata na S5.

Ponto de decisao separado, sobre tamanho de rede: a rede ASSISTENCIAL propria
confirmada tem QUATRO unidades — tres no mesmo numero do Padre Liberio e uma na
Avenida Sete de Setembro. A quinta linha da secao 4 e administrativa e esta
rotulada como tal. A skill avisa que cidade sem material local para o piso
"talvez nao comporte um pillar completo" e manda escalar em vez de encher com
conteudo nacional. As saidas honestas sao duas: publicar a city page com a
excecao declarada e a S5 construida sobre o campus unico, ou trocar o
arquetipo para artigo de hospital (HS1-HS4), que a SERP pede com muito mais
volume — "hospital santa monica divinopolis" vale 2.400 buscas por mes contra
260 de "hapvida divinopolis".
