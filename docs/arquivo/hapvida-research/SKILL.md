---
name: hapvida-research
description: >
  ⚠️ DESCONTINUADA / DEPRECATED — NÃO USAR. Este fluxo de pesquisa (DR1/DR2) foi ABSORVIDO
  pela skill `hapvida-article-builder`, na FASE 0 (ver `references/pesquisa.md` daquela skill),
  agora com motor DataForSeo (serp_local, keyword_data, related_keywords, ranked_keywords) e
  travas anti-alucinação por fase. Esta skill é mantida APENAS como referência histórica. NÃO a
  acione: qualquer pesquisa nova, DR1, DR2, SERP, keyword, FAQ, anti-doorway ou conteúdo de
  cidade/hospital Hapvida deve ser tratado pela `hapvida-article-builder` (Fase 0). Se algo
  acionar esta skill por engano, redirecione imediatamente para `hapvida-article-builder`.
---

> ⚠️ **DESCONTINUADA — NÃO USAR.** Substituída pela **FASE 0** da skill `hapvida-article-builder` (ver `references/pesquisa.md` daquela skill), que funde este DR1/DR2 com DataForSeo e travas anti-alucinação. Este arquivo permanece só como referência histórica. Para qualquer pesquisa nova, usar a builder.

# Hapvida Research Orchestrator

Manages the 2-phase Deep Research workflow for tabelaplanos.com.br articles.

## Before Starting ANY Research

1. **Check the control spreadsheet** via `web_fetch`:
   - URL: `https://docs.google.com/spreadsheets/d/1WuCRtYGTAYxh6j8g8fwZu03xqQr1yyN9IYyO5Qduek4/export?format=csv`
   - Verify if city/topic already has a published article
   - Identify data that CANNOT be repeated
   - List articles for cross-reference
   - If `web_fetch` fails, proceed from conversation context

2. **Check the article database skill** (`hapvida-article-database`):
   - Read `references/database.md` for overlap risks
   - Identify cluster (RMBH, Triângulo MG, Grande SP, etc.)
   - Cross-check FAQ, hospitals, competitors already used

3. **Consult `hapvida-data` skill** for validated corporate data:
   - Copayment values (do NOT research again)
   - National network numbers
   - Qualivida programs
   - Waiting periods
   - Use the correct regional copayment table

## Workflow: 1 Research = 1 Conversation

```
CONVERSATION 1:
├── Classify (TIPO 1 or TIPO 2)
├── Execute DR1 (complete)
├── Generate state file → /mnt/user-data/outputs/
└── END

CONVERSATION 2:
├── User pastes state file
├── Execute DR2 (complete)
├── Anti-doorway validation
├── Generate FINAL file → /mnt/user-data/outputs/
└── READY FOR ARTICLE
```

## Classification Router

```
QUESTION 1: Is the main focus a SPECIFIC CITY?
  YES → TIPO 1 (Geo-localized)
  NO  → QUESTION 2: Is it about a Hapvida procedure/process/coverage?
          YES → TIPO 2 (Educational)
          NO  → OUT OF SCOPE
```

**Ambiguous cases** (city + procedure mentioned): Ask user which is the primary focus.
**Multiple cities:** Ask if separate articles (TIPO 1 each) or panoramic overview (TIPO 2).
**Not about Hapvida:** Flag as out of scope, offer alternatives.

## Research Templates

Read the appropriate template file for detailed instructions:

| Situation | File to read |
|-----------|-------------|
| TIPO 1, starting DR1 | `references/dr1-tipo1.md` |
| TIPO 1, starting DR2 | `references/dr2-tipo1.md` |
| TIPO 2, starting DR1 | `references/dr1-tipo2.md` |
| TIPO 2, starting DR2 | `references/dr2-tipo2.md` |

## City Type Identification (TIPO 1)

| Type | Description | Examples |
|------|-------------|---------|
| Capital with owned network | Major N/NE capitals | Fortaleza, Recife, Salvador, Manaus |
| Capital with credentialed network | SE/S capitals | São Paulo, BH, Curitiba |
| Interior with regional coverage | Mid-size cities | Uberaba, Uberlândia, Anápolis |
| Metropolitan area | Satellite cities | Contagem, Betim, Santo André, Ananindeua |

## Regional Brand Mapping

| Region/City | Brand | Official websites |
|-------------|-------|-------------------|
| North / Northeast | Hapvida | hapvida.com.br |
| Grande SP / RJ | GNDI / NotreDame | gndi.com.br |
| BH / RMBH | GNDI Minas | gndiminas.com.br |
| Curitiba | Clinipam | clinipam.com.br |
| Porto Alegre / RS | CCG Saúde / Weinmann | gndisul.com.br |
| Goiânia / GO | Grupo América | — |

## Critical Rules

1. **SERP:** Minimum 10 organic competitors analyzed (excluding tabelaplanos.com.br)
2. **Anti-doorway:** TIPO 1 needs 10–15 non-substitutable local data points; TIPO 2 needs 10+ Hapvida-exclusive data points
3. **Prices:** NEVER research prices — user inserts via shortcodes
4. **State file:** Always generate after DR1 with continuation prompt
5. **TIPO 1 network mapping:** Map ALL owned units (hospitals, Hapclínicas, PAs 24h, Vida&Imagem) AND the credentialed network
6. **Copayment table:** Table 1 for most cities; Table 2 for SP and BH/RMBH only
7. **Start immediately:** Do not narrate workflow steps before executing — begin research directly

## Excluded Sources

**NEVER use:** tabelaplanos.com.br (any subdomain)

## Mandatory Sources (every research)

- www.hapvida.com.br
- www2.hapvida.com.br/unidades
- ri.hapvida.com.br

## Other Skills to Consult During Research

| Need | Skill |
|------|-------|
| Hapvida corporate data, copayment, products | `hapvida-data` |
| ANS regulation, competitor comparison framework | `hapvida-regulatory` |
| Existing article inventory, FAQ overlap check | `hapvida-article-database` |
| HTML article production (after research) | `hapvida-article-builder` |

## Quick Commands

- **"Nova pesquisa: [city/topic]"** → Classify + start DR1
- **"Continuar" + state file** → Execute DR2
- **"Status"** → Show progress
