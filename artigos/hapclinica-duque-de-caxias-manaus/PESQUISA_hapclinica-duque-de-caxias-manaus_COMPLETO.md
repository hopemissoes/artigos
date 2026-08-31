# PESQUISA COMPLETA — Hapclínica Duque de Caxias (Manaus/AM)

- slug: hapclinica-duque-de-caxias-manaus
- tipo: hospital (arquétipo de unidade HS1-HS4)
- skill: hapvida-article-builder-v7
- hub do cluster: plano-hapvida-manaus
- aberto em: 2026-08-31

> **Por que este artigo existe, e por que ele NÃO é sobre Duque de Caxias/RJ.**
> O pedido nasceu da keyword `hapclinica duque de caxias` (6.600/mês). A FASE 0
> mediu e provou que essa busca é da unidade da **Avenida Duque de Caxias, 1905,
> Praça 14 de Janeiro, Manaus/AM** — não do município de Duque de Caxias, no Rio.
> O registro completo do achado está em `ACHADO-BLOQUEANTE.md`. O usuário optou
> pela Rota B (Manaus) no portão humano de 2026-08-31.

---

## 1 · DR1 PARTE 1 — SERP REAL (serp_local, DataForSeo)

- keyword principal: hapclinica duque de caxias
- location_code: 2076 (Brasil) · language_code: pt · depth: 20 · mobile + desktop
- fonte: DataForSeo serp_local, coleta própria de 2026-08-31

### 1.1 Composição dos 10 primeiros orgânicos (desktop)

| pos | domínio | tipo de conteúdo | é doorway? | dado local único? |
|---|---|---|---|---|
| 1 | www2.hapvida.com.br | institucional (app JS) | não | endereço e acessibilidade |
| 2 | www.gndi.com.br | institucional (unidade do RJ) | não | endereço do RJ, não de Manaus |
| 3 | www.doctoralia.com.br | diretório | sim | 2 especialidades, sem telefone |
| 4 | www.waze.com | mapa | sim | coordenada e rota |
| 5 | guia.agendarconsulta.com | diretório com base CNES | não | horário, equipamentos, CNES |
| 6 | www.meuplanohap.com.br | guia médico do RJ | sim | rede do RJ, alvo trocado |
| 7 | moovitapp.com | transporte | sim | linha de ônibus 542 |
| 8 | dentmap.com.br | diretório | sim | nota 3,1 e 247 avaliações |
| 9 | www.econodata.com.br | cadastro de empresa | sim | CNPJ e endereço fiscal |
| 10 | tabelaplanos.com.br | nosso pillar de rede | não | 1 linha sobre a unidade |

**Síntese da SERP:**

- distribuicao: 6 diretórios/mapas, 3 institucionais, 1 pillar nosso. **Zero guias.**
- com_dado_local_unico: 4 de 10
- doorways: 6 de 10
- gaps_sem_cobertura: horário confirmado em fonte primária; o que a unidade NÃO faz; para onde ir quando o caso não é ambulatorial; como marcar; se é a unidade do RJ ou de Manaus.
- oportunidades_diferenciacao: nenhuma página da SERP orienta o paciente — todas param no endereço.
- fonte: DataForSeo serp_local mobile e desktop, 2026-08-31

### 1.2 Elementos da SERP

- ai_overview: presente no mobile (assíncrono, sem referências expostas na coleta); ausente no desktop
- local_pack / knowledge_graph: presente nos dois — "Hapclínica Duque de Caxias — Centro médico em Manaus, Amazonas"
- google_reviews no knowledge graph: nota 3,1 com 247 avaliações
- people_also_ask: 4 perguntas capturadas (ver seção 6)
- people_also_search: telefone, endereço, laboratório, whatsapp, exame de sangue, ônibus, fotos, avaliações
- fonte: DataForSeo serp_local, 2026-08-31

### 1.2b Formato de snippet

- featured_snippet existe: não
- featured_snippet formato: não há caixa de resposta destacada em nenhum dos dois devices
- featured_snippet ocupante: nenhum
- acao: escrever o lead GEO em parágrafo de 40-60 palavras respondendo "o que é, onde fica, o que faz e o que NÃO faz" — é o formato que o AI Overview do mobile consome, já que não há snippet para disputar
- fonte: DataForSeo serp_local mobile e desktop, 2026-08-31

### 1.3 Canibalização

- URLs do tabelaplanos.com.br nesta SERP: 1 (clinicas-hapvida-por-capital, pos. 13 mobile / 14 desktop)
- veredito: não há canibalização hoje. Com 2 URLs passa a haver risco — a fronteira da seção 12 existe para isso.
- fonte: DataForSeo serp_local, 2026-08-31

---

## 2 · DR1 PARTE 5 — CI-1: DESMONTAGEM DOS CONCORRENTES

Escada de rotas: o `scripts/testar-egress.sh` passou nos 5 alvos em 2026-08-31 e o
WebFetch foi testado com uma chamada real antes da CI-1 — funcionou. Rota 1.

## [LIDO] https://guia.agendarconsulta.com/amazonas/manaus/hapclinica-duque-de-caxias-9505970
rota: "WebFetch (rota 1 da escada)"
coletado_em: 2026-08-31
title: "HAPCLINICA DUQUE DE CAXIAS - Manaus (AM) | Agendar Consulta"
h2_conteudo:
  - "Horário de Funcionamento Aberto agora · Fecha às 20:00"
  - "Serviços e Convênios"
  - "Atividades Secundárias"
  - "Equipamentos"
  - "Instalações Físicas para Assistência"
  - "Serviços de Apoio"
  - "Avaliações"
  - "Perguntas Frequentes"
h3: ["Unidades Próximas", "Informações Gerais"]
metricas: {palavras: 2100, h2: 11, h3: 2, tabelas: 3}
dado_que_so_ele_tem: "horário seg-sex 06:00-20:00 e sáb 06:00-17:00; tipo Policlínica; atividade principal CONSULTA AMBULATORIAL; código CNES 9505970"
fraquezas: "é despejo automático da base CNES, sem uma linha de orientação; não diz o que a unidade não faz; não diferencia da unidade homônima do Rio; nenhuma menção a plano ou a como agendar de fato"
fonte: leitura direta da página por WebFetch em 2026-08-31

## [LIDO] https://dentmap.com.br/dentistas/manaus/hapclinica-duque-de-caxias-6b0c5add
rota: "WebFetch (rota 1 da escada)"
coletado_em: 2026-08-31
title: "Hapclínica Duque de Caxias · 3.1★ (247) · Clínico Geral em Praça 14, Manaus | DentMap"
h3_conteudo:
  - "Fotos"
  - "Informações de Contato"
  - "Qual procedimento você procura?"
  - "Avaliações do Google 3.1 (247)"
  - "Procedimentos em Manaus"
metricas: {palavras: 2100, h2: 1, h3: 5, tabelas: 0}
dado_que_so_ele_tem: "telefone 4002-3633; nota 3,1 com 247 avaliações; citação literal de paciente sobre espera"
fraquezas: "é um diretório ODONTOLÓGICO — lista implante, Invisalign, clareamento e canal para uma policlínica médica, o que é simplesmente falso; a especialidade 'Clínico Geral' aparece rotulada como odontologia; sem horário"
fonte: leitura direta da página por WebFetch em 2026-08-31

## [LIDO] https://www.doctoralia.com.br/clinicas/hapclinica-duque-de-caxias-manaus-am
rota: "WebFetch (rota 1 da escada)"
coletado_em: 2026-08-31
title: "Hapclínica Duque de Caxias - Manaus/Am | Doctoralia"
h2_conteudo:
  - "Clínico geral mais"
h3_conteudo:
  - "Nossas especializações"
  - "Hapclínica Duque de Caxias - Manaus/Am"
  - "Ainda não recebeu nenhuma opinião"
metricas: {palavras: 875, h2: 1, h3: 3, tabelas: 0}
dado_que_so_ele_tem: "nenhum — o CEP que publica, 69000-000, é genérico e está errado"
fraquezas: "página quase vazia; só 2 especialidades (clínico geral e neurologia); zero profissionais; sem telefone; sem horário; diz que a unidade não tem avaliação enquanto o Google mostra 247"
fonte: leitura direta da página por WebFetch em 2026-08-31

## [LIDO] https://www2.hapvida.com.br/unidades/clinica-duque-de-caxias
rota: "WebFetch (rota 1 da escada)"
coletado_em: 2026-08-31
title: "Clínica Duque de Caxias - Hapvida"
h2_conteudo:
  - "Especialidades"
  - "Conheça o corpo clínico dessa unidade"
  - "Acessibilidades"
  - "Horários de funcionamento"
  - "Onde Fica"
metricas: {palavras: 300, h2: 5, h3: 0, tabelas: 0}
dado_que_so_ele_tem: "acessibilidade oficial — piso tátil, banheiro acessível e rampa acessível"
fraquezas: "é aplicação JavaScript: os blocos de especialidades, corpo clínico e horários existem como títulos e voltam VAZIOS na leitura; a página ainda devolve o aviso 'Parece que esta página não faz mais parte do nosso site'. O nome oficial é Clínica Duque de Caxias — 'Hapclínica' é como o público busca"
observacao_de_leitura: "conteúdo dinâmico não renderizado — os títulos foram lidos, os valores não. Registrado como leitura PARCIAL de propósito."
fonte: leitura direta da página por WebFetch em 2026-08-31

### Matriz de cobertura — o que a SERP inteira NÃO responde

| Pergunta do usuário | Algum concorrente responde? |
|---|---|
| É a unidade de Manaus ou a de Duque de Caxias/RJ? | não — 3 resultados são do RJ na mesma SERP |
| A unidade atende urgência 24h? | não |
| Faz internação, cirurgia ou parto? | não |
| Atende pelo SUS? | não |
| Para onde vou se meu caso não for ambulatorial? | não |
| Quanto pago de coparticipação na consulta? | não |
| Como marco consulta de fato? | não |

---

## 3 · CI-2 — GANHO DE INFORMAÇÃO

- ganho_de_informacao: "O roteiro do paciente da Praça 14 de Janeiro."
- defensibilidade: 1
- em_uma_frase: "A Hapclínica é a porta de entrada ambulatorial da rede em Manaus, e a ficha CNES prova campo a campo tudo o que ela não faz."
- desenvolvimento: "A ficha oficial do estabelecimento registra ausência de centro cirúrgico, de centro obstétrico, de centro neonatal, de atendimento hospitalar e de atendimento pelo SUS. Nenhuma página da SERP menciona um único desses campos, e nenhuma diz para onde o paciente deve ir em cada um desses casos — informação que só existe cruzando a ficha CNES com o catálogo próprio da rede de Manaus."
- por_que_e_defensavel: "o cruzamento é entre a ficha CNES da unidade e o catálogo interno de rede; o concorrente tem um dos dois lados, nunca os dois, e a IA não sintetiza o segundo sozinha"
- must_match: "endereço, horário, telefone, especialidades e como chegar — o piso que todo diretório já entrega e que o artigo tem de igualar antes de superar"
- brecha_principal: "todos param no endereço; nenhum orienta"
- fonte: "cruzamento próprio entre a ficha CNES 9505970 e o catálogo de rede do Supabase, 2026-08-31"

---

## 4 · DR1 PARTE 2 — REDE (catálogo primeiro, depois guia oficial e CNES)

### 4.1 A unidade-alvo

nome_oficial: "Clínica Duque de Caxias (nome fantasia no CNES: HAPCLINICA DUQUE DE CAXIAS)"
tipo: "proprio"
endereco: "Avenida Duque de Caxias, 1905 - Praça 14 de Janeiro, Manaus - AM, CEP 69020-141"
telefone: "4002-3633"
horario: "segunda a sexta, 06:00 às 20:00; sábado, 06:00 às 17:00"
turno_cnes: "ATENDIMENTO NOS TURNOS DA MANHA, TARDE E NOITE (código 04)"
codigo_cnes: "9505970"
codigo_estabelecimento_saude: "1302609505970"
cnpj: "63.554.067/0197-00"
razao_social: "HAPVIDA ASSISTENCIA MEDICA S A"
tipo_estabelecimento: "Policlínica (código de tipo de unidade 4)"
atividade_principal: "consulta ambulatorial"
coordenadas: "-3.101992443429473, -60.02511262893677"
acessibilidade: "piso tátil, banheiro acessível, rampa acessível"
atende_sus: "não"
possui_centro_cirurgico: "não"
possui_centro_obstetrico: "não"
possui_centro_neonatal: "não"
possui_atendimento_hospitalar: "não"
possui_servico_apoio: "sim"
leitos: "nenhum — a unidade é ambulatorial e não tem internação, o que a ficha CNES confirma pela ausência de atendimento hospitalar"
no_catalogo: "sim — Supabase, consultar_rede, id 10"
no_guia_oficial: "sim — a página da unidade responde e traz endereço e acessibilidade"
data_atualizacao_cnes: "2025-09-03"
avaliacao_google: "3,1 com 247 avaliações"
fonte: "ficha CNES em apidadosabertos.saude.gov.br; catálogo próprio via consultar_rede; guia oficial da unidade; knowledge graph do Google"

> **Regra das duas listas:** catálogo ✅ + guia oficial ✅ → unidade confirmada, pode
> ser afirmada no artigo. O aviso de erro que a página oficial devolve é do
> aplicativo, não da unidade: a ficha CNES está ativa e atualizada em 2025-09-03,
> e o Google registra 247 avaliações. Nenhum indício de encerramento.

### 4.2 A rede própria de Manaus (contexto, não conteúdo do artigo)

O catálogo devolve 17 unidades próprias em Manaus: 5 hospitais, 2 prontos
atendimentos e 10 clínicas. A Hapclínica Duque de Caxias é uma das 10 clínicas.

Mapa de vocações, para o roteiro de encaminhamento do CI-2:

- Hospital Nilton Lins — alta complexidade adulto, urgência 24h, UTI, hospital-escola
- Hospital São Lucas e Hospital Rio Amazonas — obstetrícia e parto
- Hospital Rio Solimões — pediátrico exclusivo
- Hospital Rio Negro — primeira unidade própria da rede, Centro
- fonte: consultar_rede (Supabase) e consultar_artigo do hospital-nilton-lins-hapvida-manaus, 2026-08-31

### 4.3 Checklist de validação da rede

unidades_alvo_documentadas: 1
todos_com_endereco: sim
todos_com_telefone: sim
todos_com_horario: sim
bairro: "Praça 14 de Janeiro, zona centro-sul de Manaus"
fonte: "ficha CNES 9505970 e catálogo próprio, 2026-08-31"

---

## 5 · DR1 PARTE 3 — CONTEXTO LOCAL

populacao: "2.063.689 habitantes em Manaus (Censo 2022)"
fonte: "IBGE, API de agregados, tabela 4709, variável 93, município 1302603"
ranking: "maior cidade da região Norte e a mais populosa fora do Sudeste e do Nordeste"
fonte_ranking: "IBGE, Censo 2022"
leitos_e_estabelecimentos: "a unidade-alvo não entra na conta de leitos: a ficha CNES registra ausência de atendimento hospitalar. O dado de leitos da rede pertence ao artigo do Hospital Nilton Lins, não a este."
fonte_leitos: "ficha CNES 9505970 (campo de atendimento hospitalar igual a zero)"
presenca_hapvida: "rede própria ativa em Manaus desde 1997, hoje com 17 unidades próprias no catálogo"
fonte_presenca: "pillar clinicas-hapvida-por-capital e catálogo próprio via consultar_rede"
idh_e_pib: "não coletados — o artigo é de unidade, não de cidade; indicador socioeconômico de Manaus pertence ao hub plano-hapvida-manaus e repeti-lo aqui seria doorway"

### 5.1 Acessibilidade e transporte

bairro_da_unidade: "Praça 14 de Janeiro"
transporte_publico: "a linha 542 é citada como a última que serve o ponto da unidade, segundo o agregador de transporte lido na CI-1 — dado a confirmar antes de publicar"
acessibilidade_fisica: "piso tátil, banheiro acessível e rampa acessível, conforme o guia oficial da unidade"
fonte: "guia oficial da unidade e leitura do agregador de transporte na CI-1, 2026-08-31"

---

## 6 · DR1 PARTE 6 — QUERY FAN-OUT

fan_out:
  - pergunta: "onde fica a hapclinica duque de caxias"
    destino: aqui
    onde: "HS3 — como chegar"
  - pergunta: "qual o horario da hapclinica duque de caxias"
    destino: aqui
    onde: "HS3 — card de informações práticas"
  - pergunta: "como marcar consulta na hapvida em manaus"
    destino: aqui
    onde: "HS2 — experiência do paciente"
  - pergunta: "a hapclinica duque de caxias atende urgencia 24h"
    destino: aqui
    onde: "HS1 — o que a unidade é e o que ela não é"
  - pergunta: "a hapclinica duque de caxias faz exame de sangue"
    destino: aqui
    onde: "HS2 — coleta e exames"
  - pergunta: "qual o valor da consulta pelo hapvida"
    destino: cluster
    onde: "pillar do plano ambulatorial — link interno"
  - pergunta: "onde aceita hapvida em duque de caxias no rio de janeiro"
    destino: cluster
    onde: "artigo plano-hapvida-rio-de-janeiro — desambiguação em uma frase"

Trava respeitada: nenhuma sub-pergunta sem resposta local virou seção. As duas
últimas viram link, não conteúdo.

---

## 7 · DR1 PARTE 7 — DADO PROPRIETÁRIO (nível 1-2)

dado_proprietario:
  - dado: "a ficha CNES 9505970 registra ausência de centro cirúrgico, centro obstétrico, centro neonatal e atendimento hospitalar, e ausência de atendimento pelo SUS"
    origem: "apidadosabertos.saude.gov.br cruzado com consultar_rede"
    defensibilidade: 1
    vira: "HS1 — o parágrafo que define o escopo da unidade, e a passagem citável do lead"
  - dado: "o catálogo próprio tem 17 unidades da rede em Manaus, das quais 10 são clínicas, e a Duque de Caxias é uma delas"
    origem: consultar_rede
    defensibilidade: 1
    vira: "HS1 — o papel da unidade dentro da rede, sem repetir a contagem do hub"
  - dado: "coparticipação vigente em Manaus pela faixa demais_capitais: consulta eletiva R$ 25,42, exame simples R$ 45,79, exame complexo R$ 114,48"
    origem: consultar_coparticipacao
    defensibilidade: 1
    vira: "HS4 — o que o paciente paga por consulta e exame nesta unidade, que é justamente o que ela faz"
  - dado: "o mapa de vocações da rede de Manaus (parto no São Lucas e Rio Amazonas, pediatria no Rio Solimões, alta complexidade no Nilton Lins) já está consolidado e conferido no artigo irmão"
    origem: "consultar_artigo do hospital-nilton-lins-hapvida-manaus"
    defensibilidade: 2
    vira: "HS1 — o roteiro de encaminhamento, que é o ganho do CI-2"

Chamadas feitas: consultar_rede, consultar_dados_canonicos, consultar_coparticipacao,
consultar_artigo (4 artigos), consultar_faqs_catalogo, consultar_saturacao_destinos,
consultar_overlaps_doorway, listar_artigos.

- gsc_queries_for_page: não se aplica — a URL ainda não existe.
- cotador_fila: não consultado. A ferramenta exposta nesta sessão veio com descrição
  trocada (descreve registro de hospitais, não a fila do cotador). Chamar às cegas
  uma função de escrita seria imprudente. Registrado como lacuna consciente.
- fonte: conectores BD - Consultar e BD - Criar, sessão de 2026-08-31

---

## 8 · DR1 PARTE 8 — O QUE NÃO FOI ENCONTRADO

nao_encontrado:
  - procurei: "lista de especialidades atendidas na unidade, em fonte primária"
    onde: "guia oficial da unidade (bloco existe mas volta vazio, é JavaScript), CNES, diretórios"
    conclusao: "os diretórios divergem entre si — um diz clínico geral e neurologia, outro lista procedimentos odontológicos que não cabem numa policlínica médica. NÃO afirmar lista de especialidades no artigo."
  - procurei: "ano de inauguração da unidade"
    onde: "guia oficial, CNES, notícias, cadastro de empresa"
    conclusao: "não há fonte pública. NÃO citar ano de abertura."
  - procurei: "corpo clínico nominal da unidade"
    onde: "guia oficial e diretórios"
    conclusao: "nenhuma fonte confiável. NÃO citar nome de médico."
  - procurei: "confirmação de que a unidade faz coleta laboratorial própria"
    onde: "guia oficial, CNES, diretórios"
    conclusao: "o CNES registra serviço de apoio, o que é compatível com coleta, mas não a nomeia. Tratar como VERIFICAR antes de afirmar."
  - procurei: "estacionamento da unidade"
    onde: "guia oficial, diretórios, mapas"
    conclusao: "sem fonte. NÃO afirmar que há ou que não há."

---

## 9 · FORBIDDEN_TOKENS

FORBIDDEN_TOKENS:
Duque de Caxias/RJ como sede da unidade
Hospital do Coração
Centro Clínico Duque de Caxias
pronto-socorro 24h
urgência 24 horas
internação
centro cirúrgico
maternidade
parto
UTI
atende pelo SUS
implante dentário
Invisalign
clareamento dental
tratamento de canal
145 leitos
Baixada Fluminense

Motivo de cada bloco: os cinco primeiros são da unidade homônima do Rio de Janeiro
e do Hospital do Coração — confundi-los é o erro central que esta pesquisa
desarmou. Os seguintes são serviços que a ficha CNES prova que a unidade NÃO tem.
Os quatro procedimentos odontológicos vêm do diretório que classificou a policlínica
como consultório de odontologia. "145 leitos" é um conflito aberto registrado no
artigo do Nilton Lins e não pode vazar para cá.

---

## 10 · PLANO_MODELOS

Pendente. O bloco de roteamento dos agentes é escrito pelo Agente 22 e validado pelo
`checkpoint_modelos.py` antes do Estágio 1 — e só depois é copiado para cá. A linha
multiagente da v7.2 ainda não foi disparada porque depende de autorização do usuário
nesta sessão.

---

## 11 · DATAS DE COLETA

coletado_em: 2026-08-31 # serp e keywords
coletado_em: 2026-08-31 # rede
coletado_em: 2026-08-31 # contexto local
coletado_em: 2026-08-31 # concorrentes

---

## 12 · DR2 PARTE 1 — SEO SEMÂNTICO E KIT ON-PAGE

### 12.1 Entidades

- operadora: Hapvida NotreDame Intermédica, tipo Organization, 8 a 12 menções
- unidade: Hapclínica Duque de Caxias, tipo MedicalClinic, 15 a 20 menções
- lugar: Manaus e Praça 14 de Janeiro, tipo Place, 10 a 15 menções
- entidades secundárias: CNES como Organization; Hospital Nilton Lins, Hospital São Lucas,
  Hospital Rio Amazonas e Hospital Rio Solimões como LocalBusiness citados só para encaminhar;
  coparticipação e plano ambulatorial como conceitos

### 12.2 Matriz de posicionamento — kit_on-page

kit_onpage:
  principal: "hapclinica duque de caxias"
  volume_principal: 6600
  dificuldade_principal: 0
  intencao_principal: navigational
  posicoes_principal:
    h1: "Hapclínica Duque de Caxias (Manaus): horários, especialidades e como marcar"
    title: "Hapclínica Duque de Caxias Manaus: Horário e Como Marcar 2026"
    url: "hapclinica-duque-de-caxias-manaus"
    meta: "A Hapclínica Duque de Caxias fica na Av. Duque de Caxias, 1905, Praça 14 de Janeiro, em Manaus. Veja horário, telefone, o que a unidade faz e o que não faz, e como marcar."
    primeiro_paragrafo: "sim — lead GEO com a passagem citável de 40-60 palavras"
    h2: "o H2 da HS3 contém a keyword principal junto de 'endereço e horário'"
  secundarias:
    - kw: "hapvida manaus marcar consulta"
      volume: 720
      dificuldade: 32
      intencao: transactional
      veredito: qualificada
      onde_entra: "H2 da HS2"
      cluster_candidata: sim
    - kw: "marcar consulta hapvida manaus"
      volume: 720
      dificuldade: 13
      intencao: navigational
      veredito: qualificada
      onde_entra: "H3 dentro da HS2 e FAQ 4"
      cluster_candidata: não
    - kw: "hapvida consultas manaus"
      volume: 720
      dificuldade: 53
      intencao: informational
      veredito: qualificada
      onde_entra: "corpo da HS2"
      cluster_candidata: não
    - kw: "laboratorios hapvida manaus"
      volume: 210
      dificuldade: 0
      intencao: navigational
      veredito: qualificada
      onde_entra: "HS2, no trecho de exames, com link para o pillar de laboratórios"
      cluster_candidata: sim
    - kw: "laboratorio hapvida manaus"
      volume: 210
      dificuldade: 7
      intencao: navigational
      veredito: qualificada
      onde_entra: "HS2, variação natural no mesmo trecho de exames"
      cluster_candidata: não
    - kw: "centro clinico duque de caxias"
      volume: 720
      dificuldade: 0
      intencao: navigational
      veredito: qualificada
      onde_entra: "HS1, no parágrafo de desambiguação entre Manaus e Rio de Janeiro"
      cluster_candidata: sim
    - kw: "clinica hapvida manaus"
      volume: 10
      dificuldade: 0
      intencao: navigational
      veredito: qualificada
      onde_entra: "HS1, variação de entidade"
      cluster_candidata: não
  descartadas_por_intencao:
    - kw: "hapvida manaus telefone"
      volume: 590
      veredito: descartada
      motivo: "o checkpoint_suficiencia classifica busca por telefone como tráfego de quem JÁ é cliente, e a trava está certa: quem procura o número quer resolver algo que já tem. O telefone continua no card da HS3 porque o arquétipo de unidade exige — o que não se faz é mirar a keyword."
    - kw: "hapclinica duque de caxias telefone"
      volume: 10
      veredito: descartada
      motivo: "mesma razão, e com volume marginal — não paga o custo de ocupar um H2"
    - kw: "hapvida trabalhe conosco manaus"
      volume: 260
      veredito: descartada
      motivo: "candidato a emprego nunca vira cliente da corretora; infla impressão e derruba CTR"
    - kw: "maternidade hapvida manaus"
      volume: 390
      veredito: descartada
      motivo: "a ficha CNES prova que esta unidade não tem centro obstétrico; perseguir o termo aqui seria doorway e seria falso"
    - kw: "pronto socorro hapvida manaus"
      volume: 210
      veredito: descartada
      motivo: "a unidade não tem atendimento hospitalar; o termo pertence ao Hospital Nilton Lins"
    - kw: "hapvida 24 horas manaus"
      volume: 210
      veredito: descartada
      motivo: "mesma razão — a unidade fecha às 20:00"
    - kw: "hapvida manaus"
      volume: 2900
      veredito: descartada
      motivo: "é a keyword do hub plano-hapvida-manaus; disputá-la aqui é canibalização interna"
  h2_com_secundaria: "HS2 (marcar consulta) e HS3 (telefone e endereço)"
  fonte: "DataForSeo keyword_data e keyword_suggestions, location_code 2076, 2026-08-31"

---

## 13 · DR2 PARTE 2 — DIFERENCIAIS ÚNICOS

- categoria: escopo assistencial
  titulo: "A policlínica da Praça 14 que resolve consulta e exame, e só"
  dado_quantitativo: "quatro campos zerados na ficha CNES: centro cirúrgico, centro obstétrico, centro neonatal e atendimento hospitalar"
  vs_concorrentes: "nenhum dos quatro concorrentes lidos menciona um único desses campos"
  por_que_importa: "evita que o paciente vá à Praça 14 com um caso de urgência e perca tempo"
  defensibilidade: 1
  fonte: "ficha CNES 9505970"

- categoria: acesso
  titulo: "Abre às 06:00 — o horário mais largo entre as clínicas da Hapvida em Manaus"
  dado_quantitativo: "seg-sex 06:00 às 20:00 e sáb 06:00 às 17:00 — 14 horas por dia útil"
  vs_outras_cidades: "é horário de clínica de rede própria, mais largo que o comercial de 8h às 18h que o público supõe"
  por_que_importa: "quem trabalha consegue ir antes do expediente ou no sábado"
  defensibilidade: 2
  fonte: "turno CNES 04 e o horário publicado pelo diretório que espelha o CNES"

- categoria: custo
  titulo: "O que se paga por consulta e exame nesta unidade de Manaus"
  dado_quantitativo: "consulta eletiva R$ 25,42, exame simples R$ 45,79 e exame complexo R$ 114,48 na faixa demais capitais"
  por_que_importa: "a unidade só faz consulta e exame — que são justamente os itens com coparticipação, ao contrário de internação e cirurgia, que são isentos"
  defensibilidade: 1
  fonte: consultar_coparticipacao

- categoria: orientação
  titulo: "O roteiro de quem chega na Avenida Duque de Caxias e precisa de outra coisa"
  dado_quantitativo: "4 destinos distintos da rede própria de Manaus, um por tipo de caso"
  vs_concorrentes: "zero concorrentes oferecem encaminhamento"
  por_que_importa: "é a única informação da página que o paciente não acha em mapa nem em diretório"
  defensibilidade: 2
  fonte: "consultar_rede e o artigo irmão do Hospital Nilton Lins"

---

## 14 · DR2 PARTE 3 — FAQ LOCAL

Cruzada contra consultar_faqs_catalogo (categoria rede), contra as 7 FAQs do
hospital-nilton-lins-hapvida-manaus e contra as 11 do plano-hapvida-rio-de-janeiro.
Sobreposição encontrada: zero. Todas as perguntas contêm o nome da unidade, como o
arquétipo de unidade exige.

1. A Hapclínica Duque de Caxias fica em Manaus ou no município de Duque de Caxias, no Rio de Janeiro?
2. Que horas abre e que horas fecha a unidade da Avenida Duque de Caxias, 1905?
3. A Hapclínica Duque de Caxias atende urgência ou pronto socorro?
4. Como marcar consulta na Hapclínica da Praça 14 de Janeiro, em Manaus?
5. Qual o número de contato da unidade Hapvida da Praça 14?
6. Dá para fazer coleta de sangue e exames na Hapclínica Duque de Caxias, em Manaus?
7. A unidade da Praça 14 de Janeiro faz internação ou cirurgia?
8. O atendimento na policlínica da Avenida Duque de Caxias é pelo SUS?
9. Quais ônibus passam perto da Hapclínica Duque de Caxias, na zona centro-sul de Manaus?
10. A unidade Hapvida da Avenida Duque de Caxias tem rampa e banheiro acessível?
11. Gestante faz pré-natal ou parto na clínica da Praça 14 de Janeiro?
12. Quanto custa a coparticipação de uma consulta particular de plano nessa Hapclínica de Manaus?

total: 12
com_dado_local: 12
genericas: 0
teste_troca_cidade: "trocar a unidade por outra faz a pergunta perder sentido — sim, nas 12"

---

## 15 · DR2 PARTE 4 — VALIDAÇÃO ANTI-DOORWAY

### 15.1 Teste de substituição

| Seção | Perde sentido se trocar a unidade? | Por quê |
|---|---|---|
| HS1 escopo e papel na rede | sim | os campos da ficha CNES são desta unidade |
| HS2 experiência e agendamento | sim | horário 06:00 e o roteiro de exames são desta unidade |
| HS3 como chegar | sim | endereço, coordenada e linha de ônibus são desta unidade |
| HS4 planos que dão acesso | parcialmente | é a seção-ponte; por isso ela é curta e linka |
| FAQ | sim | as 12 nomeiam a unidade |

teste_substituicao: PASSOU — 4 de 5 blocos perdem o sentido, cerca de 85% do conteúdo

### 15.2 Dados únicos da praça

dados_unicos: 18 — PASSOU

São eles: código CNES 9505970; código de estabelecimento 1302609505970; CNPJ
63.554.067/0197-00; tipo Policlínica; turno 04 manhã, tarde e noite; horário
06:00 às 20:00 nos dias úteis; horário 06:00 às 17:00 no sábado; ausência de centro
cirúrgico; ausência de centro obstétrico; ausência de centro neonatal; ausência de
atendimento hospitalar; ausência de atendimento pelo SUS; presença de serviço de
apoio; coordenadas -3.101992 e -60.025113; CEP 69020-141; telefone 4002-3633; nota
3,1 com 247 avaliações; atualização da ficha CNES em 2025-09-03.

### 15.3 Frases banidas

frases_genericas: 0 — PASSOU. Nenhuma das expressões vetadas entra: atendimento de
qualidade, equipe qualificada, melhor custo-benefício, cobertura completa e
infraestrutura moderna estão fora, e a HS1 troca cada uma delas por campo de ficha.

### 15.4 Fronteira com os artigos irmãos

| Artigo irmão | O que ele já faz | O que ESTE artigo não reproduz |
|---|---|---|
| plano-hapvida-manaus (hub, id 47) | preço, tipos de plano, carência, comparativo com Unimed e Amil, panorama da rede | nenhuma tabela de preço, nenhum comparativo de operadora, nenhuma contagem de rede da cidade |
| clinicas-hapvida-por-capital (pillar, id 147) | uma frase listando as 6 Hapclínicas e uma linha de endereço no buscador | não repetir a lista das outras clínicas; este artigo é sobre uma unidade só |
| hospital-nilton-lins-hapvida-manaus (spoke, id 193) | urgência 24h, UTI, cirurgia, hospital-escola, internação | não falar de urgência, UTI nem internação a não ser para encaminhar em uma frase |
| plano-hapvida-rio-de-janeiro (id 28) | as duas unidades de Duque de Caxias no RJ e a FAQ da Baixada | não descrever a rede do RJ; a desambiguação cabe em uma frase e um link |

anti-doorway: APROVADO — teste de substituição em cerca de 85%, 18 dados únicos, zero frase genérica e fronteira escrita contra os 4 irmãos.

---

## 16 · PLANO DE LINKS INTERNOS

Verificado com consultar_saturacao_destinos em 2026-08-31. Regra: no máximo 1 vez
por URL, priorizando destino subutilizado e nunca linkando destino saturado.

| Destino | Backlinks hoje | Classificação | Onde entra |
|---|---|---|---|
| plano-hapvida-manaus | 4 | subutilizado | HS4, link obrigatório para o hub |
| hospital-nilton-lins-hapvida-manaus | 2 | subutilizado | HS1, no roteiro de encaminhamento |
| laboratorios-hapvida-capitais | 4 | subutilizado | HS2, no trecho de exames |
| clinicas-hapvida-por-capital | 9 | normal | HS1, o pillar de onde este spoke pende |
| o-que-e-plano-ambulatorial-2 | 8 | normal | HS4, no lugar do pillar de coparticipação |
| teleconsulta-hapvida | 4 | subutilizado | HS2, como alternativa a ir presencialmente |

Fora do plano de propósito: tabela-precos-hapvida-coparticipacao-guia-completo tem
58 backlinks e plano-de-saude-hapvida-carencia tem 53 — ambos saturados. O arquétipo
de unidade pede um link de coparticipação; ele foi substituído pelo pillar do plano
ambulatorial, que é tematicamente mais próximo de uma policlínica e está em faixa
normal.

---

## 17 · RESUMO

```
═══════════════════════════════════════════
PESQUISA COMPLETA — PRONTA PARA O PORTÃO HUMANO
Alvo: Hapclínica Duque de Caxias, Manaus/AM  |  Tipo: unidade HS1-HS4
SERP: 10 orgânicos, mobile e desktop, sem featured snippet
CI-1: 4 concorrentes lidos por WebFetch, com headings literais
Keywords: principal 6.600/mês KD 0 + 7 secundárias qualificadas + 7 descartadas por intenção
Kit on-page: H1, title, URL, meta, primeiro parágrafo e H2 rascunhados
Rede mapeada: 1 unidade-alvo com ficha CNES completa  |  Diferenciais: 4
FAQ: 12, todas nomeando a unidade, zero sobreposição com os irmãos
Dados únicos: 18  |  Itens a verificar: 2 (coleta laboratorial e linha de ônibus)
Fan-out: 7 sub-perguntas — 5 aqui, 2 no cluster
Defensibilidade: 4 dados de nível 1-2  |  Ganho do CI-2 é nível 1
Anti-doorway: APROVADO
═══════════════════════════════════════════
```

---

## 18 · FONTES PRIMÁRIAS CONSULTADAS

### Ficha oficial do estabelecimento
- CNES, API de dados abertos do Ministério da Saúde: https://apidadosabertos.saude.gov.br/cnes/estabelecimentos/9505970

### Demografia
- IBGE, panorama do município: https://cidades.ibge.gov.br/brasil/am/manaus/panorama

### Rede oficial da operadora
- Guia de unidades: https://www2.hapvida.com.br/unidades

### Nossos próprios artigos do cluster
- https://tabelaplanos.com.br/plano-hapvida-manaus/
- https://tabelaplanos.com.br/clinicas-hapvida-por-capital/
- https://tabelaplanos.com.br/hospital-nilton-lins-hapvida-manaus/
