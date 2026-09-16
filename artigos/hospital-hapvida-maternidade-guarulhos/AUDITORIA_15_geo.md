# AUDITORIA 15 — CITABILIDADE / GEO-AEO (MODO 4)

**Artigo:** `artigos/hospital-hapvida-maternidade-guarulhos/artigo.html`
**Skill:** hapvida-article-builder-v7 · `references/geo-aeo.md` §1 e §9 + `references/geo-plataformas.md`
**State file:** `PESQUISA_hospital-hapvida-maternidade-guarulhos_COMPLETO.md` (§1 — SERP medida em 16/09/2026)
**Rodado em:** 2026-09-16 · **Agente 15 — não edita o artigo, audita e reporta.**

## SERP de referência (do state file, §1)

- **SEM featured snippet.** A SERP abre com `local_pack` (3 fichas do Maps) e traz `people_also_ask` na posição absoluta 5.
- Formato premiado: **ficha de lugar** (endereço, telefone, horário) + página de unidade.
- PAA literais: (1) Qual hospital atende Hapvida em Guarulhos? · (2) Qual é o melhor hospital em Guarulhos? ·
  (3) Quais hospitais o Hapvida atende? · (4) Quais hospitais em São Paulo aceitam o plano de saúde Hapvida?

## Checkpoint mecânico (saída colada)

```
===========================================================================
CHECKPOINT — CITABILIDADE GEO/AEO (artigo.html)
===========================================================================
Seções (<h2>) analisadas: 6
  ✅ Abertura citável (faixa ideal):  6
  ⚠️  Aceitável / atenção:            0
  ❌ Reprovadas:                      0
Links externos de fonte (rel=nofollow): 4
Seções com abertura SEM número-âncora: 1 (considere ancorar com um dado da cidade/hospital)

✅ CHECKPOINT DE CITABILIDADE APROVADO (heurístico/direcional).
   Confirme manualmente que cada abertura é específica da cidade — o script
   mede forma, não unicidade. Anti-doorway continua sendo julgamento humano.
```

> O script mede **forma** (40-60 palavras, dígito, densidade de fonte). Ele passa. O que segue é o
> julgamento que o script não faz: autonomia da passagem, teste de substituição e formato × SERP.

---

## 1. Tabela — seção por seção

| Seção | Passagem de abertura (literal, truncada) | Citável? | Número em texto? | Correção |
|---|---|---|---|---|
| **Lead-herói** | "O Hospital e Maternidade Guarulhos, unidade própria da Hapvida NotreDame Intermédica na região central de Guarulhos (SP), passou a se chamar Hospital Keila Ferreira em novembro de 2025. É o mesmo hospital e o mesmo registro: o CNES 9255826 lista maternidade, UTI adulto e neonatal e pronto-socorro." | 🟢 | ✅ CNES 9255826, nov/2025 | Nenhuma. Responde sozinha a "o que é, onde fica, o que faz, como se chama hoje". É a passagem-âncora do artigo. |
| **Lead — 2º §** | "Quem digita o nome antigo no buscador raramente encontra esse aviso: nenhuma das cinco páginas de corretora e diretório que este guia leu na primeira tela explica a troca. Enquanto isso, a busca pelo nome antigo caiu 58% em um ano e a do nome novo saiu do zero." | 🟡 | ✅ 58%, cinco páginas | Os dois números são de **nível 5 auto-referente**: "cinco páginas que este guia leu" é inverificável pelo leitor e o "-58%" é métrica de keyword sem fonte nomeada no texto. Para o Claude/Brave (densidade = número + fonte + data) isso é número fraco. Nomear a fonte ("segundo o volume de busca medido em set/2026") ou trocar o parágrafo por dado do CNES. |
| **HS1 — O que mudou** | "Em 10 e 11 de novembro de 2025, o Hospital e Maternidade Guarulhos passou a se chamar Hospital Keila Ferreira, em homenagem à bispa que liderava a Assembleia de Deus no Brás. Mudou a placa: o registro CNES 9255826 continua o mesmo." | 🟢 | ✅ datas + CNES | Nenhuma. Passa no teste de substituição (nome, data e código não existem em outra cidade). |
| **HS2 — Registro oficial** | "A ficha do CNES 9255826 registra nesta unidade parto e parto em gestação de alto risco, UTI adulto e UTI neonatal, quatro tipos de pronto-socorro, cinco salas de cirurgia, treze leitos de alojamento conjunto e oito leitos de recém-nascido patológico. É o retrato oficial da unidade." | 🟢 | ✅ 6 números | Nenhuma. É a passagem mais densa do artigo e a mais defensável (fonte primária lida). |
| **H3 — As salas que a ficha lista** | "As instalações registradas incluem 11 consultórios, cinco salas de cirurgia, 1 de recuperação, duas salas de acolhimento com classificação de risco, sala de estabilização, sala de gesso e brinquedoteca. Nos equipamentos, 16 incubadoras, 8 berços aquecidos e 5 aparelhos de fototerapia." | 🟢 | ✅ | Acrescentar aqui **"1 sala de pré-parto e 1 sala de parto normal"** — hoje esse dado existe **só dentro do `quadro-comp`** (ver §3). É justamente o dado que responde "faz parto?". |
| **HS3 — Como chegar** | "O Hospital Keila Ferreira fica na Av. Tiradentes, 1015, eixo que corta a região central de Guarulhos. A ficha do CNES 9255826 registra o complemento \"1 037\" e o bairro Jardim Guarulhos; o site da operadora e a imprensa dizem Jardim Santa Edwirges. É o mesmo lugar." | 🟢 | ✅ 1015 / 1 037 / CNES | Nenhuma na frase. Falta o **envelope de ficha** ao redor dela (ver §5). |
| **H3 — Antes de ir à unidade** | "Confirme o serviço que você procura pelos canais oficiais da operadora: aplicativo, área do beneficiário, o canal de agendamento de consultas e exames ou a central de atendimento que a operadora publica para Sul, Sudeste e Centro-Oeste. O horário do pronto-socorro não está publicado em fonte oficial…" | 🔴 | ❌ | **Reprova o teste de substituição**: troque hospital e cidade e a frase continua inteira. Extraída sozinha, cita o artigo como conselho genérico de operadora. Ancorar: nomear a unidade e o fato local — "No Hospital Keila Ferreira (ex-Hospital e Maternidade Guarulhos), o CNES 9255826 registra quatro tipos de pronto-socorro e **nenhum horário**; por isso confirme antes de sair…". |
| **HS4 — Quais planos dão acesso** | "Não existe fonte pública que liste, produto por produto, quais planos incluem esta unidade. O que dá para afirmar: o hospital é rede própria, e em Guarulhos a operadora comercializa três linhas: Nosso Plano, Mix e Ambulatorial. Dessas, o Ambulatorial não cobre internação." | 🟡 | ⚠️ só por extenso ("três") — é a 1 seção sem dígito apontada pelo checkpoint | Substituição parcial: trocando "Guarulhos" a frase sobrevive em qualquer cidade com as mesmas três linhas. Ancorar no próprio estabelecimento: "…o hospital é rede própria — o CNES 9255826 registra **internação** como atividade principal — e em Guarulhos…". |
| **H3 — O que é raciocínio, não dado** | "Planos com cobertura de internação em rede própria internam em unidade própria, e este hospital é rede própria. O Ambulatorial não cobre internação: serve para consulta e exame." | 🔴 | ❌ | **Doorway disfarçado de citabilidade**: é regra nacional, válida para qualquer unidade da rede. Reescrever a partir do catálogo local já apurado (Centro Clínico Guarulhos I e II, Clínica Jardim Guarulhos, NotreLabs Imedi Guarulhos) — que é o dado que só este artigo tem — e deixar a regra como segunda frase. |
| **H3 — Confira a rede antes de contratar** | "Nenhuma página oficial publica a lista de produtos que incluem esta unidade na rede. A única confirmação que vale é o guia médico oficial do plano que você está cotando, conferido antes de assinar." | 🟡 | ❌ | Sobrevive à substituição (só "esta unidade" prende). Nomear a unidade pelos **dois nomes** e mandar procurar no guia médico pelos dois — é a instrução que só faz sentido aqui. |
| **FAQ — abertura da seção** | "São 8 perguntas sobre esta unidade, respondidas com o que a ficha do CNES 9255826, o noticiário de novembro de 2025 e o catálogo de rede publicam. Onde a fonte não existe, a resposta diz que não existe e aponta o canal oficial para confirmar." | 🟡 | ✅ 8, CNES | Passagem **meta** (fala do artigo, não do hospital). Se a IA extrair essa, não leva informação. Trocar por uma resposta de verdade — candidata natural: a resposta ao PAA nº 1 (ver §5). |
| **Conclusão** | "Hospital e Maternidade Guarulhos e Hospital Keila Ferreira são o mesmo hospital e o mesmo registro CNES 9255826. O que mudou em novembro de 2025 foi a placa, mais a chegada da primeira Sala Lilás da rede privada do país, segundo o veículo setorial Saúde Business." | 🟢 | ✅ | Nenhuma. Segunda passagem-âncora, com fonte nomeada. |
| **Sobre este guia** | "Este guia **não se apoia em normas**, e sim em cadastro público e imprensa: a ficha do estabelecimento 9255826 no CNES/DataSUS, o noticiário local e setorial de novembro de 2025 […] Atualizado em [mes_atual] de [ano_atual]." | 🟡 | ✅ | **Contradiz o próprio artigo**, que cita a Lei 9.656/98 e a Lei 10.778/2003 em dois boxes "Fonte oficial" e na conclusão. Passagem de E-E-A-T que a IA lê inteira — corrigir para "apoia-se em cadastro público, imprensa e, onde a regra é legal, no texto da lei". Aproveitar para trazer a credencial da DRV, hoje só em faixa visual (ver §3). |

## 2. Tabela — FAQ por FAQ (abertura da resposta)

| FAQ | Abertura da resposta (literal) | Citável? | Número em texto? | Correção |
|---|---|---|---|---|
| 1. Mudou de nome? | "Sim. Em 10 e 11 de novembro de 2025 a unidade passou a se chamar Hospital Keila Ferreira. É o mesmo hospital, no mesmo endereço, com o mesmo nome empresarial e o mesmo código no cadastro federal (CNES 9255826)…" | 🟡 | ✅ | Extraída sozinha entrega o nome **novo**, nunca o antigo — e é pelo antigo que 1.600 buscas/mês chegam. Nomear os dois: "Sim. O Hospital e Maternidade Guarulhos passou a se chamar Hospital Keila Ferreira em 10 e 11 de novembro de 2025." |
| 2. Quem foi Keila Ferreira? | "**Era** a bispa que liderava a Assembleia de Deus no Brás, em São Paulo, e presidia a Ciben, a Corafesp e o Ideas." | 🔴 | ❌ | Abre sem sujeito. Fora da página não se sabe de quem se fala nem que hospital leva o nome. "Keila Ferreira era a bispa … e dá nome ao hospital da Hapvida em Guarulhos desde novembro de 2025." |
| 3. O que é a Sala Lilás? | "**É** um espaço de acolhimento a meninas e mulheres em situação de violência, inaugurado na unidade em 10 de novembro de 2025." | 🔴 | ✅ data | Nem "Sala Lilás" nem o nome do hospital aparecem na resposta. "A Sala Lilás do Hospital e Maternidade Guarulhos (hoje Hospital Keila Ferreira) é um espaço…". É a passagem de maior information gain do artigo — nenhum concorrente da SERP cobre — e hoje ela é inextraível. |
| 4. Mulher sem plano é atendida? | "Segundo a divulgação da operadora, **o espaço** é aberto a todas as mulheres, inclusive as que não têm plano de saúde." | 🟡 | ❌ | "O espaço" não tem antecedente fora da página. Repetir "a Sala Lilás do Hospital Keila Ferreira, em Guarulhos". |
| 5. Que tipos de PS tem? | "**Quatro, na ficha do CNES**: geral/clínico (140-019), obstétrico (140-013), pediátrico (140-012) e traumato-ortopédico (140-016)." | 🔴 | ✅ 4 + códigos | Resposta elíptica: depende da pergunta para existir. "O Hospital e Maternidade Guarulhos tem quatro tipos de pronto-socorro registrados na ficha do CNES 9255826: …". Com a correção vira a melhor passagem do FAQ (densidade de código oficial que ninguém mais traduz). |
| 6. Bebê fica no quarto da mãe? | "A ficha do CNES registra treze leitos de alojamento conjunto na unidade, a estrutura em que mãe e recém-nascido ficam no mesmo quarto, e mais oito leitos de recém-nascido patológico…" | 🟡 | ✅ 13 + 8 | Boa densidade, mas "na unidade" não identifica ninguém e o código CNES não aparece. Nomear o hospital e o código 9255826. |
| 7. Em que bairro fica? | "**Depende da fonte**: o cadastro federal registra Jardim Guarulhos, enquanto o site da operadora e a imprensa dizem Jardim Santa Edwirges." | 🔴 | ❌ | Abertura elíptica **e** sem hospital, sem cidade e sem endereço — justo a resposta que disputa com o `local_pack`. "O Hospital e Maternidade Guarulhos fica na Av. Tiradentes, 1015, região central de Guarulhos (SP). O bairro aparece de dois jeitos: …". |
| 8. Como agendar consulta/exame? | "**Pelos canais oficiais da operadora**: aplicativo, área do beneficiário, canal de agendamento de consultas e exames ou a central de atendimento…" | 🔴 | ❌ | Elíptica **e** reprovada no teste de substituição: serve para qualquer unidade Hapvida do país. Ancorar com o fato local que justifica a resposta — a divergência de telefone entre CNES e site da operadora, que o próprio artigo apurou — e nomear a unidade. |

## 3. Número em TEXTO (a IA lê `<p>`/`<table>`, não lê arte)

| Componente visual | Dado | Existe em `<p>`? |
|---|---|---|
| `grid4` (stat cards) | CNES 9255826 · 4 tipos de PS · 13 leitos de alojamento · `[sao-paulo_menorvalor]` | ✅ todos (§HS2, FAQ 5, FAQ 6, §HS4) |
| `quadro-comp` — coluna "O que consta no registro oficial" | parto e alto risco · UTI adulto e neonatal · 4 PS · cinco salas de cirurgia | ✅ em `<p>` (HS2) |
| `quadro-comp` — mesma coluna | **"1 de pré-parto e 1 de parto normal"** | 🟡 **NÃO** — só dentro do card. Único dado do artigo preso em componente visual. Levar para o `<p>` da H3 "As salas que a ficha lista". |
| `quadro-comp` — coluna "O que nenhuma fonte publica" | horário do PS · visita/acompanhante/o que levar · estacionamento e ônibus · lista de planos | ✅ todos em `<p>` (HS2, HS3, HS4) |
| `v5-trust` (faixa de confiança) | ANS nº 359017 · DRV 11 anos especialista Hapvida · 7.000+ clientes | 🟡 **NÃO** — as três credenciais de E-E-A-T existem só em faixa visual. Levar ao menos ANS 359017 e "11 anos" para o `<p>` do "Sobre este guia". |
| `fonte-oficial` ×2 | Lei 9.656/98 · Lei 10.778/2003 | ✅ (a 10.778/2003 aparece em `<p>` na conclusão; a 9.656/98 aparece como "definida desde 1998" em HS4 — citar o número da lei no texto renderia mais em AI Overviews, que premiam citação nomeada) |

**Zero `<table>` no artigo.** Para uma SERP liderada por `local_pack`, isso é uma ausência de formato, não de conteúdo — ver §5.

## 4. Defensibilidade da passagem principal

**🟢 Nível 1-2.** O lead se apoia em **ficha do CNES 9255826 lida** (registro federal, fonte primária, transcrita em `fontes/ci1-rodada2-fontes-primarias.md`) e no site da operadora. A afirmação central — "mesmo hospital, dois nomes, mesmo registro" — é exatamente o que **nenhum dos 5 concorrentes lidos publica** e o que a IA **não responde sozinha**: é um fato de cadastro de novembro de 2025, não conhecimento de modelo. O segundo parágrafo do lead, porém, se apoia em auto-referência ("as cinco páginas que este guia leu") e em métrica de keyword sem fonte nomeada — nível 5 de defensibilidade dentro da passagem mais valiosa. Corrigir sem desmontar a ponte entre os dois nomes.

## 5. Formato da resposta × formato da SERP

A SERP **não tem featured snippet**; ela abre com `local_pack` e `people_also_ask`. O artigo hoje responde em **prosa corrida**, não em ficha.

**Ficha de lugar — parcial.** Endereço e bairro aparecem (bem) no corpo de HS3; horário e telefone estão **deliberadamente ausentes e justificados** (o CNES não registra horário; os telefones divergem entre cadastro e operadora) — decisão YMYL correta, mas que deixa a ficha incompleta justamente nos campos que o `local_pack` exibe. Falta o **envelope**: não há bloco rotulado (nem `<table>`) que entregue, num lugar só e em texto, *nome atual · nome anterior · CNES · endereço + complemento · bairro nas duas grafias · serviços registrados · o que nenhuma fonte publica · onde confirmar*. Esse bloco é o que a IA extrai como ficha e é o que alimenta `Hospital`/`MedicalOrganization` com `alternateName` no schema.

**PAA — 1 de 4 respondido, e mal posicionado:**

| PAA (literal) | Onde o artigo responde | Veredito |
|---|---|---|
| Qual hospital atende Hapvida em Guarulhos? | Só indiretamente; a lista da rede de Guarulhos (Centro Clínico I e II, Clínica Jardim Guarulhos, NotreLabs Imedi) está enterrada num `<p>` sob a H3 "O que é raciocínio, não dado" | 🔴 **buraco** — é o PAA nº 1 e o artigo tem o dado |
| Qual é o melhor hospital em Guarulhos? | Não responde | 🟡 fora de escopo por decisão YMYL (comparativo auto-promocional é armadilha conhecida — `geo-plataformas.md`). Aceitável **não** responder; registrar a decisão |
| Quais hospitais o Hapvida atende? | Não responde (escopo nacional) | 🟡 é do cluster — resolver com link, não com seção (anti-doorway) |
| Quais hospitais em SP aceitam o plano Hapvida? | Não responde (escopo estadual) | 🟡 idem — hoje o único link de cluster é `/plano-hapvida-guarulhos/`; o link estadual não existe |

## 6. Por plataforma (`geo-plataformas.md`)

| Plataforma | Estado | Observação |
|---|---|---|
| **Perplexity** (parágrafo autocontido é a moeda) | 🟡 | As 6 aberturas de seção estão autocontidas; **5 das 8 respostas de FAQ não estão** (abrem com "Era", "É", "Quatro", "Depende", "Pelos canais"). É a maior perda do artigo nesta plataforma. FAQPage em JSON-LD ainda não existe (schema é execução separada) — sem ele, perde-se a alavanca nº 1 do Perplexity. |
| **Claude** (Brave; densidade factual) | 🟢 | Densidade alta e rara: CNES 9255826, códigos 112-003/112-004/162-001/162-002/140-019/140-013/140-012/140-016, 11 consultórios, 5 salas de cirurgia, 13 + 8 leitos, 16 incubadoras, datas de 10-11/11/2025, duas leis nomeadas, 2 fontes externas nomeadas e linkadas (CNES e Saúde Business). Sustenta. Ressalva: o "-58%" sem fonte nomeada destoa do conjunto. |
| **ChatGPT** (frescor real + formato de resposta) | 🟡 | Formato de resposta bom nas seções, fraco no FAQ. **Frescor: não há data real de revisão** — o texto traz `[mes_atual] de [ano_atual]`, shortcode que rende data nova todo mês sem revisão (recência cosmética, Regra 5c). O sinal que vale é o `dateModified` do schema, que **ainda não existe**. |
| **AI Overviews** (schema + citação nomeada) | 🟡 | Citação nomeada bem feita ("segundo o veículo setorial Saúde Business", "conforme apuração do Click Guarulhos", "Lei 10.778/2003"). **Schema pendente** — sem `@graph`/`speakable`/`Person knowsAbout` não há como avaliar a maior alavanca desta plataforma. |
| **Copilot** (Bing + IndexNow) | ⚪ | Fora do escopo do artigo (checagem de site, 1×). |

**Data real de revisão: NÃO.** Só o shortcode. Ao publicar, o `dateModified` do JSON-LD tem de trazer a data real e ser registrado no banco (`atualizar_artigo`).

**Schema:** `schema.json` não existe na pasta do artigo (execução separada, prevista). `speakable`, `Person` com `knowsAbout` e `FAQPage` ficam **não verificáveis** nesta auditoria — item obrigatório de reauditoria quando o schema for gerado.

## 7. Medição de citação em IA

**NÃO MEDIDO — e não estimado.** O artigo **ainda não foi publicado** (`00-ESTADO.md` registra FASE 0, com o portão de aprovação humana em aberto; não há URL no ar). Sem página indexada não há o que consultar em `monitor_citacoes_ia` / `buraco_citacao_ia`. A classificação *citado / concorrente citado, nós não / ninguém citado* fica para a **FASE 5**, após a publicação e a indexação. Qualquer número de citação declarado agora seria invenção.

---

## VEREDITO

**🟡 APROVADO COM CORREÇÕES — a espinha está certa, o FAQ não está.**

O artigo tem o que quase nenhum concorrente tem: uma passagem-âncora defensável em fonte primária (o lead sobre os dois nomes e o CNES 9255826), densidade factual alta e honestidade explícita sobre o que nenhuma fonte publica — os três sinais que mais rendem citação. As **seções passam**: 6 de 6 aberturas são autocontidas e 5 de 6 sobrevivem ao teste de substituição.

O que impede o 🟢 é **onde o artigo mais seria citado**: o FAQ. Cinco das oito respostas abrem com pronome, elipse ou conselho genérico — extraídas sozinhas pelo Perplexity, duas não dizem sequer de que hospital falam e uma serve para qualquer unidade Hapvida do país. Somam-se dois blocos H3 reprovados no teste de substituição, o PAA nº 1 não respondido apesar de o dado estar no artigo, e a ausência de um bloco em formato de ficha numa SERP liderada por `local_pack`.

Nenhuma dessas correções mexe em fato, fonte ou estrutura: são reescritas de abertura e um bloco novo montado com dado já apurado no state file.

## AS 3 CORREÇÕES DE MAIOR RETORNO

1. **Desorfanar as 8 aberturas do FAQ** (resolve 4 🔴 e 3 🟡 de uma vez). Toda resposta começa nomeando o sujeito — "O Hospital e Maternidade Guarulhos…", "A Sala Lilás…", "Keila Ferreira…" — e, onde existir, com o número e a fonte na primeira frase ("quatro tipos de pronto-socorro registrados na ficha do CNES 9255826"). É a maior alavanca do Perplexity e custa oito frases.

2. **Criar a ficha da unidade em texto** (`<p>` rotulado ou `<table>`, logo após o lead ou no topo de HS3) com: nome atual · nome anterior · CNES 9255826 · Av. Tiradentes, 1015, complemento "1 037" · bairro nas duas grafias · serviços registrados · o que nenhuma fonte publica · onde confirmar. Atende o formato que a SERP premia (`local_pack`), dá ao artigo seu primeiro `<table>` e alimenta `Hospital` + `alternateName` no schema. No mesmo movimento, **responder literalmente o PAA nº 1** — "Qual hospital atende Hapvida em Guarulhos?" — subindo a lista da rede de Guarulhos (Centro Clínico I e II, Clínica Jardim Guarulhos, NotreLabs Imedi) de onde está hoje, enterrada sob "O que é raciocínio, não dado".

3. **Ancorar as duas passagens que reprovam no teste de substituição** — "Antes de ir à unidade" e "O que é raciocínio, não dado" — a este estabelecimento: nome da unidade, CNES 9255826, os quatro PS sem horário registrado, o catálogo de rede de Guarulhos. Hoje as duas são conselho nacional em página local; trocada a cidade, seguem verdadeiras. É o único ponto do artigo onde a citabilidade esbarra no anti-doorway.

**Pendente de reauditoria (não avaliável agora):** schema (`speakable`, `Person knowsAbout`, `FAQPage`, `dateModified` real) e medição de citação em IA — ambos na FASE 5, depois da publicação.
