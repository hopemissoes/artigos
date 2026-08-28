# TIPO 2 — Deep Research 2: Differentiation & SEO

**Prerequisite:** DR1 must be complete. You need SERP analysis, medical data, Hapvida process, and ANS coverage.

---

## PART 1: Competitor Comparison

**Consult `hapvida-regulatory` skill** (`references/competitors.md`) for search strategies and comparison framework.

### Map Each Competitor

For Unimed, Bradesco Saúde, SulAmérica, and Amil:
```yaml
coverage: "[Yes/No/Partial]"
process: "[how it works at this operator]"
network: "[type]"
copayment: "[known values]"
average_timeline: "[if available]"
differentiator: "[main advantage]"
disadvantage_vs_hapvida: "[main disadvantage]"
source: "[source]"
```

### Comparison Table
```yaml
criteria_coverage:    hapvida: "..." | unimed: "..." | bradesco: "..." | sulamerica: "..."
criteria_user_cost:   hapvida: "R$ X copayment" | ...
criteria_network:     hapvida: "owned NE / credentialed SE" | ...
criteria_timeline:    hapvida: "[X days]" | ...
criteria_technology:  hapvida: "[app, telemedicine, command center]" | ...
```

### Consultive Analysis
```yaml
when_choose_hapvida:
  - situation: "[situation 1]"
    reason: "[why Hapvida is better here]"
  # 2-3 situations

when_consider_others:
  - situation: "[situation 1]"
    alternative: "[which operator]"
    reason: "[why]"
  # 1-2 situations

comparison_conclusion: "[balanced 2-3 line summary]"
```

---

## PART 2: Semantic SEO

### 2.1 Principal Entities
```yaml
operator: "Hapvida" (Organization, 15-20×)
procedure: "[TOPIC]" (MedicalProcedure/Service/Process, 15-25×, include synonyms + technical + layman terms)
regulator: "ANS" (Organization, 3-5×)
```

### 2.2 Secondary Entities
Medical specialties, conditions, medical societies, Ministry of Health, concepts (copayment, waiting period, prior authorization), Qualivida programs.

### 2.3 Gaps vs SERP Competitors
- Missing entities → include
- Uncovered topics → opportunity
- Hapvida-exclusive data → leverage

### 2.4 Schema Markup
- Primary: FAQPage
- Secondary: HowTo (step-by-step), MedicalWebPage, Article

### 2.5 Keywords
```yaml
primary: "[procedure] hapvida"
secondary:
  - "[procedure] plano de saúde"
  - "hapvida cobre [procedure]"
  - "como funciona [procedure] hapvida"
  - "quanto custa [procedure] hapvida"
  - "carência [procedure] hapvida"
long_tail:
  - "[procedure] pelo plano hapvida como funciona"
  - "hapvida cobre [procedure] com coparticipação"
  - "[procedure] hapvida vs unimed"
```

---

## PART 3: Exclusive Hapvida Differentiators (Minimum 3-5)

### For Each Differentiator:
```yaml
title: "[name]"
category: "[process/technology/cost/program/network]"
description: "[2-3 lines]"
quantitative_data: "[number/statistic]"
vs_competitors: "[how others do it differently]"
user_benefit: "[what beneficiary gains]"
source: "[source]"
# ANTI-DOORWAY TEST:
works_if_swap_hapvida: "[Yes = bad / No = good]"
```

### Validation
Total identified → minimum 3 that are truly Hapvida-exclusive (fail the swap test).

---

## PART 4: Process FAQ (15-20 Questions)

**Anti-doorway internal rule:** Questions about PROCESSES, not locations. Do NOT ask "Which hospital in [CITY]?" DO ask "How does authorization work at Hapvida?"

### About Coverage (4-5 questions)
- Does Hapvida cover [procedure]?
- What's the waiting period for [procedure] at Hapvida?
- Does [procedure] have copayment at Hapvida? → specific value
- Is prior authorization needed for [procedure] at Hapvida?

### About Process (4-5 questions)
- How to request [procedure] through Hapvida?
- How long to get [procedure] at Hapvida? → specific timeline
- Can I do [procedure] through the Hapvida app?
- What if Hapvida denies [procedure]?

### About Costs (3-4 questions)
- How much does [procedure] cost through Hapvida? → total copayment
- What's the savings doing [procedure] via Hapvida vs private?
- Is [procedure] at Hapvida cheaper than at Unimed?

### About Network (2-3 questions)
- Does Hapvida do [procedure] at owned or credentialed hospitals?
- Can I choose where to do [procedure] through Hapvida?

### Cross-Reference Question (mandatory, 1)
- Where to do [procedure] through Hapvida in my city?
  → Answer: "For hospital list in your city, see our specific guides: [links to TIPO 1 articles]"
  → Do NOT answer with hospital list — redirect to TIPO 1

### FAQ Validation
```yaml
total_questions: [X] (minimum 15)
process_questions: [X]
location_questions: [X] (must be 0 or 1 with redirect)
all_have_hapvida_data: [Yes/No]
doorway_internal_test: "Any question duplicates TIPO 1 content?" → must be No
```

---

## PART 5: Anti-Doorway Validation

### 5.1 External Anti-Doorway (vs Other Operators)
Mentally replace "Hapvida" with "Unimed":

| Section | Loses meaning? | Exclusive data |
|---------|---------------|----------------|
| Step-by-step process | [Yes/No] | [which data] |
| Copayment | [Yes/No] | [specific values] |
| Programs | [Yes/No] | [Qualivida, etc.] |
| Comparison | [Yes/No] | — |

**Target:** 70%+ loses meaning. Result: [PASS/FAIL]

### 5.2 Internal Anti-Doorway (vs TIPO 1 Articles)
| Check | Present? | Action |
|-------|----------|--------|
| Lists hospitals with city-specific addresses? | [Yes/No] | Remove if yes |
| Price table by city? | [Yes/No] | Remove if yes |
| Focuses on ONE city only? | [Yes/No] | Fix if yes |
| Location FAQ without redirect? | [Yes/No] | Add redirect |

Cross-reference included: [Yes/No]
TIPO 1 articles linked: [list]
Result: [PASS/FAIL]

### 5.3 Exclusive Hapvida Data Count
List minimum 10:
1. [specific copayment value]
2. [process step with differentiator]
3. [Qualivida program]
4. [Command Center]
5. [owned network specific timeline]
6. [quantitative comparison]
7. [technology/app]
8-10. [more exclusive data]

Result: [PASS/FAIL] — [X]/10 minimum

### 5.4 Final Result
```yaml
external_anti_doorway: "[PASS/FAIL]"
internal_anti_doorway: "[PASS/FAIL]"
exclusive_data: "[PASS/FAIL]"
overall: "[APPROVED/FAILED]"
```

---

## Output: Final Research File

Save to `/mnt/user-data/outputs/T2_[Topic]_COMPLETO.md` with all DR1 + DR2 data, plus:

```
═══════════════════════════════════════════
✅ RESEARCH COMPLETE — READY FOR ARTICLE

Topic: [TOPIC]
Type: TIPO 2 (Educational)

📊 SUMMARY:
- SERP competitors: 10 analyzed
- Operators compared: 4
- SEO entities: [X] mapped
- Exclusive differentiators: [X]
- FAQ: [X] questions
- Exclusive Hapvida data: [X]

✅ ANTI-DOORWAY VALIDATION:
- External (vs operators): APPROVED ([X]%)
- Internal (vs TIPO 1): APPROVED
- Exclusive data: [X]/10

🔗 CROSS-REFERENCE TO TIPO 1:
- [List city articles to link]

🎯 NEXT STEP: Create article (use hapvida-article-builder skill)
═══════════════════════════════════════════
```

Include ready-to-paste article creation prompt.
