# ESTADO — hapclinica-duque-de-caxias-manaus

> Este arquivo é o **ponto de salvamento** do artigo. Quem abrir uma sessão nova
> lê ele primeiro e continua daqui — sem refazer pesquisa nem readivinhar decisão.
> **Atualize ao fim de cada fase, antes de responder ao usuário.**

## Identificação

- **Slug:** hapclinica-duque-de-caxias-manaus
- **Tipo:** hospital (unidade ambulatorial — arquétipo HS1-HS4)  <!-- city | hospital | tr | pillar | cobertura -->
- **Skill em uso:** hapvida-article-builder-v7
- **Aberto em:** 2026-08-31
- **URL de destino:** https://tabelaplanos.com.br/hapclinica-duque-de-caxias-manaus/
- **Keyword principal:** hapclinica duque de caxias (6.600/mês, KD 0, navigational)

## Fase atual

- **Fase:** portão humano APROVADO em 2026-08-31. Linha multiagente da v7.2
  autorizada e disparada. **Estágio 2 em curso** (agentes 6, 7, 23 e 24).
- **Próximo passo concreto:** revisar as quatro saídas do Estágio 2. Liberado o
  portão de pesquisa, disparar o Estágio 3 (redatores 8, 9 e 10).
- **Bloqueios:** nenhum. Nenhum HTML pode ser escrito até 23 e 24 liberarem.

## Portões

| Portão | Status | Evidência |
|---|---|---|
| CI-1 — concorrente lido (`checkpoint_ci1.py`) | ✅ aprovado | `checkpoints/ci1.txt` — 4 lidos por WebFetch |
| FASE 0 (`checkpoint_fase0.py`) | ✅ aprovado | `checkpoints/fase0.txt` |
| Aprovação humana do state file | ✅ aprovado | usuário, 2026-08-31 |
| Roteamento de modelos (`checkpoint_modelos.py`) | ✅ aprovado | `checkpoints/modelos.txt` — 4 modelos distintos |
| Portão de pesquisa (agentes 23 e 24) | 🟡 em curso | |
| Suficiência (`checkpoint_suficiencia.py`) | ✅ aprovado | `checkpoints/suficiencia.txt` — reprovou na 1ª e passou após correção |
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
- 2026-08-31 — pasta criada, tipo hospital (unidade).
- 2026-08-31 — **alvo trocado por decisão do usuário (Rota B)**: o pedido original era
  Duque de Caxias/RJ, mas a keyword dos 6.600/mês é da unidade de **Manaus**. Registro
  em `ACHADO-BLOQUEANTE.md`.
- 2026-08-31 — arquétipo definido: unidade HS1-HS4, e **não** artigo de cidade. A
  unidade é uma policlínica ambulatorial, não um hospital.
- 2026-08-31 — ficha CNES 9505970 obtida em fonte primária oficial
  (`apidadosabertos.saude.gov.br`). Ela prova ausência de centro cirúrgico, centro
  obstétrico, centro neonatal, atendimento hospitalar e SUS. É o eixo do artigo.
- 2026-08-31 — coparticipação de Manaus confirmada na faixa `demais_capitais`
  (consulta R$ 25,42 · exame simples R$ 45,79 · exame complexo R$ 114,48).
- 2026-08-31 — links de coparticipação (58) e carência (53) **excluídos do plano por
  saturação**; substituídos por `o-que-e-plano-ambulatorial-2` (8, normal).
- 2026-08-31 — `checkpoint_suficiencia` reprovou na 1ª rodada (FAQ sem âncora local,
  2 secundárias de intenção de quem já é cliente, ganho sem nível, diferenciais
  genéricos). Corrigido de verdade e aprovado na 2ª.

## Dados que faltam

Dois itens a confirmar antes de publicar (estão em `nao_encontrado`/VERIFICAR):

1. **Coleta laboratorial própria** — o CNES registra serviço de apoio, o que é
   compatível, mas não nomeia coleta. Confirmar pelo 4002-3633.
2. **Linha de ônibus 542** — veio de agregador de transporte, não de fonte primária.

Não citar, em nenhuma hipótese: lista de especialidades (os diretórios se
contradizem), ano de inauguração, nome de médico e estacionamento — todos sem fonte.

## Fio condutor

O roteiro do paciente da Praça 14. Esta é a porta de entrada ambulatorial da rede
Hapvida em Manaus — e a ficha oficial do CNES prova, campo a campo, tudo o que ela
**não** faz: sem centro cirúrgico, sem centro obstétrico, sem centro neonatal, sem
internação e sem SUS. Toda a SERP para no endereço; este artigo é o único que diz
para onde ir quando o caso não é de ambulatório.
