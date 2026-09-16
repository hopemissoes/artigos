# OUTLINE — Hospital e Maternidade Guarulhos (Hapvida) · arquétipo hospital HS1-HS4
Preparado pelo orquestrador enquanto o portão de pesquisa fecha. **Nenhum HTML antes do veredito do Agente 23.**

## Kit on-page (do state file, seção 2)
- URL: `/hospital-e-maternidade-guarulhos-hapvida/`
- H1: Hospital e Maternidade Guarulhos (Hapvida): agora Hospital Keila Ferreira
- Title SEO (60): `Hospital e Maternidade Guarulhos Hapvida: agora Keila Ferreira`
- Meta (160): `O Hospital e Maternidade Guarulhos da Hapvida agora se chama Hospital Keila Ferreira. Mesmo endereço na Av. Tiradentes: o que atende e quais planos dão acesso.`
- Principal no H1, title, URL, meta, 1º parágrafo e no H2 da HS1. Secundárias em ≥2 H2 (HS3 e HS4).

## Estrutura (entrega em bloco único)

| # | Bloco | Conteúdo | Fonte que sustenta |
|---|---|---|---|
| 0 | `<figure>` de abertura | alt e figcaption sobre a troca de nome | — (URL da imagem: pedir ao usuário) |
| 1 | Lead GEO | "O Hospital e Maternidade Guarulhos, da Hapvida, fica na Av. Tiradentes, 1015, e desde novembro de 2025 se chama Hospital Keila Ferreira." + o que o registro federal lista + público | CNES 9255826 |
| 2 | Sumário (`toc-list`) | 4 seções + FAQ + conclusão + botão de cotação → `#cotacao-1` | — |
| 3 | **HS1 — O que mudou no hospital (e o que não mudou)** `#diferencial` · fundo #f8f9fa | a troca de nome com data e motivo; quem foi Keila Ferreira; a 1ª Sala Lilás; box Resumo Rápido | 4 veículos + Saúde Business |
| 4 | **HS2 — O que o registro oficial diz que a unidade faz** `#estrutura` · branco | tradução dos códigos CNES; quadro comparativo "o que consta no registro × o que não está publicado"; reconciliação com o Rosário; 113 leitos 1× atribuído | ficha CNES + seção 6 do state file |
| 5 | `[elementor-template]` `id="cotacao-1"` + selos | — | — |
| 6 | **HS3 — Como chegar ao Hospital e Maternidade Guarulhos** `#como-chegar` · #fff8f3 | endereço + complemento 1 037; a divergência de bairro; referências a 0,1-0,2 km; o que não está publicado (ônibus, estacionamento) | ficha CNES + operadora |
| 7 | **HS4 — Quais planos dão acesso** `#planos-acesso` · #f8f9fa | rede própria × Ambulatorial; isenção de coparticipação em 1 frase; link para o guia de Guarulhos | banco |
| 8 | FAQ (8 das 10) `#faq` | todas com o nome do hospital e fonte | seção 12 |
| 9 | `[elementor-template]` final | — | — |
| 10 | Conclusão `#conclusao` + `guia-box` | síntese + "Sobre este guia" | — |
| 11 | `<style>` penúltimo · `<script>` último | — | — |

## Limites a respeitar (hospital)
4 seções · 2 formulários · ≥6 grifos animados · 6-8 FAQ · máx. 1 menção DRV · ≥4 links internos únicos (1× cada) ·
≥2 links externos · ≥150 palavras entre links · parágrafos ≤380 caracteres · ≤3 parágrafos seguidos sem quebra visual.

## Links (seção 17 do state file)
1. `/plano-hapvida-guarulhos/` — HS4 (hub)
2. `/hospital-nossa-senhora-do-rosario-hapvida/` — HS2 (alta complexidade materno-infantil)
3. `/pronto-socorro-hapvida-sp/` — HS3 ou FAQ
4. `/plano-de-saude-para-recem-nascido/` — FAQ do alojamento conjunto
Externos: ficha CNES (cnes2.datasus.gov.br) no corpo + Saúde Business ou IBGE no rodapé. **Sem ANS e sem os pillars saturados.**

## Travas que o texto tem de honrar
- Nunca "24 horas" perto de pronto-socorro. A Sala Lilás pode, com fonte.
- Nunca tomografia/colonoscopia (não constam no inventário do CNES).
- Nunca "referência em alta complexidade" para este hospital.
- Telefone: nenhum dos dois.
- 113/30/10: uma aparição, atribuída e datada, fora do lead/title/H2.
