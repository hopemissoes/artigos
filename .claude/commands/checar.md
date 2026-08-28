---
description: Roda as travas mecânicas aplicáveis a um artigo e cola as saídas
argument-hint: <slug>
---

Rodar os checkpoints de `artigos/$1`, na ordem, salvando cada saída em
`artigos/$1/checkpoints/` **e colando na conversa** (as skills exigem a saída
colada — "passou" não vale).

```bash
SKILL=hapvida-article-builder-v7        # ou a anotada em 00-ESTADO.md
TIPO=$(grep -oP '(?<=\*\*Tipo:\*\* )\w+' artigos/$1/00-ESTADO.md)

scripts/cp.sh $SKILL checkpoint_fase0.py artigos/$1/PESQUISA_$1_COMPLETO.md $TIPO | tee artigos/$1/checkpoints/fase0.txt
# a partir daqui, só quando artigo.html existir:
scripts/cp.sh $SKILL checkpoint_preco_primeiro.py artigos/$1/artigo.html $TIPO | tee artigos/$1/checkpoints/preco-primeiro.txt
scripts/cp.sh $SKILL checkpoint_voz.py           artigos/$1/artigo.html | tee artigos/$1/checkpoints/voz.txt
scripts/cp.sh $SKILL checkpoint_completude.py    artigos/$1/artigo.html $TIPO | tee artigos/$1/checkpoints/completude.txt
scripts/cp.sh $SKILL checkpoint_verificar.py     artigos/$1/artigo.html artigos/$1/PESQUISA_$1_COMPLETO.md | tee artigos/$1/checkpoints/verificar.txt
scripts/cp.sh $SKILL checkpoint_doorway_final.py artigos/$1/artigo.html | tee artigos/$1/checkpoints/doorway-final.txt
```

Confira o `--help` de cada script antes de inventar argumento. Ao fim, atualize a
tabela de portões em `artigos/$1/00-ESTADO.md` com ✅ / 🟡 / ⬜ e o caminho da saída.

**Reprovou = não publica.** Liste os bloqueios e o que cada um exige, sem
suavizar.
