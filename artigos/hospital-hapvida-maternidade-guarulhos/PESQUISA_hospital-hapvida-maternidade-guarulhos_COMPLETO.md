# PESQUISA hospital-hapvida-maternidade-guarulhos — FASE 0 (state file)

Tipo: hospital (HS1-HS4) · Skill: hapvida-article-builder-v7 · Aberto em 2026-09-16
Alvo: Hospital e Maternidade Guarulhos (Hapvida NotreDame Intermédica) — Av. Tiradentes, 1015, Jardim Santa Edwirges, Guarulhos-SP
URL de destino proposta: /hospital-e-maternidade-guarulhos-hapvida/

> **ACHADO QUE MUDA O ARTIGO:** o hospital foi **renomeado para Hospital Keila Ferreira**
> em 10-11/11/2025, em homenagem à bispa Keila Ferreira, e na mesma ocasião recebeu a
> **1ª Sala Lilás da Hapvida** (acolhimento a mulheres vítimas de violência de gênero).
> A keyword pedida é o **nome antigo** — que ainda concentra a maior parte do volume.

## 1. SERP real (serp_local)

coletado_em: 2026-09-16  # serp
- ferramenta: DataForSeo `serp_local` · location_code 2076 (Brasil) · language pt · device desktop · depth 20
  - nota: o location_code municipal de Guarulhos NÃO foi confirmado em fonte oficial (o CSV de
    geotargets do Google Ads está fora do alcance da rede desta sessão). Usado o código nacional
    já mapeado (2076). Registrado como limitação, não como escolha.
  - a mesma consulta em `device: mobile` devolveu erro 40101 do buscador (Internal SE Server Error);
    não foi possível medir o mobile nesta coleta.
- posicoes_principal: tabelaplanos.com.br NÃO aparece no top 20 de "hospital hapvida guarulhos" (site ausente da SERP-alvo)
- featured_snippet / formato de snippet: NÃO há caixa de resposta destacada. A SERP abre com
  `local_pack` (3 fichas do Google Maps) e traz `people_also_ask` na posição absoluta 5.
  Formato que o Google premia aqui: **ficha de lugar** (endereço, telefone, horário) + página de unidade.
  Consequência: a passagem citável do lead tem de responder "o que é, onde fica, o que faz, como se chama hoje"
  em parágrafo curto, no formato de ficha.
- item_types observados: local_pack · organic · people_also_ask · related_searches · google_reviews
- URLs concorrentes (SERP de "hospital hapvida guarulhos", desktop, 16/09/2026):
  - 1 (abs 4) https://www2.hapvida.com.br/unidades/hospital-keila-ferreira — oficial da operadora
  - 2 (abs 6) https://www.gndi.com.br/unidades/hospital-keila-ferreira — oficial da operadora
  - 3 (abs 7) https://www.gndi.com.br/w/noticias/o-hospital-e-maternidade-guarulhos-agora-se-chama-hospital-keila-ferreira — oficial (notícia da renomeação)
  - 4 (abs 8) https://www2.hapvida.com.br/unidades/centro-clinico-guarulhos-ii — oficial
  - 5 (abs 9) https://www.instagram.com/p/DQ4nED2EWvj/ — rede social
  - 6 (abs 10) https://www.carmelseguros.com.br/planos-saude/hapvida/duvidas-5394318-qual-endereco-hospital-guarulhos-plano-saude-hapvida-intermedica.html — CONCORRENTE (corretora)
  - 7 (abs 12) https://guia.agendarconsulta.com/sao-paulo/guarulhos/hospital-e-maternidade-guarulhos-hapvida-9255826 — CONCORRENTE (diretório)
  - 8 (abs 17) https://intermedicanotredameplanos.com.br/hospitais-notredame-intermedica-guarulhos/ — CONCORRENTE (corretora)
  - 9 (abs 18) https://www.meuplanohap.com.br/guia-medico/sp/guarulhos/ — CONCORRENTE (corretora)
  - 10 (abs 19) https://busqueplanodesaude.com.br/hospitais/hospital-e-maternidade-guarulhos — CONCORRENTE (corretora)
  - 11 (abs 20) http://cnes2.datasus.gov.br/Mod_Basico.asp?VCo_Unidade=3518809255826 — fonte primária (CNES)
  - 12 (abs 21) https://guarulhostododia.com.br/noticia/hapvida-muda-nome-de-hospital-em-guarulhos-e-inaugura-sala-de-acolhimento-para-mulheres — imprensa local
- perguntas do Google (people_also_ask), literais:
  - Qual hospital atende Hapvida em Guarulhos?
  - Qual é o melhor hospital em Guarulhos?
  - Quais hospitais o Hapvida atende?
  - Quais hospitais em São Paulo aceitam o plano de saúde Hapvida?
- related_searches, literais: Hospital hapvida guarulhos telefone · Hospital e maternidade guarulhos telefone ·
  Hospital notredame guarulhos telefone · Hospital keila ferreira guarulhos telefone · Avenida tiradentes 1015 guarulhos ·
  Hospital e maternidade guarulhos hapvida notredame intermédica · Avenida tiradentes 1037 guarulhos · Hospital keila ferreira é bom
- veredito SXO (tipo de página premiado): ficha de unidade + página de hospital. O arquétipo HS1-HS4 é o certo;
  a HS3 (como chegar / informações práticas) é a seção que disputa diretamente com o local_pack.

## 2. Kit on-page [V5]

- principal: kw: hospital e maternidade guarulhos hapvida | volume: 3.600/mês (na forma longa
  "hospital e maternidade guarulhos hapvida notredame intermédica") | dificuldade: 0-1 | intencao: transactional
  - alternativa curta medida: "hospital e maternidade guarulhos" — volume 1.600/mês, KD 0, navegacional,
    tendência anual **-58%** (o público está migrando para o nome novo)
  - a frase exata pedida ("hospital hapvida e maternidade guarulhos") tem **volume não medido**
    (`items_count: 0` no DataForSeo) — é cauda longa; entra como variação natural, não como âncora do title.
- secundarias:
  - kw: hospital keila ferreira | volume: 9.900 | intencao: navigational | veredito: qualificada | onde entra: H1/lead/HS1
    (ressalva: parte do volume pode ser busca pela pessoa homenageada, não pelo hospital — ver seção 8)
  - kw: hospital e maternidade guarulhos | volume: 1.600 | intencao: navigational | veredito: qualificada | onde entra: H2 da HS1
  - kw: hospital keila ferreira guarulhos | volume: 590 | intencao: navigational | veredito: qualificada | onde entra: H2 da HS3
  - kw: hospital hapvida guarulhos | volume: 260 (+191% no ano) | intencao: navigational + transactional | veredito: qualificada | onde entra: title e H2 da HS4
  - kw: avaliações sobre hospital e maternidade guarulhos hapvida notredame intermédica | volume: 170 | intencao: commercial | veredito: qualificada | onde entra: FAQ "é bom?"
  - kw: hospital e maternidade guarulhos hapvida | volume: 30 | intencao: transactional | veredito: qualificada | onde entra: H1
  - kw: pronto socorro hapvida guarulhos | volume: não medido isoladamente (aparece como termo relacionado) | intencao: transactional | veredito: qualificada | onde entra: H2 da HS2
  - kw: hospital e maternidade guarulhos telefone | volume: 90 | intencao: navigational | veredito: **descartada** — tráfego de quem já é paciente/cliente; o telefone é dado que a skill proíbe afirmar sem fonte viva
  - kw: hospital notredame guarulhos trabalhe conosco | volume: n/d | intencao: navigational | veredito: **descartada** — candidato a emprego, nunca vira cliente
  - kw: hospital maternidade guarulhos publico | volume: 20 | intencao: transactional | veredito: **descartada** — busca por maternidade do SUS, público que não contrata plano
- matriz de posicionamento: principal em H1, title, URL (`/hospital-e-maternidade-guarulhos-hapvida/`),
  meta description, 1º parágrafo (lead) e no H2 da HS1. Secundárias em ≥2 H2 distintos (HS3 e HS4).
- query fan-out (mínimo 5):
- pergunta: o Hospital e Maternidade Guarulhos mudou de nome? → AQUI (HS1 + FAQ)
- pergunta: o pronto-socorro do Hospital e Maternidade Guarulhos atende criança? → AQUI (HS2)
- pergunta: como chegar ao hospital da Av. Tiradentes, 1015, de ônibus? → AQUI (HS3)
- pergunta: o que levar para internar no Hospital e Maternidade Guarulhos? → AQUI (HS2) — depende de fonte viva
- pergunta: quais planos Hapvida dão acesso ao Hospital e Maternidade Guarulhos? → AQUI (HS4)
- pergunta: o que é a Sala Lilás do hospital de Guarulhos? → AQUI (HS1) — nenhum concorrente da SERP cobre
- pergunta: quanto custa o plano Hapvida em Guarulhos? → CLUSTER (link para /plano-hapvida-guarulhos/)
- pergunta: qual a carência para internação? → CLUSTER (o pillar de carências responde; aqui é 1 frase)
- pergunta: o hospital de Guarulhos ainda faz parto? → CLUSTER — já respondida na FAQ 2 do artigo de cidade; aqui vira link, não seção (anti-doorway)

## 3. Contexto local (IBGE / CNES / DATASUS)

- populacao: 1.291.771 habitantes (Censo 2022) — fonte: IBGE Cidades — https://cidades.ibge.gov.br/brasil/sp/guarulhos/panorama
  - rota: WebSearch com `allowed_domains: ibge.gov.br` — [INDEXADO — NAO E LEITURA DE PAGINA]
- densidade: 4.053,57 hab/km² (2022) — fonte: IBGE Cidades — https://www.ibge.gov.br/cidades-e-estados/sp/guarulhos.html
- posicao: 2ª cidade mais populosa de SP e maior cidade brasileira que não é capital — fonte: IBGE (a confirmar na leitura da página)
- CNES do estabelecimento: ficha CNES `VCo_Unidade=3518809255826` — fonte: CNES/DataSUS — http://cnes2.datasus.gov.br/Mod_Basico.asp?VCo_Unidade=3518809255826
  - **não lido** (egress bloqueado). Leitos, salas e UTIs ficam `[VERIFICAR]` e NÃO entram no artigo.
- acessibilidade / vias: Av. Tiradentes é eixo central de Guarulhos; proximidade da Rod. Presidente Dutra
  citada no artigo de cidade já publicado — fonte: artigo de cidade (dado da casa), a reancorar

## 4. Rede assistencial (consultar_rede ANTES da web)

coletado_em: 2026-09-16  # rede
Fonte: MCP `BD - Consultar` → `consultar_rede` (catálogo próprio) — tabela `rede_unidades`, PDF de rede pág. 217-220

### Hospital e Maternidade Guarulhos
  endereço: Av. Tiradentes, 1015 - Jardim Santa Edwirges, Guarulhos - SP
- tipo: Hospital (rede própria)
- fonte: consultar_rede (id 290, pagina_pdf 217) + www2.hapvida.com.br/unidades/hospital-keila-ferreira (SERP)
- defensibilidade: 1
- observação: o catálogo ainda registra o nome ANTIGO; o site oficial já usa "Hospital Keila Ferreira" —
  divergência interna registrada como pendência de catálogo.

### Centro Clínico Guarulhos I
  endereço: Av. Doutor Timóteo Penteado, 1168 - Centro, Guarulhos - SP
- tipo: Clínica (rede própria)
- fonte: consultar_rede (id 292, pagina_pdf 219)
- defensibilidade: 1

### Centro Clínico Guarulhos II
  endereço: Rua Cabo João Teruel Fregoni, 555 - Ponte Grande, Guarulhos - SP
- tipo: Clínica (rede própria)
- fonte: consultar_rede (id 293) + www2.hapvida.com.br/unidades/centro-clinico-guarulhos-ii (SERP)
- defensibilidade: 1

### Clínica Jardim Guarulhos
  endereço: Rua João Gonçalves, 172 - Centro, Guarulhos - SP
- tipo: Clínica (rede própria)
- fonte: consultar_rede (id 294) + consultar_artigo plano-hapvida-guarulhos
- defensibilidade: 1

### Hapvida NotreLabs Imedi Guarulhos (Ghelfond)
  endereço: Av. Paulo Faccini, 96 - Guarulhos - SP
- tipo: Diagnóstico (rede própria)
- fonte: consultar_rede (id 298, pagina_pdf 220)
- defensibilidade: 1

**Regra das duas listas:** catálogo (5 unidades) × guia oficial (não lido nesta sessão — egress).
O que o catálogo confirma pode ser afirmado; o que só aparece na SERP entra atribuído à fonte.

## 5. Desmontagem de concorrentes [V4 / CI-1]

> 🔴 **STATUS: NÃO CONCLUÍDA — a linha está PARADA neste ponto, por contrato da skill (V7.3).**
> Nenhum concorrente foi LIDO. Abaixo, cada tentativa registrada.

- rota 1 — `WebFetch`: **falhou**. `EGRESS_BLOCKED` (testado em tabelaplanos.com.br, 2026-09-16 09:45)
- rota 2 — `curl` via Bash: **falhou**. `CONNECT tunnel failed, response 403` em cnes.datasus.gov.br,
  www.hapvida.com.br e tabelaplanos.com.br; `scripts/testar-egress.sh` deu 0 alcançáveis / 5 bloqueados
- rota 3 — Chromium + Playwright: **falhou por dependência**. O binário existe (/opt/pw-browsers/chromium),
  mas todo cliente HTTP do contêiner passa pelo mesmo gateway que negou o CONNECT (confirmado com
  urllib: "Tunnel connection failed: 403 Forbidden")
- rota 4 — n8n (MCP `SEO - Hapvida`): **indisponível**. O servidor exige autorização OAuth e esta sessão
  é não-interativa; as ferramentas não estão carregadas
- rota 5 — `WebSearch`: usada só para achar URL e corroborar a renomeação. **NÃO conta como leitura.**
- concorrentes identificados e ainda NÃO lidos (alvos da CI-1 quando houver rota):
  - carmelseguros.com.br — url: https://www.carmelseguros.com.br/planos-saude/hapvida/duvidas-5394318-qual-endereco-hospital-guarulhos-plano-saude-hapvida-intermedica.html — lido_em: —
  - busqueplanodesaude.com.br — url: https://busqueplanodesaude.com.br/hospitais/hospital-e-maternidade-guarulhos — lido_em: —
  - meuplanohap.com.br — url: https://www.meuplanohap.com.br/guia-medico/sp/guarulhos/ — lido_em: —
  - intermedicanotredameplanos.com.br — url: https://intermedicanotredameplanos.com.br/hospitais-notredame-intermedica-guarulhos/ — lido_em: —
  - guia.agendarconsulta.com — url: https://guia.agendarconsulta.com/sao-paulo/guarulhos/hospital-e-maternidade-guarulhos-hapvida-9255826 — lido_em: —
  - matriz de cobertura: pendente de leitura
- **decisão pendente do usuário** (ver 00-ESTADO.md): liberar a rede, colar as páginas, ou autorizar
  expressamente o artigo sem desmontagem de concorrente.

## 6. Ganho de informação / brechas [V4 / CI-2]

> Provisório — depende da CI-1 para ser fechado. O que segue já está apoiado em dado de nível 1-2.

- must-match (o que qualquer página sobre este hospital precisa ter): endereço completo, o que o
  pronto-socorro atende, se há maternidade ativa, quais planos dão acesso, como chegar.
- brecha 1: **nenhum resultado orgânico da SERP explica a troca de nome ao leitor que busca pelo nome antigo.**
  A notícia oficial existe (gndi.com.br) mas não aparece para quem busca "hospital hapvida guarulhos" em primeiro lugar,
  e as páginas de corretora seguem usando o nome velho sem avisar que mudou.
- brecha 2: a SERP inteira é ficha cadastral (endereço + telefone). Ninguém responde
  "como é ser atendido lá" — que é justamente o mandato do arquétipo HS1-HS4.
- GANHO DE INFORMAÇÃO (candidato): **o guia da mudança de nome + a Sala Lilás.**
  Em 10-11/11/2025 o Hospital e Maternidade Guarulhos passou a se chamar Hospital Keila Ferreira e recebeu
  a **1ª Sala Lilás da Hapvida** — atendimento humanizado e reservado a mulheres e meninas vítimas de violência
  de gênero. É um serviço que nenhum concorrente da SERP menciona e que muda o que se pode dizer do hospital.
  - defensibilidade: 4 (público-trabalhoso) para o fato da renomeação — corroborado por 5 fontes independentes
  - defensibilidade: 1-2 para o que a casa acrescenta: a rede de Guarulhos conferida unidade a unidade
    (`consultar_rede`) e a leitura de quem contrata — qual plano abre a porta deste hospital
  - 🔴 **TRAVA CI-2 ACIONADA:** a v6 exige ganho em nível 1-2. Este candidato nasce em nível 4.
    Fechar exige ou a CI-1 (provar que nenhum concorrente cobre) ou reancorar o ganho no dado da casa.

## 7. Dado proprietário [V7.2] (consultar_rede · cotador_fila · banco)

- dado_proprietario: 5 unidades próprias da Hapvida em Guarulhos conferidas uma a uma (1 hospital, 3 clínicas,
  1 diagnóstico), com endereço — defensibilidade: 1 — fonte: `consultar_rede` (ids 290, 292, 293, 294, 298)
- dado_proprietario: Clínica Jardim Guarulhos — inaugurada em jun/2025, R$ 1,3 milhão investido,
  capacidade de 10.500 consultas/mês — defensibilidade: 1 — fonte: `consultar_artigo` (banco da casa, artigo de cidade)
- dado_proprietario: coparticipação vigente do grupo SP/BH — consulta eletiva R$ 43,63 · urgência R$ 61,82 ·
  exame simples R$ 51,52 · exame complexo R$ 125,93 — defensibilidade: 1 — fonte: `consultar_coparticipacao` (p_regiao sp_bh)
  - no artigo, estes valores entram por **shortcode**, nunca digitados
- dado_proprietario: números canônicos Hapvida — 86 hospitais próprios · 168 credenciados · 80 PAs 24h ·
  365 clínicas · 301 unidades de diagnóstico · 15,9 mi de beneficiários · 16 estados —
  defensibilidade: 1 — fonte: `consultar_dados_canonicos`
- dado_proprietario: o catálogo interno ainda registra o nome antigo do hospital enquanto o site oficial já
  usa o novo — defensibilidade: 2 — fonte: cruzamento `consultar_rede` × `consultar_artigo` × SERP

## 8. Não encontrado [V7.2]

nao_encontrado:
- número de leitos, salas cirúrgicas, UTI adulto/neonatal do hospital — onde foi procurado: `consultar_rede`,
  `consultar_artigo`, SERP (a ficha CNES apareceu mas não pôde ser aberta). **Fica fora do artigo.**
- telefone da unidade — onde foi procurado: catálogo do banco (não tem). O local_pack mostra (11) 2463-8610,
  mas ficha do Maps não é fonte primária e o `checkpoint_verificar.py` proíbe telefone no corpo.
- **fonte primária** da afirmação "a maternidade segue ativa" — onde foi procurado: catálogo do banco
  (registra "maternidade" só no nome antigo), SERP (nenhum resultado orgânico afirma), CNES (não pôde ser aberto).
  O artigo de cidade publicado **já afirma** parto normal, cesárea, UTI adulto e centro cirúrgico neste hospital
  (FAQ 2 e card da S4), mas a fonte daquela afirmação não está registrada no banco. Enquanto não for reconfirmada,
  o artigo novo **repete a atribuição da casa sem endurecê-la** e não acrescenta número de leito, sala ou UTI.
  Precedente que obriga cautela: o Hospital Nossa Senhora do Rosário (Vila Maria) tem artigo próprio no site
  justamente sobre "o que atende depois do fim da maternidade".
- linhas de ônibus e estrutura de estacionamento — onde foi procurado: SERP. Não confirmado.
- volume de busca da frase exata "hospital hapvida e maternidade guarulhos" — onde foi procurado:
  DataForSeo `keyword_data` devolveu `items_count: 0`.
- quanto do volume de "hospital keila ferreira" (9.900/mês) é busca pelo hospital e quanto é pela pessoa
  homenageada — onde foi procurado: `keyword_data` (não separa). Não usar esse número como promessa de tráfego.

## 9. FORBIDDEN_TOKENS

FORBIDDEN_TOKENS:
- Hospital Keila Ferreira é o maior
- 88 hospitais
- 10 anos
- (11) 2463-8610
- leitos
- UTI neonatal
- salas cirúrgicas
- ONA Nível 3
- Hospital e Maternidade São Luiz Guarulhos
- Rede D'Or
- parto humanizado

## 10. PLANO_MODELOS [V7.2]

<!-- a preencher pelo Agente 22 antes do Estágio 1 de redação -->

## 11. Datas de coleta

coletado_em: 2026-09-16  # serp
coletado_em: 2026-09-16  # rede
coletado_em: —           # concorrentes (CI-1 não realizada)

## 12. FAQ local

- O Hospital e Maternidade Guarulhos mudou de nome?
- O Hospital e Maternidade Guarulhos é o mesmo Hospital Keila Ferreira?
- Onde fica o Hospital e Maternidade Guarulhos da Hapvida?
- O pronto-socorro do Hospital e Maternidade Guarulhos funciona 24 horas?
- O Hospital e Maternidade Guarulhos atende criança no pronto-socorro?
- O Hospital e Maternidade Guarulhos ainda faz parto?
- O que é a Sala Lilás do Hospital e Maternidade Guarulhos?
- Preciso de encaminhamento para ser atendido no Hospital e Maternidade Guarulhos?
- Quais planos Hapvida dão acesso ao Hospital e Maternidade Guarulhos?
- Quem mora fora de Guarulhos pode ser internado no Hospital e Maternidade Guarulhos?
- O Hospital e Maternidade Guarulhos faz exame de imagem ou tenho de ir ao diagnóstico?
- Internação no Hospital e Maternidade Guarulhos tem coparticipação?

## 13. Anti-doorway

- teste_substituicao: trocar "Guarulhos" por "Osasco" invalida o lead (endereço, nome antigo e novo,
  Sala Lilás), a HS1 (a história da renomeação) e a HS3 (Av. Tiradentes / Dutra). A HS4 é a seção de maior
  risco — é onde o texto tende a virar molde de plano — e por isso fica curta, em bridge + link.
- dados_unicos: 12 — (1) troca de nome em 10-11/11/2025 · (2) homenagem à bispa Keila Ferreira · (3) 1ª Sala Lilás
  da Hapvida · (4) endereço Av. Tiradentes, 1015, Jd. Santa Edwirges · (5) 5 unidades próprias na cidade
  conferidas no catálogo · (6) Clínica Jardim inaugurada em jun/2025 com R$ 1,3 mi · (7) capacidade de
  10.500 consultas/mês na Clínica Jardim · (8) Centro Clínico Guarulhos II na Ponte Grande ·
  (9) NotreLabs Imedi (ex-Ghelfond) na Av. Paulo Faccini · (10) a busca pelo nome antigo caiu 58% em um ano
  enquanto a do nome novo saiu do zero · (11) Guarulhos tem 1.291.771 habitantes (Censo 2022) ·
  (12) o catálogo da casa e o site oficial divergem no nome da unidade
- frases_genericas: 0 toleradas. Proibido no artigo: "modelo verticalizado", "rede própria sempre que possível",
  "atendimento de qualidade", "tranquilidade para você e sua família", "como qualquer plano regulado pela ANS".
- anti-doorway: PENDENTE — a matriz contra o artigo de cidade está fechada (seção 15); falta só a CI-1.
  Não escrever APROVADO nesta linha antes de o concorrente ser lido ou de o usuário dispensar a CI-1.

## 14. Fio condutor

Este é o hospital que mudou de nome e ninguém avisou a quem busca. O artigo é a ponte entre os dois nomes:
começa respondendo "sim, é o mesmo hospital, na mesma Av. Tiradentes, 1015" e, a partir daí, conta o que
mudou de verdade dentro dele — a Sala Lilás — e o que o paciente precisa saber para ser atendido lá.
Tom de quem já levou gente naquele pronto-socorro, não de quem copiou a ficha do Maps.


## 15. O QUE NÃO REPRODUZIR — matriz contra o artigo de cidade (obrigatória no arquétipo hospital)

Fonte: leitura do HTML publicado de `/plano-hapvida-guarulhos/` (post 31688, 81.700 caracteres,
modificado em 2026-08-19), salvo em `fontes/artigo-cidade-guarulhos.html`.
**O artigo de cidade é muito mais denso sobre este hospital do que o normal — o risco de doorway é ALTO.**

| O artigo de cidade JÁ diz | O artigo de hospital |
|---|---|
| Card da S4: internação clínica e cirúrgica, maternidade com parto normal e cesárea, centro cirúrgico, UTI, pronto-atendimento, parque de diagnóstico | NÃO repetir a lista. Aprofundar UM item (o fluxo do pronto-atendimento) |
| Endereço "Av. Tiradentes, 1015 — Jd. Santa Edwirges" | Aparece 1× só, na HS3, e com ângulo de COMO CHEGAR |
| Linha do tempo: inauguração em 2012 pela NotreDame, fusão em 2022, renomeação em 2025, 2º hospital planejado | NÃO repetir a linha do tempo. Narrar só o episódio de 2025, com o que o de cidade não tem (a Sala Lilás) |
| "única maternidade própria da operadora na região" / "único hospital próprio de operadora verticalizada no município" | NÃO repetir a comparação com concorrentes — é a S6 do de cidade |
| Coparticipação: consulta eletiva, exame simples, isenção em internação e parto | 1 frase + link. NUNCA a mecânica |
| Tabela de bairros e tempos (Centro, Cumbica, Bonsucesso, Pimentas, Arujá) | NÃO reproduzir. Na HS3, transporte e acesso — não tabela de cobertura |
| 12 km do Aeroporto GRU, 15-25 min pela Dutra | Já é do de cidade (FAQ 12). Só pode voltar como ângulo de acesso, com dado novo |
| Clínica Jardim: jun/2025, R$ 1,3 mi, 10.500 consultas/mês, 7 especialidades | NÃO repetir. Citar só para diferenciar o que se resolve na clínica e o que exige o hospital |
| Planos: Nosso Plano, Mix, Ambulatorial descritos | NÃO descrever produto. HS4 faz só a ponte produto → acesso a este hospital |

### FAQ — ZERO overlap (6 do artigo de cidade falam do hospital e estão QUEIMADAS)

Queimadas (não repetir, nem reformuladas): "O Hospital Keila Ferreira tem maternidade e UTI neonatal?" ·
"Qual a diferença entre o Hospital Keila Ferreira e as clínicas?" · "A Hapvida tem pronto-atendimento 24h na cidade?" ·
"Quanto tempo leva do Aeroporto GRU até o Hospital Keila Ferreira?" · "A Hapvida de Guarulhos atende moradores de
Arujá e Itaquaquecetuba?" · "O segundo hospital da operadora na cidade já foi inaugurado?"

Consequência para a FAQ da seção 12: caem por overlap **"O Hospital e Maternidade Guarulhos ainda faz parto?"**
(≈ FAQ 2 do de cidade), **"O pronto-socorro funciona 24 horas?"** (≈ FAQ 9) e **"Quem mora fora de Guarulhos pode
ser internado?"** (≈ FAQ 11). Entram no lugar, todas com o nome do hospital e sem eco no de cidade:
- O que levar para internar no Hospital e Maternidade Guarulhos?
- Qual o horário de visita no Hospital e Maternidade Guarulhos?
- O acompanhante pode ficar com o paciente internado no Hospital e Maternidade Guarulhos?
- O Hospital e Maternidade Guarulhos tem estacionamento?
Estas quatro dependem de fonte viva (site oficial / CNES / regimento da unidade) e hoje estão bloqueadas pelo egress.

### Catálogo de FAQs do banco (categoria "hospital")
Templates já em uso que NÃO podem virar pergunta deste artigo: "O Hospital [X] tem maternidade ativa?" (id 12,
usado em Limeira, Bauru, Joinville, Lins) · "Qual hospital Hapvida faz parto em [cidade]?" (id 11, 8 artigos) ·
"Tem hospital da Hapvida em [cidade]?" (id 10, 10 artigos).

## 16. Plano de links (governança de âncoras + saturação)

Fonte: `consultar_saturacao_destinos` (2026-09-16). Regra da casa: nunca linkar destino SATURADO (≥15).

| Destino | Backlinks | Classificação | Uso aqui |
|---|---|---|---|
| plano-hapvida-guarulhos | 2 | SUBUTILIZADO | **hub obrigatório** — HS4, 1× |
| hospital-nossa-senhora-do-rosario-hapvida | 3 | SUBUTILIZADO | HS2 — referência de alta complexidade materno-infantil |
| plano-de-saude-para-recem-nascido | 3 | SUBUTILIZADO | FAQ de maternidade |
| pronto-socorro-hapvida-sp | 7 | NORMAL | HS2 — quando o caso vai para a capital |
| hapvida-rede-pediatrica | 11 | NORMAL | FAQ de pediatria |
| tabela-precos-hapvida-coparticipacao-guia-completo | 63 | 🔴 SATURADO | **não linkar** — a menção de coparticipação fica como texto |
| plano-de-saude-hapvida-carencia | 56 | 🔴 SATURADO | **não linkar** |
| hospitais-credenciados-hapvida | 31 | 🔴 SATURADO | **não linkar** |

Conflito registrado: `references/artigo-hospital.md` pede link para os pillars de coparticipação e carências;
os dois estão saturados no banco. Decisão proposta: honrar a saturação (regra do banco vence) e cumprir o mínimo
de 4 links internos com os destinos subutilizados acima. Confirmar no portão humano.

Externos (mín. 2, `rel="nofollow noopener"`): 1 no corpo → página oficial da unidade
(www2.hapvida.com.br/unidades/hospital-keila-ferreira); 1-2 no rodapé → CNES/DataSUS (ficha 3518809255826)
e IBGE Cidades. **Não** usar ANS (já é o par padrão dos artigos de cidade).
