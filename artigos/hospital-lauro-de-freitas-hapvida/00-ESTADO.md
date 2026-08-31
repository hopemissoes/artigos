# ESTADO — hospital-lauro-de-freitas-hapvida

> Este arquivo é o **ponto de salvamento** do artigo. Quem abrir uma sessão nova
> lê ele primeiro e continua daqui — sem refazer pesquisa nem readivinhar decisão.
> **Atualize ao fim de cada fase, antes de responder ao usuário.**

## Identificação

- **Slug:** hospital-lauro-de-freitas-hapvida
- **Tipo:** hospital (HS1-HS4)
- **Skill em uso:** hapvida-article-builder-v7 (MODO: monomodelo, declarado)
- **Aberto em:** 2026-08-31
- **URL de destino:** https://tabelaplanos.com.br/hospital-lauro-de-freitas-hapvida/
- **Keyword principal:** hospital lauro de freitas hapvida — 2.900/mês, KD 0, competição LOW
- **Hub (artigo de cidade):** plano-hapvida-salvador2

## Fase atual

- **Fase:** ARTIGO ESCRITO — todas as travas mecânicas verdes. Aguardando o portão humano final.
- **Próximo passo concreto:** (1) usuário fornecer a URL da imagem de abertura (`[URL_DA_IMAGEM]` no HTML);
  (2) confirmar se o shortcode `[cidade_menorvalor]` resolve nesta URL, que não é página de cidade;
  (3) aprovar o artigo. Só depois: schema (execução separada, sob pedido) e registro no banco.
- **Bloqueios:** 1 placeholder de imagem em aberto. Nada mais.

## Portões

| Portão | Status | Evidência |
|---|---|---|
| CI-1 — concorrente lido (`checkpoint_ci1.py`) | ✅ aprovado | `checkpoints/ci1.txt` — 5 concorrentes lidos por curl (HTTP 200) |
| FASE 0 (`checkpoint_fase0.py`) | ✅ aprovado | `checkpoints/fase0.txt` — 1 aviso ([VERIFICAR] fora do artigo) |
| Suficiência (`checkpoint_suficiencia.py`) | ✅ aprovado | `checkpoints/suficiencia.txt` — ganho em defensibilidade 1 |
| Aprovação humana do state file | ✅ aprovado | usuário aprovou em 2026-08-31 |
| Kit on-page (`checkpoint_onpage.py`) | ✅ aprovado | `checkpoints/onpage.txt` — principal em H1/title/URL/meta/1º§/3 H2 |
| Preço-primeiro / lead-herói (`checkpoint_preco_primeiro.py`) | ✅ aprovado | `checkpoints/preco_primeiro.txt` — sem H2 de preço, regra 1 não se aplica |
| Parágrafos / ritmo / citabilidade | ✅ aprovado | `paragrafos.txt`, `ritmo_visual.txt`, `citabilidade.txt` |
| Voz humana (`checkpoint_voz.py`) | ✅ aprovado | `checkpoints/voz.txt` — zero 🔴 e zero 🟡 |
| Completude (`checkpoint_completude.py`) | ✅ aprovado | `checkpoints/completude.txt` — 6 H2, 8 FAQ, 2.373 palavras |
| `[VERIFICAR]` / tokens proibidos (`checkpoint_verificar.py`) | ✅ aprovado | `checkpoints/verificar.txt` — 11 tokens armados, nenhum no texto |
| Varredura anti-doorway final (`checkpoint_doorway_final.py`) | ✅ aprovado | `checkpoints/doorway_final.txt` — **0,0% de sobreposição com Salvador** |
| Registro no banco Supabase | ✅ feito | id 194 · 3 hospitais · 4 links · 8 FAQs |

Legenda: ⬜ pendente · 🟡 rodado, com ressalva · ✅ aprovado (saída em `checkpoints/`)

## Decisões tomadas

- 2026-08-31 — pasta criada, tipo hospital. Skill escolhida pelo `docs/ROTEAMENTO.md`: artigo de hospital → `hapvida-article-builder-v7`.
- 2026-08-31 — `location_code` de Lauro de Freitas descoberto e confirmado no CSV de geotargets do Google Ads (2026-08-12): **1031776**. Salvador é 1001533. Registrar na tabela da skill `dataforseo-tabelaplanos`.
- 2026-08-31 — Labs do DataForSeo (`related_keywords`) **não aceita código de cidade**: usar 2076. Só `serp_local` aceita o código municipal.
- 2026-08-31 — **MODO monomodelo declarado.** A linha de 25 agentes da v7.2 não foi disparada: este ambiente proíbe abrir subagentes sem pedido explícito do usuário. Consequência assumida no state file, seção 10.
- 2026-08-31 — **O ganho de informação foi trocado.** A primeira versão elegeu a divergência de endereço (CNES × Guia Médico) como eixo; o `checkpoint_suficiencia.py` reprovou por defensibilidade 4. Eixo novo: **única porta hospitalar própria do corredor Estrada do Coco**, apoiado no catálogo `consultar_rede` (nível 1). A divergência de endereço virou achado de apoio da HS3.
- 2026-08-31 — **Nenhum número de leito/UTI e nenhum telefone entram no artigo.** O `checkpoint_verificar.py` reprova esses padrões mecanicamente, o que contradiz o card da HS3 descrito em `references/artigo-hospital.md`. A trava mecânica vence. Registrado em `docs/DECISOES.md`.
- 2026-08-31 — Linkagem definida contra `consultar_saturacao_destinos`: coparticipação (58) e carências (53) estão SATURADOS e **não serão linkados**, apesar de `artigo-hospital.md` sugerir. Destinos escolhidos: `plano-hapvida-salvador2` (5), `urgencia-e-emergencia-hapvida` (11), `hapvida-rede-pediatrica` (9), `clinicas-hapvida-por-capital` (9).

## Dados que faltam

Detalhe e onde foi procurado: seção 8 do state file.

- leitos e leitos de UTI — sub-módulo do CNES não renderiza por curl. **Não entram no artigo de todo modo** (trava).
- acreditação ONA, especialidades do corpo clínico, responsável técnico, horário por setor — campos existem no Guia Médico oficial e estão **vazios**.
- existência de maternidade / UTI neonatal — nenhuma fonte primária afirma nem nega. O artigo não afirma nem nega; encaminha a pergunta de parto para a rede de Salvador.
- estacionamento e linhas de ônibus — sem fonte primária.

## Pendências a propor ao usuário (não gravadas no banco)

1. **Catálogo incompleto:** `consultar_rede` não tem a *Clínica Lauro de Freitas II* nem a *Unidade de Autorização Lauro de Freitas*, que existem no Guia Médico oficial. Sugerir `adicionar_unidade_rede`.
2. ~~Possível erro no artigo de Salvador sobre leitos~~ — **RETIRADA em 2026-08-31. Eu estava errado.**
   A ampliação de set/2025 é bem documentada (Correio 24 Horas 30/09, Bahia News, Jornal O Candeeiro,
   com fala de Daniel Bonini, da Hapvida). O dado de Salvador está correto.
2b. **`urgencia-e-emergencia-hapvida` merece nuance:** o box "Importante" afirma que Salvador tem
   "apenas uma unidade hospitalar própria com emergência 24h". É verdade para o município, mas o
   Hospital Lauro de Freitas atende urgência 24h na RMS — para o leitor da região metropolitana a
   frase induz a erro.
2c. **Grafia inconsistente de Teresa/Tereza de Lisieux** entre o catálogo de rede (Tereza), o artigo
   de Salvador (Teresa), a pillar de urgência (Tereza) e a de Feira de Santana (Teresa).
3. **Pauta candidata:** `urgência e emergência hapvida salvador` — existe spoke para Recife, Fortaleza e Goiânia, não para Salvador.
4. Registrar **1031776** na tabela de `location_code` da skill `dataforseo-tabelaplanos`.

## Decisões da redação (2026-08-31)

- **Subtítulo de seção é 15px, não 18px.** O `components.md` traz 18px; o `SKILL.md` e os artigos
  publicados usam 15px. Com 18px o `checkpoint_citabilidade.py` lê o subtítulo como se fosse a
  abertura da seção e reprova todas. Seguido o `SKILL.md`. Registrado em `docs/DECISOES.md`.
- **Travessões reduzidos de 21 para 2.** Era tique de escrita, não estilo. `checkpoint_voz.py`
  fechou com zero avisos.
- **Sumário reancorado.** A primeira varredura anti-doorway reprovou por seção sem âncora local:
  era o sumário, cujos itens não citavam nem o hospital nem a via. Corrigido nos 5 itens.
- **Sem telefone e sem contagem de leitos no corpo** — trava `checkpoint_verificar.py`. O card da
  HS3 encaminha aos canais oficiais e o artigo diz, com todas as letras, por que não publica esses
  números (os campos estão vazios na ficha pública). Isso virou ponto de E-E-A-T, não limitação.

## Correção de rota (2026-08-31, após a 1ª entrega)

Na primeira entrega eu disse que o artigo de Salvador afirmava "20 leitos, 10 de UTI" sem fonte.
**Estava errado.** A ampliação de setembro de 2025 é bem documentada. A HS1 do artigo foi reescrita
para incluí-la (qualitativa e datada, sem contagens, que a trava bloqueia) e a HS2 perdeu a frase
falsa "nenhuma fonte primária confirma esses dados hoje". Travas rerodadas, todas verdes; o
anti-doorway contra Salvador seguiu em **0,0%** mesmo com o fato novo.

## Fio condutor

**O Hospital Lauro de Freitas é a porta 24h do corredor da Estrada do Coco — e a porta mais fácil de errar da rede Hapvida na Bahia.** Do km 2 ao litoral norte, só Camaçari tem outro hospital próprio: quando o caso passa de consulta, ou é aqui, ou é descer para Itaigara. E três unidades da operadora dividem o mesmo nome de cidade em dois números de uma via que tem três nomes — até o AI Overview do Google erra o endereço. O artigo existe para levar a pessoa à porta certa, na hora certa, e só depois falar de plano.
