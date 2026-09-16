modelo: sonnet
lente: P-B originalidade e valor
rodada: 1
state_file_sha256: f84b59101f37d233310bb5e45a5a88398f45bd689dee8356bb29b4fffdae8109

# Juiz 24 — P-B (originalidade e valor) — hospital-hapvida-maternidade-guarulhos

Pergunta-mãe: **"Se for publicado com esta pesquisa, esse artigo merece existir na SERP?"**

---

## 1. Teste de substituição aplicado à PESQUISA (Guarulhos → Osasco)

Quase nada estrutural sobrevive — e isso é o ponto forte da pesquisa. A renomeação
(nov/2025), a homenagem à bispa Keila Ferreira, a Sala Lilás e a tradução do CNES
9255826 são fatos do hospital, não da cidade: em Osasco não há renomeação, não há
Sala Lilás, não há esse CNES. Dos ~20 itens listados como `dados_unicos` (seção 13),
praticamente 100% morrem na troca — muito acima do piso de 70% da rubrica.

- severidade: 🟢
  achado: o núcleo do artigo (ponte de nomes + Sala Lilás + tradução do CNES) é
  genuinamente ancorado no hospital, não é molde de cidade reaproveitável.
  trecho: "dados_unicos: 20 — (1) troca de nome em 10-11/11/2025 · (2) homenagem à bispa Keila Ferreira · (3) 1ª Sala Lilás da Hapvida"
  volta para: —
  correção: nenhuma — manter como está.

## 2. Teste de canibalização interna (o mais importante aqui)

A matriz da seção 16 existe e é honesta em vários pontos (card de serviços, linha do
tempo, comparação com concorrentes, tabela de bairros), mas tem furos que a tornam
**insuficiente** para liberar o portão:

- severidade: 🔴
  achado: a "ganho de informação" do CI-2 (tradução do CNES: parto de alto risco +
  UTI neonatal nesta unidade) **contradiz** o que o artigo de cidade já publicado
  afirma sobre esta mesma unidade — que ela NÃO atende alto risco/UTI neonatal de
  alta complexidade e que a referência para isso é outro hospital (N. Sra. do
  Rosário). A matriz da seção 16 não registra esse conflito; a seção 17 até planeja
  linkar para o Rosário como "referência de alta complexidade materno-infantil" na
  mesma HS2 que vai reivindicar, via CNES, que o próprio hospital faz alto risco.
  trecho (state file, seção 6): "a tradução do registro oficial: PS obstétrico, pediátrico e traumato-ortopédico; parto e parto em gestação de alto risco; UTI adulto e neonatal"
  trecho (artigo de cidade, fontes/artigo-cidade-guarulhos.html): "Para partos de alto risco ou UTI neonatal de alta complexidade, a referência é o Hospital e Maternidade N. Sra. do Rosário (Vila Maria, SP capital), com programa Gestação Segura e UTI neonatal especializada."
  volta para: CI-2 (agente 6, conferente de fatos)
  correção: resolver a divergência antes da FASE 1 — checar se o código CNES 112-004/162-002 reflete capacidade instalada geral ou se "alta complexidade" é outro nível de credenciamento; se o hospital de fato não atende alto risco, a diferencial da seção 14 e a matriz da seção 16 têm de ser reescritas para não afirmar o oposto do que o próprio site já publicou.

- severidade: 🔴
  achado: a seção 12 (FAQ local) não foi reconciliada com a análise de overlap da
  seção 16 — ainda lista 3 perguntas que a própria seção 16 identifica como
  "queimadas" e manda cortar.
  trecho (seção 12): "O pronto-socorro do Hospital e Maternidade Guarulhos funciona 24 horas?" / "O Hospital e Maternidade Guarulhos ainda faz parto?" / "Quem mora fora de Guarulhos pode ser internado no Hospital e Maternidade Guarulhos?"
  trecho (seção 16): "Consequência para a FAQ da seção 12: caem por overlap **\"O Hospital e Maternidade Guarulhos ainda faz parto?\"** (≈ FAQ 2 do de cidade), **\"O pronto-socorro funciona 24 horas?\"** (≈ FAQ 9) e **\"Quem mora fora de Guarulhos pode ser internado?\"** (≈ FAQ 11)."
  volta para: Agente 4/5 (keywords/FAQ e síntese)
  correção: reescrever a seção 12 removendo os 3 itens queimados antes do portão humano — a versão hoje no arquivo ainda canibaliza o artigo de cidade se for usada como está.

- severidade: 🔴
  achado: as 4 perguntas propostas na seção 16 para substituir as queimadas (o que
  levar, horário de visita, acompanhante, estacionamento) não têm fonte — dependem
  de fonte viva hoje bloqueada. Ou seja, a pesquisa não tem, neste momento, um
  conjunto de FAQ sem overlap E sustentado por dado.
  trecho: "Estas quatro dependem de fonte viva (site oficial / CNES / regimento da unidade) e hoje estão bloqueadas pelo egress."
  volta para: CI-1/CI-2 (recoleta via rota n8n, como já foi feito para a desmontagem de concorrentes)
  correção: destravar essas 4 respostas pela mesma rota n8n usada na CI-1, ou trocar por outras 4 perguntas com dado disponível hoje.

## 3. Ganho de informação do CI-2 — nível 1-2 ou dado repaginado?

- severidade: 🟡
  achado: a "ponte entre os dois nomes" já é parcialmente antecipada pelo próprio
  artigo de cidade publicado (parênteses no card e na FAQ), o que a matriz da
  seção 16 não registra — ela só cobre a linha do tempo completa, não a menção
  lateral do nome antigo.
  trecho (artigo de cidade): "Hospital Keila Ferreira (ex-Hospital e Maternidade GRU)" / "O Hospital Keila Ferreira (antigo Hospital e Maternidade GRU) possui maternidade..."
  volta para: Agente 5 (síntese)
  correção: registrar esse detalhe na matriz da seção 16 e deixar explícito que o diferencial do artigo novo é a fonte primária (CNES) e a resposta completa à pergunta "mudou de nome?", não a mera existência do fato — que o site já teria "avisado", ainda que de raspão.

Descontado esse ponto, o cruzamento CNES + catálogo de rede + Sala Lilás (quando
resolvida a contradição do item 2) é, sim, nível 1-2 e não copiável em dez minutos —
a trava CI-2 está corretamente justificada nesse aspecto.

## 4. FAQ — dado local ou paráfrase de PAA nacional?

Coberto acima (item 2): 3 das 12 perguntas atuais são eco direto da FAQ do artigo
de cidade (queimadas, não paráfrase de PAA nacional) e as 4 substitutas propostas
não têm fonte hoje. As demais 9 perguntas da seção 12 nascem de dado local
verificável (CNES, Sala Lilás, rede) — essa parte está bem construída.

## 5. Keywords secundárias — quem compra ou quem já é cliente?

- severidade: 🟡
  achado: a maior secundária do kit (9.900/mês, "hospital keila ferreira" — mais
  de dois terços do volume secundário somado) tem contaminação não resolvida por
  busca pela pessoa homenageada, e mesmo assim segue como "qualificada" sem
  desconto, indo para H1/lead/HS1 — a keyword mais importante do plano tem
  intenção real desconhecida.
  trecho: "kw: hospital keila ferreira | volume: 9.900 | intencao: navigational | veredito: qualificada | onde entra: H1/lead/HS1 (ressalva: parte do volume pode ser busca pela pessoa homenageada, não pelo hospital — ver seção 8)"
  volta para: Agente 4 (keywords)
  correção: tentar segmentar com `keyword_ideas`/`related_keywords` (termos como "bispa keila ferreira", "quem é keila ferreira") para estimar a fração contaminada, ou, não sendo possível, marcar a qualificação como parcial e não apoiar sozinha a decisão de H1 nela.

O veto de intenção foi bem aplicado nas descartadas (telefone = já-cliente,
trabalhe-conosco = candidato a emprego, público = SUS) — isso está correto. O
problema é a maior keyword do plano, não as pequenas.

## 6. Fio condutor — tese ou frase bonita?

- severidade: 🟢
  achado: é tese checável, não frase genérica — apoiada na brecha nº1 do CI-2, na
  queda de -58% de busca pelo nome antigo e na Sala Lilás, todos itens rastreáveis
  no próprio state file.
  trecho: "Este é o hospital que mudou de nome e ninguém avisou a quem busca. O artigo é a ponte entre os dois nomes..."
  volta para: —
  correção: nenhuma — só ajustar o "ninguém avisou" para "nenhum dos concorrentes da SERP avisa" dado o achado 3 acima (o próprio site, num artigo diferente, já avisa de raspão).

## 7. MUST-MATCH dos 5 concorrentes — todos cobertos pelo plano?

- severidade: 🔴
  achado: "contato/como agendar" é MUST-MATCH (≥2 concorrentes cobrem bem — ex.:
  H2 "Como faço para agendar uma consulta", "Contato", "Orçamento Online") e não
  está coberto pelo plano do artigo novo: o telefone foi descartado por divergência
  de fonte e não há substituto planejado em nenhuma seção do state file.
  trecho (seção 8): "telefone da unidade — onde foi procurado: CNES (11 3155-2000) e site da operadora ((11) 2463-8610). Dois números diferentes na mesma unidade → não entra no artigo."
  trecho (seção 6, MUST-MATCH): "endereço completo com bairro · quais planos dão acesso ao hospital · especialidades e serviços do hospital · **contato/como agendar** · menção de preço com faixa · maternidade."
  volta para: Agente 2 / CI-1 (recoleta de fonte viva)
  correção: reler especificamente a página oficial da unidade pela mesma rota n8n que abriu a CI-1 para resolver o número de telefone, ou substituir por link direto ao canal de agendamento oficial da Hapvida — o artigo não pode ficar sem resposta a este must-match.

Os demais MUST-MATCH (endereço, planos que dão acesso, especialidades/serviços,
preço com faixa) estão cobertos pelo plano das seções 13-14 e pela matriz
anti-doorway. Maternidade está coberta, mas com a ressalva do item 2 acima.

---

## Rubrica (0-10, sem suavizar)

| Dimensão | Nota | Por quê |
|---|---|---|
| Suficiência por seção | 6 | FAQ da seção 12 não reconciliada com a seção 16 + must-match "contato/agendar" sem cobertura |
| Verdade e fonte | 5 | contradição não resolvida entre o CI-2 (CNES: alto risco/UTI neonatal) e o artigo de cidade já publicado sobre o mesmo hospital |
| Originalidade (substituição) | 8 | núcleo do artigo não sobrevive à troca de cidade; único desconto é o "ganho" da ponte de nomes já antecipado, de raspão, pelo artigo de cidade |
| Valor comercial | 6 | maior secundária (9.900) com intenção não resolvida; 4 FAQ substitutas sem fonte; must-match de contato ausente |

**Nenhuma dimensão atinge 8 em três das quatro, e há 4 achados 🔴.**

---

## VEREDITO: BLOQUEADO

Volta ao Estágio 1: reconciliar seção 12 × seção 16 (FAQ), resolver a contradição
CNES × artigo de cidade sobre alto risco/UTI neonatal, destravar as 4 fontes vivas
da FAQ nova, cobrir o must-match de contato/agendamento, e reavaliar a qualificação
da keyword "hospital keila ferreira" (9.900).

---
---

modelo: sonnet
lente: P-B originalidade e valor
rodada: 2
state_file_sha256: 926b6e77294c8d674a7f599d6485cfa01b34d0668a3fd0021cdc1894c6506438

# Rejulgamento — rodada 2

Pergunta-mãe, sem crédito pelo esforço: **este artigo merece existir na SERP ao
lado do nosso próprio artigo de cidade?**

## Achado 1 — contradição CNES × Rosário (era 🔴)

- severidade: 🟢 (resolvido)
  achado: a seção 6 ganhou um bloco de RECONCILIAÇÃO OBRIGATÓRIA que separa
  corretamente "ter o serviço registrado no CNES" de "ser a referência da rede
  para os casos mais complexos" e prescreve a forma de escrever (CNES atribuído +
  encaminhamento ao Rosário na mesma passagem, com link). "referencia em alta
  complexidade" entrou no FORBIDDEN_TOKENS com a nota explícita de que esse
  posicionamento é do Rosário, não desta unidade — o que também explica, sem
  inconsistência, por que a seção 17 ainda descreve o link ao Rosário como
  "referência de alta complexidade materno-infantil" (é o uso correto do termo,
  aplicado ao hospital certo).
  trecho: "ter o serviço registrado no CNES (a unidade tem) é diferente de ser a referência da rede para os casos mais complexos (é o Rosário). Forma obrigatória de escrever: dizer o que o registro federal lista, atribuindo ao CNES, e na mesma passagem manter o encaminhamento de alta complexidade para o Rosário, com link. Proibido escrever que este hospital é referência em alto risco, e proibido omitir o Rosário na seção que fala de parto."
  volta para: —
  correção: nenhuma. Fechado.

## Achado 2 e 3 — FAQ com overlap e substitutas sem fonte (eram 🔴)

- severidade: 🟢 (resolvido)
  achado: a seção 12 foi reescrita do zero — 10 perguntas, cada uma com fonte
  nomeada (CNES, imprensa local, veículo setorial ou banco da casa), zero overlap
  com as 15 FAQ do artigo de cidade. As 3 queimadas ("ainda faz parto?", "PS 24h?",
  "mora fora pode internar?") saíram; as 4 substitutas sem fonte (o que levar,
  visita, acompanhante, estacionamento) também saíram e viraram pauta futura, não
  FAQ publicada — decisão correta: pergunta sem dado não entra, por melhor que seja.
  trecho: "As três perguntas que a seção 16 marcou como queimadas foram removidas; as quatro substitutas sem fonte (...) também saíram — pergunta sem dado não entra, mesmo sendo boa pergunta."
  volta para: —
  correção: nenhuma. Conferi as 10 perguntas uma a uma contra a lista de queimadas e contra o catálogo de FAQ do banco (seção 16): nenhuma colide.

## Achado 4 — MUST-MATCH contato/como agendar (era 🔴)

- severidade: 🟢 (resolvido)
  achado: coberto sem inventar telefone — canais oficiais do rodapé de
  hapvida.com.br (app, área do beneficiário, agendamento de consultas e exames,
  0800 nacional) mais a instrução de confirmar antes de ir. É mais honesto que
  publicar um dos dois números divergentes e mais útil que o "ligue para
  confirmar" do concorrente-espelho do CNES.
  trecho: "os canais oficiais que o rodapé de hapvida.com.br publica — aplicativo, área do beneficiário, 'Agendamento de Consultas e Exames' e o 0800 nacional — mais a instrução de confirmar o atendimento antes de ir à unidade."
  volta para: —
  correção: nenhuma. Todos os MUST-MATCH da seção 6 (endereço, planos, especialidades, contato, preço, maternidade) estão cobertos.

## Achado 5 — o "ex-" já antecipado pelo artigo de cidade (era 🟡)

- severidade: 🟢 (resolvido)
  achado: registrado explicitamente na brecha 1 com a ressalva de tamanho —
  reconhece que o site já "avisa" de raspão, entre parênteses, e distingue isso do
  que o artigo novo entrega (eixo do artigo, com data, motivo e fonte oficial).
  Isso muda a moldura do ganho de informação de "só nós avisamos" para "só nós
  explicamos" — mais defensável e mais honesto.
  trecho: "o nosso próprio artigo de cidade já traz \"(ex-Hospital e Maternidade GRU)\" no card e na FAQ 2 — de passagem, entre parênteses, sem explicar quando nem por quê. Isso muda o tamanho do ganho, não a sua existência"
  volta para: —
  correção: nenhuma.

## Achado 6 — keyword de 9.900 contaminada (era 🟡)

- severidade: 🟢 (resolvido, com uma pauta menor)
  achado: passou a "qualificada com desconto", tirada do title e da promessa de
  tráfego, com a razão do pico documentada (coincide com a morte da bispa
  homenageada e a renomeação) e a instrução expressa de tratar como teto, nunca
  como previsão.
  trecho: "veredito: **qualificada com desconto** | onde entra: lead e HS1, **não no title nem como promessa de tráfego** (...) Tratar como teto, nunca como previsão"
  volta para: —
  correção: nenhuma obrigatória. Fica como pauta menor tentar segmentar via `keyword_ideas`/`related_keywords` numa rodada futura, para trocar o teto por uma estimativa — não bloqueia.

## Achados novos nesta rodada

- severidade: 🟡
  achado: o tratamento do número "113 leitos / 30 UTI / 10 neonatais" foi
  corrigido por iniciativa própria (não era um dos 6 achados originais) — a
  seção 7 agora identifica que os 4 veículos que repetem o número são uma única
  cadeia de divulgação, não fontes independentes, e restringe a 1 aparição,
  atribuída, fora do lead/title/H2. É melhoria real de rigor, registro apenas
  para constar que a rodada 2 também endureceu pontos que eu não havia cobrado —
  não é achado que bloqueie.
  trecho: "Guarulhos Todo Dia 11/11/2025, Click Guarulhos 12/11/2025, Jornal Exempplar e Joi) com a mesma frase — não são 4 fontes independentes."
  volta para: —
  correção: nenhuma.

---

## Rubrica — rodada 2 (0-10, sem suavizar)

| Dimensão | Nota | Por quê |
|---|---|---|
| Suficiência por seção | 9 | FAQ reconciliada e sourced, HS3 e HS4 ganharam material próprio, MUST-MATCH de contato coberto sem invenção |
| Verdade e fonte | 9 | contradição CNES × Rosário reconciliada com regra de escrita explícita; regra das duas listas aplicada com honestidade (lista B declarada indisponível, sem afirmar ausência); cadeia de divulgação dos "113 leitos" identificada e contida |
| Originalidade (substituição) | 9 | núcleo do artigo segue não sobrevivendo à troca de cidade; ganho agora ainda mais preciso (divergência de bairro, referências a pé do CNES) |
| Valor comercial | 8 | maior secundária descontada e hedgeada corretamente; FAQ cobre agendamento e acesso a plano; veto de intenção bem aplicado |

**As 4 dimensões ≥ 8. Zero 🔴.**

---

## VEREDITO — RODADA 2: LIBERADO

Os 4 achados 🔴 e os 2 🟡 da rodada 1 foram corrigidos, não apenas amenizados: a
contradição factual com o artigo de cidade virou regra de escrita explícita (com
FORBIDDEN_TOKENS), a FAQ foi reescrita com zero overlap e fonte nomeada em cada
item, o must-match de contato foi coberto sem inventar telefone, e a keyword
contaminada foi descontada e tirada do title. Libera para o Estágio 3, sob
condição de que a redação siga a forma obrigatória de reconciliação da seção 6 ao
pé da letra na HS2 — é o único ponto onde um redator descuidado ainda pode
reintroduzir o achado 1.
