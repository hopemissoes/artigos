# TIPO 2 — Deep Research 1: Topic Data Collection

Execute all parts in a single research session. Generate state file at the end.

**Anti-doorway internal rule:** Do NOT list hospitals by specific city. Do NOT create price tables by city. Focus on NATIONAL processes. When mentioning a city, use MULTIPLE as examples.

### Identify Subcategory First
- A. Medical Procedure (surgery, exam, treatment)
- B. Administrative Process (portability, authorization, reimbursement)
- C. Coverage/Rights (what's covered, waiting periods)
- D. Program/Service (Qualivida, telemedicine)
- E. Comparison (Hapvida vs competitor)

---

## PART 1: SERP Analysis (10 Competitors)

### Searches to Execute
```
1. "[procedure/topic] hapvida"
2. "[procedure/topic] plano de saúde"
3. "como funciona [procedure/topic] plano de saúde"
4. "[procedure/topic] cobertura ANS"
5. "quanto custa [procedure/topic] particular"
```

### For EACH of the 10 Top Results:
```yaml
position: [1-10]
url: "[URL]"
title: "[title]"
domain: "[site.com.br]"
content_type: "[guide/tutorial/institutional/blog]"
h1: "[H1]"
main_h2s: ["H2 1", "H2 2"]
strengths: ["what they do well"]
weaknesses: ["what's missing"]
has_hapvida_data: "[Yes/No — which]"
is_doorway_page: "[Yes/No]"
opportunity: "[how we outperform]"
```

### SERP Synthesis
- Types: guides, tutorials, institutionals, superficial blogs
- How many have operator-specific data: __/10
- Doorway pages: __/10
- 5+ gaps identified
- Hapvida-specific opportunities

---

## PART 2: Official Medical Data

### Sources (mandatory)
- Ministry of Health (gov.br/saude)
- WHO (who.int)
- Brazilian medical societies
- IBGE (demographics)

### Definition & Epidemiology
```yaml
definition: "[clear, accessible definition — 2-3 sentences]"
source: "[official source + URL]"

brazil_epidemiology:
  prevalence: "[X million people / X% of population]"
  most_affected_age_group: "[data]"
  trend: "[increasing/stable/decreasing]"
  source: "[source + year]"

context:
  why_important: "[impact on people's lives]"
  consequences_without_treatment: "[what happens if untreated]"
```

### Symptoms & Indications
List 5-8 main symptoms with brief explanations + urgency signs. Cite medical society source.

### Types of Procedure/Treatment
```yaml
type_1:
  name: "[name/technique]"
  description: "[how it works]"
  duration: "[average time]"
  hospitalization: "[yes/no — how long]"
  recovery: "[recovery time]"
  indication: "[when indicated]"
# Document 2-4 types with medical society source
```

---

## PART 3: Hapvida-Specific Data

### 3.1 National Operational Pattern

**Do NOT detail city by city. Focus on PATTERNS.**

```yaml
owned_network:
  where: "[regions/states]"
  example_cities: "[Fortaleza, Recife, Salvador, Manaus — multiple]"
  how_it_works: "[automatic authorization, integrated record]"

credentialed_network:
  where: "[regions]"
  example_cities: "[São Paulo, BH, Curitiba — multiple]"
  how_it_works: "[standard ANS authorization process]"

practical_difference:
  owned_authorization: "[X days / automatic]"
  credentialed_authorization: "[X business days]"
```

### 3.2 Applicable Copayment
```yaml
procedure_classification: "[consultation/simple exam/complex exam/therapy/surgery]"
applicable_values:
  pre_consultation: "R$ [value]"
  exams: "R$ [value] ([classification])"
  main_procedure: "R$ [value] or N/A"
  follow_up: "R$ [value]"
estimated_total_cost: "R$ [X] to R$ [Y]"
vs_private:
  private_average: "R$ [X] to R$ [Y]"
  savings_percentage: "[X]%"
  private_price_source: "[source]"
```

**Get copayment values from `hapvida-data` skill — do NOT research these.**

### 3.3 Step-by-Step Process at Hapvida
```yaml
step_1:
  name: "[step name]"
  how: "[description]"
  where: "[app, phone, unit]"
  timeline: "[time]"
  cost: "[copayment if applicable]"
  hapvida_differentiator: "[what's unique at Hapvida]"
# Document 3-5 steps
estimated_total_time: "[X days from start to finish]"
```

### 3.4 Related Programs
Check `hapvida-data` skill for Qualivida programs. Document which ones relate to this topic.
Also note: Command Center relevance, telemedicine applicability, app functionalities.

---

## PART 4: ANS Coverage

**Consult `hapvida-regulatory` skill for search strategies.**

```yaml
in_catalog: "[Yes/No]"
tuss_code: "[if applicable]"
waiting_periods:
  urgent_emergency: "24 hours"
  specific_procedure: "[X days]"
  if_preexisting: "CPT 720 days"
authorization_deadline: "[X business days — RN XXX]"
exceptions: ["exception 1", "exception 2"]
regulation_source: "[RN ANS nº XXX + URL]"
```

### Beneficiary Rights
- List relevant rights with legal basis
- Complaint channels: ANS 0800 701 9656, ANS website, Hapvida ombudsman, local Procon

---

## PART 5: Market Prices (Context)

**Present as NATIONAL RANGE, not by city.**

```yaml
private_national_range:
  minimum: "R$ [X]"
  average: "R$ [Y]"
  maximum: "R$ [Z]"
variation_factors: ["region", "technique", "hospital/clinic"]
sources: ["source 1 + URL", "source 2 + URL"]
research_date: "[month/year]"

comparison:
  private_total: "R$ [X] to R$ [Y]"
  hapvida_total: "R$ [X] to R$ [Y] (copayment)"
  savings_value: "R$ [X] to R$ [Y]"
  savings_percentage: "[X]% to [Y]%"
```

---

## DR1 Validation Checklist

```
SERP:
- [ ] 10 competitors analyzed
- [ ] Gaps identified
- [ ] Hapvida opportunities mapped

Medical data:
- [ ] Definition with official source
- [ ] Brazil epidemiology
- [ ] Symptoms listed
- [ ] Procedure types documented

Hapvida data:
- [ ] Operational pattern (owned vs credentialed)
- [ ] Copayment calculated
- [ ] Step-by-step process
- [ ] Related programs identified

ANS coverage:
- [ ] Waiting periods documented
- [ ] ANS deadlines
- [ ] Beneficiary rights

Anti-doorway internal:
- [ ] Did NOT list hospitals by specific city
- [ ] Used multiple cities as examples
- [ ] Focused on national processes

Total sources cited: [X]
```

---

## Output: State File

Save to `/mnt/user-data/outputs/T2_[Topic]_ESTADO.md` with all data, plus:

```
═══════════════════════════════════════════
✅ DEEP RESEARCH 1 COMPLETE

Topic: [TOPIC]
Type: TIPO 2 (Educational)
Subcategory: [A/B/C/D/E]

📊 SUMMARY:
- SERP competitors: 10 analyzed
- Medical sources: [X]
- Hapvida process steps: [X]
- Calculated savings: [X]%

📜 NEXT STEP: Deep Research 2 (Comparison + SEO + FAQ)
═══════════════════════════════════════════
```

Include ready-to-paste continuation prompt.
