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

- **Fase:** FASE 0 — pesquisa CONCLUÍDA, aguardando aprovação humana
- **Próximo passo concreto:** o usuário aprovar o state file. Só então:
  Estágio 2.5 (`checkpoint_suficiencia.py` + juízes 23/24) e Bloco A.
- **Bloqueios:** portão humano do state file (obrigatório, YMYL)

## Portões

| Portão | Status | Evidência |
|---|---|---|
| CI-1 — concorrente lido (`checkpoint_ci1.py`) | ✅ aprovado | `checkpoints/ci1.txt` — 5 concorrentes lidos, rota curl |
| FASE 0 (`checkpoint_fase0.py`) | ✅ aprovado | `checkpoints/fase0.txt` — APROVADO, 1 aviso |
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

## Fio condutor

Divinópolis não tem rede espalhada: tem um campus. Hospital, centro clínico e
diagnóstico da Hapvida ficam no mesmo número da Rua Pedro Ferreira do Amaral,
no Padre Libério, mais um ponto no Centro — e é isso que decide se o plano
serve para você, porque muda o deslocamento, não a mensalidade. O artigo
responde a uma pergunta prática: onde você vai ser atendido, de fato, nesta
cidade — e por que o guia médico que aparece primeiro no Google leva a
endereços de Belo Horizonte.
