# ESTADO — plano-hapvida-divinopolis

> Este arquivo é o **ponto de salvamento** do artigo. Quem abrir uma sessão nova
> lê ele primeiro e continua daqui — sem refazer pesquisa nem readivinhar decisão.
> **Atualize ao fim de cada fase, antes de responder ao usuário.**

## Identificação

- **Slug:** plano-hapvida-divinopolis
- **Tipo:** city
- **Skill em uso:** hapvida-article-builder-v7 (v7.4 lead-herói · v7.2 multiagente)
- **Aberto em:** 2026-09-01
- **URL de destino:** https://tabelaplanos.com.br/plano-hapvida-divinopolis/
- **Keyword principal:** plano hapvida divinópolis (variação-mãe medida:
  "hapvida divinopolis" — 260 buscas/mês, KD 0, competição LOW)

## Fase atual

- **Fase:** ESTÁGIO 2.5 — portão de pesquisa; state file aprovado pelo usuário em 2026-09-01
- **Próximo passo concreto:** o usuário revisar o rascunho no WordPress
  (post 39808) e resolver as 3 pendências abertas: URL da imagem de abertura,
  imagem da tabela (cotador). A abrangência contratual foi RESOLVIDA em
  2026-09-04 com o registro de produtos da ANS. Os ajustes pedidos após a
  varredura anti-doorway já estão aplicados no rascunho.
- **Bloqueios:** (1) rede assistencial própria tem 4 unidades, abaixo do piso
  de 5 — decisão de arquétipo pendente; (2) imagem da tabela — Divinópolis
  ainda fora do `cotador_fila`; (3) URL da `<figure>` de abertura.
- **Resolvidos:** shortcodes (usuário, 2026-09-03); abrangência contratual
  (ANS PDA-008, 2026-09-04). Produtos comerciais: o registro da ANS nomeia o
  produto PF regional (PERSONAL 200 OESTE MG) — a S3 pode sair de órfã, mas
  isso não foi pedido e não foi feito.

## Portões

| Portão | Status | Evidência |
|---|---|---|
| CI-1 — concorrente lido (`checkpoint_ci1.py`) | ✅ aprovado | `checkpoints/ci1.txt` — 5 concorrentes lidos, rota curl |
| FASE 0 (`checkpoint_fase0.py`) | ✅ aprovado | `checkpoints/fase0.txt` — APROVADO, 1 aviso |
| Aprovação humana do state file | ✅ aprovado | usuário, 2026-09-01 |
| Suficiência (`checkpoint_suficiencia.py`) | ✅ aprovado | `checkpoints/suficiencia.txt` |
| Juiz 24 (P-B, originalidade/valor) | 🟡 BLOQUEOU; 2 🔴 corrigidos | notas 6 e 7 |
| Juiz 23 (P-A, suficiência/verdade) | 🔴 BLOQUEOU; 11 🔴, 8 corrigidos | notas 4 e 5 — 3 dependem do usuário |
| Kit on-page (`checkpoint_onpage.py`) | ✅ aprovado | 7/7 posições |
| Preço-primeiro / lead-herói (`checkpoint_preco_primeiro.py`) | ✅ aprovado | ordem v7.5 |
| Voz humana (`checkpoint_voz.py`) | ✅ aprovado | 0 🔴 |
| Completude (`checkpoint_completude.py`) | ✅ aprovado | 9 H2 · 15 FAQ · 3.831 palavras |
| `[VERIFICAR]` / tokens proibidos (`checkpoint_verificar.py`) | ✅ aprovado | 65 tokens armados |
| Varredura anti-doorway final (`checkpoint_doorway_final.py`) | ✅ aprovado | `checkpoints/doorway_final.txt` — 12 irmãos, D1 25,5% (limite 45%), maior trecho idêntico 13 palavras |
| Ritmo visual (`checkpoint_ritmo_visual.py`) | ✅ aprovado | 10/10 seções ≤3 `<p>` |
| Tamanho de parágrafo (`checkpoint_paragrafos.py`) | ✅ aprovado | 45/46 ≤380 chars, 1 no limite (417) |
| Citabilidade (`checkpoint_citabilidade.py`) | ✅ aprovado | 7 ideais, 2 aceitáveis, 0 reprovadas |
| Distância entre links internos (≥150 palavras) | ✅ aprovado | 9 links, menor vão 297 palavras |
| Registro no banco Supabase | ✅ feito (parcial) | artigo id 196, status `pendente`; 3 links de entrada + 9 de saída + histórico id 47. Falta: hospitais, FAQs e virar `publicado` |
| Envio ao WordPress (rascunho) | ✅ feito | post 39808, status draft, 89.982 chars no WP (85.442 locais); texto visível e estrutura conferidos idênticos ao arquivo local em 2026-09-04 |
| Schema JSON-LD | ⬜ pendente | execução separada, só sob pedido |

Legenda: ⬜ pendente · 🟡 rodado, com ressalva · ✅ aprovado (saída em `checkpoints/`)

## Decisões tomadas

- 2026-09-01 — pasta criada, tipo city.
- 2026-09-01 — grupo tarifário de coparticipação: `demais_capitais`
  (Divinópolis não é BH/RMBH). Shortcodes `[demais_capitais_*]`.
- 2026-09-01 — CI-1 feita pela rota 2 (curl); WebFetch testado e vivo. Páginas
  salvas em `fontes/`. 5 concorrentes lidos na íntegra.
- 2026-09-01 — SERP rodada em `location_code` 2076 (Brasil): o geotarget de
  cidade de Divinópolis não foi confirmado em duas fontes. Limitação declarada
  na seção 1 do state file.
- 2026-09-01 — a home do tabelaplanos já ocupa a SERP da cidade (9º orgânico).
  Vigiar canibalização home × city page em D+30.
- 2026-09-01 — `hospital santa monica divinopolis` (2.400/mês) NÃO é alvo desta
  página: vira artigo de hospital (HS1-HS4) no cluster.
- 2026-09-01 — rede credenciada do guia do concorrente fica FORA do artigo até
  confirmação em fonte primária.
- 2026-09-01 — `checkpoint_suficiencia.py` reprovou 2×; correções feitas no
  state file: PAA agora aponta para a FAQ adaptada em vez de repeti-la; fan-out
  deixou de ser escrito como pergunta de FAQ; H3 de formulário do concorrente
  marcado como CTA, não conteúdo; nível de defensibilidade do ganho declarado
  junto ao ganho; 5 diferenciais rotulados com `titulo:` e ancorados na praça.
- 2026-09-01 — juiz P-B bloqueou com 2 🔴, ambos confirmados e corrigidos:
  (a) a CI-1 afirmava que a tabela do rotaseguros não tem data de vigência —
  FALSO, a página diz "ALTERADO EM 31/03/25"; o ponto real é a IDADE da tabela,
  não a ausência de data; (b) a lista de municípios vizinhos estava sem fonte —
  os nomes sobreviveram à verificação, mas agora vêm do IBGE (região imediata
  310065, 20 municípios) com aviso ao redator: citar geografia, nunca cobertura.
- 2026-09-01 — defensibilidade do ganho do CI-2 rebaixada de 1 para 2: o
  endereço compartilhado do campus já está publicado pelo concorrente líder. O
  ganho é o cruzamento (catálogo × guia oficial × CNES) e a correção do erro
  dele, não a descoberta do endereço.
- 2026-09-01 — lacuna de MUST-MATCH aceita de propósito e declarada: o líder
  nomeia ~30 credenciados; nós não listamos nenhum sem confirmação primária.
  Troca consciente de volume por precisão. Pendência de verificação aberta.
- 2026-09-01 — link para o pillar de tabela de preços NÃO será usado: o destino
  está SATURADO (44 backlinks) e a tabela já é renderizada na página pelo
  shortcode. O bridge de coparticipação mantém o link para o pillar de
  coparticipação, que é obrigatório para o anti-doorway funcionar.

## Achados do juiz P-A que mudaram fato (2026-09-01)

- **Parto:** o CNES 2159376 registra **centro obstétrico 0 e centro neonatal 0**
  para o Hospital e Maternidade Santa Mônica, e a lista oficial de
  especialidades do bloco cirúrgico não traz obstetrícia. O nome diz
  "Maternidade"; o registro público não confirma. Proibido afirmar cobertura de
  parto na cidade.
- **Rua Rio de Janeiro, 101:** o CNES 146250 registrado nesse endereço está
  **desabilitado (motivo 04)**. Saiu da rede assistencial, entrou nos tokens
  proibidos e passa a ser tratado apenas como endereço administrativo (S7).
  Isso resolve a contradição que eu mesmo tinha criado entre a seção 4 e o
  diferencial "única unidade fora do complexo".
- **Páginas oficiais:** respondem HTTP 200; o bloco "esta página não faz mais
  parte do nosso site" é fallback da SPA no mesmo HTML que traz os dados. A
  redação fica travada em atribuição datada — nunca "opera hoje".
- **Divergência do portal nacional:** a alegação foi reduzida à Bioimagem
  (filtro "MG - Uberlândia"). O Centro Clínico traz os dois rótulos na mesma
  página, então dele não se pode dizer que some do filtro.
- **Endereços de BH no guia do líder:** são **pelo menos cinco**, não três — e
  um deles (Centro de Oftalmologia Brasil) está no nosso próprio banco como
  retaguarda do artigo de Belo Horizonte.
- **FORBIDDEN_TOKENS:** de 16 para 65 tokens, incluindo os credenciados não
  confirmados, os 16 valores da tabela do concorrente, os números corporativos
  dele que conflitam com os canônicos e as variantes de endereço sem pontuação.

## Dados que faltam

- Natureza atual do atendimento na Rua Rio de Janeiro, 101 (administrativo,
  coleta, ou os dois) — `[VERIFICAR]`. Endereço confirmado no CNES (146250).
- Existência de pronto atendimento 24h autônomo fora do complexo Santa Mônica —
  `nao_encontrado`. Não afirmar nem negar.
- Nº de beneficiários Hapvida em Divinópolis — sem fonte primária; o número do
  concorrente está na lista de tokens proibidos.
- Abrangência formal para Nova Serrana e demais cidades da região imediata —
  sem confirmação; tratar regionalidade sem cravar município.
- Geotarget do Google Ads de Divinópolis — pendência para a Fase 5.
- Prefixo da cidade no plugin de shortcodes de preço — perguntado ao usuário.
- Os 10 valores por faixa etária para a imagem da tabela — Divinópolis não
  está na fila do cotador. Sem eles a imagem não é gerada (falha barulhenta).

## Fio condutor

Divinópolis não tem rede espalhada: tem um campus. Hospital, centro clínico e
diagnóstico da Hapvida ficam no mesmo número da Rua Pedro Ferreira do Amaral,
no Padre Libério, mais um ponto no Centro — e é isso que decide se o plano
serve para você, porque muda o deslocamento, não a mensalidade. O artigo
responde a uma pergunta prática: onde você vai ser atendido, de fato, nesta
cidade — e por que o guia médico que aparece primeiro no Google leva a
endereços de Belo Horizonte.

## Envio ao WordPress (2026-09-04)

- **Post 39808**, slug `plano-hapvida-divinopolis`, **status draft** — não publicado.
- Corpo enviado em 5 partes via `substituir_no_artigo`; o tamanho bateu exato em
  todas as etapas (17.222 → 34.488 → 51.538 → 68.683 → **84.246**, igual ao
  arquivo local). Amostragem confirmou `[divinopolis_menorvalor]` 8×,
  `Rua Pedro Ferreira do Amaral, 33` 6×.
- Meta title e meta description gravados no Rank Math; o ano vai por
  `%currentyear%`.

### Pendências antes de publicar

1. **URL da imagem de abertura** — a `<figure>` da S1 está com `[URL_DA_IMAGEM]`.
2. **Imagem da tabela** — não gerada: Divinópolis não está na fila do cotador e a
   regra proíbe inventar valor para imagem.
3. **Abrangência contratual por produto** — segue sem confirmação; o artigo trata
   a região imediata como geografia, nunca como cobertura.
4. **Schema JSON-LD** — execução separada, só sob pedido.
5. **Registro no banco** — só após a publicação.

## Varredura anti-doorway (2026-09-04)

Rodada com 12 artigos irmãos baixados do ar em `--outros`. Saída em
`checkpoints/doorway_final.txt`; relatório em `checkpoints/varredura-doorway.html`.

**Veredito: LIBERADO com ressalvas — 3 ajustes antes de publicar.**

Mecânica: D1 26,9% (limite 45%) · D2 zero seção sem âncora · D3 zero clichê ·
D4 maior trecho idêntico 13 palavras em 12 irmãos · D5 title e meta citam a praça.

Achados que dependem de decisão:
1. 🔴 Dois bridges sem link — a caixa Portabilidade promete "o guia de
   portabilidade do site" e não linka; a caixa de carência da S7 também não.
   Os dois destinos estão saturados (28 e 53), então é decisão do usuário:
   linkar mesmo assim, ou tirar a promessa do texto.
2. 🟡 Dois H2 repetem o molde de irmãos: "Como contratar o plano Hapvida em
   Divinópolis" (= Araraquara, Franca, Itapevi) e "Quanto custa o plano Hapvida
   em Divinópolis" (= Uberaba). O overlap catalogado já manda renomear.
3. 🟡 FAQ 3 tem 0,88 de semelhança com a de Betim; FAQ 5 tem 0,60 com a de Lins.
4. 🟡 S3 na família de overlap "Tipos de Planos Disponíveis" — lacuna já conhecida.
5. 🟢 Nenhum dos 4 overlaps de risco ALTO catalogados foi reproduzido.
6. 🟢 7 dos 9 links internos vão a destino NORMAL ou SUBUTILIZADO.
7. Canibalização não mensurável: a página é rascunho. Hoje quem ocupa a SERP da
   cidade é a home (9º orgânico). Medir em D+30.

Nada foi alterado no rascunho nem gravado no banco.

## Ajustes da varredura anti-doorway (2026-09-04)

Pedido do usuário: "cheque pra mim doorways" → "faça os ajustes".

| # | Achado | Ajuste aplicado |
|---|---|---|
| 1 | H2 de preço e H2 de contratação com fórmula genérica de cidade | H2 1 → "O preço do plano Hapvida em Divinópolis, faixa a faixa"; H2 7 → "O que decidir antes de assinar em Divinópolis" (sumário atualizado nos dois) |
| 2 | FAQ 3 e FAQ 5 formuladas como pergunta padrão de cidade | FAQ 3 → "O plantão do Padre Libério vale em feriado e fim de semana?" (ancorada na string de turno do CNES); FAQ 5 → "Dá para fazer a consulta e o exame de imagem no mesmo endereço?" |
| 3 | Parágrafo do S7 prometia guia de portabilidade sem link | reescrito para descrever prazo, janela de aniversário e faixa de preço como norma nacional, sem referência pendurada |
| 4 | 3 pares de links internos abaixo de 150 palavras de distância (laboratórios 109, cidades 15, teleconsulta 53) | `laboratorios-hapvida-capitais` movido para a FAQ 5, `hapvida-cidades` para a FAQ 10, `como-contratar-hapvida` para a FAQ 15; 9 links internos, menor vão agora 297 palavras |

Efeito medido no `checkpoint_doorway_final.py`: D1 (texto que sobrevive à troca
de cidade) caiu de 26,9% para 25,5%; limite 45%.

## Abrangência contratual — verificada (2026-09-04)

Pedido do usuário: "abrangencia contratual preciso que vc verifique, se nao
achar, exclua essa informação". **Foi achada** — o artigo passou a afirmar em
vez de mandar o leitor perguntar.

**Fonte:** ANS, Dados Abertos PDA-008 "Características dos Produtos de Saúde
Suplementar" — `pda-008-caracteristicas_produtos_saude_suplementar.csv` e
`pda-008-tabela_auxiliar_de_detalhamento_de_municipios.csv`
(`https://dadosabertos.ans.gov.br/FTP/PDA/caracteristicas_produtos_saude_suplementar-008/`),
arquivo com Last-Modified 2026-09-04 05:02 UTC, baixado e cruzado em 2026-09-04.
Evidência salva em `fontes/ans-abrangencia-divinopolis.json` e
`fontes/ans-area-personal200-oestemg.json`. **Defensibilidade: nível 1** (dado
público primário, reproduzível).

**Critério:** produtos com `SITUACAO_PLANO = Ativo` cujo `ID_GEO_COBERTURA`
contém o município 312230 (Divinópolis/MG), das operadoras do grupo Hapvida.

| Achado | Número |
|---|---|
| Produtos ativos do grupo que cobrem Divinópolis | 1.153 |
| Abrangências que aparecem | Grupo de municípios, Estadual, Nacional |
| Abrangência **Municipal** em Divinópolis | **0** (a categoria existe: 19.452 produtos no país) |
| PF médico-hospitalar (sem odonto) que cobre Divinópolis | 4 — as variantes do PERSONAL 200 OESTE MG (Notre Dame Intermédica Minas Gerais Saúde S.A., ANS 348520), todas "Grupo de municípios" |
| Área desse produto | 19 municípios do Oeste de Minas |
| Da região imediata 310065 (20 municípios) | 14 dentro, 6 fora |
| Fora da área | Camacho, Conceição do Pará, Itatiaiuçu, Japaraíba, Leandro Ferreira, Pedra do Indaiá |
| Fora da região imediata mas dentro da área | Bom Despacho, Formiga, Igaratinga, Oliveira, Pará de Minas |
| Melhor cobertura da região imediata entre TODAS as áreas "grupo de municípios" que incluem Divinópolis | 15 de 20 — nenhuma cobre as 20 |

Onde entrou: selo "Municípios vizinhos" da S5, subtítulo do H2 7, dois
parágrafos da S7 (com link externo `nofollow` para a ANS), FAQ 9 (Belo
Horizonte) e FAQ 10 (região). Efeito no `checkpoint_doorway_final`: D1 caiu de
25,5% para 23,7%.

**Limite do dado:** o registro da ANS diz o que está registrado e ativo, não o
que a DRV vende hoje nem a que preço. O artigo atribui e data a fonte.

## Dois defeitos anteriores achados na conferência (2026-09-04)

Encontrados ao comparar o rascunho do WordPress com o arquivo local, não pedidos:

1. **Aviso de preço sumido no ar.** O parágrafo "Valores por faixa etária
   conforme tabela vigente. Sujeitos a alteração por modalidade, acomodação e
   condições comerciais." existia no arquivo local e **não** no post 39808 —
   perdido no envio original em 5 partes. Restaurado.
2. **`<div id="cotacao-1">` removido pelo WordPress.** O editor descarta a
   `<div>` que só embrulha um shortcode, então o botão fixo "Faça uma Cotação"
   (`href="#cotacao-1"`) apontava para âncora inexistente. A âncora passou para
   o parágrafo do aviso de preço, que fica no mesmo ponto e sobrevive ao editor.
   Corrigido nos dois lados; `checkpoint_preco_primeiro` segue aprovado.
   **Regra para os próximos artigos: não pendurar id em `<div>` que só contém
   shortcode.**
3. **Experiência da DRV desatualizada.** O texto dizia "mais de dez anos" e o
   selo "mais de 10 anos". A skill `hapvida-data` v1.1 (jul/2026) fixa **11
   anos** e proíbe os valores antigos. Corrigido para "onze anos" / "11 anos"
   no arquivo e no rascunho. **Pendente, não feito:** a mesma skill troca a
   certificação de Diamante para **Safira**, com regra de redação temporal — o
   artigo não menciona certificação nenhuma, e incluir é decisão sua.

**Nota de ambiente:** os módulos `HDATA_*.md` da skill `hapvida-data` moram em
`/mnt/project/`, que não existe neste ambiente — só o resumo do `SKILL.md` está
acessível aqui.

## Título SEO com shortcode de preço (2026-09-04)

Pedido: "o titulo seo precisa conter o shortcode de preço".

| | valor |
|---|---|
| Antes | `Plano Hapvida Divinópolis: a rede própria no Padre Libério` (58 chars) |
| Depois | `Plano Hapvida Divinópolis: Padre Libério a partir de [divinopolis_menorvalor]` (77 crus) |
| Renderizado | ~62 caracteres, quando o shortcode virar o valor |

Campo alterado: `rank_math_title` do post 39808 (o título do post, o H1 e a meta
description ficaram como estavam).

**Verificado antes de escrever, não presumido:** o shortcode renderiza mesmo no
título SEO. `plano-hapvida-salvador2` tem
`rank_math_title = "Plano Hapvida Salvador [ano_atual]: Rede e Promoções de [salvador_menorvalor]"`
e a página no ar devolve
`<title>Plano Hapvida Salvador 2026: Rede e Promoções de R$ 145,72</title>`.

**Nota:** a fila do cotador (`cotador_fila`) tem só belo horizonte, fortaleza,
goiania, recife e sao paulo — Divinópolis não está lá, e Salvador também não.
A fila é o robô de coleta, não a fonte do shortcode; os dois assuntos são
separados. A imagem da tabela continua pendente por outro motivo.

**Por que este texto e não o padrão de Salvador:** "rede e preços de" passa no
teste de substituição de cidade (serve para qualquer praça). "Padre Libério" é
só de Divinópolis, então segura o D5 do anti-doorway e ainda cabe no espaço.

`checkpoint_onpage` e `checkpoint_doorway_final` reaprovados com o título novo.

## Links de entrada criados (2026-09-04)

Pedido expresso do usuário: linkar de `plano-hapvida-uberaba`,
`plano-hapvida-uberlandia` e `promed-plano-de-saude` para
`https://tabelaplanos.com.br/plano-hapvida-divinopolis/`.

| Origem | Post | Como | Âncora |
|---|---|---|---|
| `promed-plano-de-saude` | 36005 | `inserir_link_interno` — a página **já citava** "Divinópolis" na lista de praças mineiras, no mesmo parágrafo em que "Uberlândia" já era link | Divinópolis |
| `plano-hapvida-uberlandia` | 29907 | `substituir_no_artigo` — frase nova no parágrafo da tabela própria × tabela regional | plano Hapvida em Divinópolis |
| `plano-hapvida-uberaba` | 35817 | `substituir_no_artigo` — frase nova no parágrafo que contrasta o desenho de rede de Uberlândia e Uberaba | plano Hapvida em Divinópolis |

**Por que dois exigiram texto novo:** `inserir_link_interno` só transforma
frase existente em link, e nem Uberaba nem Uberlândia mencionavam Divinópolis
— natural, a página é nova. Link contextual para cidade não citada exige
acrescentar a menção. Cada um levou **uma frase**, com fato já verificado na
FASE 0 (grupo tarifário "demais praças"; hospital, centro clínico e imagem no
mesmo endereço).

Dry-run rodado antes de cada gravação. Conferido no ar depois: Uberlândia e
Promed já servindo o link; Uberaba ainda em cache na hora da checagem, mas o
link confirmado no corpo do post pela leitura do próprio WordPress.

### Duas coisas que ficaram de fora, de propósito

1. **O destino ainda é rascunho** — `https://tabelaplanos.com.br/plano-hapvida-divinopolis/`
   devolve **404** hoje. Os três links só passam a valer quando o post 39808
   for publicado. Avisado ao usuário antes de gravar.
2. ~~Nada foi registrado no Supabase.~~ **Registrado em 2026-09-04** a pedido
   do usuário — ver a seção seguinte.

## Registro no Supabase (2026-09-04)

Pedido do usuário: "registre no banco".

**A ordem importou.** `registrar_links_artigo` para um slug ausente da tabela
de artigos viraria link morto, então o artigo foi registrado primeiro.
Conferido depois: `consultar_links_quebrados` **não** lista
`plano-hapvida-divinopolis`.

| O que | Função | Resultado |
|---|---|---|
| Artigo | `registrar_artigo_novo` | **id 196**, tipo `cidade`, status **`pendente`**, versão v7.5, Divinópolis/MG, com os 9 H2, os 5 concorrentes da CI-1 e as observações |
| 3 links de entrada | `registrar_links_artigo` × 3 | uberaba (S4 rede), uberlandia (S2 preço), promed (rede MG) |
| 9 links de saída | `registrar_links_artigo` | os 9 destinos do artigo, com contexto e seção |
| Histórico | `registrar_atualizacao` | **id 47** |

Gêmeo de slug conferido no inventário antes de registrar (armadilha 6): não
existe variante de `plano-hapvida-divinopolis` no banco.

### Por que `pendente` e não `publicado`

O post 39808 ainda é rascunho e a URL responde 404. O enum `artigo_status` só
aceita `publicado` e `pendente` — não existe "rascunho" —, então `pendente` é o
valor honesto.

### ⚠️ Ao publicar, NÃO rode `registrar_artigo_novo` de novo

O artigo já existe como id 196. Publicar exige:

1. `atualizar_artigo` para virar `publicado` (o slug é a chave; não muda);
2. `registrar_hospitais_artigo` — **ainda não feito**, as 4 unidades próprias;
3. `registrar_faqs_artigo` — **ainda não feito**, as 15 FAQs;
4. `registrar_uso_faq` para as FAQs estruturais;
5. `registrar_atualizacao` da publicação.

Rodar `registrar_artigo_novo` de novo criaria duplicata.
