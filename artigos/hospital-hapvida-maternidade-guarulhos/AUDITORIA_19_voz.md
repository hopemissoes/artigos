# AGENTE 19 — Voz Humana (Modo 5, v7) — Auditoria

**Objeto:** `artigos/hospital-hapvida-maternidade-guarulhos/artigo.html`
**Papel:** auditor, não editor. Não editei o HTML.

---

## 1. Saída do checkpoint mecânico

```
====================================================================
CHECKPOINT DE VOZ HUMANA [V6] — artigos/hospital-hapvida-maternidade-guarulhos/artigo.html
2616 palavras · 72 parágrafos · 122 frases · rigor: medio
====================================================================

🔴 nenhum tique bloqueante.

🟡 DENSIDADE — o editor decide

  • travessão: 6 (2.3 por 1.000 palavras; alvo ≤ 2)

--------------------------------------------------------------------
Lembrete da regra-mãe: mexer em palavra e ritmo, NUNCA em fato.
Se limpar o tique custar precisão, o tique fica e o editor anota o porquê.
--------------------------------------------------------------------

✅ APROVADO
```

## 2. Leitura em voz alta (o que o script não faz)

Lidos: lead (3 parágrafos), abertura das 4 seções (`#diferencial`, `#estrutura`,
`#como-chegar`, `#planos-acesso`) e as 3 FAQs mais longas por contagem de
palavras (FAQ 6 — 76 palavras, FAQ 5 — 59, FAQ 8 — 54).

- **Lead:** sai bem na fala. Frases fecham curtas ("É o mesmo hospital e o
  mesmo registro"), sem enfeite.
- **Abertura de `#diferencial` e `#como-chegar`:** naturais, terminam em frase
  curta de fecho factual ("Mudou a placa: o registro CNES 9255826 continua o
  mesmo." / "É o mesmo lugar."). Isso é o oposto do ritmo metronômico — bom
  sinal.
- **Abertura de `#estrutura`:** frase de enumeração longa (lista de serviços do
  CNES) seguida de frase de 5 palavras ("É o retrato oficial da unidade.").
  Funciona falado — a enumeração é factual, não é tríade de adjetivo.
- **Abertura de `#planos-acesso`:** direta, sem molde de piloto automático
  ("Não existe fonte pública que liste... O que dá para afirmar:...").
- **FAQ 5, 6 e 8:** todas respondem de cara ("Quatro, na ficha do CNES:...",
  "Pelos canais oficiais da operadora:...") — nenhuma abre com "a resposta é
  simples" ou pergunta retórica. Sairiam numa conversa real sem soar
  automáticas.

**Nenhuma frase, nas 8 amostras lidas, precisou de correção de voz.**

## 3. Caça aos 5 tiques (varredura no artigo inteiro, não só nas amostras)

| # | Tique | Achado |
|---|---|---|
| 1 | Gerúndio de arremate | **Nenhum.** Varredura por `, <verbo>ndo` no texto corrido não achou ocorrência real (só falsos positivos de "segundo", que não é gerúndio). |
| 2 | Tríade de adjetivos | **Nenhuma.** As listas de três no texto ("obstétrico, pediátrico e traumato-ortopédico", "Nosso Plano, Mix e Ambulatorial", "farmácia, esterilização e serviço social") são enumerações factuais, não adjetivo de vitrine em fila. |
| 3 | Moldes ("não apenas... mas também", "quando o assunto é", "vale lembrar que", "seja você...", aberturas de piloto automático) | **Nenhum.** Zero ocorrências de qualquer frase da lista de moldes da referência. |
| 4 | Marketing genérico ("excelente custo-benefício", "tranquilidade para você e sua família" etc.) | **Nenhum.** Zero ocorrências. |
| 5 | Ritmo metronômico | **Não observado.** Parágrafos alternam frase longa de dado + frase curta de fecho ("É o retrato oficial da unidade.", "É o mesmo lugar.", "Internar é o que exige o hospital.") — variação real de tamanho, não cadência de vestibular. |

Resultado: os 4 tiques 🔴-reprováveis e o tique de ritmo estão limpos. O único
achado é de densidade (🟡), tratado no item 4.

## 4. Travessões — tabela de achados

Contagem confirmada por regex no HTML bruto (ignorando `<style>`/`<script>`,
como o checkpoint faz): **6 travessões no corpo do artigo**, mais 1 dentro de
um comentário CSS (`/* RESPONSIVO ... */`) que o checkpoint corretamente
ignora — por isso o `grep` bruto acha 7 e o checkpoint reporta 6.

| Trecho | Tique | Componente | Correção proposta (antes/depois) | Mexeu em fato? |
|---|---|---|---|---|
| "Operadora registrada na ANS **—** nº 359017" (selo de confiança, 2×) | Travessão | Selo de confiança (`v5-trust`) — string fixa reaproveitada em todo artigo do site | Nenhuma proposta. É boilerplate do componente, não prosa do redator; trocar o traço aqui é mexer em template do site inteiro, fora do escopo de um artigo. | — (não aplicável) |
| "Lei 9.656/98 **—** define as segmentações do plano de saúde..." | Travessão | Faixa "Fonte oficial" — formato fixo do componente (`título da norma — glosa curta`) dentro do próprio link | Nenhuma proposta. É o formato padrão do componente E-E-A-T, repetido em todos os artigos com essa faixa; não é "muleta de variar frase" do redator. | — (não aplicável) |
| "Lei 10.778/2003 **—** notificação compulsória de violência..." | Travessão | Faixa "Fonte oficial" | Idem acima. | — (não aplicável) |
| "...o noticiário local e setorial de novembro de 2025 **—** incluindo a reportagem do Saúde Business sobre a Sala Lilás **—** e o catálogo de rede da operadora." | Travessão (2 no mesmo período) | Caixa "Sobre este guia" | **ACEITA.** Antes: "...o noticiário local e setorial de novembro de 2025 — incluindo a reportagem do Saúde Business sobre a Sala Lilás — e o catálogo de rede da operadora." Depois: "...o noticiário local e setorial de novembro de 2025 (incluindo a reportagem do Saúde Business sobre a Sala Lilás) e o catálogo de rede da operadora." | Não. Mesmas fontes citadas (CNES/DataSUS, noticiário de novembro/2025, reportagem do Saúde Business, catálogo de rede), só troca travessão por parênteses — exatamente o conserto que a própria referência recomenda (§7) para aposto/informação lateral. |

## 5. Veredito sobre a decisão do editor-chefe

O editor registrou: "sobraram 6 travessões, todos dentro de componentes
congelados da skill (selos de confiança, faixas 'fonte oficial', caixa 'sobre
este guia')."

- **Contagem e localização: corretas.** Não há travessão fora desses três
  componentes em nenhum lugar do artigo — nem no lead, nem nas 4 seções, nem
  em nenhuma das 8 FAQs. Conferido por regex no HTML inteiro, não só nas
  amostras lidas em voz alta. O editor não deixou passar nenhum caso fora do
  esperado.
- **Mas a generalização "componente congelado ⇒ travessão intocável" é
  imprecisa para 2 dos 6.** Selo de confiança e faixa "Fonte oficial" são,
  de fato, template fixo (string/formato repetido em todos os artigos do
  site) — aí o travessão é do componente, não do redator, e a trava de
  conteúdo se aplica corretamente. Já a caixa "Sobre este guia" é congelada
  na *moldura* (ícone, rótulo, cor), mas o *parágrafo dentro dela* é prosa
  livre escrita especificamente para este artigo — e os 2 travessões ali
  são exatamente o padrão de "muleta para variar frase" que a referência
  descreve em §7, não citação formatada. Dá para corrigir sem tocar em
  nenhum fato (ver item 4).

**Recomendação:** aplicar a correção do item 4 nos 2 travessões da caixa
"Sobre este guia" (parênteses no lugar do travessão). Os outros 4 ficam como
estão — são componente, não voz.

## 6. Veredito final

**🟢 APROVADO**, com uma sugestão de ajuste fino não bloqueante (item 4/5,
2 travessões dentro da caixa "Sobre este guia"). Zero tiques reprováveis nos
5 caçados; o único item de densidade (travessão) já estava, em 4 de 6 casos,
corretamente protegido como componente — a diferença fica só na leitura de
"o que é componente" vs. "o que é prosa dentro do componente", e não muda o
veredito de aprovação.
