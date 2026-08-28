---
description: Abre um artigo novo do jeito certo — escolhe a skill, cria a pasta e trava na FASE 0
argument-hint: <slug> [city|hospital|tr|pillar|cobertura]
---

Abrir o artigo `$1` (tipo: `$2`, padrão `city`). Siga **nesta ordem**, sem pular:

1. Leia `docs/ROTEAMENTO.md` e **declare em voz alta** qual skill você vai usar e
   por quê. Se o tipo for `cobertura`, a skill é `hapvida-coverage-builder`, não a
   builder de cidade. Em dúvida entre arquétipos, **pergunte antes de criar a pasta**.
2. Invoque a skill escolhida (Skill tool). Não produza nada antes disso.
3. Consulte `hapvida-article-database` e o banco (via `banco-tabelaplanos`) para
   saber o que já existe do mesmo cluster — FAQs usadas, hospitais citados,
   overlaps. Anti-doorway começa aqui, não no fim.
4. Rode `scripts/novo-artigo.sh $1 $2`.
5. Execute a **FASE 0** da skill, preenchendo
   `artigos/$1/PESQUISA_$1_COMPLETO.md`.
6. Rode o checkpoint e **cole a saída**:
   `scripts/cp.sh <skill> checkpoint_fase0.py artigos/$1/PESQUISA_$1_COMPLETO.md $2 | tee artigos/$1/checkpoints/fase0.txt`
7. Atualize `artigos/$1/00-ESTADO.md` e faça commit.
8. **PARE** e peça a aprovação humana do state file. Não escreva uma linha de HTML
   antes de ela vir — nem se for pedido o HTML direto.
