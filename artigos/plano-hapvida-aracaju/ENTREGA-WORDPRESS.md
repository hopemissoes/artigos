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
Plano Hapvida Aracaju: Preços, Promoção e Rede | Guia [ano_atual]
```

**O que muda em relação ao seu de hoje** (`Hapvida Aracaju: Preços, Rede e Hospital | Guia
[ano_atual]`): entra a palavra **"plano"**, sem a qual o H1 não contém a keyword principal e
reprova no `checkpoint_onpage.py`. E "Promoção" entra no lugar de "Hospital", para o H1
refletir a mesma prioridade do título.

---

## 3. Título SEO (Rank Math)

```
Plano Hapvida Aracaju [ano_atual]: promoção a partir de [aracaju_menorvalor]
```

**O seu de hoje já passa em tudo** — keyword à esquerda, shortcode de preço, 50 caracteres
renderizados. A única mudança que proponho é de clareza: `promoções de R$ 144,77` pode ser
lido como um desconto **de** R$ 144,77, não como o preço **a partir de** R$ 144,77. Trocar
por "promoção a partir de" tira a ambiguidade e mantém a promoção em destaque. Custa 8
caracteres (vai a 58 de 60).

Se preferir manter o seu, não há perda de SEO — é escolha de redação.

---

## 4. Meta description

```
Plano Hapvida Aracaju [ano_atual] em promoção a partir de [aracaju_menorvalor]: tabela por faixa etária, 7 unidades próprias e o Hospital Gabriel Soares 24h.
```

139 caracteres renderizados (limite 160).

**O que muda em relação à sua de hoje**, em ordem de importância:

1. **"10 unidades próprias" → "7 unidades próprias".** O catálogo (`consultar_rede`) tem 7. É
   o mesmo erro do corpo do artigo, mas na SERP.
2. **Entra "Plano"** — a sua abre em "Hapvida Aracaju" e não contém a keyword principal.
3. **A promoção sobe para a frente**, no lugar de "Menor preço de Sergipe" no fim.
4. Saiu "Guia completo DRV" — é autopromoção ocupando ~20 caracteres que rendem mais como
   dado. A autoria é carregada pelo widget de autor e pelo nó `Person` do schema.

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

## 6. Correção de um achado meu que estava errado

Eu havia registrado que os títulos do site estavam com preço e ano cravados na mão, e
sugerido uma força-tarefa para trocá-los por shortcode. **Estava errado** — li o HTML
renderizado e tomei a saída dos shortcodes por texto fixo. Belo Horizonte, Recife e a pillar
de tabela já são dinâmicos como este. Não há essa pauta.

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
