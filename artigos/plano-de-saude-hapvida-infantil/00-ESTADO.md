# ESTADO — plano-de-saude-hapvida-infantil

> Este arquivo é o **ponto de salvamento** do artigo. Quem abrir uma sessão nova
> lê ele primeiro e continua daqui — sem refazer pesquisa nem readivinhar decisão.
> **Atualize ao fim de cada fase, antes de responder ao usuário.**

## Identificação

- **Slug:** plano-de-saude-hapvida-infantil
- **Tipo:** pillar  <!-- city | hospital | tr | pillar | cobertura -->
- **Skill em uso:** hapvida-article-builder-v7
- **Aberto em:** 2026-09-08
- **URL de destino:** https://tabelaplanos.com.br/plano-de-saude-hapvida-infantil/ (MANTER — sem 301)
- **Keyword principal:** plano hapvida infantil (a decidir no DR2: "valor do plano da hapvida infantil" é a de maior clique)

## Fase atual

- **Fase:** FASE P0 concluída → FASE 0 (pesquisa) pendente de início
- **Próximo passo concreto:** CI-1 — ler tabelasaude.com e joov.com.br (os dois
  concorrentes que ranqueiam junto), montar a matriz de cobertura e só então preencher
  `PESQUISA_plano-de-saude-hapvida-infantil_COMPLETO.md` + rodar `checkpoint_fase0.py`
- **Bloqueios:** aguardando aprovação do usuário para seguir da P0 para a FASE 0

## FASE P0 — veredito (2026-09-08) · detalhe em `FASE-P0.md`

- **Causa:** CONTEÚDO. A página é #2 orgânica nas duas keywords-cabeça e é fonte nº 1
  do AI Overview em "valor do plano da hapvida infantil" — mas está abaixo do mínimo do
  arquétipo P1-P9 em 6 itens (7 H2/mín. 8 · 2 H3/mín. 15 · 7 FAQ/mín. 12 · 0 cartão
  fonte-oficial · 0 guia-box · schema sem Person).
- **URL:** MANTER. 8 links internos apontam para ela e o AI Overview a cita pela URL.
  Contraponto registrado: o slug não tem "valor"/"preço", que é o que a demanda pede.
- **Canibalização:** parcial e não bloqueante — `/tabela-de-preco-hapvida/` aparece em
  #9 na mesma SERP em que a página é #2. Vigiar na Fase 5. A home não aparece.
- **Trava da reforma:** a passagem de preço atual é a que a IA extrai. Ampliar, nunca
  substituir o enquadramento.

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
- 2026-09-08 — pasta criada, tipo pillar.

## Dados que faltam

<!-- o que ficou como [VERIFICAR] ou nao_encontrado, e onde procurar -->

## Fio condutor

<!-- 2-3 linhas: a voz e o ângulo único deste artigo (Agente 5). Todos os blocos
     honram isto. Preencher ao fim da FASE 0. -->
