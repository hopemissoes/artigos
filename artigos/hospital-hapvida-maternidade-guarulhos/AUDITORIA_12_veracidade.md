# AUDITORIA 12 — Veracidade Factual
## hospital-hapvida-maternidade-guarulhos/artigo.html

Auditor: Agente 12 (Modo 1 — auditoria, não edita)
Data: 2026-09-16
Fontes da verdade usadas (fechadas, nenhuma outra consultada — rede externa bloqueada nesta sessão):
1. `PESQUISA_hospital-hapvida-maternidade-guarulhos_COMPLETO.md`
2. `fontes/ci1-rodada2-fontes-primarias.md`
3. `fontes/ci1-extracao-n8n.json`
4. `fontes/ci1-rodada3.json`
5. `fontes/artigo-cidade-guarulhos.html` (para o item 5, consistência interna)

---

## Método

Toda afirmação verificável do HTML foi extraída (números, códigos CNES, nomes, datas, endereços,
cargos, citações atribuídas, superlativos) e conferida contra as fontes acima, trecho literal a
trecho literal. Também foi rodada uma varredura de `FORBIDDEN_TOKENS` (seção 9 do state file) e uma
comparação linha a linha com `artigo-cidade-guarulhos.html` nos pontos que o próprio state file
(seção 16) marcou como zona de risco de contradição.

---

## Tabela completa

### A. Códigos CNES (item de atenção especial do editor-chefe)

| Código | Tradução no artigo | Fonte (`ci1-rodada2-fontes-primarias.md`, transcrição literal) | Status |
|---|---|---|---|
| 112-003 | "parto" | "112-003 PARTO" | ✅ |
| 112-004 | "parto em gestação de alto risco" | "112-004 PARTO EM GESTACAO DE ALTO RISCO" | ✅ |
| 162-001 | "UTI adulto" | "162-001 ADULTO" (sob SERVICO DE TERAPIA INTENSIVA) | ✅ |
| 162-002 | "UTI neonatal" | "162-002 NEONATAL" | ✅ |
| 140-019 | "pronto-socorro geral/clínico" | "140-019 PRONTO SOCORRO GERAL/CLINICO" | ✅ |
| 140-013 | "PS obstétrico" | "140-013 PRONTO SOCORRO OBSTETRICO" | ✅ |
| 140-012 | "PS pediátrico" | "140-012 PRONTO SOCORRO PEDIATRICO" | ✅ |
| 140-016 | "PS traumato-ortopédico" | "140-016 PRONTO SOCORRO TRAUMATO ORTOPEDICO" | ✅ |
| 142-001, 121-001, 125-006 | citados só por nome ("endoscopia digestiva", "radiologia", "farmácia hospitalar"), sem o código na prosa | fonte confirma os três nomes | ✅ (sem risco de tradução errada — o artigo não expõe o código, só o nome) |

Todos os 8 códigos expostos no corpo/FAQ estão traduzidos corretamente. Nenhum erro de tradução de
código encontrado.

### B. Contagens por extenso

| Contagem no artigo | Fonte literal | Status |
|---|---|---|
| "cinco salas de cirurgia" | "SALA DE CIRURGIA 5" | ✅ |
| "treze leitos de alojamento conjunto" | "LEITOS DE ALOJAMENTO CONJUNTO 13" | ✅ |
| "oito leitos de recém-nascido patológico" | "LEITOS RN PATOLOGICO 8" | ✅ |
| "duas salas de acolhimento com classificação de risco" | "SALA DE ACOLHIMENTO COM CLASSIFICACAO DE RISCO 2" | ✅ |
| "quatro tipos de pronto-socorro" | 4 códigos 140-xxx listados | ✅ |
| "11 consultórios" | "CONSULTORIOS MEDICOS 11" | ✅ |
| "1 de recuperação, 1 de pré-parto, 1 de parto normal" | "SALA DE RECUPERACAO 1 · SALA DE PRE-PARTO 1 · SALA DE PARTO NORMAL 1" | ✅ |
| "16 incubadoras, 8 berços aquecidos, 5 aparelhos de fototerapia" | "Incubadora 16 · Berço Aquecido 8 · Fototerapia 5" | ✅ |
| sala de gesso, brinquedoteca | "SALA DE GESSO 1 · BRINQUEDOTECA 1" | ✅ |

Todas as contagens batem exatamente com a ficha.

### C. Datas

| Afirmação | Fonte | Status |
|---|---|---|
| Sala Lilás inaugurada em 10/11/2025 | Guarulhos Todo Dia ("segunda-feira (10)"), Guarulhos Online (10/11), Jornal Exempplar ("nesta segunda-feira (10)") | ✅ |
| Morte da bispa em fevereiro de 2025 | Guarulhos Todo Dia: "morreu... vítima de infarto fulminante" + "fevereiro deste ano" (matéria de nov/2025) | ✅ |
| **"Em 10 e 11 de novembro de 2025, o Hospital... passou a se chamar Hospital Keila Ferreira" (HS1 e FAQ 1)** | O evento (troca de nome) aconteceu em 10/11, junto com a Sala Lilás. Guarulhos Todo Dia **publicou** em 11/11. Click Guarulhos **publicou** em 12/11 — e é a fonte citada para o dado "prefeito Lucas Sanches sugeriu o nome", usado no mesmo parágrafo. | ⚠️ **O artigo funde data do acontecimento com datas de publicação e omite 12/11**, justamente a data da matéria de onde vem um dado citado ao lado ("conforme apuração do Click Guarulhos"). Não é dado errado, é imprecisão: dizer "10 e 11" sugere que a troca ocorreu em dois dias, quando na verdade ocorreu em 10/11 e foi noticiada em 10, 11 e 12/11 por veículos diferentes. Correção sugerida: "em novembro de 2025" no corpo, com as datas específicas de cada matéria só na nota "Sobre este guia" ou nas âncoras dos links. |

### D. Nomes próprios e citações atribuídas

| Nome/citação | Uso no artigo | Fonte | Status |
|---|---|---|---|
| Keila Ferreira — bispa, liderava Assembleia de Deus no Brás | HS1, FAQ 2 | Guarulhos Todo Dia | ✅ |
| Keila Ferreira presidia Ciben, Corafesp, Ideas | HS1, FAQ 2 | Click Guarulhos (nomes por extenso das siglas) | ✅ |
| morte por infarto fulminante, fev/2025 | HS1, FAQ 2 | Guarulhos Todo Dia | ✅ |
| nome sugerido pelo prefeito Lucas Sanches, "conforme apuração do Click Guarulhos" | HS1, FAQ 2 | Click Guarulhos: "O Click Guarulhos apurou que o nome foi sugerido pelo prefeito Lucas Sanches (PL) ao grupo Hapvida" | ✅ |
| Samuel Ferreira (marido) | **não usado no artigo** | só consta em oitapecericano.com.br; o state file exigia atribuição explícita a essa fonte se entrasse | ✅ decisão correta — não entrou, e por isso não precisa da atribuição de fonte única |
| Christine Marques, Gustavo Ribeiro, Fuad Massabki Junior, Instituto Nós por Elas | **não usados no artigo** | constam nas fontes, mas o artigo não os cita | — (nada a auditar: nenhuma afirmação feita sobre eles) |
| "primeira Sala Lilás da rede privada do país" atribuída ao Saúde Business | lead (implícito), HS1, FAQ 3, conclusão | Saúde Business, 13/11/2025: "a primeira da rede privada, no Brasil" | ✅ atribuição correta — é a fonte setorial mais forte, e o artigo não afirma isso como fato do mundo, só "descreve como" |
| "Segundo a Hapvida, ele opera 24 horas por dia" | HS1 | Guarulhos Todo Dia, citando divulgação da operadora: "funciona 24 horas por dia" | ✅ corretamente atribuído, e distante da expressão "pronto-socorro" (regra do FORBIDDEN_TOKENS respeitada) |

### E. Endereço e CNES cadastral

| Afirmação | Fonte | Status |
|---|---|---|
| CNES 9255826 | ficha CNES, todas as fontes | ✅ |
| Av. Tiradentes, 1015, complemento "1 037" | ficha CNES | ✅ |
| Bairro no CNES = Jardim Guarulhos; site/imprensa = Jardim Santa Edwirges | ficha CNES × gndi.com.br × oitapecericano.com.br | ✅ divergência corretamente registrada e explicada, não escondida |
| Nome empresarial NOTRE DAME INTERMEDICA SAUDE S A | ficha CNES (seção 3 do state file) | ✅ (usado como base do item 4, abaixo — não aparece escrito no corpo do artigo) |
| Eixo "Av. Tiradentes corta a região central de Guarulhos" | Guarulhos Todo Dia: "fica na Av. Tiradentes, 1015, na região central de Guarulhos" | ✅ |

### F. Selos de confiança e citações legais

| Item | Status |
|---|---|
| "Operadora registrada na ANS — nº 359017" (aparece 2×) | ⚠️ ver item 4, abaixo — decisão isolada |
| "DRV: 11 anos especialista Hapvida" | ✅ consistente com o dado padrão da casa (skill `hapvida-data`); não é "10 anos" (token proibido) |
| "7.000+ clientes atendidos" | não aparece em nenhuma das 4 fontes desta auditoria — é credencial de estoque do template (`components.md`), fora do escopo verificável aqui. Não é dado YMYL de saúde; não bloqueia. |
| Caixa "Fonte oficial" — Lei 9.656/98 (segmentações) | ⚠️ ver abaixo |
| Caixa "Fonte oficial" — Lei 10.778/2003 (notificação compulsória) | ⚠️ ver abaixo |

**Achado sobre as duas caixas "Fonte oficial":** nenhuma das duas leis (9.656/98 e 10.778/2003), nem
os links para planalto.gov.br, aparecem em qualquer um dos quatro arquivos-fonte desta auditoria
(`PESQUISA_...COMPLETO.md`, `ci1-rodada2-fontes-primarias.md`, `ci1-extracao-n8n.json`,
`ci1-rodada3.json`). O conteúdo descrito é compatível com o que essas leis dizem (9.656/98 define as
segmentações do plano, inclusive a ambulatorial; 10.778/2003 trata da notificação compulsória de
violência contra a mulher em serviço de saúde), mas isso é conhecimento geral do auditor, não uma
conferência contra fonte primária lida nesta produção — e a regra 6 do `CLAUDE.md` deste repositório
é explícita: **"Não está no state file conferido → não escreve."** Recomendação: antes de publicar,
rodar essas duas citações pela skill `hapvida-regulatory` (ou registrá-las no state file com o
trecho literal da lei) para que passem a ter lastro dentro da produção. Não é um erro de fato — é um
processo de verificação pulado.

### G. Consistência interna com o artigo de cidade (`fontes/artigo-cidade-guarulhos.html`)

| Ponto de risco (apontado pelo próprio state file, seção 16, como zona de contradição) | Artigo de cidade (publicado) | Artigo novo | Status |
|---|---|---|---|
| Parto de alto risco / UTI neonatal de alta complexidade | FAQ 2: "Para partos de alto risco ou UTI neonatal de alta complexidade, a referência é o Hospital e Maternidade N. Sra. do Rosário (Vila Maria, SP capital)" | HS2: "O CNES diz que parto de alto risco e UTI neonatal existem aqui. Para a gestação de maior risco e para a UTI neonatal de alta complexidade, a referência da rede continua sendo o Hospital N. Sra. do Rosário, na capital." | ✅ sem contradição — a reconciliação obrigatória (achado 🔴 do juiz P-B) foi cumprida: o registro é uma coisa, a referência de alta complexidade é outra, e as duas convivem exatamente como o state file exigia |
| Urgência ortopédica fora do horário comercial | FAQ 9: "Para atendimento especializado fora do horário comercial, como ortopedia de urgência, o beneficiário pode acessar o pronto-socorro Hapvida em SP capital, onde unidades como o Salvalus e o Bosque da Saúde operam 24h" | Box "Importante" da HS2: "O CNES mostra que o pronto-socorro traumato-ortopédico existe aqui, mas não informa o horário... fora do horário comercial, o encaminhamento da rede para ortopedia de urgência continua sendo o pronto-socorro Hapvida em São Paulo" | ✅ sem contradição — cumpre a reconciliação obrigatória (achado 🔴 do juiz P-A, rodada 2): nunca afirma que a unidade resolve ortopedia de urgência a qualquer hora |
| Mudança de nome | FAQ 8 / card: "Hospital Keila Ferreira (ex-Hospital e Maternidade GRU)" — citado de passagem, sem data, motivo ou fonte | Artigo novo: eixo inteiro do texto, com data, motivo (homenagem), fonte (CNES + imprensa) | ✅ consistente — o state file já previa que o de cidade trata isso de raspão e o novo é que aprofunda; não há contradição, só complementaridade |
| Repetição de conteúdo do artigo de cidade proibida pela matriz da seção 16 | linha do tempo (2012/2022/2025), tabela de bairros e tempos, mecânica de coparticipação, descrição de produtos, dados da Clínica Jardim (jun/2025, R$ 1,3 mi) | nenhum desses blocos aparece no artigo novo | ✅ anti-doorway respeitado |

Nenhuma contradição 🔴 encontrada contra o artigo de cidade.

---

## Item 4 — Selo ANS 359017 (achado do editor-chefe)

**Fatos verificados nas fontes desta auditoria:**
- A ficha CNES 9255826 registra o nome empresarial da unidade como **NOTRE DAME INTERMEDICA SAUDE S A**
  (`PESQUISA...md`, seção 3, e `ci1-rodada2-fontes-primarias.md`, item 1) — isso é conferido e sólido.
- A correspondência "359017 = NotreDame Intermédica" e "368253 = Hapvida Assistência Médica" **não está
  em nenhuma das quatro fontes desta auditoria** — foi trazida pelo editor-chefe como fato dado, fora do
  conjunto fechado de fontes. Não pude confirmá-la de forma independente nesta sessão (rede externa
  bloqueada; o cadastro de operadoras da ANS não está entre as fontes listadas para este trabalho).

**Decisão, combinando as duas coisas:** o selo já publicado no artigo diz "nº 359017" — e, **se a
correspondência do editor-chefe estiver certa**, 359017 é exatamente o número que corresponde ao CNPJ
que o CNES confirma para esta unidade (NotreDame Intermédica). Ou seja, **o número que já está no
artigo é o correto para esta unidade específica, e não precisa mudar para 368253** — trocar para
368253 (Hapvida Assistência Médica) introduziria o erro que o editor-chefe estava tentando evitar,
porque a operadora que responde legalmente por este CNPJ/hospital é a NotreDame Intermédica, não a
Hapvside Assistência Médica.

**Ressalva que preciso registrar:** essa conclusão depende de um dado (o mapeamento 359017/368253) que
está fora do meu conjunto de fontes auditáveis nesta tarefa. Antes de considerar o item fechado,
recomendo que alguém com acesso à consulta de operadoras da ANS (ans.gov.br/gov-br/pt-br ou o
conector de banco `banco-tabelaplanos`, se ele guardar esse dado canônico) confirme os dois números.
Não é um bloqueio — é uma verificação de segunda camada que esta auditoria, sozinha, não consegue
fechar com uma fonte primária lida.

---

## Veredito

🟡 **AJUSTAR** — não bloqueia.

Todos os dados YMYL centrais (códigos CNES, contagens de leitos/salas/equipamentos, o que a unidade
tem registrado vs. o que não tem, os dois pontos de reconciliação obrigatória com o artigo de cidade —
parto de alto risco/UTI neonatal e urgência ortopédica) conferem exatamente com as fontes primárias e
não contradizem o artigo publicado. Nenhum `FORBIDDEN_TOKEN` foi encontrado no texto.

Antes de publicar, ajustar três pontos, nenhum deles um erro de dado, os três evitáveis:
1. Suavizar "10 e 11 de novembro de 2025" para não confundir data do acontecimento com datas de
   publicação das matérias (a matéria de 12/11 nem é citada nessa frase, mas é a fonte de um dado ao
   lado).
2. Lastrear as duas caixas "Fonte oficial" (Lei 9.656/98 e Lei 10.778/2003) no state file, via skill
   `hapvida-regulatory`, ou removê-las até estarem lastreadas — hoje elas não vêm de nenhuma das quatro
   fontes designadas para esta produção.
3. Confirmar o mapeamento 359017/368253 numa fonte primária (ANS) antes de tratar o item 4 como
   definitivamente fechado — a leitura desta auditoria é que **o número já publicado (359017) é o
   correto e não deve virar 368253**, mas essa conclusão herda a incerteza da fonte que a sustenta.

Nota à parte, fora do escopo de veracidade: a FAQ entregue tem 8 perguntas; o state file (seção 12)
planejava 10. Não é erro factual — as duas que faltam ("quantas salas de cirurgia" e "quais planos dão
acesso", ambas já respondidas no corpo do artigo) não geram dado errado nem contradição, só um
descompasso entre o planejado e o entregue que o editor pode considerar aceitável ou não.
