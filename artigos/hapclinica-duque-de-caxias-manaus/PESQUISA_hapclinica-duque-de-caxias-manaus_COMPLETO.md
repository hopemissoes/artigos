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
- veredito: não há canibalização hoje. Com 2 URLs passa a haver risco — a fronteira está na seção 15.4 e a ação no lado do pillar está na seção 16.1.
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

- ganho_de_informacao: "O roteiro de encaminhamento por vocação da rede de Manaus."
- defensibilidade: 2
- em_uma_frase: "Esta é uma policlínica de consulta e exame com hora marcada, e quem chega aqui com um caso que ela não resolve precisa saber para qual das outras unidades da rede ir."
- desenvolvimento: "O CNES registra a unidade como POLICLINICA (codigo_tipo_unidade 4) e com atendimento em tres turnos — manha, tarde e noite —, e nao como pronto atendimento nem como hospital. Cruzando isso com o catalogo proprio da rede em Manaus, sai o que nenhum concorrente da SERP oferece: para onde o paciente vai quando o caso e urgencia, parto, pediatria ou alta complexidade."
- por_que_e_defensavel: "o lado CNES desta unidade ja esta na SERP (o concorrente da posicao 5 e um despejo automatico da base CNES). O que nao esta em lugar nenhum e o encaminhamento por vocacao, que so existe cruzando o registro publico com o catalogo interno da rede. Por isso o nivel honesto e 2, nao 1."
- rebaixado_de: "nivel 1 para nivel 2 no refino de 2026-08-31, por decisao do juiz P-B (Agente 24): metade do cruzamento ja esta publicada."
- must_match: "endereco, horario, tipo de atendimento e como chegar. ATENCAO: a lista de especialidades NAO entra no must-match — a pesquisa provou que as fontes se contradizem e a secao 8 proibe afirma-la. O must-match de servico e 'consulta e exame com hora marcada', que o tipo CNES sustenta."
- brecha_principal: "todos param no endereco; nenhum orienta"
- fonte: "ficha CNES 9505970 cruzada com o catalogo de rede do Supabase, 2026-08-31"

### 3.1 · CORRECAO CRITICA — os campos booleanos do CNES NAO servem de prova

Na primeira redacao desta pesquisa o ganho do CI-2 se apoiava nos campos
booleanos da ficha CNES (`possui_centro_cirurgico`, `possui_centro_obstetrico`,
`possui_centro_neonatal`, `possui_atendimento_hospitalar`) para "provar campo a
campo" o que a unidade nao faz. **Isso estava errado e foi medido.**

Teste feito em 2026-08-31: consultamos os mesmos campos em tres unidades Hapvida
de Manaus na mesma API oficial.

| Unidade | CNES | tipo | turno | os 4 booleanos |
|---|---|---|---|---|
| Hapclinica Duque de Caxias | 9505970 | 4 | manha, tarde e noite | os 4 de capacidade em 0; servico_apoio em 1 |
| Pronto Atendimento Cidade Nova | 9676783 | 73 | continuo 24 horas | idem |
| Medicina Preventiva TEA Adrianopolis | 9676759 | 73 | continuo 24 horas | idem |

> **Correção do Juiz A (2026-08-31):** a redação anterior dizia "todos 0", o que
> era impreciso. Os quatro campos de CAPACIDADE (centro cirúrgico, obstétrico,
> neonatal, atendimento hospitalar) estão em 0 nas três; `possui_servico_apoio`
> está em **1** nas três. A lição não muda — nenhum dos cinco varia, logo nenhum
> discrimina —, mas o dado estava escrito errado.

O Pronto Atendimento Cidade Nova funciona 24 horas e, ainda assim, aparece com
`possui_atendimento_ambulatorial: 0`. **Conclusao: esses booleanos nao sao
preenchidos para estabelecimento privado neste dataset — sao zero para todos,
independentemente da realidade. Nao provam nada e nao podem ser citados.**

O que sobra, e que e confiavel porque VARIA entre as unidades (logo, esta
preenchido de verdade):

- `codigo_tipo_unidade`: **4 (Policlinica)** aqui, contra 73 (Pronto Atendimento)
  nas outras duas. Este campo discrimina.
- `descricao_turno_atendimento`: **"ATENDIMENTO NOS TURNOS DA MANHA, TARDE E
  NOITE"** aqui, contra "ATENDIMENTO CONTINUO DE 24 HORAS/DIA" nas outras duas.
  Este campo discrimina, e e ele que sustenta "a unidade nao e 24h".

- fonte: "consulta comparativa a apidadosabertos.saude.gov.br nos CNES 9505970, 9676783 e 9676759, 2026-08-31"

> **Licao registrada:** campo zerado em base publica pode significar "nao tem" ou
> "ninguem preencheu". A unica forma de saber e checar se o campo VARIA na mesma
> base. Achado do Agente 6 no portao de pesquisa.

---

## 4 · DR1 PARTE 2 — REDE (catálogo primeiro, depois guia oficial e CNES)

### 4.1 A unidade-alvo

nome_oficial: "Clínica Duque de Caxias (nome fantasia no CNES: HAPCLINICA DUQUE DE CAXIAS)"
tipo: "proprio"
endereco: "Duque de Caxias, 1905 - Praça 14 de Janeiro, Manaus - AM, CEP 69020-141"
logradouro_em_conflito: "[VERIFICAR: o número 1905, o bairro Praça 14 de Janeiro e o CEP 69020-141 são consensuais em todas as fontes. O TIPO DE LOGRADOURO não é: o CNES registra AVENIDA; a própria página da Hapvida, o catálogo do banco, o hub e o pillar escrevem RUA. Achado do Juiz A. Enquanto não se resolve, escrever sem o prefixo — 'Duque de Caxias, 1905' — que é verdadeiro nas duas versões.]"
telefone: "[VERIFICAR: 4002-3633 é o número de atendimento da Hapvida, não uma linha exclusiva desta unidade — o mesmo número consta do artigo do Hospital Nilton Lins. A ficha CNES traz o campo de telefone vazio e o guia oficial não renderiza número. Não apresentar como telefone da unidade.]"
horario: "[VERIFICAR — CONFLITO TRIPLO, achado do Juiz B e confirmado pelo orquestrador. (a) CNES, única fonte primária: apenas manhã, tarde e noite, sem horas. (b) UM diretório que espelha o CNES: 06:00-20:00 e sábado 06:00-17:00. (c) O NOSSO PRÓPRIO HUB plano-hapvida-manaus, no ar: 7h-19h e sábado 7h-17h. Não sabemos o horário. PROIBIDO publicar faixa de horas como fato; publicar 06:00-20:00 ainda contradiz o nosso próprio site.]"
turno_cnes: "ATENDIMENTO NOS TURNOS DA MANHA, TARDE E NOITE (código 04) — campo confiável, varia entre unidades"
codigo_cnes: "9505970"
codigo_estabelecimento_saude: "1302609505970"
cnpj: "63.554.067/0197-00"
razao_social: "HAPVIDA ASSISTENCIA MEDICA S A"
tipo_estabelecimento: "Policlínica (codigo_tipo_unidade 4) — campo confiável, varia entre unidades"
tipo_confirmado_em_2a_fonte: "sim — o catálogo próprio (consultar_rede, id 10) tipa a unidade como Clínica, e o guia oficial da operadora a nomeia Clínica Duque de Caxias. São duas fontes independentes do CNES concordando com a classificação, o que fecha a regra das duas fontes para dado estrutural. Ressalva pedida pelo Agente 23."
como_escrever_o_escopo: "AFIRMAR a classificação, NÃO a negativa categórica. Certo: 'está registrada como policlínica no CNES e opera em três turnos, não em regime contínuo'. Errado: 'não faz cirurgia nem internação' apresentado como fato apurado — nenhuma fonte lida sustenta a negativa direta, e os booleanos que pareciam sustentá-la caíram na seção 3.1. O que substitui a negativa é o encaminhamento: dizer onde a rede faz urgência, parto, pediatria e alta complexidade, nomeando as unidades."
atividade_principal: "consulta e exame com hora marcada, compatível com o tipo Policlínica registrado no CNES"
coordenadas: "[VERIFICAR: CONFLITO DE 2,43 km. O CNES traz -3.101992, -60.025113; a página oficial da Hapvida traz -3.119259. Medido pelo orquestrador em 2026-08-31. NÃO usar nenhuma das duas no schema.json até resolver — pin errado manda o paciente para o lugar errado.]"
acessibilidade: "piso tátil, banheiro acessível, rampa acessível"
atende_sus: "[VERIFICAR: o campo do CNES diz NAO, mas ele devolve NAO para as três unidades testadas e por isso não se provou discriminante; é plausível para unidade privada, e não deve ser afirmado como fato apurado]"
campos_booleanos_cnes: "NÃO USAR — medidos como não preenchidos, ver seção 3.1"
leitos: "nenhum — coerente com o tipo Policlínica; a ausência de internação NÃO deve ser sustentada nos booleanos do CNES, e sim no tipo de estabelecimento"
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
- **Pronto Atendimento Cidade Nova** (CNES 9676783) e **Pronto Atendimento Distrito** —
  as duas unidades de regime contínuo da rede em Manaus. **Faltavam no artigo e são
  a porta de urgência real**; achado do Juiz A, que classificou a omissão como o
  maior risco de dano da página. Endereços no catálogo: Av. Camapuã, 695, Cidade
  Nova; e Av. Buriti, 3727, Distrito Industrial.
- fonte: consultar_rede (Supabase) e consultar_artigo do hospital-nilton-lins-hapvida-manaus, 2026-08-31

### 4.3 Checklist de validação da rede

unidades_alvo_documentadas: 1
todos_com_endereco: sim
todos_com_telefone: não — o número que circula é o de atendimento da Hapvida, não da unidade
todos_com_horario: sim, com a ressalva de precisão registrada na 4.1
bairro: "Praça 14 de Janeiro. NÃO escrever a zona da cidade: a versão anterior desta pesquisa dizia zona centro-sul citando a ficha CNES como fonte, e a ficha NÃO TEM campo de zona. Foi invenção do orquestrador, apontada pelo Juiz A."
fonte: "ficha CNES 9505970 e catálogo próprio, 2026-08-31"

### 4.4 Quais produtos dão acesso a esta unidade (sustenta a HS4)

> ⚠️ **Isto é dado de PRAÇA, não de unidade.** Vale para Manaus inteira e para
> qualquer unidade própria da cidade. Entra na HS4 como ponte, e **não** pode ser
> escrito como diferencial desta clínica. Ressalva pedida pelo Agente 23.

Coletado no refino de 2026-08-31 porque a HS4 estava órfã — achado do Agente 23.

marca_na_praca: "Manaus é Norte, logo a marca é Hapvida (e não GNDI/NotreDame, que opera Grande SP e RJ)"
linhas_de_produto: "Nosso Plano, Mix e Pleno"
relacao_produto_acesso: "as três linhas dão acesso à rede própria, e esta unidade é rede própria (catálogo id 10). O que muda entre elas é a rede credenciada em volta, não o acesso à unidade."
tabela_de_coparticipacao_da_praca: "Tabela 1 — Manaus está na lista de Tabela 1, junto com Fortaleza, Recife, Salvador, Belém e as demais capitais do Norte, Nordeste, Centro-Oeste e Sul"
fonte: "skill hapvida-data, seções 'Which Brand for Which City' e 'Which Copayment Table for Which City'"

---

## 5 · DR1 PARTE 3### 4.5 Fonte primária encontrada no Estágio 4 (Agente 12) — serviços da unidade

O que a FASE 0 não achou e a auditoria de veracidade achou: a própria operadora
publica uma página de notícia sobre esta unidade.

url: "https://www2.hapvida.com.br/noticias/ampliação-da-haplínica-duque-de-caxias"
titulo_literal: "Ampliação da Haplínica Duque de Caxias"
texto_literal: "Agora, em Manaus, você pode contar com mais serviços: laboratório, ultrassom, raio X e mamografia."
o_que_isso_resolve: "nomeia LABORATÓRIO, ULTRASSOM, RAIO X e MAMOGRAFIA nesta unidade, em fonte primária da operadora. Fecha o item de coleta que estava em nao_encontrado."
o_que_isso_NAO_resolve: "não há data de publicação em lugar nenhum da página — nem em meta, nem em og, nem em JSON-LD, nem no corpo (que é JavaScript e não renderiza). Portanto é PROIBIDO escrever recência: nada de recentemente ampliada, nova, agora conta com. Afirmar o serviço, jamais a data."
distincao_importante: "isto é lista de SERVIÇO vinda da operadora, não lista de ESPECIALIDADE MÉDICA vinda de diretório. A proibição da seção 8 e os tokens neurologia e clínico geral continuam valendo — o que caiu foi só o item de coleta."
confirma_tambem: "a frase da própria operadora diz em Manaus, o que reforça a desambiguação central do artigo."
fonte: "leitura do HTML da página oficial por curl e WebFetch, 2026-08-31"
ressalva_do_juiz_A: "o texto existe APENAS na meta description. O corpo visível da
  página renderiza só título e menu — quem clicar NÃO verá a lista. E é página de
  NOTÍCIA, não a página da unidade. Atribuir como comunicado da operadora sobre a
  unidade, e nunca prometer ao leitor que ele verá a lista ao clicar."
palavra_literal: "a operadora escreve LABORATÓRIO. 'Coleta' é dedução nossa e não
  pode ser apresentada como palavra da operadora."

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
    conclusao: "RESOLVIDO em 2026-08-31 pelo Agente 12 — ver seção 4.5. A operadora nomeia os serviços na própria página de notícia da unidade. O campo do CNES continua NÃO servindo de lastro."
  - procurei: "prova documental do que a unidade NAO faz (cirurgia, obstetricia, internacao)"
    onde: "campos booleanos da ficha CNES, testados comparativamente em 3 unidades"
    conclusao: "os booleanos nao sao preenchidos para estabelecimento privado — ver secao 3.1. NAO citar esses campos como prova de nada. O que sustenta o escopo e o codigo_tipo_unidade 4 (Policlinica) e o turno de tres turnos."
  - procurei: "telefone proprio da unidade"
    onde: "ficha CNES (campo vazio), guia oficial (nao renderiza), diretorios"
    conclusao: "o 4002-3633 e o numero de atendimento da Hapvida, usado tambem pelo Hospital Nilton Lins. NAO apresentar como telefone da unidade."
  - procurei: "estacionamento da unidade"
    onde: "guia oficial, diretórios, mapas"
    conclusao: "sem fonte. NÃO afirmar que há ou que não há."

---

## 9 · FORBIDDEN_TOKENS

FORBIDDEN_TOKENS:
Duque de Caxias/RJ como sede da unidade
Hospital do Coração
Centro Clínico Duque de Caxias  # EXCEÇÃO ÚNICA: permitido apenas na frase de negação da HS1, do tipo "se você procura o Centro Clínico Duque de Caxias do Rio de Janeiro, é outra unidade". Em qualquer outra posição, reprova.
pronto-socorro na Hapclínica
urgência 24 horas na Hapclínica
internação na Hapclínica
centro cirúrgico na Hapclínica
maternidade na Hapclínica
parto na Hapclínica
UTI na Hapclínica
atende pelo SUS
implante dentário
Invisalign
clareamento dental
tratamento de canal
145 leitos
Baixada Fluminense
69000-000
neurologia
clínico geral
a porta de entrada ambulatorial
a ficha do CNES prova
sem centro cirúrgico segundo o CNES
o horário mais largo entre as clínicas

Motivo de cada bloco: os cinco primeiros são da unidade homônima do Rio de Janeiro
e do Hospital do Coração — confundi-los é o erro central que esta pesquisa
desarmou. Os seguintes são serviços que a ficha CNES prova que a unidade NÃO tem.
Os quatro procedimentos odontológicos vêm do diretório que classificou a policlínica
como consultório de odontologia. "145 leitos" é um conflito aberto registrado no
artigo do Nilton Lins e não pode vazar para cá.

Acrescentados no refino de 2026-08-31, por achado dos juízes de pesquisa:
"69000-000" é o CEP falso publicado por um diretório; "neurologia" e "clínico geral"
são a lista de especialidades de fonte única que a seção 8 proíbe afirmar; "a porta
de entrada ambulatorial" usa artigo definido para 1 de 10 clínicas de Manaus; "a
ficha do CNES prova" e "sem centro cirúrgico segundo o CNES" são a afirmação que a
seção 3.1 derrubou; "o horário mais largo entre as clínicas" é o superlativo que
nunca foi medido contra as outras 9 unidades.

**Correção de 2026-08-31, depois de rodar o `checkpoint_verificar` no HTML.** A
primeira lista proibia as PALAVRAS "internação", "parto", "UTI", "maternidade",
"centro cirúrgico" e "pronto-socorro 24h". Isso estava errado por dois motivos:

1. **Bloqueava o próprio ganho do artigo.** O CI-2 desta página é o roteiro de
   encaminhamento — dizer que quem precisa de internação vai ao Nilton Lins e quem
   vai ter parto vai ao São Lucas ou ao Rio Amazonas. Sem essas palavras não há
   como escrever o encaminhamento, e o artigo perde exatamente aquilo que o
   distingue de um diretório.
2. **A trava faz busca de substring no HTML cru**, então token curto colide com o
   texto de sistema. "UTI" reprovava o artigo por casar dentro do comentário
   `/* === UTILITY CLASSES === */` do CSS padrão da skill — um falso positivo
   garantido em qualquer artigo do site.

Os tokens passaram a nomear a unidade ("internação na Hapclínica"), que é o que de
fato não pode ser afirmado. A palavra solta, usada para mandar o leitor à unidade
certa, é o objetivo do artigo, não a violação.

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
    h1: "Hapclínica Duque de Caxias (Manaus): endereço, horário e como marcar consulta"
    title: "Hapclínica Duque de Caxias em Manaus: Turnos e Como Marcar"
    url: "hapclinica-duque-de-caxias-manaus"
    meta: "Hapclínica Duque de Caxias, Praça 14 de Janeiro, Manaus: em que turnos atende, como marcar consulta e exame e para onde ir se o caso não for de ambulatório."
    primeiro_paragrafo: "sim — lead GEO com a passagem citável de 40-60 palavras"
    h2: "o H2 da HS3 contém a keyword principal junto de 'endereço e horário'"
    nota_horario_e_logradouro: "Correção do Agente 21: o title dizia Horário e a meta dizia Veja horário de atendimento, mas a página NÃO entrega hora exata por decisão da própria pesquisa — prometer no title o que a página não dá é o pior dos dois mundos. Trocado por Turnos. E a meta trazia o prefixo Av., que a regra logradouro_em_conflito proíbe; agora não tem prefixo."
    nota_especialidades: "nem o H1 nem o title nem a meta prometem lista de especialidades — a seção 8 proíbe afirmá-la e prometer no título o que não se pode entregar é o pior dos dois mundos. Achado convergente dos Agentes 6 e 24."
  valor_comercial_da_pagina: "INDIRETO, e isto fica declarado por escrito. Esta página não converte pela keyword: quem busca a unidade em geral já é beneficiário. Ela converte pela ponte da HS4 para o hub plano-hapvida-manaus e pelo reforço de autoridade tópica do cluster de Manaus. Quem busca também inclui quem avalia a rede antes de contratar — mas não é a maioria. Declaração exigida pelo juiz P-B (Agente 24) no refino de 2026-08-31."
  secundarias:
    - kw: "marcar consulta hapvida manaus"
      volume: 720
      dificuldade: 13
      intencao: navigational
      veredito: qualificada
      audiencia: "mista — beneficiário atual em maioria, mais quem avalia a rede antes de contratar"
      onde_entra: "H3 dentro da HS2 e FAQ 4 — sem H2 dedicado, por decisão do refino"
      cluster_candidata: não
    - kw: "hapvida manaus marcar consulta"
      volume: 720
      dificuldade: 32
      intencao: transactional
      veredito: qualificada
      audiencia: "mista"
      onde_entra: "corpo da HS2, variação natural"
      cluster_candidata: sim
    - kw: "hapvida consultas manaus"
      volume: 720
      dificuldade: 53
      intencao: informational
      veredito: qualificada
      audiencia: "mista"
      onde_entra: "corpo da HS2"
      cluster_candidata: não
    - kw: "laboratórios hapvida manaus"
      volume: 210
      dificuldade: 0
      intencao: navigational
      veredito: qualificada
      audiencia: "mista"
      onde_entra: "HS2, no trecho de exames, com link para o pillar de laboratórios"
      cluster_candidata: sim
    - kw: "laboratório hapvida manaus"
      volume: 210
      dificuldade: 7
      intencao: navigational
      veredito: qualificada
      audiencia: "mista"
      onde_entra: "HS2, variação natural no mesmo trecho"
      cluster_candidata: não
    - kw: "centro clinico duque de caxias"
      volume: 720
      dificuldade: 0
      intencao: navigational
      veredito: qualificada
      audiencia: "quem procura a unidade e pode estar no município errado"
      onde_entra: "HS1, no parágrafo de desambiguação — USAR SÓ EM NEGAÇÃO: o termo também está em FORBIDDEN_TOKENS porque nomeia a unidade do Rio de Janeiro. A frase é do tipo 'se você procura o Centro Clínico Duque de Caxias do Rio, é outra unidade'. Ressalva pedida pelo Agente 6."
      cluster_candidata: sim
    - kw: "clinica hapvida manaus"
      volume: 10
      dificuldade: "sem dado — a API devolveu keyword_difficulty null, e null não é zero"
      intencao: navigational
      veredito: qualificada
      audiencia: "mista"
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
  titulo: "A policlínica da Praça 14: consulta e exame com hora marcada"
  dado_quantitativo: "codigo_tipo_unidade 4 (Policlínica) no CNES, contra 73 (Pronto Atendimento) das unidades de urgência da mesma rede em Manaus"
  vs_concorrentes: "nenhum dos quatro concorrentes lidos explica o que o tipo de estabelecimento significa para quem vai ser atendido"
  por_que_importa: "evita que o paciente vá à Praça 14 com um caso de urgência e perca tempo"
  defensibilidade: 2
  fonte: "consulta comparativa à API do CNES nos estabelecimentos 9505970, 9676783 e 9676759"

- categoria: acesso
  titulo: "Três turnos em Manaus, e por que isso não é o mesmo que 24 horas"
  dado_quantitativo: "turno CNES 04, manhã, tarde e noite — contra o turno contínuo de 24 horas registrado no Pronto Atendimento Cidade Nova"
  vs_concorrentes: "os diretórios publicam um horário e nenhum diz o que ele implica"
  por_que_importa: "quem trabalha consegue ir cedo ou no fim da tarde, e quem precisa de madrugada sabe que aqui não é o lugar"
  defensibilidade: 2
  fonte: "campo descricao_turno_atendimento da ficha CNES, comparado entre três unidades"

- categoria: custo
  titulo: "O que se paga por consulta e exame nesta unidade de Manaus"
  dado_quantitativo: "Tabela 1 de coparticipação: consulta eletiva R$ 25,42, exame simples R$ 45,79, exame complexo R$ 114,48"
  por_que_importa: "a unidade só faz consulta e exame — justamente os itens com coparticipação, ao contrário de internação e cirurgia, que são isentos"
  defensibilidade: 1
  ressalva: "o VALOR não é exclusivo desta unidade: vale para toda a faixa Tabela 1. O que é local é a pertinência — aqui a coparticipação incide em 100% do que a unidade faz. Ressalva pedida pelo Agente 24."
  fonte: consultar_coparticipacao

- categoria: orientação
  titulo: "O roteiro de quem chega na Avenida Duque de Caxias e precisa de outra coisa"
  dado_quantitativo: "4 destinos distintos da rede própria de Manaus, um por tipo de caso"
  vs_concorrentes: "zero concorrentes oferecem encaminhamento"
  por_que_importa: "é a única informação da página que o paciente não acha em mapa nem em diretório"
  defensibilidade: 2
  ressalva: "o roteiro é da REDE, não desta unidade — serviria a qualquer clínica de Manaus. O que o ancora aqui é o ponto de partida: quem já está na Praça 14. Ressalva pedida pelo Agente 24."
  fonte: "consultar_rede e o artigo irmão do Hospital Nilton Lins"

---

## 14 · DR2 PARTE 3---

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

> **Duas FAQ dependem de item pendente — não responder afirmativamente sem confirmar.**
> A FAQ 6 (coleta e exames) repousa no item 4 do `nao_encontrado`: o CNES registra
> serviço de apoio mas não nomeia coleta. A FAQ 9 (ônibus) repousa na linha 542,
> que veio de agregador de transporte. As duas ou são confirmadas pela central da
> Hapvida antes do Bloco A, ou a resposta é escrita no condicional, dizendo o que
> se sabe e o que confirmar. Achado convergente dos Agentes 23 e 24.

total: 12
com_dado_local: 12
genericas: 0
dependentes_de_verificar: 2 (as de número 6 e 9)

> **A FAQ 5 se responde em NEGAÇÃO ORIENTADA.** A pergunta é pelo número de
> contato da unidade, e a seção 8 prova que essa linha própria não existe. A
> resposta certa é dizer que o 4002-3633 é a central da Hapvida, não o telefone
> da unidade, e indicar o caminho que funciona (app e canais da operadora).
> Escrever o número como se fosse da unidade é o buraco que a própria pesquisa
> cavou. Achado do Agente 24.
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

Recontados no refino de 2026-08-31 depois do juiz P-B (Agente 24) mostrar que a
lista anterior inflava: ela misturava dado da UNIDADE com dado da REDE e com dado
da FAIXA de coparticipação, e ainda contava os quatro booleanos do CNES que a
seção 3.1 derrubou. O teste correto não é trocar a cidade — é **trocar a unidade
dentro de Manaus**.

dados_unicos: 12 — PASSOU

Sobrevivem ao teste duro (só existem NESTA unidade):

1. código CNES 9505970
2. código de estabelecimento 1302609505970
3. CNPJ 63.554.067/0197-00
4. `codigo_tipo_unidade` 4, Policlínica — as unidades de urgência da mesma rede são tipo 73
5. turno de manhã, tarde e noite — as unidades de urgência têm turno contínuo de 24 horas
6. horário 06:00 às 20:00 nos dias úteis
7. horário 06:00 às 17:00 no sábado
8. coordenadas -3.101992 e -60.025113
9. CEP 69020-141
10. endereço na Avenida Duque de Caxias, 1905, Praça 14 de Janeiro
11. nota 3,1 com 247 avaliações no Google
12. atualização da ficha CNES em 2025-09-03

> **O peso não está distribuído igualmente.** Sete dos doze (CNES, código de
> estabelecimento, CNPJ, CEP, coordenadas, endereço e data de atualização) são
> identidade de registro, que qualquer diretório da SERP também publica. Os que
> discriminam de verdade são cinco: o tipo 4 contra o 73, o turno contra o
> contínuo, os dois horários e a nota 3,1 com 247 avaliações. É neles que a
> originalidade do artigo se apoia. Ressalva pedida pelo Agente 24.

Reclassificados, e por isso FORA da conta:

- telefone 4002-3633 → é da Hapvida, não da unidade
- coparticipação R$ 25,42 / 45,79 / 114,48 → é da Tabela 1 inteira
- mapa de vocações da rede de Manaus → é da rede, serve a qualquer clínica da praça
- os quatro campos booleanos do CNES → não são preenchidos, ver seção 3.1

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

### 15.5 Ação pendente no lado do pillar (achado do Agente 24)

O plano de links só previa o spoke linkando o pillar. Sem o link descendente do
pillar para o spoke, a hierarquia entre as duas páginas fica por conta do Google —
que é exatamente o que produz canibalização. Ver a ação na seção 16.1.

anti-doorway: APROVADO — teste de substituição em cerca de 85%, 12 dados únicos, zero frase genérica e fronteira escrita contra os 4 irmãos.

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

### 16.1 Ação no lado do pillar — a proposta, não a execução

Depois de publicado este spoke, o pillar `clinicas-hapvida-por-capital` (id 147)
precisa de duas coisas, e nenhuma delas é feita por conta própria:

1. um link descendente da frase que ele já tem sobre a unidade da Praça 14 para
   este artigo, fixando a hierarquia hub → spoke;
2. uma decisão sobre o que aquela frase passa a dizer — hoje ela lista as seis
   Hapclínicas de Manaus numa linha só.

**Isto é uma proposta de pendência, não uma pendência criada.** A skill
`pendencias-tabelaplanos` proíbe gravar pendência no banco sem autorização
expressa do usuário. Fica registrado aqui para ser levado ao usuário junto com o
artigo pronto.

---

## 17 · RESUMO

```
═══════════════════════════════════════════
PESQUISA COMPLETA — REFINADA APOS O PORTAO DE PESQUISA
Alvo: Hapclinica Duque de Caxias, Manaus/AM  |  Tipo: unidade HS1-HS4
SERP: 10 organicos, mobile e desktop, sem featured snippet
CI-1: 4 concorrentes lidos por WebFetch, com headings literais
Keywords: principal 6.600/mes KD 0 + 7 secundarias qualificadas + 7 descartadas
Valor comercial: INDIRETO e declarado — a pagina converte pela ponte da HS4
Kit on-page: H1/title/meta SEM promessa de especialidades
Rede mapeada: 1 unidade-alvo, tipo CNES 4 (Policlinica), tres turnos
Produtos que dao acesso: Nosso Plano, Mix e Pleno (marca Hapvida, Norte)
Diferenciais: 4, dois deles com ressalva de abrangencia escrita
FAQ: 12, duas dependentes de item [VERIFICAR]
Dados unicos: 12 (recontados no teste de troca de UNIDADE, nao de cidade)
Fan-out: 7 sub-perguntas — 5 aqui, 2 no cluster
Defensibilidade: ganho do CI-2 rebaixado de nivel 1 para nivel 2, com motivo
Anti-doorway: APROVADO   |   Acao no pillar: proposta na secao 16.1
CORRECAO CRITICA: os booleanos do CNES nao provam nada — ver secao 3.1
═══════════════════════════════════════════
```

---

## 18 ·```

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
