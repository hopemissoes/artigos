# publicados/

Cópia do que foi de fato ao ar, por artigo:

```
publicados/<slug>/
├── artigo.html      ← exatamente o HTML publicado
├── schema.json
└── META.md          ← URL, data de publicação, id do WordPress, id no banco
```

Serve para duas coisas: comparar o que está no ar com o que foi escrito
(o WordPress e o Elementor mexem no HTML), e alimentar a auditoria e a
FASE 5 de colheita do GSC sem depender de raspagem.

Não é o lugar do rascunho — rascunho fica em `artigos/<slug>/`.
