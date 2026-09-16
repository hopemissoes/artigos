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
- **Próximo passo concreto:** PORTÃO HUMANO nº 2 — as 2 rodadas de juízes da pesquisa se esgotaram.
  O juiz P-B liberou (9/9/9/8). O juiz P-A ficou em 7/7/8/7 e apontou 2 achados vermelhos, os dois já
  corrigidos no state file. A skill manda escalar ao humano quando as 2 rodadas acabam: a decisão de
  seguir para a redação é do usuário.
- **Bloqueios:** nenhum mecânico no artigo novo. **Mas há um achado que afeta conteúdo JÁ PUBLICADO:**
  o Hospital N. Sra. do Rosário (Vila Maria) encerrou maternidade e PS de ginecologia e obstetrícia em
  06/10/2025, e a FAQ 2 do artigo de cidade de Guarulhos ainda manda gestante de alto risco para lá.
  O banco já registrava o mesmo problema na FAQ 6 do pillar `plano-hapvida-sao-paulo2`. É correção de
  site, não deste artigo — e depende de autorização expressa do usuário (REGRA ZERO).

## Portões

| Portão | Status | Evidência |
|---|---|---|
| CI-1 — concorrente lido (`checkpoint_ci1.py`) | ✅ APROVADO | `checkpoints/ci1.txt` — 5 concorrentes lidos pela rota n8n |
| FASE 0 (`checkpoint_fase0.py`) | ✅ APROVADO | `checkpoints/fase0.txt` — 0 bloqueios, 1 aviso |
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
- 2026-09-16 — CI-1 DESTRAVADA pela rota 4: o MCP `SEO - Hapvida` (n8n) ficou disponível e o workflow
  `i0jtkZgMawCjqYHk` leu 7 páginas no servidor, fora do egress. 5 concorrentes lidos + ficha CNES.
- 2026-09-16 — decisão do usuário: keyword principal = ponte entre o nome antigo e o novo.
- 2026-09-16 — FASE 0 e CI-1 aprovadas nos checkpoints; portão humano nº 1 aprovado pelo usuário.
- 2026-09-16 — juízes da pesquisa, rodada 1: os dois BLOQUEARAM (10 achados vermelhos somados).
- 2026-09-16 — refino rodada 1: 3ª coleta pelo n8n, HS3 e HS4 deixam de ser órfãs, FAQ reescrita com fonte,
  113 leitos reclassificado como cadeia única de divulgação, reconciliação com o artigo de cidade.
- 2026-09-16 — juízes, rodada 2: P-B LIBEROU (9/9/9/8, zero vermelhos); P-A BLOQUEOU (7/7/8/7, 2 vermelhos).
- 2026-09-16 — artigo escrito (redator opus), editor-chefe (fable) costurou, 4 auditorias rodaram em
  modelos distintos: voz 🟢, veracidade 🟡, anti-doorway 🟡, GEO pendente.
- 2026-09-16 — 🔴 ACHADO DO ANTI-DOORWAY, confirmado no banco: o Rosário encerrou a maternidade em
  06/10/2025. O artigo novo mandava gestante de alto risco para lá (seguindo o artigo de cidade).
  Corrigido: agora o texto avisa do encerramento e manda confirmar a maternidade de referência no pré-natal.
- 2026-09-16 — os 2 vermelhos do P-A foram corrigidos: (a) apagado o bloco de distâncias que eu havia
  atribuído ao CNES sem estar no CNES; (b) escrita a reconciliação da urgência ortopédica com a FAQ 9 do
  artigo de cidade. Mais 5 amarelos (HS4 vira inferência declarada, Sala Lilás 24h atribuída, 0800 certo
  para a região, diferencial trocado, fonte "Joi" com URL).

## Dados que faltam

- horário de visita, acompanhante e o que levar para internar — ninguém publica (nem CNES, nem operadora)
- estacionamento e linhas de ônibus da Av. Tiradentes, 1015 — não confirmado
- telefone: CNES diz 11 3155-2000, a operadora diz (11) 2463-8610 — dois números, nenhum entra no artigo
- horário do pronto-socorro: o CNES registra PS obstétrico/pediátrico/ortopédico, mas não diz 24h
- certificação ONA — não consta em nenhuma fonte lida

## Fio condutor

Este é o hospital que mudou de nome e ninguém avisou a quem busca. O artigo é a ponte entre os dois
nomes: responde primeiro "é o mesmo hospital, na mesma Av. Tiradentes, 1015" e então conta o que mudou
dentro dele — a Sala Lilás — e o que o paciente precisa saber para ser atendido lá.
