# RELATÓRIO DE MELHORIAS — plano-hapvida-aracaju

Data: 2026-09-01 · Base: FASE 0 retroativa (`PESQUISA_plano-hapvida-aracaju_COMPLETO.md`),
aprovada em `checkpoint_fase0.py`, `checkpoint_ci1.py` e `checkpoint_suficiencia.py`.
Artigo no ar: `https://tabelaplanos.com.br/plano-hapvida-aracaju/` (banco id 3, V4.3.2).

**Onde o artigo está hoje:** orgânico **#3** em "plano hapvida aracaju" na SERP local de
Aracaju (mobile). Acima dele só a própria Hapvida (#1 e #2). Ou seja, é a **primeira posição
não-operadora** — o teto prático para uma corretora nesta busca. Os problemas abaixo não são
"o artigo é ruim"; são o que separa a posição de hoje de uma página defensável.

Prioridade: 🔴 bloqueia · 🟡 ajuste recomendado · 🟢 polimento.

---

## 🔴 CRÍTICOS

### 1. "10 pontos de atendimento" não se sustenta em nenhuma fonte

O número está no lead-herói, no H2 da rede, no sumário e na meta description. Medido contra
`consultar_rede` (catálogo, páginas 106-108 do PDF de rede):

| Fonte | Contagem |
|---|---|
| Catálogo do banco | **7 unidades / 7 endereços distintos** |
| Lista do próprio artigo | 9 itens (1 hospital + 4 clínicas + 4 diagnósticos) |
| Endereços distintos na lista do artigo | **6** |
| Afirmado no texto | **10** |

A inflação vem de contar como "ponto de atendimento" dois serviços de imagem que ficam
**dentro** de unidades já contadas: `Diagnóstico Aracaju` (Rua Campo do Brito, 1180 — mesmo
endereço da Hapclínica Aracaju) e `Diagnóstico Gabriel Soares` (Rua Itabaiana, 690 — mesmo
endereço do hospital). São serviços, não pontos.

`checkpoint_verificar.py` reprova com 7 tokens proibidos. **Correção:** trocar por
"7 unidades próprias" em todas as ocorrências e apresentar os diagnósticos como serviço
integrado ao hospital e à clínica.

### 2. Falta uma unidade que existe no catálogo

`Clínica São José` — Tv. Juca Barreto, 177, São José (catálogo id 176) — não aparece no
artigo. A v7 é explícita: o editor-chefe reprova rede incompleta; "rede enxuta" só pode ser
dito se o catálogo confirmar. Aqui o catálogo diz o contrário.

**Correção:** incluir na S4 (cards de rede) e na S5 (cobertura por bairro).

### 3. H1 e meta description não contêm a keyword principal

`checkpoint_onpage.py` → **REPROVADO**.

- H1 no ar: `Hapvida Aracaju: Preços, Rede e Hospital | Guia 2026` — **sem a palavra "plano"**
- Meta no ar: `Hapvida Aracaju 2026: Hospital Gabriel Soares 24h, 10 unidades próprias...`

A skill antecipa exatamente este caso: o molde antigo "Hapvida [Cidade]: …" reprova porque
não contém "plano". **Correção:** abrir os dois com "Plano Hapvida Aracaju".

### 4. ~~Title e meta com preço e ano congelados~~ — ACHADO RETIRADO (falso)

**Este achado estava errado e foi retirado em 2026-09-01.** Eu li o HTML renderizado da
página (`2026`, `R$ 144,77`) e concluí que eram valores fixos. Eram a saída dos shortcodes
`[ano_atual]` e `[aracaju_menorvalor]`, que o site já usa no título e na meta — o
renderizado não distingue as duas coisas, e eu não conferi a origem antes de afirmar.

Consequência: a pauta de "tirar o preço fixo dos 40+ artigos de cidade" **não existe**.
Belo Horizonte, Recife e a pillar de tabela também já são dinâmicos.

O que **permanece** verdadeiro no title e na meta está nos itens 3 e 4b.

### 4b. A meta afirma "10 unidades próprias"

Mesmo erro de contagem do item 1, mas na SERP — que é onde mais custa. O catálogo tem 7.

### 5. Canibalização confirmada na SERP

Na mesma busca "plano hapvida aracaju", em Aracaju:

- `tabelaplanos.com.br/plano-hapvida-aracaju/` → orgânico **#3**
- `tabelaplanos.com.br/` (a **home**) → orgânico **#17**

Duas URLs do site disputando a mesma query. O artigo está ganhando, então não é urgência —
mas é o mesmo padrão que a skill registra como causa de pillar que não sobe. Vale registrar
como diagnóstico e observar em D+30.

---

## 🟡 MODERADOS

### 6. Must-match não coberto: preço por modalidade de contratação

O líder de cobertura da SERP (`meuplanohap`, orgânico #4, 4.095 palavras, 45 tabelas) separa
o preço em **quatro** blocos: Adesão, Empresarial PME, Empresarial 30-99 e Individual.
`facaseuplano` (#6) separa em três. Nós temos **um** shortcode de uma modalidade.

É a maior lacuna competitiva do artigo — e a única em que um concorrente nos supera de fato.

### 7. Must-match não coberto: preço por perfil (infantil e idoso)

`facaseuplano` tem H2 dedicado a "Qual o preço do Hapvida Infantil?" e "Qual o preço do
Hapvida para idoso?". O PAA da SERP confirma a intenção de preço. Cabem como H3 dentro da
seção de preço, sem seção nova.

### 8. Perfil de links interno muito abaixo do mínimo — e mirando destinos saturados

| Regra da skill | Mínimo | Hoje |
|---|---|---|
| Destinos internos distintos | 5 | **2** |
| Links externos | 2 | **1** (IBGE) |
| Cada URL no máximo 1× | — | `plano-de-saude-hapvida-carencia` aparece **2×** |

Pior: os dois destinos linkados estão **SATURADOS** por `consultar_saturacao_destinos` —
carências (53 backlinks) e hospitais credenciados (30). A regra manda priorizar
subutilizados. Candidatos relevantes e subutilizados:

| Destino | backlinks | onde encaixa |
|---|---|---|
| `aplicativo-hapvida` | 1 | seção de tecnologia |
| `teleconsulta-hapvida` | 4 | seção de tecnologia |
| `laboratorios-hapvida-capitais` | 4 | S4, ao falar de coleta e imagem |
| `plano-hapvida-maceio` | 1 | cross-link de capital vizinha |
| `plano-hapvida-salvador2` | 6 | cross-link de capital do Nordeste |
| `hapvida-rede-pediatrica` | 10 | Hapclínica Hermes Fontes (pediatria) |
| `clinicas-hapvida-por-capital` | 10 | S5 cobertura por bairro |
| `urgencia-e-emergencia-hapvida` | 12 | o ponto forte do artigo |

### 9. A seção "Tecnologia e Atendimento Digital" é 100% nacional

A tabela de migração da própria skill lista essa seção como **ELIMINADA** ("100% nacional,
zero variação local"), e o banco já a cataloga em `consultar_overlaps_doorway` como overlap
de risco médio, com ação recomendada "ELIMINAR — 1 frase no artigo + link pillar
Tecnologia/App". Hoje ela é um H2 inteiro que sobrevive à troca de cidade.

**Correção:** virar 1-2 frases dentro da S7 + link para `teleconsulta-hapvida` e
`aplicativo-hapvida` — que, além de tudo, são os dois destinos mais subutilizados do site.

### 10. Nenhum H2 contém keyword secundária

`checkpoint_onpage.py` exige ≥2. Hoje é **0**. As 8 secundárias qualificadas (com volume real
medido) não estão em nenhum H2 — inclusive `hospital hapvida aracaju` (140/mês) e
`urgência hapvida aracaju` (100/mês somando variantes), que o artigo já responde no corpo.

### 11. 13 menções à DRV — o limite é 3

Lead + conclusão + 1 Dica DRV. Hoje há 3 boxes "DICA DRV" mais 10 menções no texto corrido.
Acima de 3 vira autopromoção e cobra o preço em E-E-A-T.

### 12. 18 FAQ — a faixa é 12-15

Não é erro grave, mas 3 perguntas passam do teto. Duas delas são candidatas naturais a corte
por serem nacionais: "Qual a diferença entre Nosso Plano e Mix" e "Como funciona a
coparticipação total" (as duas já são território de pillar).

### 13. O banco está defasado em relação ao artigo no ar

`consultar_artigo` devolve, para o slug:

- `faqs: []` — o artigo tem 18 perguntas, nenhuma registrada
- `links_saida`: 1 registro (`mamografia-preco-popular`, âncora "mamografia") que **não existe**
  no artigo no ar
- `versao: V4.3.2` · `cluster_slug: null` · `titulo_seo: null` · `data_atualizacao: null`
- os `h2s` gravados ainda trazem "10 Pontos de Atendimento" e âncoras antigas (`#por-que`,
  `#rede`, `#hospital`), diferentes das que estão no HTML (`#por-que-aracaju`, `#rede-propria`,
  `#hospital-gabriel-soares`)

### 14. Telefones e contagens de leitos sem fonte no state file

`checkpoint_verificar.py` acusa 3 telefones — (79) 4002-3633 (2×) e (79) 3205-6200 — e várias
contagens de leitos (56, 74, 130, 145, 186). São dados YMYL: ou entram com fonte primária
citada, ou saem. O "130 leitos" tem fonte (F5 News, dez/2025); os demais, não.

---

## 🟢 POLIMENTO

- **Sumário com 14 itens** (faixa da skill: 10-11). É consequência de o artigo ter 13 H2 em
  vez dos 7 canônicos. Resolve-se junto com o item 9 e o 12.
- **Falta a `<figure>` de abertura** (obrigatória em city) e a **imagem da tabela de preço**
  (`gerar_imagem_artigo.py`), que deveria fechar a seção de preço. As duas dependem de
  material seu — URL da imagem e os 10 valores da tabela vigente.
- **Citabilidade da seção de FAQ**: o `checkpoint_citabilidade.py` reprova por não haver `<p>`
  logo após o H2. É limite do script — o template de FAQ da própria skill vai do H2 direto
  para os `<details>`. Não mexer.
- **Densidade de travessão**: 95 ocorrências (alvo ≤2 por 1.000 palavras). É 🟡 do
  `checkpoint_voz.py`, herdado do texto original, não bloqueia.

---

## OPORTUNIDADES DE CLUSTER (com volume medido)

Duas páginas que **não existem** e que a pesquisa mostra que valem mais que qualquer ajuste
acima. As duas seguem padrão já publicado no site para outras cidades.

### A. `plano-de-saude-aracaju` — arquétipo "mercado amplo"

- volume: **880/mês** · KD **0** · intenção **comercial** · tendência **+22% no mês**
- o padrão já existe para Recife, Belém, Teresina, Goiânia, BH e Fortaleza. Aracaju não tem.
- responde ao PAA "Qual o melhor plano de saúde em Aracaju, Sergipe?", que hoje ninguém
  nosso responde.
- é 17× o volume da keyword que o artigo atual persegue ("plano hapvida aracaju", 50/mês,
  em queda de 29% no ano).

### B. `urgencia-e-emergencia-hapvida-aracaju`

- volume: **100/mês** somando "urgência hapvida aracaju" (70) e "emergência hapvida
  aracaju" (30) · KD 0
- o padrão já existe em Recife, Fortaleza e Goiânia.
- **é exatamente o ganho de informação do artigo atual**: Aracaju não tem PA 24h autônomo, e
  toda a urgência da operadora no estado passa por um único endereço. Hoje isso é uma FAQ; dá
  uma página.

---

## ORDEM SUGERIDA

1. Itens 1 e 2 (a rede) — é o dado YMYL e destrava o `checkpoint_verificar.py`.
2. Itens 3 e 4 (H1, title, meta) — mudança barata, efeito direto em CTR e no on-page.
3. Itens 8, 9 e 10 (links e a seção de tecnologia) — resolvem-se no mesmo movimento.
4. Itens 6 e 7 (cobertura de preço) — é onde o concorrente ganha de nós.
5. Item 13 (sincronizar o banco) — depois que o texto estabilizar.
6. Cluster A e B — pauta nova, decisão sua.
