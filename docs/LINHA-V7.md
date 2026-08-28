# A linha de 25 agentes da v7.2 — como rodar aqui

Este é o ponto em que **este ambiente é melhor que o Claude Desktop**, e vale
saber por quê: a v7.2 exige que quem confere rode em **modelo diferente** de quem
produziu, e que o painel de juízes tenha **≥2 modelos distintos**. Isso depende de
poder escolher o modelo de cada subagente. O Desktop não tem esse controle — lá a
linha vira "o mesmo modelo com prompts diferentes", que é exatamente o que a skill
diz **não** ser separação: *"o ponto cego é do modelo, não do prompt"*.

Aqui existe a ferramenta `Agent`, com `model` por chamada.

## Os degraus (a skill manda; isto é só o mapa para cá)

| Degrau | Uso | `model` |
|---|---|---|
| **forte** 🔒 | julgamento, verificação, síntese, juízo | `opus` |
| **médio** | redação com trava, coleta que exige classificar | `sonnet` |
| **barato** | ler arquivo grande, rodar script, coleta verificável | `haiku` |

**Quarto modelo disponível: `fable`.** Não é um degrau novo — serve para cumprir a
regra de "modelo diferente" sem rebaixar o degrau. Onde a skill pede um juiz forte
em modelo diferente do editor-chefe, `fable` resolve sem descer para `sonnet`.

## Os pares que não podem compartilhar modelo (§4 da skill)

```
2×6    4×7    8/9/10×11    11×19    5×13    13×21
```

E no painel de juízes: 16a/16b/16c com ≥2 modelos distintos, e ≥1 juiz em modelo
diferente do editor-chefe (Agente 11). Os juízes de pesquisa 23 e 24 também: `24 ≠ 23`,
e ao menos um dos dois ≠ Agente 5.

## Chamada

```
Agent(
  subagent_type: "general-purpose",
  model: "opus",
  description: "CI-1 desmontagem",
  prompt: "<bastão curto + o que produzir + o que NÃO fazer>"
)
```

Agentes independentes vão **na mesma mensagem**, para rodarem em paralelo.

## O contrato do orquestrador (não afrouxe)

Você, sessão principal:

- decide o roteamento e guarda o state file;
- **revisa toda saída de subagente antes de ela virar insumo** — rascunho de
  agente médio/barato não entra no artigo sem sua revisão;
- segura os portões e resolve empate;
- **não** executa tarefa em lote, **não** aprova o próprio trabalho, **não**
  repassa o histórico da conversa no lugar do bastão.

*Você é o único que vê tudo, e por isso é o único que não pode julgar sozinho.*

## Antes de disparar

1. Leia `references/modelos-agentes.md` da skill — roteamento dos 25 agentes.
2. Agente 22 escreve `PLANO_MODELOS_<slug>.md`.
3. `scripts/cp.sh hapvida-article-builder-v7 checkpoint_modelos.py artigos/<slug>/PESQUISA_<slug>_COMPLETO.md <tipo>`
4. **Reprovou = a linha não é disparada.**

Se por algum motivo só houver um modelo disponível, declare `MODO: monomodelo` no
state file e diga ao usuário o que se perde: o voto majoritário vale menos e o
portão humano vale mais.

## Orquestração determinística (opcional, e só a pedido)

A ferramenta `Workflow` roda um script que orquestra os agentes de forma
determinística, com retomada de execuções já feitas. Ela **só pode ser usada
quando o usuário pedir explicitamente** ("usa um workflow", "ultracode"). Não
dispare por conta própria — a linha normal com `Agent` já cumpre a v7.2.
