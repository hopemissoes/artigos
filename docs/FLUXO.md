# FLUXO — as fases de um artigo e os portões entre elas

Vale para qualquer builder (Hapvida, cobertura, bookkeeping, Mowana). Os nomes
dos blocos mudam entre skills; a lógica dos portões não.

```
  pedido
    │
    ▼
┌─────────────────────────────────────────────────────────┐
│ 0. ROTEAMENTO   docs/ROTEAMENTO.md → declarar a skill    │  sem skill = pare
└─────────────────────────────────────────────────────────┘
    ▼
┌─────────────────────────────────────────────────────────┐
│ 1. INVENTÁRIO   hapvida-article-database + banco         │  o que já existe?
│    (FAQs usadas, hospitais, overlaps, saturação)         │  anti-doorway começa aqui
└─────────────────────────────────────────────────────────┘
    ▼
┌─────────────────────────────────────────────────────────┐
│ 2. FASE 0 — PESQUISA                                     │
│    DR1 coleta · DR2 posicionamento · CI-1 · CI-2         │
│    → PESQUISA_<slug>_COMPLETO.md                         │
└─────────────────────────────────────────────────────────┘
    ▼  🚦 checkpoint_ci1.py · checkpoint_fase0.py · APROVAÇÃO HUMANA
┌─────────────────────────────────────────────────────────┐
│ 3. PRODUÇÃO    Bloco A → Bloco B → Bloco C               │
│    só com dado do state file aprovado                    │
└─────────────────────────────────────────────────────────┘
    ▼  🚦 onpage · preço-primeiro · voz · completude · verificar
┌─────────────────────────────────────────────────────────┐
│ 4. VARREDURA FINAL   checkpoint_doorway_final.py         │  reprovou = não publica
└─────────────────────────────────────────────────────────┘
    ▼
┌─────────────────────────────────────────────────────────┐
│ 5. PUBLICAÇÃO   WordPress + schema (execução separada)   │
│    → copiar para publicados/<slug>/ com URL e data       │
└─────────────────────────────────────────────────────────┘
    ▼
┌─────────────────────────────────────────────────────────┐
│ 6. REGISTRO   banco Supabase (registrar_artigo_novo,     │
│    registrar_links_artigo, registrar_faqs_artigo,        │
│    registrar_hospitais_artigo) + article-database        │
└─────────────────────────────────────────────────────────┘
    ▼
   FASE 5 — colheita de GSC, semanas depois
```

## O que é um portão

Um portão tem **três partes**, e as três são obrigatórias:

1. o script rodou;
2. **a saída foi colada na conversa** (não "passou", não "rodei e ficou ok");
3. o `00-ESTADO.md` foi atualizado com o resultado.

Portão reprovado **não** vira ressalva em letra miúda. Reprovou, para, conserta,
roda de novo.

## O portão humano

Existe um só e ele não é automatizável: **a aprovação do state file da FASE 0**.
É trava de saúde (YMYL). Se o usuário pedir o HTML direto, a resposta certa é
mostrar o checkpoint e o que falta — nunca pular a trava para obedecer.

## Ao fim de cada fase

```bash
git add artigos/<slug>
git commit -m "artigo(<slug>): <fase> — <resultado do checkpoint>"
git push -u origin <branch>
```

O contêiner da sessão é efêmero. O que não foi commitado e enviado não existe.
