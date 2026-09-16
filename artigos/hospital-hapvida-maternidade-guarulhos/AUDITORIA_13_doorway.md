# AUDITORIA 13 — ANTI-DOORWAY
**Objeto:** `artigo.html` (Hospital e Maternidade Guarulhos / Hospital Keila Ferreira)
**Comparado contra:** artigo de cidade publicado `/plano-hapvida-guarulhos/` (fontes/artigo-cidade-guarulhos.html), seção 16 do state file, banco (overlaps_doorway, catálogo FAQ, artigos-irmãos Salvalus e N. Sra. do Rosário).
**Data da auditoria:** 2026-09-16

---

## 1. Teste de substituição (Guarulhos → Osasco; Hospital e Maternidade Guarulhos → outro hospital)

Contagem de `<p>` de corpo no `artigo.html`: 50 (inclui boxes e respostas de FAQ).

**Parágrafos que SOBREVIVEM à substituição (genéricos, sem âncora local/hospitalar):**
- Box "Fonte oficial" — Lei 9.656/98 (segmentação): citação de lei federal, válida em qualquer cidade/hospital.
- Box "Fonte oficial" — Lei 10.778/2003 (notificação compulsória): idem, genérica.
- "Não existe fonte pública que liste, produto por produto, quais planos incluem esta unidade..." (planos-acesso, abertura) — molde reaproveitável para qualquer hospital.
- "Planos com cobertura de internação em rede própria internam em unidade própria, e este hospital é rede própria..." — silogismo genérico, só a cláusula final ancora.
- "Nenhuma página oficial publica a lista de produtos que incluem esta unidade na rede..." — disclaimer padrão.
- Box "DICA DRV" (planos-acesso) — conselho genérico ("procure a unidade no guia médico... pelo nome novo e pelo antigo"), reaproveitável.
- Box "Antes de ir à unidade" (como-chegar) — canais oficiais (app, central Sul/Sudeste/Centro-Oeste): texto-padrão de voz da casa, sem âncora de Guarulhos.
- "O que não está publicado, este guia não inventa..." (como-chegar) — frase de disclaimer editorial, molde da série.
- Fechamento da conclusão: "Antes de procurar a unidade, confirme pelo canal oficial o serviço e o horário. Antes de contratar, confira a rede do plano no guia médico..." — genérico.
- "Ter o serviço registrado é uma coisa; ser a porta de entrada da rede para o caso mais grave é outra" (estrutura) — moldura analítica reaproveitável (a âncora entra só na cláusula seguinte, que nomeia o Rosário).

**Total estimado:** ~9-10 parágrafos/boxes genéricos em 50 (≈ 18-20% do corpo, folgadamente abaixo do limite de 45%). Nenhuma seção inteira ficou sem âncora — todas (lead, diferencial, estrutura, como-chegar, planos-acesso, FAQ, conclusão) têm maioria de conteúdo amarrado a CNES 9255826, ao endereço, à data de novembro/2025, a Keila Ferreira ou à Sala Lilás.

**Veredito do item 1: 🟢** — dentro do limite, sem seção "oca".

---

## 2. Matriz de sobreposição com o artigo de cidade (seção a seção)

| Seção do artigo novo | Seção do artigo de cidade | Overlap literal (≥40 palavras) | Conteúdo condensado (mesmo fato, outra forma) | Veredito |
|---|---|---|---|---|
| Lead | Lead / S1 | 0% | Baixo — lead novo é sobre a troca de nome, não sobre a cidade | 🟢 |
| `#diferencial` (renomeação, Keila Ferreira, Sala Lilás) | S4 (linha do tempo) / S6 (comparação concorrentes) | 0% | Baixo — cidade não menciona Sala Lilás nem a biografia; narra só "2025: renomeado" em 1 linha na timeline | 🟢 |
| `#estrutura` (ficha CNES, códigos, salas, leitos) | S4 — card "Hospital Keila Ferreira" (lista curta de serviços) | 0% (nenhum n-grama ≥8 palavras em comum) | **Médio** — o card da cidade resume em 1 frase (internação clínica/cirúrgica, maternidade, centro cirúrgico, UTI, pronto-atendimento, diagnóstico); a HS2 do artigo novo relista as MESMAS categorias em versão detalhada de CNES (parto, UTI adulto/neonatal, 4 PS, salas de cirurgia, leitos). O state file (seção 16) mandava aprofundar SÓ o fluxo do pronto-atendimento — a seção foi além disso e recobriu o terreno inteiro do card, só que em grão mais fino | 🟡 |
| `#como-chegar` (endereço, divergência de bairro) | S4 (endereço no card) / S5 (tabela bairro×tempo) | 0% | Baixo — endereço aparece 1× (conforme plano), sem repetir a tabela de bairros/tempos nem os 12 km do aeroporto (FAQ 12 da cidade) | 🟢 |
| `#planos-acesso` (segmentação, Ambulatorial não cobre internação, clínicas de apoio) | S3 (Nosso Plano/Mix/Ambulatorial descritos) / S6 (comparação concorrentes) | 0% | Baixo — não descreve os produtos, só cita os 3 nomes e a regra de segmentação (ponte, não descrição) | 🟢 |
| `#faq` (8 perguntas) | `#faq` (15 perguntas) + catálogo do banco | 0% literal | Ver seção 3 abaixo | ver 3 |
| `#conclusao` | `#conclusao` (S9 da cidade) | 0% | Baixo — a cidade fecha com estatísticas de rede/preço; o artigo novo fecha com "hospital, dois nomes, uma ponte" | 🟢 |

**Checagem automatizada (n-gramas de 5-8 palavras, corpo inteiro, excluindo CSS/JS):** nenhum trecho de 8+ palavras idêntico entre os dois artigos fora do CSS/JS compartilhado (esperado, é o mesmo template). Únicos hits de 5-7 palavras: "≡ Neste Guia Você Vai Encontrar" (rótulo de UI do sumário, não é conteúdo) e a fórmula de rodapé "em [mes_atual] de [ano_atual]. Preços sujeitos a" (disclaimer padrão da série). Nenhum overlap de conteúdo substantivo.

**Achado extra (fora do escopo estrito, mas relevante):** a frase-fato "a referência [da rede / é o Hospital] ... N. Sra. do Rosário ... UTI neonatal de alta complexidade" aparece 2× no artigo novo (HS2 e FAQ6) e 1× na cidade (FAQ2), sempre reafirmando que o Rosário é a referência de alta complexidade materno-infantil. Isso **não é doorway** (é uma remissão factual necessária, com forma diferente cada vez), mas há um risco de exatidão: o artigo-irmão `hospital-nossa-senhora-do-rosario-hapvida` (consultado via `consultar_artigo`) registra que a **maternidade e o PS de ginecologia/obstetrícia do Rosário foram ENCERRADOS em 06/10/2025** — ou seja, a alegação de que ele é referência para parto de alto risco / UTI neonatal pode estar desatualizada tanto no artigo novo quanto no artigo de cidade. Não é achado de doorway, mas merece checagem YMYL antes de publicar.

---

## 3. FAQ — teste de overlap (8 novas × 15 da cidade × catálogo do banco)

| # | Pergunta nova | Overlap com FAQ queimada da cidade? | Overlap com catálogo (`consultar_faqs_catalogo`, categoria hospital)? |
|---|---|---|---|
| 1 | Mudou de nome? | Não (tema exclusivo do artigo novo) | Não |
| 2 | Quem foi Keila Ferreira? | Não | Não |
| 3 | O que é a Sala Lilás? | Não (cidade não cita Sala Lilás) | Não |
| 4 | Mulher sem plano é atendida na Sala Lilás? | Não | Não |
| 5 | Que tipos de PS tem registrados? | **Parcial** — não é a mesma pergunta da FAQ 9 queimada ("tem pronto-atendimento 24h na cidade?"), mas a resposta reutiliza quase a mesma cláusula de fechamento que a FAQ 9 da cidade ("fora do horário comercial... ortopedia de urgência... pronto-socorro Hapvida ... capital") — ver trecho abaixo | Não é nenhum dos templates id 10-20 |
| 6 | Bebê fica no mesmo quarto da mãe? | Não (ângulo de alojamento conjunto, não coberto na cidade) | Não é o template id 12 ("tem maternidade ativa?") — pergunta é sobre rooming-in, mais específica |
| 7 | Em que bairro fica? | Não | Não |
| 8 | Como agendar consulta/exame? | Não | Não |

**Overlap literal com as 6 FAQ queimadas da seção 16:** ZERO — nenhuma das 8 perguntas novas repete, nem reformulada, as 6 queimadas ("tem maternidade e UTI neonatal?", "diferença hospital×clínicas", "pronto-atendimento 24h?", "tempo do GRU", "atende Arujá/Itaquaquecetuba?", "segundo hospital já inaugurado?").

**Trecho quase-duplicado (não é FAQ inteira, é uma cláusula dentro da resposta):**
- FAQ 9 da cidade: *"Para atendimento especializado fora do horário comercial, como ortopedia de urgência, o beneficiário pode acessar o pronto-socorro Hapvida em SP capital, onde unidades como o Salvalus e o Bosque da Saúde operam 24h..."*
- FAQ 5 do artigo novo: *"...Fora do horário comercial, o encaminhamento da rede para ortopedia de urgência continua sendo o pronto-socorro Hapvida na capital."*
- A mesma cláusula também aparece no box "Importante" da seção `#estrutura` do próprio artigo novo (repetição interna, 2×).
- **Correção proposta:** manter (é o mesmo fato correto e a redundância é <40 palavras, não é doorway), mas cortar uma das duas ocorrências internas no próprio artigo novo (box "Importante" x FAQ 5) para reduzir repetição redundante — bridge/corte, não reescrita.

**Veredito do item 3: 🟢** — zero overlap de FAQ propriamente dito; a única observação é uma cláusula de fechamento repetida, fato correto e curto, não caracteriza doorway.

---

## 4. Caça-clichê

Busca literal pelas 5 frases-gatilho do prompt ("modelo verticalizado", "rede própria sempre que possível", "atendimento de qualidade", "como qualquer plano regulado pela ANS", "tranquilidade para você e sua família"): **zero ocorrências** no `artigo.html`.

Não encontrado nenhum discurso genérico de operadora do tipo listado. O texto é predominantemente factual (códigos CNES, datas, nomes), o que reduz naturalmente o risco de clichê.

Ressalva (não são os clichês listados, mas são fórmulas reaproveitáveis da série, ver item 1): o box "Antes de ir à unidade", a frase "O que não está publicado, este guia não inventa" e o box "DICA DRV" são molduras de voz-da-casa que sobrevivem à troca de hospital — aceitável como padrão de série, mas contam para o teto de 45% do item 1.

---

## 5. Title e meta — teste de substituição

- **Title:** "Hospital e Maternidade Guarulhos Hapvida: agora Keila Ferreira" — cita os dois nomes específicos do hospital; **não sobrevive** à troca por outro hospital sem reescrita completa. 🟢
- **Meta:** "O Hospital e Maternidade Guarulhos da Hapvida agora se chama Hospital Keila Ferreira. Mesmo endereço na Av. Tiradentes: o que atende e quais planos dão acesso." — cita nome antigo, nome novo e o logradouro; **não sobrevive** à substituição. 🟢

**Veredito do item 5: 🟢**

---

## 6. Canibalização

O artigo de cidade (`/plano-hapvida-guarulhos/`) dispara para intenção **comercial/transacional de escopo municipal** — preço, modalidades, rede completa da cidade, comparação com concorrentes, "como contratar". Já responde, en passant, a 3 perguntas sobre o hospital (FAQ 2, 8, 9) e tem um card de serviços na S4.

O artigo novo dispara para intenção **informacional/de desambiguação de entidade** — "o Hospital e Maternidade Guarulhos virou o quê?", "quem é Keila Ferreira", "o que é a Sala Lilás", ficha oficial do CNES. É um ângulo de notícia/identidade que a cidade não cobre (a cidade nem menciona a Sala Lilás nem a troca de nome além de 1 linha na timeline).

**Ponto de atrito real:** consultas do tipo "Hospital Keila Ferreira tem maternidade e UTI neonatal" podem satisfazer tanto a FAQ 2 da cidade quanto a FAQ 6 do artigo novo (embora com ângulos diferentes — a da cidade responde direto "sim, tem"; a nova fala de alojamento conjunto/leitos). Risco de canibalização nessa consulta pontual é **baixo-moderado**, não killer.

**Veredito do item 6: 🟡 (risco baixo-moderado, monitorar)** — intenções primárias são distintas; a única zona cinzenta é a pergunta "tem maternidade/UTI neonatal", coberta por ambos com ângulos diferentes.

---

## VEREDITO FINAL: 🟡

O artigo new **passa** nos testes mais duros do escopo do state file: zero overlap literal ≥40 palavras, zero overlap de FAQ (nenhuma das 6 queimadas repetida), endereço citado 1× só, linha do tempo reduzida ao episódio de 2025, nenhuma comparação com concorrentes repetida, coparticipação em 1 frase, tabela de bairros não reproduzida, produtos não descritos, nenhum clichê genérico de operadora. O risco ALTO sinalizado na seção 16 do state file foi, na prática, bem mitigado.

Os pontos que impedem o 🟢 pleno:
1. A seção `#estrutura` (HS2) recobre o terreno inteiro do card de serviços da cidade (S4) em vez de aprofundar só o fluxo do pronto-atendimento, como o state file mandava — não é overlap literal, mas é desvio do plano e dobra a exposição do mesmo assunto (parto/UTI/PS/cirurgia) em formato mais granular.
2. Repetição interna (não com a cidade) da cláusula sobre redirecionamento a ortopedia de urgência na capital, 2× dentro do próprio artigo novo mais 1× análoga na cidade.
3. ~9-10 parágrafos/boxes de voz-de-casa genérica (disclaimers, caixas de lei, "dica DRV") que sobrevivem à substituição — dentro do teto de 45%, mas seria saudável cortar 2-3 para reforçar o índice de conteúdo local.
4. Achado colateral de exatidão (não-doorway): a referência ao Hospital N. Sra. do Rosário como ponto de parto de alto risco/UTI neonatal pode estar desatualizada — a maternidade do Rosário foi encerrada em 06/10/2025 segundo o próprio artigo-irmão no banco.

**Nenhum item obriga reescrita total.** Recomendação: revisar a HS2 para focar no PS (cortar/condensar a relistagem completa de serviços), cortar uma das duas ocorrências da cláusula de redirecionamento à capital, e — antes da publicação — confirmar com o time se a referência ao Rosário para parto de alto risco ainda procede após o fechamento de outubro/2025.
