# Análise de construção — página infantil do concorrente (08/09/2026)

Concorrente: `descontoplanodesaude.com.br/plano-hapvida-infantil/` (nota 14 do banco).
Minha página: `/plano-de-saude-hapvida-infantil/`.

**Eixo:** duas escolas. Ela faz página-monólito (27 H2, cobertura de toda a jornada,
linguagem sem afirmação absoluta). Eu faço nó de cluster (7 H2, tema profundo
delegado a hub, dado exato).

**Técnicas dela, medidas no HTML:** bloco padronizado (H2 + linha-resumo + 3
parágrafos); 27 H2 / 15 H3 cobrindo cauda longa (viagem, sazonalidade, gêmeos,
erros comuns); FAQ de 15 perguntas com resposta de 1-2 frases; 3 caixas "Fonte
oficial" com link para Lei 9.656/98 e ANS; faixa de 4 números citáveis; hospitais
pediátricos nomeados; bloco de autor + "Sobre este guia"; 36 "costuma" (blindagem
YMYL); keyword exata 33x, 19 em negrito; preço em faixa aproximada (4 referências,
sem tabela).

**Minha página:** 19 valores exatos em R$, 4 cidades, Art. 12 da Lei 9.656/98,
RN 566/2022, ANS 359017, 27 links internos, FAQPage + 5 tipos de schema.

**A copiar:** linha-resumo sob cada H2; nomear hospitais pediátricos (tenho página
própria de vários); caixa de fonte oficial com link externo; ampliar FAQ para a
cauda dela; bloco de autor e declaração de fontes. **Não copiar:** keyword em
negrito 19x; e nenhuma das seções cujo tema tem hub próprio.

**Sete menções sem link na minha página** (destinos existentes e subutilizados):
teleconsulta-hapvida, aplicativo-hapvida, plano-odontologico-hapvida,
hapvida-cobre-fisioterapia, hapvida-cobre-psicologo, convenio-medico-para-mei,
hospital-mandacaru-hapvida-recife. Hubs de carência (53), coparticipação (59) e
contratar (27) estão SATURADOS — não linkar mais.

## Correções de afirmações anteriores desta sessão

1. "A página dela não traz nenhum valor em R$" — FALSO. Traz R$ 150-160
   (individual) e ~R$ 100 (empresarial). O teste rodou sobre um recorte de 9.000
   caracteres e a seção de preço estava fora dele.
2. "Falta tabela de carência na minha página" — não é lacuna: a página linka o hub
   `/plano-de-saude-hapvida-carencia/`. É o anti-doorway funcionando.

Documento visual: `comparativo.html`.
Textos completos das duas páginas: `dados/*.md`. Extração on-page: `dados/*.jsonl`.
CI-1: rota 2 (workflow n8n `NUUZmP5y4AtFb2jL`) — egress externo bloqueado.
