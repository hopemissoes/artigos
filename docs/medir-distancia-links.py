import sys,json,re,html
d=json.load(open(sys.argv[1],encoding='utf-8'))
if isinstance(d,list): d=d[0]
c=d['dados']['conteudo']; slug=d['dados']['slug']
open('/tmp/cur_'+slug+'.html','w',encoding='utf-8').write(c)
c=re.sub(r'<(style|script).*?</\1>','',c,flags=re.S)
print(f"### {slug}")
tot=0;last=None;pos=0;linhas=[]
for m in re.finditer(r'<a\s[^>]*href=[\'"]([^\'"]+)[\'"]',c):
    tot+=len(html.unescape(re.sub(r'<[^>]+>',' ',c[pos:m.start()])).split()); pos=m.start()
    u=m.group(1)
    if 'tabelaplanos.com.br' in u and '#' not in u:
        gap=None if last is None else tot-last
        linhas.append((tot,gap,u.replace('https://tabelaplanos.com.br','')))
        last=tot
resto=len(html.unescape(re.sub(r'<[^>]+>',' ',c[pos:])).split())
for p,g,u in linhas:
    flag='  <<< ABAIXO DE 150' if (g is not None and g<150) else ''
    print(f"  {p:>5} {str(g) if g is not None else '-':>6}  {u}{flag}")
print(f"  total de palavras visiveis: {tot+resto}")
viol=sum(1 for _,g,_ in linhas if g is not None and g<150)
print(f"  links internos: {len(linhas)} | violacoes de 150 palavras: {viol}\n")
