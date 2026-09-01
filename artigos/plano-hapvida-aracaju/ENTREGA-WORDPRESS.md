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

## 2. Título do post (H1)

```
Plano Hapvida Aracaju: Preços, Rede Própria e Hospital 24h
```

**O que muda:** o H1 no ar é `Hapvida Aracaju: Preços, Rede e Hospital | Guia 2026`, que
não contém a palavra "plano" e por isso reprovava no `checkpoint_onpage.py`. Também sai o
ano fixo.

---

## 3. Título SEO (Rank Math) — 54 caracteres

```
Plano Hapvida Aracaju: Preços e as 7 Unidades da Rede
```

**O que muda:** o title no ar é `Plano Hapvida Aracaju 2026: promoções de R$ 144,77` — preço
e ano congelados, que passam a mentir na SERP no primeiro reajuste. O novo abre com a keyword
e carrega o ganho de informação da pesquisa (a rede endereçada, que nenhum concorrente tem).

Se você preferir manter o ano no título, use o shortcode do Rank Math, nunca o número:
`Plano Hapvida Aracaju %currentyear%: Preços e Rede` (50 caracteres).

---

## 4. Meta description — 149 caracteres

```
Plano Hapvida Aracaju: tabela de preços por faixa etária, as 7 unidades próprias com endereço e o único pronto-socorro 24h do estado, no Centro.
```

**O que muda:** a meta no ar abre em "Hapvida Aracaju 2026:" — sem a keyword principal e com
ano fixo. E repetia o número errado de unidades ("10 unidades próprias").

---

## 5. Conferência depois de publicar

```bash
scripts/cp.sh hapvida-article-builder-v7 checkpoint_onpage.py artigos/plano-hapvida-aracaju/artigo.html \
  --kw "plano hapvida aracaju" --h1 "<H1 real>" --title "<title real>" \
  --url "plano-hapvida-aracaju" --meta "<meta real>"
```

---

## 6. O que NÃO foi feito e depende de você

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
