const fs = require('fs');
const src = f => fs.readFileSync(require("path").join(__dirname, f), "utf8");
function run(file, ctx) {
  const nodes = ctx.nodes || {};
  const $ = (n) => ({ first: () => ({ json: nodes[n] }) });
  const $input = { first: () => ({ json: ctx.input }) };
  const fn = new Function('$', '$input', src(file));
  return fn($, $input);
}

const POST = {
  id: 33477, slug: 'plano-hapvida-manaus', status: 'publish', link: 'https://tabelaplanos.com.br/plano-hapvida-manaus/',
  date: '2025-01-01', modified: '2026-09-02T11:57:27',
  title: { raw: 'Plano Hapvida Manaus', rendered: 'Plano Hapvida Manaus' },
  excerpt: { raw: 'resumo', rendered: 'resumo' },
  meta: { rank_math_title: 'Titulo SEO antigo', rank_math_description: 'Descricao antiga' },
  content: { raw: '<p>Rua A, 8 fica aqui. Veja a <h2>Hapclinica X</h2> e Hapclinica X no texto.</p><p>Outra mencao a Rua A, 8.</p>' }
};

function pipeline(req, httpResp) {
  const rota = run('rota.js', { input: req })[0].json;
  const conf = run('conferir.js', { input: httpResp, nodes: { Parametros: req, Rota: rota } })[0].json;
  const ifOk = conf.ok === true && conf.aplicar === true;
  let out;
  if (ifOk) {
    const salvo = { statusCode: req.operacao === 'criar' ? 201 : 200, body: Object.assign({}, POST, { id: req.operacao === 'criar' ? 99999 : POST.id, modified: '2026-09-02T12:00:00', link: 'https://x/y/' }) };
    out = run('gravado.js', { input: salvo, nodes: { 'Conferir e Montar': conf } })[0].json;
  } else {
    out = run('semgravar.js', { input: conf })[0].json;
  }
  return { urlBusca: rota.urlBusca, saida: out };
}

const P = (o) => Object.assign({ operacao:'', id:0, find:'', repl:'', frase:'', destino:'', esperado:'', ocorrencia:'', apply:false, valor:'', titulo:'', conteudo:'', slug:'', status:'', resumo:'', meta_titulo:'', meta_descricao:'', categorias:'', orderby:'', order:'', per_page:'', busca:'' }, o);
const ok200 = (body) => ({ statusCode: 200, body });
const casos = [];
const add = (nome, req, resp) => casos.push([nome, req, resp]);

add('listar padrao', P({operacao:'listar'}), ok200([{id:1,title:{rendered:'A'},slug:'a',link:'l',status:'publish',date:'d',modified:'m'}]));
add('listar com busca', P({operacao:'listar', per_page:5, busca:'manaus', orderby:'modified', order:'asc'}), ok200([]));
add('buscar', P({operacao:'buscar', id:33477}), ok200(POST));
add('auditar_links', P({operacao:'auditar_links', per_page:3}), ok200([{id:1,internal_in:0}]));
add('meta_title dry', P({operacao:'meta_title', id:33477, valor:'Novo Titulo SEO'}), ok200(POST));
add('meta_title apply', P({operacao:'meta_title', id:33477, valor:'Novo Titulo SEO', apply:true}), ok200(POST));
add('meta_title igual', P({operacao:'meta_title', id:33477, valor:'Titulo SEO antigo'}), ok200(POST));
add('meta_title vazio', P({operacao:'meta_title', id:33477}), ok200(POST));
add('meta_description dry', P({operacao:'meta_description', id:33477, valor:'Nova desc'}), ok200(POST));
add('criar dry', P({operacao:'criar', titulo:'Artigo Novo', conteudo:'<p>oi</p>', slug:'artigo-novo', meta_titulo:'MT', meta_descricao:'MD', categorias:'3, 7'}), ok200([]));
add('criar apply', P({operacao:'criar', titulo:'Artigo Novo', conteudo:'<p>oi</p>', slug:'artigo-novo', status:'publish', apply:true}), ok200([]));
add('criar duplicado', P({operacao:'criar', titulo:'X', conteudo:'<p>oi</p>', slug:'artigo-novo'}), ok200([{id:5, slug:'artigo-novo', status:'draft', link:'L'}]));
add('criar sem conteudo', P({operacao:'criar', titulo:'X', slug:'s'}), ok200([]));
add('conteudo dry', P({operacao:'conteudo', id:33477, conteudo:'<p>corpo novo</p>', resumo:'r'}), ok200(POST));
add('substituir dry', P({operacao:'substituir', id:33477, find:'Rua A, 8', repl:'Rua A, 695', esperado:2}), ok200(POST));
add('substituir contagem errada', P({operacao:'substituir', id:33477, find:'Rua A, 8', repl:'X', esperado:1}), ok200(POST));
add('substituir apply', P({operacao:'substituir', id:33477, find:'Rua A, 8', repl:'Rua A, 695', esperado:2, apply:true}), ok200(POST));
add('link ambiguo', P({operacao:'link', id:33477, frase:'Hapclinica X', destino:'destino-novo'}), ok200(POST));
add('link escolhido', P({operacao:'link', id:33477, frase:'Hapclinica X', destino:'destino-novo', ocorrencia:1}), ok200(POST));
add('link ja aponta', P({operacao:'link', id:33477, frase:'Hapclinica X', destino:'Rua'}), ok200(POST));
add('op desconhecida', P({operacao:'apagar_tudo', id:1}), ok200(POST));
add('http 404', P({operacao:'buscar', id:1}), {statusCode:404, body:{code:'rest_post_invalid_id'}});
add('sem content.raw', P({operacao:'substituir', id:1, find:'a', repl:'b'}), ok200({id:1, slug:'s', content:{rendered:'x'}}));

for (const [nome, req, resp] of casos) {
  const r = pipeline(req, resp);
  const s = r.saida;
  const resumo = { ok: s.ok, gravado: s.gravado, erro: s.erro, op: s.operacao };
  if (s.resumoAcao) resumo.resumoAcao = s.resumoAcao;
  if (s.ocorrencias !== null && s.ocorrencias !== undefined) resumo.ocorrencias = s.ocorrencias;
  if (s.total !== null && s.total !== undefined) resumo.total = s.total;
  if (s.dados && Array.isArray(s.dados)) resumo.dados = s.dados.length + ' item(ns)';
  else if (s.dados) resumo.dados = 'objeto(' + Object.keys(s.dados).length + ' campos)';
  resumo.aviso = s.aviso;
  console.log('--- ' + nome);
  console.log('    GET  ' + r.urlBusca);
  console.log('    OUT  ' + JSON.stringify(resumo));
}
