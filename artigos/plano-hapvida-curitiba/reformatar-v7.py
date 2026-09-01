# -*- coding: utf-8 -*-
"""Reordena o artigo de Curitiba para a ordem V7.4 (preco-primeiro + lead-heroi).
NAO altera texto, dado, shortcode nem link. So move blocos e cria o heroi a
partir do lead que ja existia."""
import re, sys

src = open('artigo-ORIGINAL.html', encoding='utf-8').read()

def cut(a, b=None):
    return src[a:b] if b is not None else src[a:]

ART_OPEN = cut(0, 126)
INTRO    = cut(126, 2192)
TOC      = cut(2192, 10515)
S1       = cut(10515, 16625)
S2       = cut(16625, 22877)
FORM1    = cut(22877, 22989)
S3       = cut(22989, 27541)
S4COPART = cut(27541, 31139)
S5REDE   = cut(31139, 42259)
S6HOSP   = cut(42259, 47340)
S7COB    = cut(47340, 53573)
S8COMP   = cut(53573, 57888)
CTAINT   = cut(57888, 58000)
S9CAR    = cut(58000, 65731)
S10TEC   = cut(65731, 69627)
S11CON   = cut(69627, 74956)
FAQ      = cut(74956, 92698)
CTAFIN   = cut(92698, 92802)
CONCL    = cut(92802, 97383)
TAIL     = cut(97383)

assert ART_OPEN.startswith('<article'), ART_OPEN[:40]
assert 'INTRODU' in INTRO[:60] and INTRO.rstrip().endswith('</section>')
assert 'SUMÁRIO' in TOC[:60] and TOC.rstrip().endswith('</section>')
for name, blk, needle in [('S1', S1, 'por-que-curitiba'), ('S2', S2, 'id="precos"'),
                          ('S3', S3, 'tipos-planos'), ('S4', S4COPART, 'coparticipacao'),
                          ('S5', S5REDE, 'rede-propria'), ('S6', S6HOSP, 'hospital-onix'),
                          ('S7', S7COB, 'cobertura-regional'), ('S8', S8COMP, 'comparativo'),
                          ('S9', S9CAR, 'carencias'), ('S10', S10TEC, 'tecnologia'),
                          ('S11', S11CON, 'contratacao'), ('FAQ', FAQ, 'id="faq"'),
                          ('CONCL', CONCL, 'conclusao')]:
    assert needle in blk, (name, blk[:120])
    assert blk.rstrip().endswith('</section>'), (name, blk[-80:])
assert 'elementor-template' in FORM1 and 'elementor-template' in CTAINT and 'elementor-template' in CTAFIN
assert TAIL.startswith('<style>') and TAIL.rstrip().endswith('</article>')

# ---------------------------------------------------------------- 1. LEAD-HEROI
# A passagem citavel e os 3 numeros vem, sem excecao, do texto que ja estava no
# artigo (lead + grid de metricas da S1). Nada de dado novo.
HERO = (
 '<!-- ══════ [V7.4] LEAD-HERÓI — a faixa navy É o lead, 1º elemento do artigo ══════ -->\n'
 '<div class="v5-hero-conv" style="background:linear-gradient(135deg,#1a1a2e,#16213e);'
 'border-radius:20px;padding:28px 24px;margin-bottom:4px;">'
 '<div style="font-size:12px;font-weight:700;color:#ff8533;text-transform:uppercase;'
 'letter-spacing:1px;margin-bottom:6px;">Plano Hapvida em Curitiba</div>'
 '<div style="font-size:34px;font-weight:900;color:#fff;line-height:1.1;margin-bottom:18px;">'
 'A partir de <span style="color:#ff8533;">[curitiba_emp_ambulatorialtotal_0]</span>/mês</div>'
 '<p style="text-align:justify!important;font-size:18px;line-height:1.7;color:#e2e8f0;'
 'margin-bottom:16px;">O plano Hapvida em Curitiba opera com '
 '<strong style="color:#ff8533;">rede 100% própria herdada da Clinipam</strong>, fundada em 1983: '
 'são 3 hospitais 24h, mais de 19 centros clínicos e a única maternidade de operadora da cidade. '
 'Os planos começam em <strong style="color:#ff8533;">[curitiba_emp_ambulatorialtotal_0]</strong> '
 'por mês, com coparticipação pela Tabela 1, a de menores valores do país.</p>'
 '<div class="v5-hero-metricas" style="display:flex!important;flex-wrap:wrap!important;'
 'gap:24px!important;margin-top:20px;padding-top:18px;border-top:1px solid rgba(255,255,255,0.15);">'
 '<div><div style="font-size:20px;font-weight:900;color:#fff;">3</div>'
 '<div style="font-size:12px;color:#94a3b8;">hospitais próprios 24h</div></div>'
 '<div><div style="font-size:20px;font-weight:900;color:#fff;">19+</div>'
 '<div style="font-size:12px;color:#94a3b8;">centros clínicos</div></div>'
 '<div><div style="font-size:20px;font-weight:900;color:#fff;">40+</div>'
 '<div style="font-size:12px;color:#94a3b8;">anos de rede própria</div></div>'
 '</div></div>\n'
)

# ------------------------------------------- 2. S2 partida em S2↑a e S2↑b
SC = '[curitiba_empresarial_total]'
i = S2.find(SC)
assert i > 0
corte = i + len(SC)
S2A = (S2[:corte].replace('SEÇÃO 2: TABELA DE PREÇOS — branco',
                          'SEÇÃO 2↑a [V7]: TABELA DE PREÇOS — branco — 1ª SEÇÃO, fecha na tabela')
       + '\n</section>')
resto = S2[corte:].lstrip('\n')
S2B = ('<!-- ══════ SEÇÃO 2↑b [V7.1]: ANÁLISE DE PREÇO — branco (mesma S2↑, sem H2 novo) ══════ -->\n\n'
       '<section style="background: #fff; padding: 20px 10px; border-radius: 20px; '
       'margin-bottom: 4px; border: 1px solid #e2e8f0;">\n' + resto)
assert S2B.rstrip().endswith('</section>')

# ------------------------------------------- 3. formulário ganha id="cotacao-1"
FORM1_NEW = FORM1.replace('<div style="margin-bottom: 4px;">[elementor-template id="11215"]</div>',
                          '<div id="cotacao-1" style="margin-bottom: 4px;">'
                          '[elementor-template id="11215"]</div>')
assert 'cotacao-1' in FORM1_NEW

# ---------------------- 4. parágrafos 2 e 3 do lead descem para a S1 (nada se perde)
ps = re.findall(r'<p style="text-align: justify!important; font-size: 17px;.*?</p>', INTRO, re.S)
assert len(ps) == 3, len(ps)
p2, p3 = ps[1], ps[2]
# compensa, no corpo, o grifo animado que saiu do lead (sobre navy ele sumiria)
p2 = p2.replace('50,4% da população possui convênio médico',
                '<span class="destaque-laranja-suave" style="background-image: '
                'linear-gradient(120deg,rgba(255,107,0,0.22) 0%,rgba(255,133,51,0.22) 100%); '
                'background-repeat: no-repeat; background-position: 0 50%; '
                'background-size: 100% 100%; padding: 2px 6px; '
                'transition: background-size 1.2s ease-out;">50,4% da população possui '
                'convênio médico</span>', 1)
p3 = p3.replace('margin-bottom: 0;', 'margin-bottom: 16px;', 1)
BARRA = ('<div style="width: 60px; height: 4px; background: linear-gradient(90deg,#ff6b00,#ff8533); '
         'border-radius: 2px; margin-bottom: 28px;"></div>')
assert S1.count(BARRA) == 1
S1_NEW = S1.replace(BARRA, BARRA + '\n' + p2 + '\n' + p3, 1)
S1_NEW = S1_NEW.replace('SEÇÃO 1: POR QUE CURITIBA É DIFERENTE — #f8f9fa',
                        'SEÇÃO 1 [V7]: POR QUE CURITIBA É DIFERENTE — #f8f9fa — desceu para 2º bloco CORE')

# ------------------------------------------- 5. sumário reordenado + item de cotação
todos = re.findall(r'<div class="toc-item".*?</div>\n?', TOC, re.S)
# o 1o "toc-item" e o cabecalho "Neste Guia Voce Vai Encontrar" (sem href) — fica onde esta
itens = [it for it in todos if 'href="#' in it]
assert len(todos) == 14 and len(itens) == 13, (len(todos), len(itens))
by_href = {}
for it in itens:
    h = re.search(r'href="(#[^"]+)"', it).group(1)
    by_href[h] = it
ordem = ['#precos', '#coparticipacao', '#por-que-curitiba', '#tipos-planos', '#rede-propria',
         '#hospital-onix', '#cobertura-regional', '#comparativo', '#carencias', '#tecnologia',
         '#contratacao', '#faq', '#conclusao']
assert set(ordem) == set(by_href), set(ordem) ^ set(by_href)

CTA_ITEM = ('<div class="toc-item" style="display: flex!important; align-items: center!important; '
            'gap: 10px!important; padding: 0!important; margin: 0!important;">'
            '<span class="toc-badge" style="min-width: 28px; height: 28px; flex-shrink: 0!important; '
            'background: #ff6b00; border-radius: 8px; display: flex!important; '
            'align-items: center!important; justify-content: center!important; color: #fff; '
            'font-size: 13px; font-weight: bold;">›</span>'
            '<a style="color: #ff6b00; font-weight: 800; font-size: 15px; text-decoration: none;" '
            'href="#cotacao-1">Faça uma Cotação</a></div>\n')

novos = []
for n, h in enumerate(ordem, 1):
    it = by_href[h]
    it = re.sub(r'(font-weight: bold;">)\d+(</span>)', r'\g<1>%d\g<2>' % n, it, count=1)
    novos.append(it)
    if h == '#contratacao':
        novos.append(CTA_ITEM)
TOC_NEW = TOC
for it in itens:
    TOC_NEW = TOC_NEW.replace(it, '\x00', 1)
partes = TOC_NEW.split('\x00')
assert len(partes) == 14
TOC_NEW = partes[0] + ''.join(novos) + partes[-1]
assert TOC_NEW.count('toc-item') == 15, TOC_NEW.count('toc-item')

# ------------------------------------------- 6. anti-wpautop do componente novo
TAIL_NEW = TAIL.replace(
    '.box-row>p{display:contents!important}',
    '.v5-hero-metricas>p,.v5-hero-metricas>br{display:none!important}\n'
    '.box-row>p{display:contents!important}', 1)
assert 'v5-hero-metricas>p' in TAIL_NEW

# ------------------------------------------- 7. montagem na ordem V7.4
out = ''.join([ART_OPEN, HERO, S2A, '\n', TOC_NEW, FORM1_NEW, S2B, '\n',
               S4COPART, S1_NEW, S3, S5REDE, S6HOSP, S7COB, S8COMP, CTAINT,
               S9CAR, S10TEC, S11CON, FAQ, CTAFIN, CONCL, TAIL_NEW])
# --- correcao de shortcode confirmada pelo usuario (2026-09-01) -----------
# A tabela e renderizada por [curitiba_menortabela] (utilitario documentado em
# references/shortcodes.md). Os usos INLINE, que estavam com shortcode de TABELA
# INTEIRA dentro de celula de tabela e de resposta de FAQ, passam para o chamariz
# [cidade_menorvalor] — o mesmo que o /plano-clinipam-curitiba/ publicado usa.
# Aplicado no fim, para nao deslocar as posicoes do fatiamento acima.
assert out.count('[curitiba_empresarial_total]') == 1
out = out.replace('[curitiba_empresarial_total]', '[curitiba_menortabela]', 1)
for antigo, novo, n in [('[curitiba_emp_ambulatorialtotal]', '[curitiba_menorvalor]', 3),
                        ('[belo-horizonte_emp_ambulatorialtotal]', '[belo-horizonte_menorvalor]', 2),
                        ('[recife_ind_ambulatorialtotal]', '[recife_menorvalor]', 1)]:
    assert out.count(antigo) == n, (antigo, out.count(antigo))
    out = out.replace(antigo, novo)
# [sao-paulo_pme_enfermariatotal] fica como estava: e outro produto (enfermaria,
# nao ambulatorial) e o usuario nao foi consultado sobre ele.
# o [..._0] do lead-heroi nao e afetado (sufixo de faixa preservado)

open('artigo.html', 'w', encoding='utf-8').write(out)

# ------------------------------------------- 8. conferência de não-perda
def txt(s):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', s)).strip()
print('bytes original -> reformatado: %d -> %d' % (len(src), len(out)))
for nome, pat in [('<section', r'<section\b'), ('</section>', r'</section>'),
                  ('<h2', r'<h2\b'), ('<h3', r'<h3\b'),
                  ('elementor-template', r'elementor-template'),
                  ('grifos', r'destaque-laranja-suave'),
                  ('links tabelaplanos', r'href="https://tabelaplanos\.com\.br'),
                  ('links externos', r'rel="nofollow noopener"'),
                  ('shortcodes', r'\[[a-z0-9_\-]{4,}\]')]:
    print('  %-20s %3d -> %3d' % (nome, len(re.findall(pat, src)), len(re.findall(pat, out))))
