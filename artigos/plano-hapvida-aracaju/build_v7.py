# -*- coding: utf-8 -*-
"""Reformata o artigo de Aracaju (ordem v6) para a ordem v7.4.
Nao reescreve conteudo: recorta os blocos existentes e os remonta na ordem
canonica preco-primeiro + lead-heroi. As unicas edicoes de texto sao as
apontadas em EDICOES (transicoes quebradas pela reordenacao, ano fixo e
limpeza do wpautop no <style>/<script>)."""
import re

SRC = 'artigos/plano-hapvida-aracaju/fontes/artigo-original-v6.html'
OUT = 'artigos/plano-hapvida-aracaju/artigo.html'
s = open(SRC, encoding='utf-8').read()

# ------------------------------------------------------------------ recortes
ART_OPEN = s[0:144]
TOC_OLD  = s[2295:10770]
S1       = s[10770:17360]
PRECO    = s[17360:20858]          # secao de preco, sem o formulario
FORM1    = s[20858:20989]          # comentario + div do 1o [elementor-template]
TIPOS    = s[20989:27245]
COPART   = s[27245:31945]
REDE     = s[31945:44911]
HOSP     = s[44911:52614]
COBERT   = s[52614:60503]
COMPAR   = s[60503:66949]          # inclui o 2o [elementor-template] (CTA inter)
CARENC   = s[66949:71754]
TECNO    = s[71754:76589]
CONTRAT  = s[76589:82400]
FAQ      = s[82400:101535]         # inclui o 3o [elementor-template] (CTA final)
CONCL    = s[101535:105857]
TAIL     = s[105857:]

# ------------------------------------------------------- 1. LEAD-HEROI v7.4
# Passagem citavel e metricas saem do lead original e da S1 (10 pontos, 2007,
# 130 leitos no Grageru). Nenhum dado novo.
def metrica(n, rot):
    return ('<div><div style="font-size:20px;font-weight:900;color:#fff;">%s</div>'
            '<div style="font-size:12px;color:#94a3b8;">%s</div></div>' % (n, rot))

HEROI = (
 '<div class="v5-hero-conv" style="background:linear-gradient(135deg,#1a1a2e,#16213e);'
 'border-radius:20px;padding:28px 24px;margin-bottom:4px;">'
 '<div style="font-size:12px;font-weight:700;color:#ff8533;text-transform:uppercase;'
 'letter-spacing:1px;margin-bottom:6px;">Plano Hapvida em Aracaju</div>'
 '<div style="font-size:34px;font-weight:900;color:#fff;line-height:1.1;margin-bottom:18px;">'
 'A partir de <span style="color:#ff8533;">[aracaju_menorvalor]</span>/mês</div>'
 '<p style="text-align:justify!important;font-size:18px;line-height:1.7;color:#e2e8f0;'
 'margin-bottom:16px;">O plano Hapvida em Aracaju começa em '
 '<strong style="color:#ff8533;">[aracaju_menorvalor]</strong> por mês e é o menor '
 'valor entre as operadoras que vendem plano pessoa física na capital sergipana. '
 'A rede própria soma cerca de <strong style="color:#ff8533;">10 pontos de atendimento</strong>, '
 'ancorados no Hospital e Maternidade Gabriel Soares, no Centro, em operação desde 2007 '
 '— com um novo hospital de 130 leitos anunciado no bairro Grageru.</p>'
 '<div class="v5-hero-metricas" style="display:flex!important;flex-wrap:wrap!important;'
 'gap:24px!important;margin-top:20px;padding-top:18px;border-top:1px solid rgba(255,255,255,0.15);">'
 + metrica('10', 'pontos de atendimento próprio')
 + metrica('2007', 'Hospital Gabriel Soares, no Centro')
 + metrica('130', 'leitos do novo hospital, no Grageru')
 + '</div></div>\n')

# ------------------------------------------- 2. S2↑a — H2 + contexto + TABELA
# Corta a secao de preco no shortcode da tabela: o que vem depois dele
# (box Importante + paragrafo final) desce para a S2↑b, depois do sumario.
i_tab = PRECO.index('[aracaju_menortabela]') + len('[aracaju_menortabela]')
PRECO_A = PRECO[:i_tab] + '\n</section>\n'
resto   = PRECO[i_tab:]
resto   = resto[:resto.rindex('</section>')]          # tira o fecho antigo

# ano fixo -> shortcode (Regra 5b)
PRECO_A = PRECO_A.replace('Tabela de Preços Hapvida Aracaju 2026',
                          'Tabela de Preços Hapvida Aracaju [ano_atual]')

# transicao quebrada pela reordenacao: depois da analise vem a coparticipacao
resto = resto.replace(
    'A seguir, detalhamos cada tipo de plano disponível na capital sergipana.',
    'A seguir, você vê quanto custa cada uso do plano nas duas modalidades de '
    'coparticipação praticadas em Aracaju.')

PRECO_B = ('<section style="background: #fff; padding: 20px 10px; border-radius: 20px; '
           'margin-bottom: 4px;">\n' + resto.lstrip('\n') + '\n</section>\n')

# --------------------------------------- 3. formulario id="cotacao-1" pós-sumário
FORM1 = ('<!-- 1º Formulário — [v7.1] logo APÓS o sumário, abrindo a S2↑b -->\n'
         '<div id="cotacao-1" style="margin-bottom: 4px;">[elementor-template id="11215"]</div>\n')

# ------------------------------------------------ 4. SUMÁRIO reordenado + CTA
cab = TOC_OLD[:TOC_OLD.index('<div class="toc-item"', TOC_OLD.index('toc-list'))]
itens = re.findall(r'<div class="toc-item".*?</a></div>', TOC_OLD, re.S)
cabecalho_item = re.search(r'<div class="toc-item"[^>]*><span style="min-width: 28px.*?</span></div>',
                           TOC_OLD, re.S).group(0)
por_href = {}
for it in itens:
    m = re.search(r'href="(#[^"]+)"', it)
    if m:
        por_href[m.group(1)] = it

ORDEM = ['#precos', 'CTA', '#coparticipacao', '#por-que-aracaju', '#tipos-planos',
         '#rede-propria', '#hospital-gabriel-soares', '#cobertura-regional',
         '#comparativo', '#carencias', '#tecnologia', '#contratacao', '#faq', '#conclusao']

BADGE = ('<span class="toc-badge" style="min-width: 28px; height: 28px; flex-shrink: 0!important; '
         'background: %s; border-radius: 8px; display: flex!important; align-items: center!important; '
         'justify-content: center!important; color: #fff; font-size: 13px; font-weight: bold;">%s</span>')
CTA_ITEM = ('<div class="toc-item" style="display: flex!important; align-items: center!important; '
            'gap: 10px!important; padding: 0!important; margin: 0!important;">'
            + (BADGE % ('#ff6b00', '→')) +
            '<a style="color: #ff6b00; font-weight: 800; font-size: 15px; text-decoration: none;" '
            'href="#cotacao-1">Faça uma Cotação</a></div>')

novos, n = [], 0
for chave in ORDEM:
    if chave == 'CTA':
        novos.append(CTA_ITEM)
        continue
    it = por_href[chave]
    n += 1
    it = re.sub(r'(<span class="toc-badge"[^>]*>)\d+(</span>)', r'\g<1>%d\g<2>' % n, it)
    novos.append(it)

TOC = (cab + cabecalho_item + '\n' + '\n'.join(novos) + '\n</div>\n</section>\n')
TOC = TOC.replace('Tabela de Preços Hapvida Aracaju 2026',
                  'Tabela de Preços Hapvida Aracaju [ano_atual]')

# ------------------------------- 5. S1 recebe a fonte demográfica que vinha no lead
FONTE = ('<p style="text-align: justify!important; font-size: 14px; line-height: 1.7; '
         'color: #64748b; margin-bottom: 0;">Fonte demográfica: '
         '<a style="color: #2563eb; text-decoration: underline;" '
         'href="https://www.ibge.gov.br/cidades-e-estados/se/aracaju.html" target="_blank" '
         'rel="nofollow noopener">IBGE Cidades — Aracaju</a>.</p>\n')
S1 = S1[:S1.rindex('</section>')] + FONTE + '</section>\n'

# -------------------------------------- 6. conclusão: H2 deixa de ser H2 de preço
CONCL = CONCL.replace('Hapvida em Aracaju — Menor Preço, Rede em Expansão e Cobertura Nacional',
                      'Hapvida em Aracaju — Rede em Expansão e Cobertura Nacional')

# ------------------------------------------ 7. <style>/<script>: limpar o wpautop
# O original foi colado no editor visual: o wpautop injetou <br /> dentro do
# <style> e do <script> (o que quebra a folha de estilo e o JS inteiro) e
# embaralhou os comentarios de bloco. Aqui o rodape e remontado a partir do
# conteudo real, sem <br /> e com os comentarios refeitos.
TAIL = TAIL.replace('<br />\n', '\n').replace('<br />', '')
css = TAIL[TAIL.index('html{scroll-behavior'):TAIL.index('</style>')]
js  = TAIL[TAIL.index("document.addEventListener('DOMContentLoaded'"):TAIL.index('</script>')]
TAIL = ('<!-- ══════════════════════════════════════════════ -->\n'
        '<!-- BLOCO STYLE FINAL -->\n'
        '<!-- ══════════════════════════════════════════════ -->\n'
        '<style>\n' + css.strip() + '\n</style>\n'
        '<!-- ══════════════════════════════════════════════ -->\n'
        '<!-- BLOCO SCRIPT FINAL — INTERSECTION OBSERVER + FIX COTAÇÃO -->\n'
        '<!-- ══════════════════════════════════════════════ -->\n'
        '<script>\n' + js.strip() + '\n</script>\n\n</article>')

# ---- 8. <p> de corpo na tipografia da skill (18px / line-height 1.7) --------
def tipografia(x):
    return x.replace('font-size: 17px; line-height: 1.9;', 'font-size: 18px; line-height: 1.7;')

PRECO_A, PRECO_B, COPART, S1, TIPOS = map(tipografia, (PRECO_A, PRECO_B, COPART, S1, TIPOS))
REDE, HOSP, COBERT, COMPAR = map(tipografia, (REDE, HOSP, COBERT, COMPAR))
CARENC, TECNO, CONTRAT, FAQ, CONCL = map(tipografia, (CARENC, TECNO, CONTRAT, FAQ, CONCL))

# ---- 9. quebra de <p> acima de 480 chars (checkpoint_paragrafos) -----------
# Quebra em fronteira de frase. Nenhuma palavra e alterada, acrescentada ou
# removida: so entra o fecha/abre <p>.
QUEBRA_P = '</p>\n<p style="text-align: justify!important; font-size: 18px; line-height: 1.7; margin-bottom: 16px;">'

def quebrar(x, frase):
    """Fecha o <p> logo depois de `frase` e abre outro."""
    assert x.count(frase) == 1, frase[:50]
    return x.replace(frase, frase.rstrip() + QUEBRA_P)

TIPOS = quebrar(TIPOS, 'incluindo referências locais como o Hospital Primavera no Jardins. ')
TIPOS = quebrar(TIPOS, 'enquanto o Mix inclui hospitais e clínicas credenciados. ')
REDE  = quebrar(REDE, 'está concentrada no Hospital Gabriel Soares, no Centro. ')
HOSP  = quebrar(HOSP, 'endocrinologia, ginecologia/obstetrícia e pediatria. ')
CONCL = quebrar(CONCL, 'conseguem entregar com o mesmo custo. ')

# ---- 10. break visual na HS do Gabriel Soares (checkpoint_ritmo_visual) ----
# A quebra do <p> de especialidades deixou 6 <p> seguidos. Entra um H3 no ponto
# em que a secao muda de assunto (do hospital atual para o novo do Grageru).
H3_GRAGERU = ('<h3 style="font-size:19px;font-weight:800;color:#1a202c;margin:14px 0 8px 0;">'
              'O novo hospital do Grageru</h3>\n')
alvo = '<p style="text-align: justify!important; font-size: 18px; line-height: 1.7; margin-bottom: 16px;">O anúncio do novo hospital no Grageru'
assert HOSP.count(alvo) == 1
HOSP = HOSP.replace(alvo, H3_GRAGERU + alvo)

# ---- 11. nota de atualizacao: ano fixo -> shortcode (Regra 5b) -------------
assert CONCL.count('Dados de preços atualizados em 2026.') == 1
CONCL = CONCL.replace('Dados de preços atualizados em 2026.',
                      'Dados de preços atualizados em [mes_atual] de [ano_atual].')

# ------------------------------------------------------------------ montagem
partes = [ART_OPEN, HEROI, PRECO_A, TOC, FORM1, PRECO_B, COPART, S1, TIPOS,
          REDE, HOSP, COBERT, COMPAR, CARENC, TECNO, CONTRAT, FAQ, CONCL, TAIL]
out = ''.join(partes)
open(OUT, 'w', encoding='utf-8').write(out)
print('escrito:', OUT, len(out), 'chars (original:', len(s), ')')
