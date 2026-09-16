# ESTADO — hospital-hapvida-maternidade-guarulhos

> Este arquivo é o **ponto de salvamento** do artigo. Quem abrir uma sessão nova
> lê ele primeiro e continua daqui — sem refazer pesquisa nem readivinhar decisão.
> **Atualize ao fim de cada fase, antes de responder ao usuário.**

## Identificação

- **Slug:** hospital-hapvida-maternidade-guarulhos
- **Tipo:** hospital  <!-- city | hospital | tr | pillar | cobertura -->
- **Skill em uso:** hapvida-article-builder-v7
- **Aberto em:** 2026-09-16
- **URL de destino:** /hospital-e-maternidade-guarulhos-hapvida/ (proposta)
- **Keyword principal:** hospital e maternidade guarulhos hapvida (3.600/mês na forma longa) — A CONFIRMAR com o usuário: o hospital mudou de nome para Hospital Keila Ferreira em nov/2025

## Fase atual

- **Fase:** FASE 0 — pesquisa
- **Próximo passo concreto:** DECISÃO DO USUÁRIO sobre a CI-1 (concorrente não lido) e sobre qual
  nome vira a keyword principal. Sem isso a linha não anda — é contrato da skill (V7.3).
- **Bloqueios:** 🔴 CI-1 — as 5 rotas da escada caíram (egress bloqueado; n8n sem autorização OAuth).
  🔴 anti-doorway não pode ser marcado APROVADO enquanto a CI-1 não fechar.

## Portões

| Portão | Status | Evidência |
|---|---|---|
| CI-1 — concorrente lido (`checkpoint_ci1.py`) | 🔴 REPROVADO | `checkpoints/ci1.txt` — 0 de 3 concorrentes lidos |
| FASE 0 (`checkpoint_fase0.py`) | 🟡 1 bloqueio restante | `checkpoints/fase0.txt` — só o anti-doorway, que depende da CI-1 |
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
- 2026-09-16 — pasta criada, tipo hospital (HS1-HS4), skill hapvida-article-builder-v7.
- 2026-09-16 — rede de Guarulhos puxada do catálogo (`consultar_rede`): 5 unidades próprias.
- 2026-09-16 — SERP medida (DataForSeo, Brasil/desktop): o site não aparece no top 20; SERP dominada por
  local_pack e páginas oficiais da operadora; sem featured snippet.
- 2026-09-16 — ACHADO: o hospital foi renomeado para "Hospital Keila Ferreira" em 10-11/11/2025 e recebeu
  a 1ª Sala Lilás da Hapvida. A keyword pedida é o nome antigo.
- 2026-09-16 — artigo de cidade lido no ar (post 31688): ele já cobre o hospital com profundidade incomum
  (card, linha do tempo, 6 FAQs). Risco de doorway ALTO — matriz na seção 15 do state file.
- 2026-09-16 — links: os pillars de coparticipação (63) e carências (56) estão SATURADOS; plano de links
  redesenhado com destinos subutilizados (seção 16 do state file).

## Dados que faltam

- leitos, salas cirúrgicas e UTI do hospital — na ficha CNES 3518809255826 (não pôde ser aberta: egress)
- telefone e horários por setor — site oficial da unidade (não pôde ser aberto)
- fonte primária de "maternidade ativa" — o artigo de cidade afirma, o banco não registra a fonte
- estacionamento, linhas de ônibus, horário de visita — nenhuma fonte alcançável nesta sessão
- leitura das 5 páginas concorrentes (CI-1)

## Fio condutor

Este é o hospital que mudou de nome e ninguém avisou a quem busca. O artigo é a ponte entre os dois
nomes: responde primeiro "é o mesmo hospital, na mesma Av. Tiradentes, 1015" e então conta o que mudou
dentro dele — a Sala Lilás — e o que o paciente precisa saber para ser atendido lá.
