# Relatório: duas superfícies

O JSON é para o agente. O HTML é para o dono do sistema. Não misture.

| Arquivo | Para quem | O que carrega |
|---------|-----------|---------------|
| `{SOURCE_PATH}/docs/reports/architecture-review-<id>.scorecard.json` | o agente e o `score.py` | Q1–Q9, paths, prior-art, `round`, amostragem |
| `{SOURCE_PATH}/docs/reports/architecture-review-<id>.html` | empresário / operador | o que segura o chão, o que já roda, o que ainda é discurso, um próximo passo |

Crie `docs/reports/` se não existir. Não grave em `$TMPDIR`, `/tmp` nem `/private/tmp`. Não grave em `/docs/reports` na raiz da máquina. Não escreva o HTML em outro lugar do repo. Abra o HTML (`open` no macOS). No chat, o path do HTML. O JSON só se a pessoa pedir o laudo.

Não copie Tailwind, slugs nem notas de outro laboratório. Tokens AIOX se o HTML for deste acervo: cream `#F4F4E8`, lima `#D1FF00`, ink `#050505`, Geist, raio 0. Senão, paleta neutra com **legenda explícita**.

DAGs: [dags.md](dags.md). Sem path no disco, o nó é “ainda não existe”. Sem execução encontrada, um cartão só — não desenhe a aula.

## Voz do HTML (não negociável)

Escreva como o review editorial: pergunta humana, uma frase, o que a máquina já faz, o que ela recusa. Ensine as três palavras **uma vez** e depois use só elas:

- **motor** — a IA que raciocina; pode ser trocada
- **painel** — o que manda parar, prova e escolhe a porta
- **memória da empresa** — gavetas de verdade, voz, prova; não é o chat

Proibido na página (isso mora no JSON):

`tese`, `21b`, `/3camadas`, `Q1`–`Q9`, `scorecard`, `HIGH`, `MEDIUM`, `GAP`, `prior-art`, `probe`, `score.py`, `soldado`, `AS-IS`, `capability`, `override`, `blocked_class`, `adapter`, `harness`, `brain`, `eval`, `ACL`, `write-back`, `SKILL.md`

Traduza:

| No JSON | Na página |
|---------|-----------|
| 0–3 soldado | Trocar de IA hoje provavelmente quebra a operação |
| 4–6 separação parcial | As peças começaram a se separar; ainda falta prova |
| 7–9 troca operacional | Dá para trocar o motor sem redesenhar a empresa — se o teste passar |
| GAP / false | Ainda não. Procuramos e não achamos no sistema. |
| HIGH + path | A máquina já faz isso. (arquivo só se couber numa linha humana) |
| shadow / canary | teste na sombra / piloto pequeno |
| write-back | o que a IA extraiu fica candidato; não vira fato sozinho |
| ACL | quem pode ver o quê, **antes** de buscar |

Título da página: uma frase sobre **este** sistema. Não ` /3camadas — {repo} `.

Carimbo da rodada: rodapé pequeno. “Esta leitura foi feita por {modelo} em {data}.” Sem `id`, sem `runtime`, sem classe. Se houve override: uma linha “Você pediu para rodar com um modelo mais fraco. Leia com desconfiança.”

## Estrutura da página

1. **Como ler** — legenda em português + tabela “se a pergunta for / olhe”.
2. **Em uma frase** — o chão deste sistema, hoje.
3. **Três promessas** — trocar o motor / painel fino / memória com gavetas. Cada cartão: já segura, começou, ou ainda é conversa. Uma frase. Sem número 1/4.
4. **Quando você pede algo** — swimlane + mermaid do mesmo caminho + tabela (o sistema já diz / a máquina faz sem perguntar / ela recusa).
5. **O que já trava sozinho** e **o que ainda é conversa** — prosa curta. Path só se a pessoa precisar achar o arquivo; senão fica no JSON.
6. **O único próximo passo** — o que fazer esta semana, em linguagem de operação. Sem `remover` / `enforcement` no título (pode no JSON).

Sem tabela de nove perguntas. Sem `rg`. Sem “amostragem: ok”.

## Gramática visual (página)

| Marca | O dono lê |
|-------|-----------|
| Lima | O motor, ou uma decisão sua |
| Ink | O painel — já governa |
| Fundo escuro | Memória da empresa |
| Tracejado | Ainda não existe |
| Vermelho | Caminho errado ou alguém no trabalho de outro |

Duas vistas da **mesma** execução. Diagrama que precisa de parágrafo deve ser redesenhado.

## Scaffold

```html
<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{frase humana sobre este sistema}</title>
  <script type="module">
    import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";
    mermaid.initialize({
      startOnLoad: true,
      theme: "base",
      securityLevel: "strict",
      flowchart: { curve: "basis", htmlLabels: true },
      themeVariables: {
        primaryColor: "#F4F4E8",
        primaryTextColor: "#050505",
        primaryBorderColor: "#050505",
        lineColor: "#050505",
        textColor: "#050505",
        mainBkg: "#F4F4E8",
        nodeBorder: "#050505",
        clusterBkg: "#111111",
        clusterBorder: "#D1FF00",
        titleColor: "#050505",
        edgeLabelBackground: "#F4F4E8",
      },
    });
  </script>
  <style>
    :root { --cream:#F4F4E8; --lima:#D1FF00; --ink:#050505; --leak:#B42318; --deep:#111; --panel:#fff; }
    * { box-sizing: border-box; }
    body { margin:0; background:var(--cream); color:var(--ink); font-family:Geist,ui-sans-serif,system-ui,sans-serif; line-height:1.55; }
    .chrome { background:var(--ink); color:var(--cream); padding:1.2rem 1.25rem; }
    .chrome h1 { margin:0; font-size:clamp(1.5rem,4vw,2.2rem); font-weight:500; letter-spacing:-.03em; }
    .chrome p { margin:.4rem 0 0; color:rgba(244,244,232,.72); max-width:72ch; }
    .subnav { background:var(--ink); border-top:1px solid rgba(244,244,232,.12); padding:.45rem 1.25rem; overflow-x:auto; }
    .subnav a { color:rgba(244,244,232,.75); text-decoration:none; font-size:.75rem; margin-right:.8rem; white-space:nowrap; }
    main { max-width:72rem; margin:0 auto; padding:1.25rem; }
    section { background:var(--panel); border:1px solid var(--ink); padding:1.1rem 1.2rem 1.3rem; margin:0 0 1rem; }
    .lede { max-width:72ch; font-size:1.05rem; }
    .legend { display:flex; flex-wrap:wrap; gap:.6rem 1rem; font-size:.78rem; font-weight:700; }
    .swatch { display:inline-block; width:.75rem; height:.75rem; margin-right:.35rem; vertical-align:-1px; border:1px solid var(--ink); }
    .swatch.modelo { background:var(--lima); }
    .swatch.harness { background:var(--ink); }
    .swatch.brain { background:var(--deep); }
    .swatch.humano { background:var(--cream); outline:2px solid var(--lima); }
    .swatch.gap { background:var(--cream); border-style:dashed; }
    .swatch.vazamento { background:#F4E8E8; border-color:var(--leak); }
    .cards { display:grid; gap:.7rem; }
    @media (min-width:800px) { .cards.three { grid-template-columns:repeat(3,1fr); } }
    .card { border:1px solid var(--ink); padding:.85rem .9rem; }
    .card h3 { margin:0 0 .35rem; font-size:1.05rem; font-weight:500; }
    .flow { display:grid; gap:.75rem; margin:.5rem 0 1rem; padding:1rem; border:1px solid var(--ink); }
    .flow-row { display:flex; flex-wrap:wrap; gap:.5rem; }
    .flow-col { flex:1 1 12rem; display:grid; gap:.4rem; align-content:start; padding:.75rem; border:1px solid var(--ink); }
    .flow-col h4 { margin:0; font-size:.7rem; letter-spacing:.06em; text-transform:uppercase; }
    .flow-node { padding:.5rem .65rem; border:1px solid var(--ink); font-size:.78rem; }
    .flow-node b { display:block; }
    .flow-node.modelo { background:var(--lima); }
    .flow-node.harness { background:var(--ink); color:var(--cream); }
    .flow-node.brain { background:var(--deep); color:var(--cream); }
    .flow-node.humano { background:var(--cream); outline:2px solid var(--lima); }
    .flow-node.gap { border-style:dashed; }
    .flow-node.vazamento { border-color:var(--leak); color:var(--leak); }
    .mermaid { overflow-x:auto; padding:.75rem; border:1px solid var(--ink); }
    table { width:100%; border-collapse:collapse; font-size:.86rem; }
    th, td { border:1px solid var(--ink); padding:.4rem .55rem; text-align:left; vertical-align:top; }
    .callout { margin:.8rem 0 0; padding:.85rem .95rem; border-left:3px solid var(--lima); background:#fff; }
    .callout.warn { border-left-color:#c45c26; }
    .callout.stop { border-left-color:var(--leak); }
    footer { max-width:72rem; margin:0 auto 2rem; padding:0 1.25rem; font-size:.8rem; color:#333; }
  </style>
</head>
<body>
  <div class="chrome">
    <h1>{frase humana}</h1>
    <p>{uma linha: o que esta página responde neste sistema}</p>
  </div>
  <nav class="subnav">
    <a href="#ler">Como ler</a>
    <a href="#frase">Em uma frase</a>
    <a href="#promessas">Três promessas</a>
    <a href="#pedido">Quando você pede</a>
    <a href="#segura">O que já segura</a>
    <a href="#passo">Próximo passo</a>
  </nav>
  <main>
    <section id="ler">
      <h2>Como ler esta página</h2>
      <p class="meta">Lima é o motor ou uma decisão sua. Preto é o que o painel já faz sozinho. Escuro é memória da empresa. Tracejado ainda não existe. Vermelho é caminho errado.</p>
      <div class="legend">
        <span><span class="swatch humano"></span>Você decide</span>
        <span><span class="swatch harness"></span>O painel já faz</span>
        <span><span class="swatch brain"></span>Memória da empresa</span>
        <span><span class="swatch modelo"></span>O motor (a IA)</span>
        <span><span class="swatch gap"></span>Ainda não existe</span>
        <span><span class="swatch vazamento"></span>Caminho errado</span>
      </div>
      <table>
        <thead><tr><th>Se a pergunta for</th><th>Olhe</th></tr></thead>
        <tbody>
          <tr><td>Este sistema já tem chão, ou ainda é discurso?</td><td>Em uma frase e três promessas</td></tr>
          <tr><td>O que acontece quando eu peço um trabalho?</td><td>Quando você pede</td></tr>
          <tr><td>O que já trava sozinho se alguém errar?</td><td>O que já segura</td></tr>
          <tr><td>O que eu faço esta semana?</td><td>Próximo passo</td></tr>
        </tbody>
      </table>
    </section>
    <section id="frase"><h2>Em uma frase</h2><p class="lede">{chão deste sistema, hoje}</p></section>
    <section id="promessas">
      <h2>As três promessas</h2>
      <div class="cards three">
        <article class="card"><h3>O motor se troca</h3><p>{já / começou / ainda não — uma frase}</p></article>
        <article class="card"><h3>O painel é fino</h3><p>{uma frase}</p></article>
        <article class="card"><h3>A memória tem gavetas</h3><p>{uma frase}</p></article>
      </div>
    </section>
    <section id="pedido">
      <h2>O que acontece quando você pede algo</h2>
      <div class="flow"><div class="flow-row"><!-- Você / Painel / Memória / Motor --></div></div>
      <pre class="mermaid"><!-- o mesmo caminho --></pre>
      <table>
        <thead><tr><th>O sistema já diz</th><th>A máquina faz sem perguntar</th><th>Ela recusa sozinha</th></tr></thead>
        <tbody></tbody>
      </table>
    </section>
    <section id="segura"></section>
    <section id="passo"></section>
  </main>
  <footer>Esta leitura foi feita por {modelo} em {data}.</footer>
</body>
</html>
```
