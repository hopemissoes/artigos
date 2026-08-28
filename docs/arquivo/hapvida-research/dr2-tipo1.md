# TIPO 1 — Deep Research 2: SEO Positioning & Differentiation

**Prerequisite:** DR1 must be complete. You need SERP analysis, network mapping, local context, and Hapvida presence data.

---

## PART 1: Semantic SEO

### 1.1 Principal Entities (Mandatory)

```yaml
operator:
  name: "Hapvida"
  type: "Organization"
  recommended_mentions: "15-20× in article"
  variations: "[Hapvida NotreDame Intermédica, Grupo Hapvida]"

city:
  name: "[CITY]"
  type: "Place"
  recommended_mentions: "20-30× in article"
  variations: "[Capital of [STATE], Metropolitan Region of...]"

product:
  name: "Plano de Saúde"
  type: "Product/Service"
  recommended_mentions: "10-15×"
  variations: "[convênio médico, plano empresarial, plano individual]"
```

### 1.2 Secondary Entities
Map local entities: main hospital (LocalBusiness), key neighborhoods (Place), ANS (Organization), local Unimed (Organization), concepts (copayment, waiting period, credentialed network).

### 1.3 Gap Analysis vs Competitors
Compare with 10 SERP competitors from DR1:
- Entities competitors have that we don't → action plan
- Entities exclusive to us → leverage
- Topics no one covers → opportunity

### 1.4 Schema Markup Plan
- Primary: FAQPage
- Secondary: LocalBusiness (per hospital/clinic listed), Organization (Hapvida), Product (health plan)

### 1.5 Keywords

```yaml
primary: "plano de saúde hapvida [CITY]"
secondary:
  - "hapvida [CITY] preços" (commercial)
  - "hospitais hapvida [CITY]" (informational)
  - "hapvida [CITY] telefone" (navigational)
  - "hapvida [CITY] emergência" (urgent transactional)
long_tail:
  - "plano hapvida [CITY] para idosos"
  - "hapvida [CITY] cobre [procedure]"
  - "hapvida ou unimed [CITY]"
  - "hapvida [CITY] vale a pena"
```

---

## PART 2: Unique Differentiators (Minimum 3-5)

### Categories of Valid Differentiators
Infrastructure, pioneering, service, history, technology

### For Each Differentiator:
```yaml
category: "[infrastructure/pioneering/service/history/technology]"
title: "[name]"
description: "[3-5 line explanation]"
quantitative_data: "[specific number]"
vs_other_cities: "[how different from SP, BH, etc.]"
vs_competitors: "[how different from local Unimed, Bradesco]"
why_it_matters: "[benefit for user]"
source: "[source]"
suggested_article_phrase: "[how to write it]"
```

### Differentiators by Network Type

**Owned network (N/NE):** Integrated electronic record, automatic emergency authorization, unified care standard, no inter-unit bureaucracy, integrated telemedicine

**Credentialed network (S/SE):** City reference hospitals, geographic flexibility, specialized center partnerships, coverage in premium neighborhoods

### Validation
Each differentiator must pass: "Does another city have this exact same thing?" If yes → not unique enough.
Minimum 3 truly unique differentiators required.

---

## PART 3: Local FAQ (15-20 Questions)

All questions must be based on REAL city data from DR1. Zero generic questions.

### About the Network (5-7 questions)
- Which Hapvida hospitals in [CITY] serve 24h?
- Does [CITY] have a Hapvida emergency room?
- Which Hapvida hospital does deliveries in [CITY]?
- Where is the nearest Hapvida clinic to [CENTRAL NEIGHBORHOOD]?
- Does Hapvida [CITY] have owned or credentialed hospitals?

### About Geographic Coverage (3-5 questions)
- Can I use my Hapvida plan from [CITY] in other cities?
- Does Hapvida serve in the interior of [STATE]?
- Can I use it in [NEIGHBORING METRO CITY]?
- How does Hapvida emergency work outside [CITY]?

### About Differentiators (3-4 questions)
- Why is Hapvida in [CITY] different from [OTHER CAPITAL]?
- Hapvida or Unimed in [CITY]: which to choose?
- What's the advantage of owned network in [CITY]? (if applicable)

### About Contracting (3-4 questions)
- How long to approve a Hapvida plan in [CITY]?
- Does Hapvida accept portability in [CITY]?
- How to schedule a Hapvida appointment in [CITY]?

### FAQ Validation
```yaml
total_questions: [X] (minimum 15)
questions_with_local_data: [X]
generic_questions: [X] (must be 0)
city_swap_test: "If you swap [CITY] for another, do questions lose meaning?" → must be YES
```

---

## PART 4: Anti-Doorway Validation

### 4.1 City Substitution Test
Mentally replace [CITY] with São Paulo throughout the article plan:

| Section | Loses meaning if swapped? | Why |
|---------|--------------------------|-----|
| Network | [Yes/No] | [reason] |
| Local context | [Yes/No] | [reason] |
| Differentiators | [Yes/No] | [reason] |
| FAQ | [Yes/No] | [reason] |

**Target:** 70%+ of content loses meaning when city is swapped.

### 4.2 Unique Data Point Count
List minimum 10 data points that exist ONLY for this city:
1. [unique data point 1]
2. [unique data point 2]
... (minimum 10, target 15)

### 4.3 Generic Phrase Check
**Banned phrases:** "atendimento de qualidade", "equipe qualificada", "melhor custo-benefício", "cobertura completa", "infraestrutura moderna"

If any found → replace with specific data.
Maximum allowed: 0.

### 4.4 Final Result
```yaml
substitution_test: "[PASS/FAIL] — [X]% loses meaning"
unique_data_points: "[PASS/FAIL] — [X] points (min 10)"
generic_phrases: "[PASS/FAIL] — [X] found (max 0)"
overall: "[APPROVED/FAILED]"
```

---

## Output: Final Research File

Generate complete file saved to `/mnt/user-data/outputs/T1_[City]_COMPLETO.md` with all DR1 + DR2 data, plus:

```
═══════════════════════════════════════════
✅ RESEARCH COMPLETE — READY FOR ARTICLE

City: [CITY]
Type: TIPO 1 (Geo-localized)

📊 SUMMARY:
- SERP competitors: 10 analyzed
- Units mapped: [X]
- SEO entities: [X]
- Unique differentiators: [X]
- FAQ: [X] questions
- Unique data points: [X]

✅ ANTI-DOORWAY VALIDATION: APPROVED
- Substitution test: [X]% loses meaning
- Generic phrases: 0

📁 MOVE TO: HAPVIDA_PESQUISAS/COMPLETAS/
File: T1_[City]_COMPLETO.md

🎯 NEXT STEP: Create article (use hapvida-article-builder skill)
═══════════════════════════════════════════
```

Include a ready-to-paste article creation prompt at the end.
