# ESTADO — {{SLUG}}

> Este arquivo é o **ponto de salvamento** do artigo. Quem abrir uma sessão nova
> lê ele primeiro e continua daqui — sem refazer pesquisa nem readivinhar decisão.
> **Atualize ao fim de cada fase, antes de responder ao usuário.**

## Identificação

- **Slug:** {{SLUG}}
- **Tipo:** {{TIPO}}  <!-- city | hospital | tr | pillar | cobertura -->
- **Skill em uso:** hapvida-article-builder-v7
- **Aberto em:** {{DATA}}
- **URL de destino:** [X]
- **Keyword principal:** [X]

## Fase atual

- **Fase:** FASE 0 — pesquisa
- **Próximo passo concreto:** preencher `PESQUISA_{{SLUG}}_COMPLETO.md` e rodar o
  `checkpoint_fase0.py`
- **Bloqueios:** nenhum

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
- {{DATA}} — pasta criada, tipo {{TIPO}}.

## Dados que faltam

<!-- o que ficou como [VERIFICAR] ou nao_encontrado, e onde procurar -->

## Fio condutor

<!-- 2-3 linhas: a voz e o ângulo único deste artigo (Agente 5). Todos os blocos
     honram isto. Preencher ao fim da FASE 0. -->
