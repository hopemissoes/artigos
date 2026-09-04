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
  imagem da tabela (cotador) e abrangência contratual. Os ajustes pedidos após
  a varredura anti-doorway já estão aplicados no rascunho.
- **Bloqueios:** (1) produtos comerciais vendidos em Divinópolis — nenhuma
  fonte pública nomeia; a S3 fica órfã; (2) prefixo do shortcode e valor de
  entrada — sem eles não há lead-herói nem tabela; (3) abrangência contratual
  por produto — decide 3 FAQs e a S5; (4) rede assistencial própria tem 4
  unidades, abaixo do piso de 5 — decisão de arquétipo pendente.

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
| Registro no banco Supabase | ⬜ pendente | só após publicação |
| Envio ao WordPress (rascunho) | ✅ feito | post 39808, status draft, 88.839 chars no WP (84.584 locais) |
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
