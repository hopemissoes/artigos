---
description: Retoma um artigo exatamente de onde a sessão anterior parou
argument-hint: <slug>
---

Retomar `artigos/$1`. Sem reconstruir pesquisa e sem readivinhar decisão já tomada.

1. Leia `artigos/$1/00-ESTADO.md` **inteiro** — inclusive "Decisões tomadas" e
   "Fio condutor".
2. Leia `artigos/$1/PESQUISA_$1_COMPLETO.md`. **Ele é a fonte da verdade.** Dado
   que não está nele não entra no artigo.
3. Invoque a skill anotada em "Skill em uso" (não outra versão).
4. Confira as saídas em `artigos/$1/checkpoints/` — o que já passou, não refaça.
5. Diga em uma frase onde o artigo está e qual é o próximo passo; então execute
   **só esse passo**.
6. Ao terminar, atualize `00-ESTADO.md` e faça commit antes de responder.

Se o estado contradisser os arquivos da pasta, confie nos arquivos, corrija o
estado e avise o usuário do que estava errado.
