# Kit on-page final — hospital-lauro-de-freitas-hapvida

Validado por `checkpoint_onpage.py` (saída em `checkpoints/onpage.txt`): ✅ APROVADO.

## H1 — título do post no WordPress (70 caracteres)

Hospital Lauro de Freitas Hapvida: Endereço na BA-099 e Emergência 24h

## Title SEO — Rank Math (59 caracteres, limite 60)

Hospital Lauro de Freitas Hapvida: Endereço e 24h na BA-099

Alternativas medidas, caso queira testar CTR depois:
- B (60 ch): Hospital Lauro de Freitas Hapvida: Endereço e Emergência 24h
- C (57 ch): Hospital Lauro de Freitas Hapvida: 24h na Estrada do Coco

## Meta description — Rank Math (148 caracteres, limite 160)

Hospital Lauro de Freitas Hapvida: o endereço certo na BA-099, a Estrada do Coco, emergência 24h, como chegar e quais planos dão entrada na unidade.

## Slug

hospital-lauro-de-freitas-hapvida

## Por que este miolo, e não "Guia Completo"

O molde de `references/artigo-hospital.md` sugere "Hospital [Nome] Hapvida [Cidade]:
Guia Completo [ano_atual]". A regra 2 do bloco "[V5] REGRAS DE TÍTULO E META" do
SKILL.md vence o molde: a parte variável tem de vir do **ganho de informação**, não de
um descritor genérico. "Guia Completo" sobrevive à troca do nome do hospital — é o
padrão doorway visível na própria página de resultados, que é onde ele mais pesa.

**BA-099** só existe nesta praça e é exatamente o dado que o artigo disputa: o AI
Overview do Google entrega hoje um número de rua diferente do que a Hapvida publica.

## Sobre o ano

Nenhuma das três peças leva ano. Se quiser recência visível, o campo do Rank Math
aceita a variável nativa `%currentyear%` — **não** o shortcode `[ano_atual]`, que só
renderiza no corpo do post, não nos campos de SEO.

Sugestão com ano, ainda dentro de 60 caracteres quando renderizado:
Hospital Lauro de Freitas Hapvida: Endereço e 24h %currentyear%
