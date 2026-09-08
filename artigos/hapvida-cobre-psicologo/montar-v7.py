# -*- coding: utf-8 -*-
"""Reordena o artigo /hapvida-cobre-psicologo/ para o layout da v7.

NAO reescreve prosa: fatia o HTML publicado e remonta na ordem preco-primeiro,
acrescentando os componentes que a v7 exige e o artigo nao tinha
(lead-heroi v7.4, fonte-oficial e guia-box da v7.6, selos v5-trust).

Toda URL oficial usada aqui devolveu 200 na conferencia de 08/09/2026.
"""
import re

ORIG = "artigos/hapvida-cobre-psicologo/artigo-ATUAL.html"
SAIDA = "artigos/hapvida-cobre-psicologo/artigo.html"
BASE = "https://tabelaplanos.com.br/hapvida-cobre-psicologo/"

c = open(ORIG, encoding="utf-8").read()

# ------------------------------------------------------------------ fatias
art_open = c[: c.index(">") + 1]
lead_ini = c.index("<section", len(art_open))
toc_ini = c.index('<section style="background: linear-gradient(135deg,#fafbfc')
toc_fim = c.index("</section>", toc_ini) + len("</section>")
sec1_ini = c.index('<section id="saúde-mental-brasil"')
cop_ini = c.index('<section id="coparticipação"')
tab_fim = c.index("</div>", c.index("</table>", cop_ini)) + len("</div>")
cop_fim = c.index("</section>", cop_ini) + len("</section>")
form1 = c[cop_fim : c.index("</div>", c.index('<div id="cotacao-1"')) + len("</div>")].strip()
tele_ini = c.index('<section id="telepsicologia"')
style_ini = c.index("<style>")

LEAD = c[lead_ini:toc_ini]
SECS_A = c[sec1_ini:cop_ini]          # saude-mental + cobertura-ans + passo-a-passo
COP_A = c[cop_ini:tab_fim]            # H2 + subtitulo + regua + contexto + TABELA
COP_B = c[tab_fim:cop_fim]            # analise + cards + box Importante + </section>
TAIL = c[tele_ini:style_ini]          # telepsicologia ... conclusao
STYLE = c[style_ini:]

# o 2o paragrafo do lead (ANS + linhas de produto) e realocado para a secao da ANS
p_lead = re.findall(r"<p [^>]*>.*?</p>", LEAD, re.S)
assert len(p_lead) == 3, len(p_lead)
P_ANS = p_lead[1]

# ------------------------------------------------------------------ v7.4 heroi
HERO = (
 '<div class="v5-hero-conv" style="background:linear-gradient(135deg,#1a1a2e,#16213e);'
 'border-radius:20px;padding:28px 24px;margin-bottom:4px;">'
 '<div style="font-size:12px;font-weight:700;color:#ff8533;text-transform:uppercase;'
 'letter-spacing:1px;margin-bottom:6px;">Cobertura de psicologia no Hapvida</div>'
 '<div style="font-size:34px;font-weight:900;color:#fff;line-height:1.1;margin-bottom:18px;">'
 'A partir de <span style="color:#ff8533;">[demais_capitais_demais_terapias]</span> por sessão</div>'
 '<p style="text-align:justify!important;font-size:18px;line-height:1.7;color:#e2e8f0;margin-bottom:16px;">'
 'Sim, o <strong style="color:#ff8533;">Hapvida cobre psicólogo</strong>. Todos os planos com cobertura '
 'ambulatorial garantem psicoterapia e, desde agosto de 2022, a RN 541 da ANS acabou com o limite de '
 'sessões: a cobertura é <strong style="color:#ff8533;">ilimitada</strong> para qualquer condição com CID, '
 'mediante encaminhamento médico. A coparticipação por sessão começa em '
 '[demais_capitais_demais_terapias].</p>'
 '<div class="v5-hero-metricas" style="display:flex!important;flex-wrap:wrap!important;gap:24px!important;'
 'margin-top:20px;padding-top:18px;border-top:1px solid rgba(255,255,255,0.15);">'
 '<div><div style="font-size:20px;font-weight:900;color:#fff;">0</div>'
 '<div style="font-size:12px;color:#94a3b8;">limite de sessões desde 2022</div></div>'
 '<div><div style="font-size:20px;font-weight:900;color:#fff;">24h</div>'
 '<div style="font-size:12px;color:#94a3b8;">carência em urgência psiquiátrica</div></div>'
 '<div><div style="font-size:20px;font-weight:900;color:#fff;">40 mil</div>'
 '<div style="font-size:12px;color:#94a3b8;">teleconsultas de psicologia/mês</div></div>'
 '</div></div>'
)

# ------------------------------------------------------------------ v7.6 fonte oficial
def fonte_oficial(url, titulo, legenda):
    return (
     '<div class="fonte-oficial" style="position:relative;background:#f8fafc;border:1px solid #cbd5e1;'
     'border-radius:10px;padding:18px 18px 14px;margin:6px 0 28px;">'
     '<span style="position:absolute;top:-11px;left:16px;background:#fff;color:#1e3a8a;font-size:10.5px;'
     'font-weight:800;letter-spacing:1px;text-transform:uppercase;padding:2px 8px;border:1px solid #cbd5e1;'
     'border-radius:6px;line-height:1.4;font-family:Arial,Helvetica,sans-serif;">Fonte oficial</span>'
     f'<a href="{url}" target="_blank" rel="nofollow noopener" style="display:block;color:#1e3a8a;'
     'font-weight:700;font-size:15px;text-decoration:none;line-height:1.45;text-align:left!important;">'
     f'{titulo} <span style="color:#2563eb;">&#8599;</span></a>'
     '<span style="display:block;font-size:12.5px;color:#94a3b8;margin-top:4px;text-align:left!important;">'
     f'{legenda}</span></div>'
    )

URL_ANS_RN541 = ("https://www.gov.br/ans/pt-br/assuntos/noticias/periodo-eleitoral/"
                 "ans-acaba-com-limites-de-cobertura-de-quatro-categorias-profissionais")
URL_LEI = "https://www.planalto.gov.br/ccivil_03/leis/l9656.htm"

FONTE_RN541 = fonte_oficial(
    URL_ANS_RN541,
    "RN 541/2022 — ANS acaba com o limite de sessões de psicologia",
    "Comunicado oficial da Agência Nacional de Saúde Suplementar · gov.br/ans")
FONTE_LEI = fonte_oficial(
    URL_LEI,
    "Lei 9.656/98 — regras de cobertura e carência dos planos de saúde",
    "Texto integral no Planalto · planalto.gov.br")

# ------------------------------------------------------------------ selos
SELOS = (
 '<div class="v5-trust" style="display:flex!important;flex-wrap:wrap!important;'
 'justify-content:center!important;gap:10px!important;margin:10px 0 24px 0;">'
 '<span style="font-size:12px;color:#64748b;font-weight:600;border:1px solid #e2e8f0;border-radius:999px;'
 'padding:6px 12px;background:#fff;">Operadora registrada na ANS — nº 359017</span>'
 '<span style="font-size:12px;color:#64748b;font-weight:600;border:1px solid #e2e8f0;border-radius:999px;'
 'padding:6px 12px;background:#fff;">DRV: 11 anos especialista Hapvida</span>'
 '<span style="font-size:12px;color:#64748b;font-weight:600;border:1px solid #e2e8f0;border-radius:999px;'
 'padding:6px 12px;background:#fff;">Certificação Safira — nível máximo Hapvida</span></div>'
)

# ------------------------------------------------------------------ v7.6 quadro comparativo
def item(t):
    return ('<li style="position:relative;padding-left:22px;margin:0 0 8px;font-size:14.5px;line-height:1.5;'
            'color:#1a202c;text-align:left!important;"><span style="position:absolute;left:0;top:0;'
            f'color:#ff6b00;font-weight:800;font-size:13px;">&#10003;</span>{t}</li>')

QUADRO = (
 '<div class="quadro-comp" style="display:flex!important;flex-wrap:wrap!important;gap:14px!important;'
 'margin:18px 0 22px;">'
 '<div class="quadro-card" style="flex:1 1 260px!important;box-sizing:border-box!important;'
 'background:#fff3e8;border:1px solid #f6d3b8;border-radius:10px;padding:16px;">'
 '<h4 style="margin:0 0 10px!important;padding:0!important;font-size:13px!important;font-weight:800!important;'
 'text-transform:uppercase!important;letter-spacing:.03em!important;color:#ff6b00!important;'
 'line-height:1.3!important;">O que a cobertura garante</h4>'
 '<ul style="margin:0!important;padding:0!important;list-style:none!important;">'
 + item("Sessões de psicoterapia sem limite anual") +
 item("Qualquer condição listada no CID") +
 item("Teleterapia com cobertura equivalente à presencial") +
 '</ul></div>'
 '<div class="quadro-card" style="flex:1 1 260px!important;box-sizing:border-box!important;'
 'background:#fff3e8;border:1px solid #f6d3b8;border-radius:10px;padding:16px;">'
 '<h4 style="margin:0 0 10px!important;padding:0!important;font-size:13px!important;font-weight:800!important;'
 'text-transform:uppercase!important;letter-spacing:.03em!important;color:#ff6b00!important;'
 'line-height:1.3!important;">O que o plano exige</h4>'
 '<ul style="margin:0!important;padding:0!important;list-style:none!important;">'
 + item("Plano com segmentação ambulatorial ou referência") +
 item("Encaminhamento médico contendo o CID") +
 item("Psicólogo com registro ativo no CRP") +
 '</ul></div></div>'
)

# ------------------------------------------------------------------ v7.6 sobre este guia
GUIA = (
 '<div class="guia-box" style="background:linear-gradient(135deg,#eff6ff 0%,#dbeafe 100%);'
 'border:1px solid #bfdbfe;border-radius:12px;padding:22px 26px;margin:36px 0 0;">'
 '<div class="box-row" style="display:flex!important;align-items:center!important;gap:10px!important;'
 'margin-bottom:10px!important;line-height:1!important;flex-wrap:nowrap!important;">'
 '<span style="width:28px!important;height:28px!important;min-width:28px!important;max-width:28px!important;'
 'flex-shrink:0!important;background:#2563eb!important;border-radius:8px!important;display:inline-flex!important;'
 'align-items:center!important;justify-content:center!important;color:#fff!important;font-size:14px!important;'
 'font-weight:800!important;line-height:1!important;font-family:Arial,Helvetica,sans-serif!important;'
 'text-align:center!important;box-sizing:border-box!important;padding:0!important;margin:0!important;'
 'vertical-align:middle!important;">G</span>'
 '<span style="font-size:14px;font-weight:700;color:#1e40af;text-transform:uppercase;letter-spacing:1px;'
 'line-height:1.2;">Sobre este guia</span></div>'
 '<p style="text-align:justify!important;font-size:15px;line-height:1.7;color:#1e40af;margin:0 0 8px;">'
 f'Conteúdo produzido com base na <a href="{URL_ANS_RN541}" target="_blank" rel="nofollow noopener" '
 'style="color:#1e40af;font-weight:700;">RN 541/2022 da ANS</a>, que encerrou o limite de sessões de '
 f'psicoterapia, e na <a href="{URL_LEI}" target="_blank" rel="nofollow noopener" '
 'style="color:#1e40af;font-weight:700;">Lei 9.656/98</a>, que fixa as regras de cobertura e carência. '
 'Serve a quem tem ou pretende contratar plano Hapvida e precisa entender o acesso à psicoterapia: o que '
 'está coberto, quanto se paga por sessão e em quanto tempo se consegue atendimento. '
 'Atualizado em [mes_atual] de [ano_atual].</p>'
 '<p style="font-size:13px;line-height:1.5;color:#64748b;margin:0;font-style:italic;text-align:left!important;">'
 'Valores de coparticipação sujeitos a alteração. Confirme as condições vigentes antes de contratar.</p></div>'
)

# ------------------------------------------------------------------ sumario novo
ITENS = [
 ("1", "Quanto Custa por Sessão — Coparticipação", BASE + "#precos"),
 ("$", "Faça uma Cotação", "#cotacao-1"),
 ("2", "Saúde Mental no Brasil — Por Que Isso Importa", BASE + "#sa%C3%BAde-mental-brasil"),
 ("3", "Hapvida Cobre Psicólogo — O Que a ANS Garante", BASE + "#cobertura-ans"),
 ("4", "Como Funciona no Hapvida — Passo a Passo", BASE + "#passo-a-passo"),
 ("5", "Telepsicologia — Sessões Online pelo Hapvida", BASE + "#telepsicologia"),
 ("6", "Linhas de Cuidado em Saúde Mental", BASE + "#linhas-cuidado"),
 ("7", "Onde Encontrar Psicólogos Hapvida no Brasil", BASE + "#onde-encontrar"),
 ("8", "Hapvida vs Unimed vs Bradesco vs SulAmérica", BASE + "#comparativo"),
 ("9", "Carências e Portabilidade", BASE + "#car%C3%AAncias"),
 ("10", "Quando Procurar um Psicólogo", BASE + "#quando-procurar"),
 ("11", "Como Contratar um Plano Hapvida", BASE + "#contrata%C3%A7%C3%A3o"),
 ("12", "Perguntas Frequentes", BASE + "#faq"),
 ("13", "Conclusão", BASE + "#conclus%C3%A3o"),
]
IT = ('<div class="toc-item" style="display: flex!important; align-items: center!important; gap: 10px!important;'
      ' padding: 0!important; margin: 0!important;">')
BADGE = ('<span class="toc-badge" style="min-width: 28px; height: 28px; flex-shrink: 0!important;'
         ' background: #ff6b00; border-radius: 8px; display: flex!important; align-items: center!important;'
         ' justify-content: center!important; color: #fff; font-size: 13px; font-weight: bold;">{}</span>')
LINK = ('<a style="color: #1a202c; font-weight: 600; font-size: 15px; text-decoration: none;" href="{}">{}</a>')
LINK_CTA = ('<a style="display: inline-block; color: #fff!important; font-weight: 800; font-size: 15px;'
            ' text-decoration: none; padding: 6px 14px; background: linear-gradient(135deg,#ff6b00,#e85d00);'
            ' border-radius: 6px; box-shadow: 0 4px 14px rgba(255,107,0,0.35);" href="{}">{}</a>')

linhas = [IT + '<span style="min-width: 28px; height: 28px; flex-shrink: 0!important; background: #ff6b00;'
          ' border-radius: 8px; display: flex!important; align-items: center!important;'
          ' justify-content: center!important; color: #fff; font-size: 14px; font-weight: bold;">≡</span>'
          '<span style="font-size: 17px; font-weight: 800; color: #1a202c;">Neste Guia Você Vai Encontrar</span></div>']
for n, txt, href in ITENS:
    a = (LINK_CTA if n == "$" else LINK).format(href, txt)
    linhas.append(IT + BADGE.format(n) + a + "</div>")

TOC = ('<section style="background: linear-gradient(135deg,#fafbfc 0%,#f0f4f8 100%); padding: 20px 10px;'
       ' border-radius: 20px; margin-bottom: 4px; border: 1px solid #e2e8f0;">'
       '<div class="toc-list" style="display: flex!important; flex-direction: column!important;'
       ' gap: 10px!important; padding: 0!important; margin: 0!important;">'
       + "".join(linhas) + "</div></section>")

# ------------------------------------------------------------------ remontagem
cop_a = COP_A.replace('<section id="coparticipação"', '<section id="precos"', 1) + "\n</section>"
cop_b = ('<section style="background: #fff; padding: 20px 10px; border-radius: 20px; margin-bottom: 4px;">'
         + SELOS + COP_B.replace("</section>", FONTE_RN541 + "</section>", 1))

# paragrafo do lead que fala de ANS entra na secao da ANS, logo apos a regua laranja
alvo = '<section id="cobertura-ans"'
i = SECS_A.index(alvo)
j = SECS_A.index('margin-bottom: 28px;"></div>', i) + len('margin-bottom: 28px;"></div>')
secs_a = SECS_A[:j] + "\n" + P_ANS + SECS_A[j:]
# quadro comparativo + fonte oficial da Lei fecham a secao da ANS
k = secs_a.index("</section>", secs_a.index(alvo))
secs_a = secs_a[:k] + QUADRO + FONTE_LEI + secs_a[k:]

# "Sobre este guia" e o ultimo bloco da conclusao
tail = TAIL.rstrip()
assert tail.endswith("</section>"), tail[-40:]
tail = tail[: -len("</section>")] + GUIA + "</section>\n"

# anti-wpautop dos componentes novos
STYLE = STYLE.replace(
    "<style>\n",
    "<style>\n.v5-hero-conv>br,.v5-hero-metricas>p,.v5-hero-metricas>br,.v5-trust>p,.v5-trust>br,"
    ".quadro-comp>p,.quadro-comp>br,.quadro-card>p,.quadro-card>br,.fonte-oficial>p,.fonte-oficial>br,"
    ".guia-box>br{display:none!important}\n", 1)

novo = (art_open + "\n" + HERO + "\n" + cop_a + "\n" + form1 + "\n" + TOC + "\n"
        + cop_b + "\n" + secs_a + tail + STYLE)

open(SAIDA, "w", encoding="utf-8").write(novo)

# ------------------------------------------------------------------ conferencia
def texto(h):
    h = re.sub(r"<(script|style)[\s\S]*?</\1>", " ", h)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]*>", " ", h)).strip()

print("ANTES:", len(c), "chars ·", len(texto(c).split()), "palavras")
print("DEPOIS:", len(novo), "chars ·", len(texto(novo).split()), "palavras")
print("H2:", len(re.findall(r"<h2", novo)), "| H3:", len(re.findall(r"<h3", novo)),
      "| FAQ:", len(re.findall(r"<details", novo)),
      "| formularios:", len(re.findall(r"elementor-template", novo)))
print("grifos animados:", len(re.findall(r"destaque-laranja-suave", novo)))
i_hero = novo.index("v5-hero-conv"); i_tab = novo.index("<table"); i_toc = novo.index("toc-list")
i_cot = novo.index('id="cotacao-1"')
print("ordem -> heroi", i_hero, "< tabela", i_tab, "< cotacao-1", i_cot, "< sumario", i_toc,
      ":", i_hero < i_tab < i_cot < i_toc)
print("texto visivel antes da tabela:", len(texto(novo[:i_tab])), "chars")
print("texto visivel entre tabela e sumario:",
      len(texto(novo[novo.index("</table>"):i_toc])), "chars")
