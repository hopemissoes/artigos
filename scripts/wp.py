#!/usr/bin/env python3
"""
wp.py — edicao PONTUAL de artigos no WordPress do tabelaplanos.com.br.

Existe porque a ferramenta MCP `editar_conteudo_artigo` sobrescreve o corpo
INTEIRO do post. Para trocar tres caracteres numa pagina de 300 mil, o corpo
teria que passar pelo contexto do modelo e ser redigitado — risco maior que o
erro a consertar. Aqui o corpo nunca passa pelo modelo: o script baixa, altera
e devolve.

LEITURA nao precisa de credencial. ESCRITA precisa de:
    WP_USER            usuario do WordPress
    WP_APP_PASSWORD    Application Password (Usuarios > Perfil > Senhas de aplicativo)

Toda operacao de escrita e DRY-RUN por padrao. So grava com --apply.

Comandos:
    get     <id> [--out ARQ]                    baixa o corpo
    grep    <id> <regex> [-C N]                 ocorrencias com contexto
    replace <id> --find S --repl R [--esperado N] [--apply]
    link    <id> --frase F --destino SLUG [--ocorrencia N] [--apply]
    verify  <id> --destino SLUG                 confere se o link esta no ar
"""
import argparse, json, os, re, sys, urllib.request, urllib.error, base64

BASE = "https://tabelaplanos.com.br/wp-json/wp/v2"
SITE = "https://tabelaplanos.com.br"


def _req(url, method="GET", payload=None, auth=False):
    data = json.dumps(payload).encode() if payload is not None else None
    r = urllib.request.Request(url, data=data, method=method)
    r.add_header("Content-Type", "application/json")
    r.add_header("User-Agent", "tabelaplanos-wp-edit/1.0")
    if auth:
        u, p = os.environ.get("WP_USER"), os.environ.get("WP_APP_PASSWORD")
        if not u or not p:
            sys.exit("ERRO: escrita exige WP_USER e WP_APP_PASSWORD no ambiente.\n"
                     "      Crie em: WordPress > Usuarios > Perfil > Senhas de aplicativo.")
        tok = base64.b64encode(f"{u}:{p.replace(' ', '')}".encode()).decode()
        r.add_header("Authorization", "Basic " + tok)
    try:
        with urllib.request.urlopen(r, timeout=60) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        sys.exit(f"ERRO HTTP {e.code} em {method} {url}\n{e.read().decode()[:600]}")


def get_post(pid):
    return _req(f"{BASE}/posts/{pid}?context=edit" if os.environ.get("WP_APP_PASSWORD")
                else f"{BASE}/posts/{pid}", auth=bool(os.environ.get("WP_APP_PASSWORD")))


def body_of(post):
    c = post.get("content", {})
    return c.get("raw") or c.get("rendered") or ""


# ---------------------------------------------------------------- mascara
TAG = re.compile(r'<!--.*?-->|<(/?)([a-zA-Z][a-zA-Z0-9]*)\b[^>]*?(/?)>', re.S)
OPACOS = {"script", "style", "a", "h1", "h2", "h3", "h4", "h5", "h6",
          "title", "textarea", "iframe", "code", "pre"}


def mascara_segura(html):
    """True nas posicoes de TEXTO onde e seguro inserir/alterar conteudo visivel.

    Fica FALSO dentro de tags, comentarios, <a>, headings, script/style,
    e dentro de shortcodes do WordPress ([mes_atual], [elementor-template ...]).
    Sem isso, um replace ingenuo acerta atributo alt=, o <title>, ou aninha
    um <a> dentro de outro — que e HTML invalido.
    """
    n = len(html)
    safe = bytearray(b"\x01") * n
    profundidade = {t: 0 for t in OPACOS}
    pos = 0
    for m in TAG.finditer(html):
        # texto entre a ultima tag e esta
        if any(profundidade.values()):
            for i in range(pos, m.start()):
                safe[i] = 0
        for i in range(m.start(), m.end()):
            safe[i] = 0                       # a propria tag nunca e segura
        pos = m.end()
        if m.group(0).startswith("<!--"):
            continue
        fecha, nome, autofecha = m.group(1), (m.group(2) or "").lower(), m.group(3)
        if nome in OPACOS and not autofecha:
            if fecha:
                profundidade[nome] = max(0, profundidade[nome] - 1)
            else:
                profundidade[nome] += 1
    if any(profundidade.values()):
        for i in range(pos, n):
            safe[i] = 0
    for m in re.finditer(r'\[[^\]\n]{1,120}\]', html):   # shortcodes
        for i in range(m.start(), m.end()):
            safe[i] = 0
    return safe


def ocorrencias_seguras(html, agulha):
    safe = mascara_segura(html)
    out = []
    for m in re.finditer(re.escape(agulha), html):
        if all(safe[i] for i in range(m.start(), m.end())):
            out.append(m.start())
    return out


def ctx(html, ini, fim, janela=110):
    a, b = max(0, ini - janela), min(len(html), fim + janela)
    return re.sub(r'\s+', ' ', html[a:ini]) + " >>>" + html[ini:fim] + "<<< " + \
           re.sub(r'\s+', ' ', html[fim:b])


def salvar(pid, novo, resumo):
    r = _req(f"{BASE}/posts/{pid}", method="POST", payload={"content": novo}, auth=True)
    print(f"OK  post {pid} salvo — modified {r.get('modified')} — {resumo}")
    print("    WordPress guardou revisao; da para reverter pelo editor.")


# ---------------------------------------------------------------- comandos
def cmd_get(a):
    b = body_of(get_post(a.id))
    if a.out:
        open(a.out, "w", encoding="utf-8").write(b)
        print(f"{len(b)} caracteres -> {a.out}")
    else:
        print(b)


def cmd_grep(a):
    html = body_of(get_post(a.id))
    safe = mascara_segura(html)
    n = 0
    for m in re.finditer(a.regex, html):
        n += 1
        seguro = all(safe[i] for i in range(m.start(), m.end()))
        print(f"[{n}] pos={m.start()} {'TEXTO' if seguro else 'dentro de tag/link/heading'}")
        print("    " + ctx(html, m.start(), m.end(), a.C))
    print(f"\n{n} ocorrencia(s).")


def cmd_replace(a):
    html = body_of(get_post(a.id))
    todas = [m.start() for m in re.finditer(re.escape(a.find), html)]
    print(f"post {a.id}: {len(todas)} ocorrencia(s) de {a.find!r}")
    if a.esperado is not None and len(todas) != a.esperado:
        sys.exit(f"ABORTADO: esperava {a.esperado}, achou {len(todas)}. Nada foi alterado.")
    if not todas:
        sys.exit("ABORTADO: nada a trocar.")
    for p in todas:
        print("  " + ctx(html, p, p + len(a.find)))
    novo = html.replace(a.find, a.repl)
    print(f"\nresultado: {len(html)} -> {len(novo)} caracteres")
    if not a.apply:
        print("DRY-RUN. Rode de novo com --apply para gravar.")
        return
    salvar(a.id, novo, f"{len(todas)}x {a.find!r} -> {a.repl!r}")


def cmd_link(a):
    post = get_post(a.id)
    html = body_of(post)
    url = f"{SITE}/{a.destino.strip('/')}/"
    if re.search(r'href=["\']' + re.escape(url) + r'["\']', html) or a.destino in html:
        sys.exit(f"ABORTADO: o post {a.id} ja aponta para {a.destino}. "
                 "Regra da casa: um link por destino por pagina.")
    pos = ocorrencias_seguras(html, a.frase)
    print(f"post {a.id} ({post.get('slug')}): {len(pos)} ocorrencia(s) de {a.frase!r} em texto seguro")
    for i, p in enumerate(pos, 1):
        print(f"  [{i}] " + ctx(html, p, p + len(a.frase)))
    if not pos:
        sys.exit("ABORTADO: a frase nao aparece em texto linkavel "
                 "(pode estar so dentro de tag, heading ou link).")
    if len(pos) > 1 and a.ocorrencia is None:
        sys.exit(f"ABORTADO: {len(pos)} ocorrencias. Escolha com --ocorrencia N.")
    alvo = pos[(a.ocorrencia or 1) - 1]
    novo = html[:alvo] + f'<a href="{url}">{a.frase}</a>' + html[alvo + len(a.frase):]
    print(f"\nancora: {a.frase!r} -> {url}")
    print(f"resultado: {len(html)} -> {len(novo)} caracteres")
    if not a.apply:
        print("DRY-RUN. Rode de novo com --apply para gravar.")
        return
    salvar(a.id, novo, f"link -> {a.destino}")
    print(json.dumps({"origem": post.get("slug"), "destino": a.destino,
                      "ancora": a.frase}, ensure_ascii=False))


def cmd_verify(a):
    html = body_of(get_post(a.id))
    url = f"{SITE}/{a.destino.strip('/')}/"
    achou = list(re.finditer(r'<a\b[^>]*href=["\']' + re.escape(url) + r'["\'][^>]*>(.*?)</a>',
                             html, re.S))
    if not achou:
        print(f"NAO — o post {a.id} nao linka para {a.destino}")
        sys.exit(1)
    for m in achou:
        anc = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', m.group(1))).strip()
        print(f"SIM — ancora: {anc!r}")
    if len(achou) > 1:
        print(f"AVISO: {len(achou)} links para o mesmo destino (a regra e 1).")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    s = p.add_subparsers(dest="cmd", required=True)

    g = s.add_parser("get");     g.add_argument("id", type=int); g.add_argument("--out"); g.set_defaults(f=cmd_get)
    g = s.add_parser("grep");    g.add_argument("id", type=int); g.add_argument("regex")
    g.add_argument("-C", type=int, default=110); g.set_defaults(f=cmd_grep)
    g = s.add_parser("replace"); g.add_argument("id", type=int)
    g.add_argument("--find", required=True); g.add_argument("--repl", required=True)
    g.add_argument("--esperado", type=int); g.add_argument("--apply", action="store_true")
    g.set_defaults(f=cmd_replace)
    g = s.add_parser("link");    g.add_argument("id", type=int)
    g.add_argument("--frase", required=True); g.add_argument("--destino", required=True)
    g.add_argument("--ocorrencia", type=int); g.add_argument("--apply", action="store_true")
    g.set_defaults(f=cmd_link)
    g = s.add_parser("verify");  g.add_argument("id", type=int)
    g.add_argument("--destino", required=True); g.set_defaults(f=cmd_verify)

    a = p.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
