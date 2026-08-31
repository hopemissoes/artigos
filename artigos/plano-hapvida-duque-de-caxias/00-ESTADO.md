# ESTADO — plano-hapvida-duque-de-caxias

> Este arquivo é o **ponto de salvamento** do artigo. Quem abrir uma sessão nova
> lê ele primeiro e continua daqui — sem refazer pesquisa nem readivinhar decisão.
> **Atualize ao fim de cada fase, antes de responder ao usuário.**

## Identificação

- **Slug:** plano-hapvida-duque-de-caxias
- **Tipo:** city  <!-- city | hospital | tr | pillar | cobertura -->
- **Skill em uso:** hapvida-article-builder-v7
- **Aberto em:** 2026-08-31
- **URL de destino:** [X]
- **Keyword principal:** [X]

## Fase atual

- **Fase:** FASE 0 — pesquisa (DR1 parcial) — **INTERROMPIDA no portão humano**
- **Próximo passo concreto:** o usuário escolhe o alvo (Rota A / Rota B / descartar) —
  ver `ACHADO-BLOQUEANTE.md`. Só depois o DR1 continua.
- **Bloqueios:** 🔴 a keyword do pedido ("hapclinica duque de caxias", 6.600/mês) é de
  **Manaus/AM**, não de Duque de Caxias/RJ. E `plano hapvida duque de caxias` tem volume
  ZERO. O alvo do artigo não está definido — slug, arquétipo e cidade dependem disso.

## Portões

| Portão | Status | Evidência |
|---|---|---|
| CI-1 — concorrente lido (`checkpoint_ci1.py`) | ⬜ pendente | |
| FASE 0 (`checkpoint_fase0.py`) | ⬜ pendente | |
| Aprovação humana do state file | ⬜ pendente | |
| Suficiência (`checkpoint_suficiencia.py`) | ⬜ pendente | |
| Kit on-page (`checkpoint_onpage.py`) | ⬜ pendente | |
| Preço-primeiro / lead-herói (`checkpoint_preco_primeiro.py`) | ⬜ pendente | |
| Voz humana (`checkpoint_voz.py`) | ⬜ pendente | |
| Completude (`checkpoint_completude.py`) | ⬜ pendente | |
| `[VERIFICAR]` / tokens proibidos (`checkpoint_verificar.py`) | ⬜ pendente | |
| Varredura anti-doorway final (`checkpoint_doorway_final.py`) | ⬜ pendente | |
| Registro no banco Supabase | ⬜ pendente | |

Legenda: ⬜ pendente · 🟡 rodado, com ressalva · ✅ aprovado (saída em `checkpoints/`)

## Decisões tomadas

<!-- uma linha por decisão, com data. Serve para a próxima sessão não reabrir. -->
- 2026-08-31 — pasta criada, tipo city. **O slug é provisório** e provavelmente muda:
  depende da rota escolhida (`centro-clinico-duque-de-caxias-hapvida` na Rota A,
  `hapclinica-duque-de-caxias-manaus` na Rota B).
- 2026-08-31 — FASE 0 medida: `hapclinica duque de caxias` = 6.600/mês mas é **Manaus**
  (Knowledge Graph + 8/10 da SERP + `consultar_rede` id 10). Fonte tripla, em
  `ACHADO-BLOQUEANTE.md`.
- 2026-08-31 — `plano hapvida duque de caxias` = `items_count: 0`. Pela regra de
  prioridade da FASE 0, não pode virar título nem H2. Artigo de cidade no padrão do repo
  está descartado por falta de público.
- 2026-08-31 — doorway confirmado no banco: o `plano-hapvida-rio-de-janeiro` (id 28) já
  lista as 2 unidades de DC e tem FAQ própria da Baixada; o `hospital-duque-de-caxias-hapvida`
  (id 130) já esgota o Hospital do Coração. Sobra apenas o **Centro Clínico** como eixo livre.

## Dados que faltam

- Tudo do DR1 a partir da Parte 2 (guia oficial, CNES, Maps) e o DR2 inteiro — a coleta
  parou de propósito no portão humano, para não pesquisar a cidade errada.
- CI-1 (leitura de concorrente) não iniciada. Egress testado em 2026-08-31: curl alcança
  os 5 alvos; o WebFetch ainda não foi provado nesta sessão.

## Fio condutor

<!-- 2-3 linhas: a voz e o ângulo único deste artigo (Agente 5). Todos os blocos
     honram isto. Preencher ao fim da FASE 0. -->
