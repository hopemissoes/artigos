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
