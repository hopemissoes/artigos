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
  - kw: hospital keila ferreira | volume: 9.900 | intencao: navigational | veredito: **qualificada com
    desconto** | onde entra: lead e HS1, **não no title nem como promessa de tráfego**
    (o volume saltou de 0 para 12-18 mil entre out/2025 e jan/2026, exatamente quando a bispa homenageada
    morreu e o hospital foi renomeado; o `keyword_data` não separa busca pela pessoa de busca pelo hospital.
    Tratar como teto, nunca como previsão — ver seção 8)
  - kw: hospital e maternidade guarulhos | volume: 1.600 | intencao: navigational | veredito: qualificada | onde entra: H2 da HS1
  - kw: hospital keila ferreira guarulhos | volume: 590 | intencao: navigational | veredito: qualificada | onde entra: H2 da HS3
  - kw: hospital hapvida guarulhos | volume: 260 (+191% no ano) | intencao: navigational + transactional | veredito: qualificada | onde entra: title e H2 da HS4
  - kw: avaliações sobre hospital e maternidade guarulhos hapvida notredame intermédica | volume: 170 | intencao: commercial | veredito: qualificada | onde entra: FAQ "é bom?"
  - kw: hospital e maternidade guarulhos hapvida | volume: 30 | intencao: transactional | veredito: qualificada | onde entra: H1
  - kw: pronto socorro hapvida guarulhos | volume: não medido isoladamente (aparece como termo relacionado) | intencao: transactional | veredito: qualificada | onde entra: H2 da HS2
  - kw: hospital e maternidade guarulhos telefone | volume: 90 | intencao: navigational | veredito: **descartada** — tráfego de quem já é paciente/cliente; o telefone é dado que a skill proíbe afirmar sem fonte viva
  - kw: hospital notredame guarulhos trabalhe conosco | volume: n/d | intencao: navigational | veredito: **descartada** — candidato a emprego, nunca vira cliente
  - kw: hospital maternidade guarulhos publico | volume: 20 | intencao: transactional | veredito: **descartada** — busca por maternidade do SUS, público que não contrata plano
- **DECISÃO DO USUÁRIO (2026-09-16): a keyword principal é a PONTE entre os dois nomes.**
  H1/title abrem com "Hospital e Maternidade Guarulhos" (nome antigo, onde está o volume) e trazem
  "Hospital Keila Ferreira" entre parênteses. O lead responde a equivalência na primeira frase — é a
  passagem citável e a brecha nº 1 da SERP.
  - title proposto (60 chars): `Hospital e Maternidade Guarulhos Hapvida: agora Keila Ferreira`
  - meta proposta: `O Hospital e Maternidade Guarulhos da Hapvida agora se chama Hospital Keila Ferreira. Mesmo endereço na Av. Tiradentes: o que atende, como chegar e quais planos dão acesso.`
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
- posicao no ranking de municípios: `[VERIFICAR]` — a leitura da página do IBGE não foi possível (egress).
  Fica FORA do artigo enquanto não for conferida.
- CNES do estabelecimento: código 9255826 — **ficha LIDA em 2026-09-16 pela rota n8n** — fonte: CNES/DataSUS
  - estabelecimento: **HOSPITAL KEILA FERREIRA** (o registro federal já usa o nome novo)
  - nome empresarial: NOTRE DAME INTERMEDICA SAUDE S A · diretor clínico: FUAD MASSABKI JUNIOR
  - logradouro: TIRADENTES, 1015, JARDIM GUARULHOS, CEP 07090000, GUARULHOS/SP
  - atividade principal: INTERNACAO · convênios: particular e plano de saúde privado
  - serviços registrados (tradução do código oficial, o que nenhum concorrente faz):
    112-003 PARTO · 112-004 PARTO EM GESTAÇÃO DE ALTO RISCO · 162-001 UTI ADULTO · 162-002 UTI NEONATAL ·
    140-019 PRONTO SOCORRO GERAL/CLÍNICO · 140-013 PS OBSTÉTRICO · 140-012 PS PEDIÁTRICO ·
    140-016 PS TRAUMATO-ORTOPÉDICO · 140-004 SALA DE ESTABILIZAÇÃO · 142-001 ENDOSCOPIA DIGESTIVA ·
    121-001 RADIOLOGIA · 125-006 FARMÁCIA HOSPITALAR · 170-001 NÚCLEO DE SEGURANÇA DO PACIENTE
  - instalações: 11 consultórios · 5 salas de cirurgia · 1 sala de pré-parto · 1 sala de parto normal ·
    8 leitos de RN patológico · 13 leitos de alojamento conjunto · 2 salas de acolhimento com classificação
    de risco · brinquedoteca · sala de gesso
  - equipamentos: 16 incubadoras · 8 berços aquecidos · 5 aparelhos de fototerapia · 14 laparoscópios ·
    35 respiradores · 10 desfibriladores · ultrassom · 3 aparelhos de raio-X
  - apoio próprio: farmácia, central de esterilização, serviço social, prontuário. Terceirizados: nutrição,
    lactário, lavanderia, ambulância.
  - fonte transcrita em `fontes/ci1-rodada2-fontes-primarias.md`
### Material da HS3 (como chegar e informações práticas) — coletado para fechar a seção órfã
- endereço no registro federal: **Av. Tiradentes, nº 1015, complemento "1 037"** — fonte: ficha CNES 9255826.
  O complemento explica a related_search medida "Avenida Tiradentes 1037 Guarulhos": são o mesmo endereço.
- **divergência de bairro, registrada de propósito:** o CNES diz "JARDIM GUARULHOS"; o site da operadora e a
  imprensa dizem "Jardim Santa Edwirges" — fontes: ficha CNES × gndi.com.br/unidades/hospital-keila-ferreira ×
  Joi/oitapecericano.com.br (https://www.oitapecericano.com.br/noticia/hospital-guarulhos-passa-a-se-chamar-hospital-keila-ferreira, lido em 2026-09-16). Quem procura pelo bairro errado no mapa não acha. É material de HS3, não erro a esconder.
- CEP: 07090000 — fonte: ficha CNES
- coordenadas da unidade: -23.46507433030174 / -46.53342107370293 — fonte: gndi.com.br (HTML da página da unidade)
- ❌ **bloco de "referências a pé" REMOVIDO** (achado 🔴 do juiz P-A, rodada 2). As distâncias de 0,1-0,2 km
  vinham do widget "Unidades Próximas" do agregador, não de campo do CNES, e a atribuição anterior estava
  errada. A transcrição literal ficou salva em `fontes/ci1-rodada2-fontes-primarias.md`, seção 6, **fora do
  artigo**: distância de widget não é medida oficial, e uma das unidades listadas é hospital municipal —
  citá-la aqui misturaria rede pública e rede própria.
- eixo viário: a Av. Tiradentes corta a região central de Guarulhos — fonte: Guarulhos Todo Dia 11/11/2025
  ("fica na Av. Tiradentes, 1015, na região central de Guarulhos")
- **não confirmado e declarado como tal:** linha de ônibus (a página de itinerário da prefeitura não publica
  o dado no HTML) e estacionamento (nenhuma fonte)

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

**Regra das duas listas — aplicada, com o resultado declarado:**
- lista A (catálogo da casa, `consultar_rede`): 5 unidades próprias em Guarulhos.
- lista B (guia oficial da operadora): **não obtida**. As duas páginas de unidades (gndi.com.br/nossas-unidades
  e www2.hapvida.com.br/unidades) foram buscadas em 2026-09-16 pela rota n8n e voltaram com 320 e 307 palavras
  de menu — são SPA, a lista só existe depois do JavaScript.
- **Consequência para a escrita, sem exceção:** o artigo NÃO afirma que a Hapvida tem 5 unidades em Guarulhos
  como fato do mundo. Escreve **atribuído ao catálogo** ("no catálogo de rede da operadora constam...") e
  **nunca** afirma ausência ("não há outra unidade em X") — ausência no catálogo não é prova de ausência na
  rede. As 3 unidades que o artigo de cidade cita e o catálogo confirma são as únicas nomeadas.
- unidade-objeto: o catálogo está **comprovadamente desatualizado** nela (registra o nome antigo enquanto o
  CNES e o site já usam o novo). Para o hospital, a fonte que manda é a ficha CNES 9255826, não o catálogo.

## 5. Desmontagem de concorrentes [V4 / CI-1]

> ✅ **CI-1 FECHADA em 2026-09-16 09:59 pela ROTA 4 (n8n).** As rotas 1, 2 e 3 caíram por política de
> egress do ambiente (403 no CONNECT, em duas rodadas de teste). A rota 4 abriu quando o servidor MCP
> `SEO - Hapvida` ficou disponível na sessão: o workflow "CI-1 Concorrentes — Hospital e Maternidade
> Guarulhos" (id `i0jtkZgMawCjqYHk`, execuções 33231 e 33232) roda no servidor do usuário, fora do
> gateway que bloqueia o contêiner. Páginas salvas em `fontes/`.

### https://www.carmelseguros.com.br/planos-saude/hapvida/duvidas-5394318-qual-endereco-hospital-guarulhos-plano-saude-hapvida-intermedica.html
- coletado_em: 2026-09-16 | rota: n8n (HTTP Request rodando no servidor, fora do gateway)
- titulo_da_pagina: Qual é o endereço do Hospital Guarulhos do Plano de Saúde Hapvida Intermédica
  h2_literais:
  - "Qual é o endereço do Hospital Guarulhos do Plano de Saúde Hapvida Intermédica?"
  - "Outras dúvidas sobre o Plano de saúde Hapvida"
  - "Faça sua cotação online agora mesmo"
  - "Dados Pessoais"
  - "Dados para cotação"
- cobertura: 643 palavras, 0 tabela. É uma página de FAQ de uma pergunta só, com formulário. Não fala do
  hospital além do endereço. Fraqueza: conteúdo fino; o resto da página é FAQ de produto de viagem
  ("Plano Infinity"), sem relação com Guarulhos.

### https://busqueplanodesaude.com.br/hospitais/hospital-e-maternidade-guarulhos
- coletado_em: 2026-09-16 | rota: n8n (HTTP Request rodando no servidor, fora do gateway)
- title: "Hospital e Maternidade Guarulhos: convênios, contato e planos de saúde aceitos"
  h2_literais:
  - "Sobre o Hospital e Maternidade Guarulhos"
  - "Hospital e Maternidade Guarulhos: referência em atendimento multidisciplinar"
  - "Quais planos cobrem o Hospital e Maternidade Guarulhos"
  - "Contato"
  - "Especialidades do Hospital e Maternidade Guarulhos"
  - "Convênios e planos relacionados ao Hospital e Maternidade Guarulhos"
  - "Dúvidas sobre planos aceitos pelo Hospital e Maternidade Guarulhos"
  - "Infraestrutura Moderna e Completa"
  - "Maternidade de excelência e equipe qualificada"
  - "Quais planos de saúde atendem o Hospital e Maternidade Guarulhos?"
  - "O Hospital e Maternidade Guarulhos aceita todos os convênios listados?"
- cobertura: 1.900 palavras, 10 H2, 18 H3, 1 tabela, preços de R$ 175,24 a R$ 727,74.
- **é o concorrente mais completo da SERP** — é ele que define o piso de profundidade.
- fraquezas: (1) usa o **nome antigo** e não avisa que mudou; (2) texto institucional genérico
  ("referência em atendimento multidisciplinar", "maternidade de excelência") sem um dado do hospital;
  (3) lista planos de operadoras concorrentes (Porto, Sami, Amil) na página de um hospital da Hapvida;
  (4) nenhuma instrução prática — como chegar, o que levar, horário de visita.

### https://www.meuplanohap.com.br/guia-medico/sp/guarulhos/
- coletado_em: 2026-09-16 | rota: n8n (HTTP Request rodando no servidor, fora do gateway)
- title: "Hapvida Guarulhos SP: Guia Médico e Rede Credenciada"
  h2_literais:
  - "Hapvida Guarulhos SP: Guia Médico e Rede Credenciada"
  - "Endereços em Guarulhos"
  - "Dúvidas Frequentes"
  - "Orçamento Online"
  - "Opinião dos nossos clientes"
  - "Hapvida em cidades vizinhas"
- cobertura: 4.312 palavras — mas o volume é lista de especialidades e endereços despejados, não texto.
- fraqueza: é diretório, não guia. Trata o hospital como uma linha de endereço no meio da rede.

### https://intermedicanotredameplanos.com.br/hospitais-notredame-intermedica-guarulhos/
- coletado_em: 2026-09-16 | rota: n8n (HTTP Request rodando no servidor, fora do gateway)
  h2_literais:
  - "Rede Credenciada NotreDame Intermédica na Cidade de Guarulhos"
  - "Clinicas Medicas em Guarulhos"
  - "Confira Abaixo a rede Completa de hospitais NotreDame Intermédica"
  - "Hospitais e Laboratório em Guarulhos"
- cobertura: 11.718 palavras, 1 tabela, 0 H1. É um despejo da rede credenciada inteira.
- fraquezas: sem H1, marca desatualizada ("NotreDame Intermédica" sem Hapvida), zero conteúdo sobre o
  hospital em si. Página de listagem que ranqueia por tamanho, não por resposta.

### https://guia.agendarconsulta.com/sao-paulo/guarulhos/hospital-e-maternidade-guarulhos-hapvida-9255826
- coletado_em: 2026-09-16 | rota: n8n (HTTP Request rodando no servidor, fora do gateway)
- title: "HOSPITAL E MATERNIDADE GUARULHOS HAPVIDA - Guarulhos (SP) | Agendar Consulta"
  h2_literais:
  - "Horário de Funcionamento"
  - "Serviços e Convênios"
  - "Serviços Especializados"
  - "Atividades Secundárias"
  - "Equipamentos"
  - "Instalações Físicas para Assistência"
  - "Serviços de Apoio"
  - "Perguntas Frequentes"
  - "Como faço para agendar uma consulta em HOSPITAL E MATERNIDADE GUARULHOS HAPVIDA?"
  - "Como chegar até HOSPITAL E MATERNIDADE GUARULHOS HAPVIDA em Guarulhos?"
  - "Este hospital possui pronto-socorro 24 horas?"
- cobertura: 975 palavras, 19 H2, 14 tabelas. É um espelho automático do CNES.
- fraquezas: (1) "Horário de Funcionamento: informação não disponível para esta unidade";
  (2) responde "Este hospital possui pronto-socorro 24 horas?" com **"a disponibilidade varia por hospital,
  ligue para confirmar"** — ou seja, a pergunta mais urgente da SERP fica sem resposta;
  (3) nome antigo; (4) nenhum contexto de plano — não diz o que abre a porta daquele hospital.

### Matriz de cobertura (subtópico × concorrente)

| Subtópico | carmel | busque | meuplanohap | intermedica | agendarconsulta | NÓS |
|---|---|---|---|---|---|---|
| Endereço | cobre | cobre | cobre | cobre mal | cobre | cobre (HS3) |
| **Mudança de nome (nov/2025)** | não | não | não | não | não | **só nós** |
| **Sala Lilás** | não | não | não | não | não | **só nós** |
| Estrutura real (salas, UTI, PS) | não | cobre mal | não | não | cobre (CNES cru) | cobre traduzido (HS1/HS2) |
| PS — o que o registro mostra | não | não | não | não | "ligue para confirmar" | **diz quais PS existem no registro federal (geral, obstétrico, pediátrico, traumato-ortopédico) e diz que o horário não consta em fonte nenhuma** |
| Parto / alto risco | não | cobre mal | não | não | cobre (código CNES) | cobre (HS2 + FAQ) |
| Como chegar / transporte | não | não | não | não | só botão de mapa | cobre (HS3) |
| O que levar / visita / acompanhante | não | não | não | não | não | **só nós** (depende de fonte) |
| Quais planos dão acesso | cobre mal | cobre (com concorrentes juntos) | cobre mal | não | não | cobre (HS4) |
| Preço | não | cobre | não | não | não | 1 frase + link |
| **palavras · subtópicos** | 643 · 2 | **1.900 · 10** | 4.312 · 5 | 11.718 · 3 | 975 · 19 | piso: superar busque |

**Piso de profundidade dinâmico:** o líder de cobertura real é o `busqueplanodesaude` (10 subtópicos de
conteúdo em 1.900 palavras). O artigo tem de cobrir todos os MUST-MATCH dele e superá-lo em subtópicos —
com material local, não com enchimento.

## 6. Ganho de informação / brechas [V4 / CI-2]

resumo: ponte entre os dois nomes do hospital + tradução do registro CNES + Sala Lilás.
defensibilidade: 2 — o ganho não é o dado público cru: é o cruzamento da ficha CNES 9255826 com o
catálogo de rede da casa (nível 1) e com a leitura de quem contrata. Nenhum dos 5 concorrentes lidos tem.


- **MUST-MATCH** (≥2 concorrentes cobrem bem; faltar = perder): endereço completo com bairro · quais planos
  dão acesso ao hospital · especialidades e serviços do hospital · contato/como agendar · menção de preço
  com faixa · maternidade.
  - **como o MUST-MATCH "contato/como agendar" é coberto sem o telefone** (achado 🔴 do juiz P-B): os dois
    números divergem entre CNES e site da operadora, então nenhum entra. No lugar, os canais oficiais que
    o rodapé de hapvida.com.br publica — aplicativo, área do beneficiário, "Agendamento de Consultas e Exames"
    e o **0800 018 3456**, que é o número do Sul/Sudeste/Centro-Oeste, a região de Guarulhos (o outro,
    0800 280 9130, é Norte/Nordeste — citar o número errado repetiria o erro dos dois telefones da unidade) —
    mais a instrução de confirmar o atendimento antes de ir à unidade. É mais honesto que
    publicar um dos dois números e mais útil que "ligue para confirmar", que é a resposta do concorrente.
- **BRECHAS** (todos cobrem mal ou ninguém cobre):
  1. **Nenhum dos cinco concorrentes avisa que o hospital mudou de nome.** Quem busca "Hospital e Maternidade
     Guarulhos" e chega numa placa escrita "Hospital Keila Ferreira" não encontra a ponte em nenhuma das
     páginas que ranqueiam. Ressalva honesta (achado 🟡 do juiz P-B): **o nosso próprio artigo de cidade já
     traz "(ex-Hospital e Maternidade GRU)" no card e na FAQ 2** — de passagem, entre parênteses, sem explicar
     quando nem por quê. Isso muda o tamanho do ganho, não a sua existência: aqui a ponte é o eixo do artigo,
     com data, motivo, fonte oficial e o que mudou dentro do hospital; lá é uma abreviação.
  2. **A pergunta do pronto-socorro fica sem resposta útil.** O espelho do CNES pergunta e responde
     "ligue para confirmar"; os outros nem perguntam. **O que nós podemos fazer — e ninguém faz — é dizer
     QUAIS pronto-socorros a unidade tem registrados no CNES (geral/clínico, obstétrico, pediátrico e
     traumato-ortopédico) e dizer com todas as letras que o HORÁRIO não está publicado em fonte alguma.**
     Isso é mais útil que "ligue para confirmar" e é verdadeiro. Proibido afirmar 24h.
  3. **Ninguém traduz o CNES.** O `agendarconsulta` publica os códigos crus (112-004, 162-002, 140-013);
     nenhum concorrente explica que aquilo quer dizer parto de alto risco, UTI neonatal e PS obstétrico.
  4. **Ninguém dá instrução prática** — como chegar, o que levar para internar, visita, acompanhante.
  5. **Ninguém cita a Sala Lilás**, inaugurada na unidade em 10/11/2025.
- **GANHO DE INFORMAÇÃO (fechado):** *este é o hospital que trocou de nome e virou a primeira unidade da
  Hapvida com Sala Lilás — e o guia que liga o nome antigo (onde está a busca) ao que o registro oficial
  mostra que a unidade faz hoje.* Duas camadas que nenhum concorrente tem:
  - **a ponte de nome**, ancorada em fonte primária: o CNES já registra o estabelecimento 9255826 como
    HOSPITAL KEILA FERREIRA, no mesmo CNPJ e no mesmo endereço do antigo Hospital e Maternidade Guarulhos;
  - **a tradução do registro oficial**: PS geral, obstétrico, pediátrico e traumato-ortopédico; parto e
    parto em gestação de alto risco; UTI adulto e neonatal; 5 salas de cirurgia; 8 leitos de RN patológico;
    13 de alojamento conjunto; 16 incubadoras.
  - ⚠️ **SEGUNDA RECONCILIAÇÃO OBRIGATÓRIA — URGÊNCIA ORTOPÉDICA (achado 🔴 do juiz P-A, rodada 2).**
    A FAQ 9 do artigo de cidade publicado diz: "Para atendimento especializado **fora do horário comercial**,
    como ortopedia de urgência, o beneficiário pode acessar o pronto-socorro Hapvida em SP capital, onde
    unidades como o Salvalus e o Bosque da Saúde operam 24h". O artigo novo vai dizer que o CNES registra
    PS traumato-ortopédico (140-016) nesta unidade. Sem regra, o mesmo site daria duas orientações sobre
    onde levar uma fratura de madrugada — e isso é pior que doorway, é dano ao leitor.
    **Forma obrigatória:** o registro no CNES diz que o serviço EXISTE na unidade; **não** diz em que horário
    funciona — e nenhuma fonte diz. Então a passagem que citar o PS traumato-ortopédico tem de, na mesma
    respiração, (a) dizer que o horário não está publicado, (b) mandar confirmar antes de sair de casa e
    (c) manter o encaminhamento à capital fora do horário comercial, com o link `pronto-socorro-hapvida-sp`.
    **Proibido** escrever que a unidade resolve ortopedia de urgência a qualquer hora.
  - ⚠️ **RECONCILIAÇÃO OBRIGATÓRIA COM O ARTIGO DE CIDADE (achado 🔴 do juiz P-B).** O artigo publicado diz:
    "Para partos de alto risco ou UTI neonatal de alta complexidade, a referência é o Hospital e Maternidade
    N. Sra. do Rosário (Vila Maria, SP capital)". Não é contradição, e o artigo novo **não pode** deixar
    parecer que é. As duas coisas convivem: **ter o serviço registrado no CNES** (a unidade tem) é diferente
    de **ser a referência da rede para os casos mais complexos** (é o Rosário). Forma obrigatória de escrever:
    dizer o que o registro federal lista, atribuindo ao CNES, e na mesma passagem manter o encaminhamento de
    alta complexidade para o Rosário, com link. **Proibido** escrever que este hospital é referência em alto
    risco, e proibido omitir o Rosário na seção que fala de parto.
  - defensibilidade: **4** para o dado CNES isolado (público-trabalhoso: exige abrir a ficha, ler o código e
    traduzir) — mas o ganho **não** é o dado cru: é o cruzamento dele com o catálogo de rede da casa
    (nível 1) e com a leitura de quem contrata. Cruzamento de nível 1-2 sobre base pública trabalhosa.
  - **trava CI-2 satisfeita:** o ganho não sobrevive à troca de cidade nem é copiável em dez minutos —
    exige ter a ficha CNES, a notícia local e o catálogo de rede na mesma mesa.

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
- dado_proprietario: o catálogo interno ainda registra o nome antigo enquanto o site oficial e o CNES já usam
  o novo — defensibilidade: 2 — fonte: cruzamento `consultar_rede` × `consultar_artigo` × ficha CNES 9255826
  (vira pendência de catálogo: `rede_unidades` id 290 a atualizar para "Hospital Keila Ferreira")
### Material da HS4 (quais planos dão acesso) — coletado para fechar a seção órfã
- produtos comercializados em Guarulhos: **Nosso Plano** (rede 100% própria), **Plano Mix** (híbrido) e
  **Ambulatorial** (sem internação) — defensibilidade: 1 — fonte: `consultar_artigo` do artigo de cidade
  (campo `produtos`, banco da casa)
- regra que liga produto a esta unidade: **INFERÊNCIA, não dado de fonte** (rebaixamento pedido pelo juiz
  P-A, rodada 2). O hospital é rede própria, e planos com internação em rede própria (Nosso Plano, Mix)
  cobrem internação em unidade própria; o **plano Ambulatorial não cobre internação**, então quem tem só
  ambulatorial usa a rede para consulta e exame. O que é dado: a lista de produtos de Guarulhos
  (`consultar_artigo`, banco) e a definição de ambulatorial (pillar `o-que-e-plano-ambulatorial-2`).
  O que é inferência: o mapeamento produto → esta unidade específica.
  **Forma obrigatória na HS4:** escrever o raciocínio (rede própria × ambulatorial) e mandar **conferir a
  rede do plano no guia médico oficial antes de contratar**. **Proibido** escrever "o plano X dá acesso a
  este hospital" como fato — nenhuma fonte publica esse mapeamento (o guia oficial é SPA e não abriu).
- internação e cirurgia em rede própria são isentas de coparticipação — defensibilidade: 1 —
  fonte: `consultar_coparticipacao` + artigo de cidade. No artigo: 1 frase, sem explicar a mecânica.
- **proibições dos pillars a respeitar na HS4** (fonte: `consultar_pillars_proibicoes`): não descrever o
  produto Nosso Plano, não explicar o modelo híbrido do Mix, não analisar perfil ideal, não comparar
  produtos. Só a ponte produto → acesso a esta unidade, e link.
- dado_proprietario: estrutura divulgada pela Hapvida em nov/2025 — 113 leitos de internação, 30 de UTI e
  10 neonatais; pronto-socorro adulto, infantil, ortopédico e maternidade — defensibilidade: 4 —
  fonte: **uma única cadeia de divulgação** reproduzida por 4 veículos (Guarulhos Todo Dia 11/11/2025,
  Click Guarulhos 12/11/2025, Jornal Exempplar e Joi) com a mesma frase — **não são 4 fontes independentes**.
  A ficha CNES lida NÃO traz total de leitos (só 8 de RN patológico e 13 de alojamento conjunto).
  Tratamento obrigatório no artigo: no máximo **uma** aparição, atribuída e datada ("segundo a divulgação da
  Hapvida, em novembro de 2025"), **fora** do lead, do title/meta e de qualquer H2, e **nunca** misturada à
  lista traduzida do CNES. Sem superlativo e sem comparação em cima dele. Se a atribuição não couber em uma
  frase, o número sai — a estrutura verificável do artigo é a do CNES.

## 7b. Legislação citada (lastro das faixas "Fonte oficial")

- Lei 10.778/2003 — notificação compulsória de violência contra a mulher em serviço de saúde, público ou
  privado — fonte: planalto.gov.br, lida em 2026-09-16 pela rota n8n (200, ementa transcrita em
  `fontes/ci1-rodada2-fontes-primarias.md`, seção 7). Sustenta a passagem da Sala Lilás.
- Lei 9.656/1998 — dispõe sobre os planos e seguros privados de assistência à saúde; é onde estão as
  segmentações (ambulatorial, hospitalar, com obstetrícia) — fonte: planalto.gov.br, lida em 2026-09-16
  pela rota n8n (200, ementa transcrita na mesma seção 7). Sustenta a passagem da HS4.
- **Limite:** foi conferida a ementa e a resposta 200, não artigo nem inciso. O artigo cita as duas pelo
  que regulam, sem número de artigo — e é assim que tem de continuar.

## 8. Não encontrado [V7.2]

nao_encontrado:
- horário de visita, regra de acompanhante e o que levar para internar — onde foi procurado: ficha CNES,
  espelho do CNES, páginas da operadora (SPA) e os 5 concorrentes lidos. Nenhum publica. É a maior brecha da
  busca e continua sem fonte: o artigo diz que a regra é da unidade e manda confirmar, não inventa.
- estacionamento e linhas de ônibus da Av. Tiradentes, 1015 — onde foi procurado: as mesmas fontes.
  Não confirmado. A HS3 fala de vias de acesso, não de linha de ônibus.
- telefone da unidade — onde foi procurado: CNES (11 3155-2000) e site da operadora ((11) 2463-8610).
  Dois números diferentes na mesma unidade → não entra no artigo.
- horário do pronto-socorro — o CNES registra PS geral, obstétrico, pediátrico e traumato-ortopédico, mas
  não registra horário; o espelho responde "informação não disponível". Só a Sala Lilás tem 24h por escrito.
  O artigo NÃO afirma pronto-socorro 24h.
- certificação ONA — onde foi procurado: CNES e as páginas lidas. Não consta.
- **mapeamento oficial produto → esta unidade** ("quais planos incluem o Hospital Keila Ferreira na rede") —
  onde foi procurado: página da unidade em gndi.com.br e www2.hapvida.com.br (as duas trazem o botão
  "Compare planos que incluem ... na rede", mas o conteúdo é SPA e não abre pela rota n8n) e guia médico.
  **Não obtido.** É por isso que a HS4 escreve raciocínio e manda conferir no guia médico, em vez de afirmar.
- linhas de ônibus que servem a Av. Tiradentes, 1015 — a página de itinerário da prefeitura não publica o
  dado no HTML. Não confirmado. **E as distâncias do widget do agregador foram descartadas** (ver seção 3).
- quanto do volume de "hospital keila ferreira" é busca pela bispa homenageada — `keyword_data` não separa.
- volume da frase exata "hospital hapvida e maternidade guarulhos" — items_count 0.

## 9. FORBIDDEN_TOKENS

FORBIDDEN_TOKENS:
- Hospital Bispa Keila Ferreira
- 88 hospitais
- 10 anos
- (11) 2463-8610
- 3155-2000
- pronto-socorro 24 horas
- pronto socorro 24 horas
- PS 24h
- funciona 24 horas
- aberto 24 horas
- atendimento ininterrupto
- tomografia
- tomografo
- colonoscopia
- certificacao ONA
- parto humanizado
- Hospital e Maternidade Sao Luiz Guarulhos
- Rede D'Or
- maior hospital de Guarulhos
- referencia em alta complexidade

<!-- Notas do orquestrador sobre esta lista:
     · "24 horas" está proibido para o PRONTO-SOCORRO. Para a Sala Lilás o 24h aparece em duas veiculações
       que reproduzem a mesma divulgação da operadora (Guarulhos Todo Dia e Click Guarulhos) — mesmo
       de-rateio que se fez nos leitos. Então: escrever **atribuído** ("segundo a Hapvida, funciona 24 horas
       por dia"), nunca como fato do artigo, e nunca colado à expressão pronto-socorro.
     · tomografia e colonoscopia aparecem na divulgação da operadora, mas o inventário de equipamentos da
       ficha CNES traz raio-X, 1 ultrassom e 3 endoscópios — nenhum tomógrafo. Fora do artigo.
     · "referência em alta complexidade" é o posicionamento que o artigo de cidade dá ao Hospital N. Sra. do
       Rosário (Vila Maria); não pode migrar para este hospital. -->

## 10. PLANO_MODELOS [V7.2]

Agente 22 · 2026-09-16 · orquestrador: sessão principal

Modelos disponíveis nesta sessão para subagente: opus · sonnet · haiku · fable.
Degrau = quanto julgamento o assento exige. Modelo = qual cérebro senta nele. São coisas diferentes.

PLANO_MODELOS:
1 | buscas e tipo de página (SERP) | medio | sonnet | SERP já coletada pelo orquestrador com DataForSeo
2 | rede assistencial | medio | sonnet | catálogo do banco + ficha CNES; conferido pelo 6
3 | contexto local (IBGE/CNES) | barato | haiku | dado público, conferido pelo 6
4 | keywords e perguntas (fan-out) | medio | sonnet | volume real do DataForSeo, conferido pelo 7
ci-1 | desmontagem de concorrentes | forte | opus | 5 páginas lidas pela rota n8n; julgar enquadramento é julgamento
ci-2 | ganho de informação | forte | opus | decide o eixo do artigo; erro aqui não é pego por trava
5 | diferenciais, FAQ e fio condutor | forte | opus | síntese da pesquisa
6 | conferente de fatos | forte | opus | T2: modelo diferente do agente 2 (sonnet)
7 | conferente DataForSeo | barato | haiku | T2: modelo diferente do agente 4 (sonnet); número confere número
8 | redator do lead + HS1 | forte | opus | hospital entrega em bloco único; 8 escreve a abertura e a HS1
9 | redator HS2 + HS3 | medio | sonnet | experiência do paciente e como chegar
10 | redator HS4 + FAQ + conclusão | medio | sonnet | a seção de maior risco de doorway, curta e em bridge
11 | editor-chefe | forte | fable | T2: modelo diferente de 8 (opus), 9 e 10 (sonnet)
19 | voz humana | medio | sonnet | T2: modelo diferente do editor-chefe (fable)
12 | auditoria de veracidade | forte | sonnet | YMYL: cada número contra a fonte
13 | auditoria anti-doorway | forte | sonnet | T2: modelo diferente do agente 5 (opus)
14 | requisitos da skill | medio | haiku | roda os checkpoints; o script é que julga
15 | citabilidade e GEO | forte | opus | passagem citável é julgamento, não contagem
16a | juiz A — lente factual/YMYL | forte | opus | painel multimodelo
16b | juiz B — lente anti-doorway/SEO | forte | sonnet | painel multimodelo
16c | juiz C — lente do leitor | forte | fable | T3: 16a e 16b diferem do editor-chefe (fable)
21 | varredura final anti-doorway | forte | opus | T2: modelo diferente do agente 13 (sonnet)
23 | juiz P-A — suficiência e verdade | forte | opus | portão de pesquisa
24 | juiz P-B — originalidade e valor | forte | sonnet | T2: modelo diferente de 23; e do agente 5
17 | schema JSON-LD | medio | sonnet | execução separada, só sob pedido
18 | registro no banco | barato | haiku | só depois do artigo aprovado e publicado
22 | roteador de modelos | barato | haiku | este documento

## Observações do roteamento
- **Não é monomodelo.** Quatro modelos distintos sentam na linha.
- Agente 0 (diagnóstico de pillar) não entra: o artigo é novo e não é pillar.
- Agente 20 (imagem da tabela) não entra: artigo de hospital não tem seção de preço própria —
  o preço aparece só como chamariz na HS4, por shortcode.
- Nenhum agente 🔒 foi rebaixado de degrau.
- Rebaixamentos em agentes não travados: 3 e 7 em barato (dado público e conferência numérica,
  ambos com trava a jusante); 14 em haiku porque quem julga ali é o script, não o modelo.

## 11. Datas de coleta

coletado_em: 2026-09-16  # serp
coletado_em: 2026-09-16  # rede
coletado_em: 2026-09-16  # concorrentes (CI-1 realizada pela rota n8n; 5 concorrentes lidos)

## 12. FAQ local

Regra aplicada aqui: **toda pergunta tem o nome do hospital, zero overlap com as 15 FAQ do artigo de cidade
(seção 16) e um item de pesquisa com fonte atrás.** As três perguntas que a seção 16 marcou como queimadas
foram removidas; as quatro substitutas sem fonte (o que levar, visita, acompanhante, estacionamento) também
saíram — pergunta sem dado não entra, mesmo sendo boa pergunta.

- O Hospital e Maternidade Guarulhos mudou de nome? — fonte: ficha CNES 9255826 + 4 veículos (nov/2025)
- Quem foi Keila Ferreira, que dá nome ao Hospital e Maternidade Guarulhos? — fonte: Click Guarulhos
  (Ciben, Corafesp, Ideas) e Guarulhos Todo Dia (liderava a Assembleia de Deus no Brás; morreu em fev/2025).
  O detalhe do casamento com o bispo Samuel Ferreira aparece **só** em oitapecericano.com.br — se entrar,
  entra atribuído a essa fonte; biografia de pessoa real recém-falecida não se escreve de oitiva.
- O que é a Sala Lilás do Hospital e Maternidade Guarulhos? — fonte: Saúde Business 13/11/2025 + 3 veículos
- Mulher sem plano de saúde é atendida na Sala Lilás do Hospital e Maternidade Guarulhos? — fonte: Guarulhos
  Todo Dia ("aberto a todas as mulheres - inclusive as que não tem plano de saúde")
- Que tipos de pronto-socorro o Hospital e Maternidade Guarulhos tem registrados? — fonte: ficha CNES
  (140-019 geral/clínico, 140-013 obstétrico, 140-012 pediátrico, 140-016 traumato-ortopédico)
- O bebê que nasce no Hospital e Maternidade Guarulhos fica no mesmo quarto da mãe? — fonte: ficha CNES
  (13 leitos de alojamento conjunto)
- Quantas salas de cirurgia o Hospital e Maternidade Guarulhos tem no registro oficial? — fonte: ficha CNES
  (5 salas de cirurgia, 1 sala de recuperação, 1 de pré-parto, 1 de parto normal)
- Em que bairro fica o Hospital e Maternidade Guarulhos? — fonte: ficha CNES (Jardim Guarulhos) × site da
  operadora e imprensa (Jardim Santa Edwirges) — a resposta é a divergência, e ela é útil a quem usa mapa
- Quais planos Hapvida dão acesso ao Hospital e Maternidade Guarulhos? — fonte: banco (`produtos` do artigo
  de cidade) + regra de rede própria; o plano Ambulatorial não cobre internação
- Como agendar consulta ou exame no Hospital e Maternidade Guarulhos? — fonte: canais oficiais publicados no
  rodapé de hapvida.com.br (app, área do beneficiário, agendamento de consultas e exames e o 0800 nacional).
  **Sem o telefone da unidade** — há dois números divergentes entre CNES e site (seção 8).

**Perguntas que NÃO entram, e por quê:** "o PS funciona 24 horas?" (nenhuma fonte diz o horário — e o artigo
de cidade já responde o que dá para responder); "ainda faz parto?" (FAQ 2 do artigo de cidade); "quem mora
fora de Guarulhos pode ser internado?" (FAQ 11 do artigo de cidade); "preciso de encaminhamento?" (nenhuma
fonte sobre encaminhamento nesta unidade).

## 13. Anti-doorway

- teste_substituicao: trocar "Guarulhos" por "Osasco" invalida o lead (endereço, nome antigo e novo,
  Sala Lilás), a HS1 (a história da renomeação) e a HS3 (Av. Tiradentes / Dutra). A HS4 é a seção de maior
  risco — é onde o texto tende a virar molde de plano — e por isso fica curta, em bridge + link.
- dados_unicos: 20 — (1) troca de nome em 10-11/11/2025 · (2) homenagem à bispa Keila Ferreira · (3) 1ª Sala Lilás
  da Hapvida · (4) endereço Av. Tiradentes, 1015, Jd. Santa Edwirges · (5) 5 unidades próprias na cidade
  conferidas no catálogo · (6) Clínica Jardim inaugurada em jun/2025 com R$ 1,3 mi · (7) capacidade de
  10.500 consultas/mês na Clínica Jardim · (8) Centro Clínico Guarulhos II na Ponte Grande ·
  (9) NotreLabs Imedi (ex-Ghelfond) na Av. Paulo Faccini · (10) a busca pelo nome antigo caiu 58% em um ano
  enquanto a do nome novo saiu do zero · (11) Guarulhos tem 1.291.771 habitantes (Censo 2022) ·
  (12) o catálogo da casa e o site oficial divergem no nome da unidade ·
  (13) o CNES 9255826 já registra o estabelecimento como Hospital Keila Ferreira, mesmo CNPJ e endereço ·
  (14) o registro federal traz parto em gestação de alto risco (112-004) e UTI neonatal (162-002) ·
  (15) PS obstétrico, pediátrico e traumato-ortopédico registrados separadamente ·
  (16) 5 salas de cirurgia, 8 leitos de RN patológico e 13 de alojamento conjunto na ficha oficial ·
  (17) 16 incubadoras e 8 berços aquecidos · (18) 1ª Sala Lilás da Hapvida, 24h, aberta a mulheres sem
  convênio · (19) nome sugerido pelo prefeito ao grupo Hapvida (apuração do Click Guarulhos) ·
  (20) nenhum dos 5 concorrentes lidos avisa que o hospital mudou de nome
- frases_genericas: 0 toleradas. Proibido no artigo: "modelo verticalizado", "rede própria sempre que possível",
  "atendimento de qualidade", "tranquilidade para você e sua família", "como qualquer plano regulado pela ANS".
- anti-doorway: APROVADO — CI-1 fechada com 5 concorrentes lidos (checkpoint_ci1 aprovado em 2026-09-16),
  matriz contra o artigo de cidade fechada na seção 16, e o ganho de informação não existe em nenhuma das
  5 páginas concorrentes nem no artigo de cidade.

## 14. Diferenciais do artigo (com âncora local)

- titulo: A ponte entre os dois nomes — âncora: o CNES 9255826 registra HOSPITAL KEILA FERREIRA no mesmo
  CNPJ e no mesmo endereço (Tiradentes, 1015) do antigo Hospital e Maternidade Guarulhos
- titulo: O que o registro oficial diz que a unidade faz — âncora: códigos 112-004 (parto de alto risco),
  162-002 (UTI neonatal), 140-013 (PS obstétrico) e 140-016 (PS traumato-ortopédico) na ficha de Guarulhos
- titulo: A primeira Sala Lilás — âncora: inaugurada nesta unidade em 10/11/2025, funciona 24h e atende
  inclusive mulheres sem convênio. O superlativo tem fonte setorial, não só imprensa local: Saúde Business
  (13/11/2025) escreve "a primeira da rede privada, no Brasil". No artigo, atribuído a essa fonte.
- titulo: O que se resolve no hospital e o que se resolve na clínica de Guarulhos — âncora: as 5 unidades
  próprias da cidade no catálogo (Centro Clínico I e II, Clínica Jardim, NotreLabs Imedi, o hospital)
- titulo: O endereço que aparece de dois jeitos — âncora: a ficha CNES registra bairro "Jardim Guarulhos" e
  complemento "1 037"; o site da operadora e a imprensa dizem "Jardim Santa Edwirges". Quem procura pelo
  bairro errado no mapa não acha a unidade — e a related_search medida "Avenida Tiradentes 1037 Guarulhos"
  mostra que a confusão já acontece na busca

## 15. Fio condutor

Este é o hospital que mudou de nome e ninguém avisou a quem busca. O artigo é a ponte entre os dois nomes:
começa respondendo "sim, é o mesmo hospital, na mesma Av. Tiradentes, 1015" e, a partir daí, conta o que
mudou de verdade dentro dele — a Sala Lilás — e o que o paciente precisa saber para ser atendido lá.
Tom de quem já levou gente naquele pronto-socorro, não de quem copiou a ficha do Maps.


## 16. O QUE NÃO REPRODUZIR — matriz contra o artigo de cidade (obrigatória no arquétipo hospital)

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

Consequência para a FAQ, **já aplicada na seção 12**: saíram por overlap "ainda faz parto?" (≈ FAQ 2 do de
cidade), "o pronto-socorro funciona 24 horas?" (≈ FAQ 9) e "quem mora fora de Guarulhos pode ser internado?"
(≈ FAQ 11). As quatro substitutas que a versão anterior desta seção prescrevia — o que levar, horário de
visita, acompanhante e estacionamento — **também saíram**: nenhuma fonte publica esses dados (nem o CNES, nem
a operadora, nem os 5 concorrentes lidos), e pergunta sem dado atrás não entra, por melhor que seja.
A FAQ final tem 10 perguntas, todas com fonte nomeada — ver seção 12.
**Pauta registrada, não usada:** as quatro perguntas sem fonte são material de uma futura atualização, se a
unidade publicar regimento de visita ou se o usuário trouxer o dado.

### Catálogo de FAQs do banco (categoria "hospital")
Templates já em uso que NÃO podem virar pergunta deste artigo: "O Hospital [X] tem maternidade ativa?" (id 12,
usado em Limeira, Bauru, Joinville, Lins) · "Qual hospital Hapvida faz parto em [cidade]?" (id 11, 8 artigos) ·
"Tem hospital da Hapvida em [cidade]?" (id 10, 10 artigos).

## 17. Plano de links (governança de âncoras + saturação)

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
