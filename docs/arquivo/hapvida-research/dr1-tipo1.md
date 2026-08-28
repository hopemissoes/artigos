# TIPO 1 — Deep Research 1: City Data Collection

Execute all parts in a single research session. Generate state file at the end.

---

## PART 1: SERP Analysis (10 Competitors)

### Searches to Execute
```
1. "plano de saúde hapvida [CITY]"
2. "hapvida [CITY] preços"
3. "hapvida [CITY] hospitais"
4. "plano de saúde [CITY]" (generic)
5. "melhor plano de saúde [CITY]"
```

### For EACH of the 10 Top Results, Document:

```yaml
position: [1-10]
url: "[full URL]"
title: "[page title]"
domain: "[site.com.br]"
content_type: "[guide/comparison/institutional/blog/landing]"
h1: "[H1 title]"
main_h2s: ["H2 1", "H2 2", "H2 3"]
strengths: ["what they do well"]
weaknesses: ["what's missing"]
city_specific_data: "[Yes/No — which data]"
is_doorway_page: "[Yes/No — why]"
opportunity: "[how we can outperform]"
```

### SERP Synthesis
- Count: guides, comparisons, institutionals, superficial blogs
- How many have unique city data: __/10
- How many are doorway pages: __/10
- List 5+ gaps no competitor covers
- List 5+ differentiation opportunities
- List keywords found across competitors

---

## PART 2: Complete Network Mapping

### Sources
**Mandatory:** https://www2.hapvida.com.br/unidades, Google Maps (validate addresses)
**Complementary:** Unit social media, local news (inaugurations), city hall website

### Map ALL Owned Units

**Hospitals** (goal: every unit in the city):
```yaml
name: "[official name]"
type: "[owned/credentialed]"
address: "[street, number, neighborhood, ZIP]"
phone: "[phone]"
services: [ER 24h, adult ICU, neonatal ICU, maternity, surgical center, hemodynamics, oncology]
differentiators: ["notable features"]
accreditation: "[ONA/JCI if applicable]"
inauguration_year: "[if found]"
source: "[where this info came from]"
```

**Urgent Care 24h (PAs):**
```yaml
name, full_address, phone, services (X-ray, medication, suture, etc.), source
```

**Clinics (Hapclínicas):**
```yaml
name, full_address, phone, specialties[], source
```

**Diagnostic Centers (Vida & Imagem / Labs):**
```yaml
name, full_address, phone, exam_types (simple, complex, imaging), source
```

### Credentialed Network
Map key credentialed hospitals and clinics — especially important for Plano Mix coverage and cities without full owned infrastructure.

### Network Validation Checklist
```yaml
hospitals_documented: [X]
pas_24h_documented: [X]
clinics_documented: [X]
labs_documented: [X]
all_have_full_address: [Yes/No]
all_have_phone: [Yes/No]
coverage_by_zone:
  north: [X] units
  south: [X] units
  east: [X] units
  west: [X] units
  center: [X] units
neighborhoods_without_coverage: [list or "none"]
```

---

## PART 3: Local Context

### Demographics (IBGE) — Source: ibge.gov.br/cidades-e-estados
```yaml
population: "[X] inhabitants ([year])"
metro_population: "[X] ([year])"
ranking: "[Xth largest in Brazil / region / state]"
idh: "[0.XXX] ([year]) — [above/below] state average"
gdp_per_capita: "R$ [X] ([year])"
age_profile:
  youth_0_14: "[X]%"
  adults_15_59: "[X]%"
  elderly_60_plus: "[X]%"
```

### Health Data (CNES) — Source: cnes.datasus.gov.br
```yaml
health_establishments: "[X] total, [X] with hospitalization"
hospital_beds: "[X] total, [X] per 10k inhabitants (national avg: [X])"
icu_beds: "[X] total, [X] per 10k inhabitants"
```

### Hapvida Presence in City
```yaml
operating_since: "[year]"
network_type: "[owned/credentialed/mixed]"
estimated_beneficiaries: "[X] (source)"
market_share: "[X]% (if available)"
owned_hospitals: "[X]"
total_units: "[X]"
key_milestones:
  - year: "[year]"
    event: "[what happened]"
    source: "[source]"
recent_investments:
  - description: "[investment]"
    value: "R$ [X] (if disclosed)"
    year: "[year]"
    source: "[source]"
```

---

## PART 4: Accessibility Analysis

```yaml
unit_concentration:
  main_neighborhoods:
    - neighborhood: "[name]"
      units: [X]
      types: "[Hospital, Clinic, PA]"
well_served_regions: ["region — why"]
underserved_regions: ["region — how many units"]
public_transport:
  near_metro: [X] (if city has metro)
  near_bus_terminal: [X]
observations: "[general coverage analysis]"
```

---

## PART 5: Local Competitors

```yaml
competitor_1:
  name: "[Unimed Local / etc.]"
  type: "[cooperative/insurance/group medicine]"
  network: "[owned/credentialed]"
  presence: "[strong/medium/weak]"
  main_differentiator: "[what they highlight]"
# Map 2-3 main local competitors
```

---

## DR1 Validation Checklist

```
SERP:
- [ ] 10 competitors analyzed
- [ ] Gaps identified
- [ ] Opportunities mapped

Network:
- [ ] Minimum 5 units with full address
- [ ] At least 1 hospital detailed
- [ ] Coverage by region mapped
- [ ] Credentialed network documented

Local context:
- [ ] IBGE population with source
- [ ] IDH with source
- [ ] CNES beds with source

Hapvida presence:
- [ ] Operating since [year]
- [ ] Network type identified
- [ ] Estimated beneficiaries (if available)

Total sources cited: [X]
```

---

## Output: State File

Generate a complete state file saved to `/mnt/user-data/outputs/T1_[City]_ESTADO.md` containing all collected data in the structure above, plus:

```
═══════════════════════════════════════════
✅ DEEP RESEARCH 1 COMPLETE

City: [CITY]
Network type: [Owned/Credentialed/Mixed]
SERP competitors: 10 analyzed
Units mapped: [X]
Sources consulted: [X]

📁 SAVE TO: HAPVIDA_PESQUISAS/EM_ANDAMENTO/
File: T1_[City]_ESTADO.md

📜 NEXT STEP: Deep Research 2 (SEO + Differentiators + FAQ)
═══════════════════════════════════════════
```

Include a ready-to-paste continuation prompt at the end of the file.
