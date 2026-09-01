# ENTREGA — o que colar no WordPress (plano-hapvida-aracaju)

Data: 2026-09-01 · Artigo: `artigo.html` · Slug: `/plano-hapvida-aracaju/` (não muda)

> **Nada aqui foi publicado.** O artigo no ar continua o de antes. Os campos abaixo
> substituem os atuais quando você mandar publicar.

---

## 1. Corpo do artigo

`artigo.html` — colar no **editor de código / HTML**, nunca no editor visual.

O original foi colado no visual e o `wpautop` injetou `<br />` dentro do `<style>` e do
`<script>`, o que deixava o JS do grifo animado sem rodar e a maior parte do CSS quebrada.
Os dois blocos foram remontados limpos; se forem colados no visual de novo, o defeito volta.

---

## 2. Título do post (H1) — 58 caracteres

```
Plano Hapvida Aracaju: Preços, Rede Própria e Hospital 24h
```

**O que muda:** o H1 no ar é `Hapvida Aracaju: Preços, Rede e Hospital | Guia 2026`, que não
contém a palavra "plano" e por isso reprovava no `checkpoint_onpage.py`. Também sai o ano fixo.

---

## 3. Título SEO (Rank Math) — 58 caracteres renderizados

```
Plano Hapvida Aracaju: Rede e Preços a Partir de [aracaju_menorvalor]
```

Renderiza hoje como **"Plano Hapvida Aracaju: Rede e Preços a Partir de R$ 144,77"** — 58
caracteres, dentro do limite de 60. O valor sai do mesmo shortcode que alimenta o corpo do
artigo, então título e tabela nunca divergem: quando a tabela é reajustada, a SERP acompanha
sozinha.

**O que muda:** o title no ar é `Plano Hapvida Aracaju 2026: promoções de R$ 144,77` — preço
e ano congelados na mão, que passam a mentir no primeiro reajuste. O novo abre com a keyword
principal e carrega o ganho de informação da pesquisa (a rede endereçada, que nenhum
concorrente da SERP tem).

> Se um dia o `[aracaju_menorvalor]` passar de 4 dígitos, o título encosta no limite de 60.
> Nesse caso, encurtar para `Plano Hapvida Aracaju a Partir de [aracaju_menorvalor]`.

---

## 4. Meta description — 145 caracteres renderizados

```
Plano Hapvida Aracaju a partir de [aracaju_menorvalor]: tabela por faixa etária, as 7 unidades próprias com endereço e o único pronto-socorro 24h do estado.
```

Renderiza como: *"Plano Hapvida Aracaju a partir de R$ 144,77: tabela por faixa etária, as 7
unidades próprias com endereço e o único pronto-socorro 24h do estado."*

**O que muda:** a meta no ar abre em "Hapvida Aracaju 2026:" — sem a keyword principal, com
ano fixo e repetindo o número errado de unidades ("10 unidades próprias").

---

## 5. Conferência depois de publicar

Rodar o kit on-page com os valores **renderizados** (não com o shortcode cru):

```bash
scripts/cp.sh hapvida-article-builder-v7 checkpoint_onpage.py artigos/plano-hapvida-aracaju/artigo.html \
  --kw "plano hapvida aracaju" --h1 "<H1 real>" --title "<title renderizado>" \
  --url "plano-hapvida-aracaju" --meta "<meta renderizada>"
```

E conferir o `<title>` que foi realmente ao ar:

```bash
curl -sSL -A "Mozilla/5.0" https://tabelaplanos.com.br/plano-hapvida-aracaju/ \
  | grep -o '<title>[^<]*</title>'
```

Tem que aparecer o valor em reais, não o shortcode entre colchetes.

---

## 6. Fica como pauta: o resto do site tem o mesmo problema

Os títulos que conferi no ar têm preço e ano cravados na mão:

| Página | Título no ar |
|---|---|
| `/plano-hapvida-belo-horizonte/` | Plano Hapvida Belo Horizonte 2026: Promoção por R$ 71,98 |
| `/plano-hapvida-recife/` | Plano Hapvida Recife 2026: PROMOÇÃO por R$ 131,32 |
| `/tabela-de-preco-hapvida/` | Tabela de Preços Hapvida 2026 \| PROMOÇÃO por R$ 71,98 |

Se o Aracaju confirmar que o shortcode renderiza no título, dá para virar padrão nos 40+
artigos de cidade de uma vez — e o ano também sai da mão, com o `%currentyear%` do Rank Math.

---

## 7. O que NÃO foi feito e depende de você

- **`<figure>` de abertura** — obrigatória em artigo de cidade. A v7.4 a coloca dentro da
  primeira seção CORE (a S1, "Por Que Aracaju É um Caso À Parte"). Falta a URL da imagem.
- **Imagem da tabela de preço** (`gerar_imagem_artigo.py`) — fecharia a seção de preço.
  Precisa dos 10 valores da tabela vigente, na mesma fonte dos shortcodes.
- **Sincronizar o banco** (`atualizar_artigo`, `registrar_faqs_artigo`,
  `registrar_links_artigo`) — o registro está defasado: 0 FAQ gravadas para 14 no artigo,
  1 link registrado que não existe, versão V4.3.2, âncoras antigas. São escritas no
  Supabase e não faço sem você mandar.
- **Cobertura de preço por modalidade e por perfil** (achados 6 e 7 do relatório) — é a
  única frente em que o concorrente `meuplanohap` nos supera. Depende de existirem
  shortcodes de tabela para adesão, PME e empresarial 30-99 em Aracaju.
