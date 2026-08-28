---
description: Dispara a linha multiagente/multimodelo da v7.2 para um artigo
argument-hint: <slug>
---

Rodar a linha de agentes da v7.2 para `artigos/$1`.

Antes de disparar, nesta ordem:

1. Leia `docs/LINHA-V7.md` (mapa de degrau → modelo neste ambiente) e
   `references/modelos-agentes.md` da skill (roteamento dos 25 agentes).
2. Rode `scripts/testar-egress.sh`. Bloqueado → leia `docs/CI1-SEM-EGRESS.md` e
   escolha a rota da CI-1 **antes** de começar, não no meio.
3. Escreva `artigos/$1/PLANO_MODELOS_$1.md` (Agente 22) respeitando os pares que
   não compartilham modelo: `2×6 · 4×7 · 8/9/10×11 · 11×19 · 5×13 · 13×21`.
4. Rode `checkpoint_modelos.py` e **cole a saída**. Reprovou = não dispara.

Ao rodar:

- agentes independentes vão **na mesma mensagem**, para rodarem em paralelo;
- passe **bastão curto** para cada agente — nunca o histórico da conversa;
- **revise toda saída antes de ela virar insumo**; você não aprova o próprio
  trabalho;
- atualize `artigos/$1/00-ESTADO.md` a cada estágio fechado.

Os 14 agentes travados (0, CI-1, CI-2, 5, 6, 11, 12, 13, 15, 16a-c, 21, 23, 24)
rodam em degrau forte. Sem exceção por prazo ou por lote.
