# ACHADO BLOQUEANTE — FASE 0 interrompida antes do DR1 fechar

**Data:** 2026-08-31 · **Skill:** hapvida-article-builder-v7 · **Fase:** 0.1 (DR1), parcial

Este arquivo existe porque a FASE 0 encontrou, logo na Parte 1 (SERP real), um fato que
**derruba a premissa do pedido**. A skill manda parar e avisar em vez de seguir — é a
lição registrada em `docs/DECISOES.md` (2026-08-27: limitação de coleta não vira nota de
rodapé). Nada de HTML até o portão humano decidir o rumo.

---

## 1. O fato: a "Hapclínica Duque de Caxias" dos 6.600/mês fica em MANAUS

A keyword que originou o pedido **não é do município de Duque de Caxias/RJ**. Ela é da
**Hapclínica da Avenida/Rua Duque de Caxias, 1905 — Praça 14 de Janeiro, Manaus/AM**.

Três fontes independentes, coletadas em 2026-08-31:

| Fonte | Evidência |
|---|---|
| `serp_local` (DataForSeo, mobile, depth 20, location 2076) | Knowledge Graph na posição 1: **"Hapclínica Duque de Caxias — Centro médico em Manaus, Amazonas"** (cid 11236428093663763165, 247 avaliações, nota 3,1) |
| SERP orgânica | 8 dos 10 primeiros resultados são de Manaus: doctoralia "Hapclínica Duque de Caxias - **Manaus/Am**"; Waze "Av. Duque de Caxias, 1905 **Manaus**"; Moovit "ônibus linha 542 **Manaus**"; econodata CNPJ 63.554.067/0197-00 "Avenida Duque de Caxias, 1905 - Praça 14 de Janeiro, **Manaus - AM**, 69.020-141"; reclameaqui "hapclinica Duque de Caxias **da cidade de Manaus**"; dentmap "Praça 14, **Manaus**". O image pack inteiro é "Plano Hapvida **Manaus**". |
| `consultar_rede` (banco Supabase — dado proprietário, nível 1) | id 10 — **"Clínica Duque de Caxias", Rua Duque de Caxias, 1905 - Praça 14 de Janeiro, Manaus - AM**, tipo Clínica, `faz_imagem: true` |

**Consequência:** um artigo sobre o município de Duque de Caxias/RJ mirando essa keyword
não ranquearia (intenção é achar a unidade de Manaus), e seria uma página enganosa — o
oposto do que o anti-doorway protege.

---

## 2. A demanda real, medida (DataForSeo, location_code 2076, 2026-08-31)

| Keyword | Volume/mês | KD | Intenção | Onde está a demanda |
|---|---|---|---|---|
| `hapclinica duque de caxias` | **6.600** | 0 | navigational | **Manaus/AM** |
| `hapvida duque de caxias` | 1.900 | 0 | informational | poluída: Manaus + Fortaleza (há Av. Duque de Caxias nas duas) + RJ |
| `centro clinico duque de caxias` | **720** | 0 | **navigational** | **Duque de Caxias/RJ** (nomenclatura GNDI) |
| `plano de saude duque de caxias` | 90 | 0 | informacional/comercial | Duque de Caxias/RJ |
| `plano hapvida duque de caxias` | **0** (`items_count: 0`) | — | — | não existe |

Salto histórico da `hapclinica duque de caxias`: ~590/mês até out/2023 → 5.400 em nov/2023
→ 6.600 desde então. A unidade de Manaus mudou de patamar ali.

**Leitura:** o padrão `plano-hapvida-<cidade>` que o repo usa **não tem público** em Duque
de Caxias/RJ. Pela Regra de Prioridade da FASE 0 (`references/pesquisa.md`, DR2 1.3),
keyword de volume ~0 **não vira título nem H2** — é vaidade.

---

## 3. O risco de doorway que o usuário levantou é REAL — e é triplo

O `plano-hapvida-rio-de-janeiro` (id 28) **já cobre Duque de Caxias por dentro**:

- lista as **duas** unidades de DC entre seus hospitais próprios:
  - "Hospital do Coração Duque de Caxias" (R. Marechal Floriano, 117)
  - "Centro Clínico Duque de Caxias" (R. Prof. José de Souza Herdy, 1216)
- tem a **FAQ nº 9 inteira** dedicada: *"A Hapvida atende na Baixada Fluminense?"*,
  respondida exatamente com essas duas unidades;
- já **linka** para `hospital-duque-de-caxias-hapvida` na seção `#rede`.

E o `hospital-duque-de-caxias-hapvida` (id 130, V4.6.0) já esgota o Hospital do Coração:
HS1-HS4, 7 FAQs, seção de desambiguação vs. o hospital público homônimo (HMCOR São José),
`cluster_slug: rio-de-janeiro`.

**Conclusão:** um "artigo de cidade" para Duque de Caxias/RJ teria como rede assistencial
inteira 2 unidades — ambas já descritas no artigo do Rio, uma delas com artigo próprio.
Seria doorway por construção, não por descuido. A preocupação do usuário estava certa,
e a causa é mais profunda do que ele supunha.

---

## 4. O que sobra de legítimo (as duas rotas com dado)

### Rota A — Centro Clínico Duque de Caxias/RJ (unidade, arquétipo HS1-HS4)
- **720/mês, KD 0, competição 0,04, intenção navigational, ~0 backlinks** na SERP.
- É a **única unidade de DC/RJ sem artigo próprio**. No artigo do Rio ela é uma linha; no
  artigo do Hospital ela aparece só como contraste ("NÃO confundir").
- Anti-doorway limpo por construção: o eixo é ambulatorial (consulta, exame, agendamento,
  especialidades, horário 8h-18h) — o oposto do eixo do Hospital do Coração
  (urgência 24h, internação) e do eixo do artigo do Rio (comprar plano).
- Ocupantes atuais da busca: só diretório (Waze, gndi.com.br, doctoralia). Nenhuma
  página de conteúdo. É a lacuna mais barata do cluster RJ.

### Rota B — Hapclínica Duque de Caxias/Manaus (unidade, arquétipo HS1-HS4)
- **6.600/mês, KD 0, intenção navigational** — o volume que o usuário viu.
- `tabelaplanos.com.br` **já ranqueia em 13º** nessa busca com
  `/clinicas-hapvida-por-capital/` (id 147), cujo snippet já cita "Praça 14 de Janeiro
  (Duque de Caxias)". Ou seja: o site já tangencia a keyword sem nunca ter mirado nela.
- ⚠️ **Risco de canibalização a tratar na FASE 0**: uma página nova dedicada disputaria
  com a `clinicas-hapvida-por-capital` e com `plano-hapvida-manaus` (id 47). Exige
  `consultar_saturacao_destinos` + desenho de fronteira antes de aprovar.
- Não é o que o usuário pediu (é Manaus, não Duque de Caxias) — decisão dele.

---

## 5. Estado da FASE 0

| Parte | Status |
|---|---|
| Pré-requisitos — banco consultado (`listar_artigos`, `consultar_artigo` ×2, `consultar_rede` ×2, `consultar_overlaps_doorway`) | ✅ feito |
| Parte 1 — SERP real (`serp_local` mobile, principal) | ✅ feito (1 keyword) |
| Parte 1 — SERP desktop + secundárias | ⬜ pendente (depende do alvo escolhido) |
| Parte 2 — rede (catálogo ✅ / guia oficial / CNES / Maps) | 🟡 só o catálogo |
| Partes 3-8, DR2 inteiro, CI-1, CI-2 | ⬜ pendentes |

**Bloqueio:** o alvo do artigo não está definido. Escolher entre Rota A e Rota B (ou
descartar as duas) é decisão do usuário, não da máquina — muda cidade, arquétipo, slug,
kit on-page e a fronteira anti-doorway inteira.
