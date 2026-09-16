# PLANO_MODELOS — hospital-hapvida-maternidade-guarulhos (tipo: hospital, HS1-HS4)
Agente 22 · 2026-09-16 · orquestrador: sessão principal

Modelos disponíveis nesta sessão para subagente: opus · sonnet · haiku · fable.
Degrau = quanto julgamento o assento exige. Modelo = qual cérebro senta nele. São coisas diferentes.

PLANO_MODELOS:
1 | buscas e tipo de página (SERP) | medio | sonnet | SERP já coletada pelo orquestrador com DataForSeo
2 | rede assistencial | medio | sonnet | catálogo do banco + ficha CNES; conferido pelo 6
3 | contexto local (IBGE/CNES) | barato | haiku | dado público, conferido pelo 6
4 | keywords e perguntas (fan-out) | medio | sonnet | volume real do DataForSeo, conferido pelo 7
ci-1 | desmontagem de concorrentes | forte | opus | 5 páginas lidas pela rota n8n; julgar enquadramento é julgamento
ci-2 | ganho de informação | forte | opus | decide o eixo do artigo; erro aqui não é pego por trava
5 | diferenciais, FAQ e fio condutor | forte | opus | síntese da pesquisa
6 | conferente de fatos | forte | opus | T2: modelo diferente do agente 2 (sonnet)
7 | conferente DataForSeo | barato | haiku | T2: modelo diferente do agente 4 (sonnet); número confere número
8 | redator do lead + HS1 | forte | opus | hospital entrega em bloco único; 8 escreve a abertura e a HS1
9 | redator HS2 + HS3 | medio | sonnet | experiência do paciente e como chegar
10 | redator HS4 + FAQ + conclusão | medio | sonnet | a seção de maior risco de doorway, curta e em bridge
11 | editor-chefe | forte | fable | T2: modelo diferente de 8 (opus), 9 e 10 (sonnet)
19 | voz humana | medio | sonnet | T2: modelo diferente do editor-chefe (fable)
12 | auditoria de veracidade | forte | sonnet | YMYL: cada número contra a fonte
13 | auditoria anti-doorway | forte | sonnet | T2: modelo diferente do agente 5 (opus)
14 | requisitos da skill | medio | haiku | roda os checkpoints; o script é que julga
15 | citabilidade e GEO | forte | opus | passagem citável é julgamento, não contagem
16a | juiz A — lente factual/YMYL | forte | opus | painel multimodelo
16b | juiz B — lente anti-doorway/SEO | forte | sonnet | painel multimodelo
16c | juiz C — lente do leitor | forte | fable | T3: 16a e 16b diferem do editor-chefe (fable)
21 | varredura final anti-doorway | forte | opus | T2: modelo diferente do agente 13 (sonnet)
23 | juiz P-A — suficiência e verdade | forte | opus | portão de pesquisa
24 | juiz P-B — originalidade e valor | forte | sonnet | T2: modelo diferente de 23; e do agente 5
17 | schema JSON-LD | medio | sonnet | execução separada, só sob pedido
18 | registro no banco | barato | haiku | só depois do artigo aprovado e publicado
22 | roteador de modelos | barato | haiku | este documento

## Observações do roteamento
- **Não é monomodelo.** Quatro modelos distintos sentam na linha.
- Agente 0 (diagnóstico de pillar) não entra: o artigo é novo e não é pillar.
- Agente 20 (imagem da tabela) não entra: artigo de hospital não tem seção de preço própria —
  o preço aparece só como chamariz na HS4, por shortcode.
- Nenhum agente 🔒 foi rebaixado de degrau.
- Rebaixamentos em agentes não travados: 3 e 7 em barato (dado público e conferência numérica,
  ambos com trava a jusante); 14 em haiku porque quem julga ali é o script, não o modelo.
