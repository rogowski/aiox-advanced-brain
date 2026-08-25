# Gates — disciplina do anatomist, sem o pipeline

O `code-anatomist` impede mapa de ficção com erratas e amostragem. `/3camadas` rouba **só isso**. Não clone, não rode 9 fases, não peça signoff G3.

## Resolver o alvo

```
cwd com .git ou manifesto  → SOURCE_PATH = cwd
path local que existe      → SOURCE_PATH = path
URL / slug / "não sei"     → PARE. Uma pergunta. Sem chute.
```

Não clone. Isso é anatomia. `/3camadas` pontua um disco que já está na máquina.

`SOURCE_PATH` é **somente leitura**, exceto a pia `docs/reports/`. Não grave HTML em `$TMPDIR`, `/tmp` nem `/private/tmp`.

## Isolamento de rodada

Cada `/3camadas` é uma corrida cega. O 0–9 desta sessão não pode nascer do HTML, do JSON ou das respostas da corrida anterior — senão o “segundo modelo” só ecoa o primeiro.

Faça. Não anuncie. Rodada, isolamento e “não vou ler o scorecard anterior” são procedimento — o JSON carimba, o chat não narra.

Até **este** HTML existir e ser aberto:

- Não leia `docs/reports/architecture-review-*`, `$TMPDIR/architecture-review-*` nem `/tmp/architecture-review-*`.
- Não abra HTML/JSON de rodada anterior em `docs/reports/`.
- Não copie `sim`/`não` de um `/3camadas` já feito nesta conversa. Recomece no probe.
- Comparar modelos = chat novo, ou só depois desta rodada concluir.

Depois de abrir o HTML desta rodada: pode listar arquivos anteriores. Não revise as 9 respostas por causa deles. Diff entre rodadas é pedido novo.

## Identidade do modelo (obrigatória)

O scorecard JSON leva `round` **antes** do `score.py`. Sem isso o script falha e não há entrega.

| Campo | O que é |
|-------|---------|
| `id` | `{utc}-{slug-do-modelo}` — único nesta máquina |
| `modelo` | O que esta sessão mostrou: nome, apelido da UI (Sol, Grok 4.6) e esforço (`xhigh`). Sem chute de SKU. Se o ID exato não veio: `Codex Sol · xhigh`, não invente `gpt-5.6-sol` |
| `runtime` | `cursor` \| `codex` \| `claude` \| `outro` |
| `started_at` | UTC ISO-8601 |
| `harness` | opcional: superfície (`cursor-agent`, `codex-cli`, …) |

Arquivos desta rodada (não sobrescreva outra). Crie a pasta se faltar. Path relativo ao `SOURCE_PATH`, nunca a raiz da máquina:

```text
docs/reports/architecture-review-<id>.scorecard.json
docs/reports/architecture-review-<id>.html
```

Não use `/docs/reports` na raiz do disco. É `{SOURCE_PATH}/docs/reports/`.

O JSON carimba `round` inteiro. O HTML só diz no rodapé, em português: quem leu e quando. Sem `id` na cara da página. Sem modelo no JSON, a rodada não existe.

## Classe de capacidade (não denylist de marca)

`/3camadas` é a rota `analise-arquitetural-profunda`: prior-art, amostragem, DAG no disco, isolamento. Modelo leve inventa costura e infla o 0–9. Isso é **classe da tarefa**, não “proibido Sonnet / liberado Opus”.

A aula 19/21b: identifique o papel (`review-seguranca`, aqui `analise-arquitetural-profunda`) e resolva o ocupante no runtime. Nome comercial tem meia-vida curta. Luna, Terra e Sonnet de 2026 não serão os nomes de 2027.

Classifique pelo **sinal positivo**. Não invente um ID melhor. SKU oculto **não** é recusa.

Ordem:

1. Sinal **leve** no nome ou no seletor → pare. Sem probe.
2. Sinal **médio** e nenhum high/xhigh → pare e avise. Override só com frase da pessoa.
3. Sinal **alto** (incluindo esforço high/xhigh, Sol, Codex frontier) → `capability: alto`. Siga.
4. Sem SKU e sem sinal leve → **alto**. Carimbe o que a sessão mostrou (`Codex · xhigh`, `Cursor · modelo não exposto`). Não peça “rode mesmo assim”.

| Classe | Sinais (exemplos, não lista fechada) | Ação |
|--------|--------------------------------------|------|
| `leve` | luna, terra, spark, haiku, flash, mini, nano, lite, composer-fast, `*-fast` barato | **Pare.** |
| `medio` | sonnet, composer (sem high), gpt-4o — e nenhum high/xhigh | **Pare e avise.** |
| `alto` | opus, grok 4.6 / thinking, gpt-5 / 5.5 / 5.6, **sol**, **xhigh**, high, o3/o4, gemini pro thinking, Codex sem sinal leve | Segue |

Override (`rode mesmo assim`): só quando o passo 1 ou 2 bloqueou. SKU ausente não entra aqui.

`score.py` só aceita `capability: alto` ou `capability: override`. `leve` no JSON é falha.

Sonnet ≠ Luna. Luna recusa. Sonnet avisa. Codex Sol Xhigh é `alto` mesmo se o ID `gpt-5.6-sol` não aparecer no prompt.

## Habitat antes do número

Rode `scripts/probe.py SOURCE_PATH`. Depois leia os hits. Sem leitura, o hit não marca ponto.

Se o probe não achar superfície agentic (sem cliente de modelo, sem harness, sem retrieve) e o README também não mentir um agent: pontue 0/9 com contexto `não é um sistema agentic`. Isso é score, não falha.

Se o sistema **parece** agentic (chat, tools, RAG, “cérebro”) e depois do probe você **não** consegue apontar um arquivo por pilar: **não pontue**. Handoff para `code-anatomist`. Score sem costura é o mapa inventado da aula 03.

## Confiança por afirmação

| Tag | Quando | Efeito no 0–9 |
|-----|--------|----------------|
| HIGH | Probe achou e você leu o trecho | Pode ser `true` |
| MEDIUM | Você leu o arquivo; o probe não tinha o padrão | Pode ser `true` |
| LOW | Inferência por nome de pasta | `false` |
| REDUCED | Corrida só no olho, sem probe | Nenhuma pergunta `true` |

A aula do anatomist: peça o path de três afirmações; se alguma não abrir código existente, o mapa é ficção. Aqui: **todo `true` carrega path + tag**. Sem os dois, vira `false`.

## Amostragem (obrigatória antes de entregar)

1. Escolha duas perguntas marcadas `true` (se houver só uma, use essa).
2. Abra os arquivos citados. Confirme que fazem o que a pergunta afirma.
3. Se não fizerem: vire `false`, rode `score.py` de novo, reescreva o HTML.
4. No relatório, uma linha: `amostragem: {paths} — ok` ou `amostragem: {path} — ponto retirado`.

## DAG sem disco é ficção

`#fluxos` descreve o caminho que o probe leu. Nó sem path = `gap`. Aresta de vazamento só se o arquivo mostra a camada no trabalho de outra. Não desenhe o mermaid da aula 21b como se fosse o repo.

## Save before HTML

1. Grave o scorecard JSON em `docs/reports/`.
2. Rode `score.py`.
3. Só então escreva o HTML com os totais do script.
4. Sem JSON + stdout do script, não há entrega.

## O que não copiar do anatomist

- 9 fases, C4, métricas, clone, `outputs/decoded/`
- G3 humano para “aprovar arquitetura”
- 12 agentes, domain-decoder, extração de regras
- Descrever a arquitetura prometida no README

## Do SINKRA, sem o pipeline

O `sinkra-chief` mapeia processo em 7 fases, com VETO e specialist por etapa. `/3camadas` não orquestra fase, não gera squad e não materializa board. Rouba **quatro contratos** que continuam válidos se trocar o modelo.

### 1. AS-IS não é TO-BE

O 0–9 descreve o disco de hoje. Candidato e primeiro movimento são direção, não um segundo score. “Temos routing no README” não marca Q1. Aspiração vai no contexto, não na rubrica.

### 2. Prior-art antes de ausência

Todo `false` / `GAP` por “não existe” leva uma linha:

```text
claim: {o que faltaria para marcar sim}
busca: {Grep ou Glob, comando real}
matches: {n}
veredito: ausente | existe-sem-leitor | existe-e-o-ponto-foi-marcado
```

Sem essa linha, ausência é chute. Prove que procurou. Hit em vocabulário (`cursos/`, `SKILL.md`) não conta como leitor de runtime.

### 3. Verdade veta; média não salva

Amostragem que derruba um `true` **retira o ponto**. Não existe “aprovado com ressalva” no 0–9. Veto de segurança continua incompensável. Não persiga +1 no HTML se o custo for inventar costura.

### 4. Processo vs missão

O mesmo número lê diferente:

| Contexto | Leitura do 0–3 |
|----------|----------------|
| Processo recorrente, dinheiro, ACL, write-back | soldado = risco operacional |
| Missão descartável, sem dado sensível | soldado pode ser a decisão madura |

Declare o contexto no HTML. Não “ajuste” o total por simpatia.

### Primeiro movimento (uma classe)

Roubado do tipping point SINKRA, comprimido:

| Classe | Significa |
|--------|-----------|
| `remover` | Apoio de raciocínio sem hipótese; ablação |
| `enforcement` | Controle que hoje vive em prosa; vai para código no harness |
| `deixar` | Já está na camada certa; o próximo passo é outro pilar |

Uma classe, um path, um **não faça** (rabbit hole). Sem top-10.

## O que não copiar do SINKRA

- 7 fases, 11 agentes, RACI, DAG de missão, board, factory de squad
- Checkpoints com peso 0,7 / compliance ≥ 80
- Chief que só roteia specialists — aqui um agent lê o disco e para
- Manifesto de 200 linhas; o scorecard JSON já é o digest
