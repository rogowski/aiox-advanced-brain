---
type: source-brief
course: aiox-agent-engineering
source_id: 83
status: canonical
canonical_scope: cursos/AIOX-Agent-Engineering
updated: '2026-08-25'
---

# Fonte 83 — Modelos substituíveis, harness fino e cérebro modular

Síntese autocontida para a aula [21b](../aulas/21b-modelos-substituiveis-harness-fino-cerebro-modular.md). O foco não é prever o modelo vencedor. É projetar uma capacidade que absorva a troca de modelos sem perder operação nem conhecimento institucional.

## Sinal de época

Três movimentos acontecem juntos:

1. **Custo e tamanho caem.** O [AI Index 2025](https://hai.stanford.edu/news/ai-index-2025-state-of-ai-in-10-charts) registrou queda de mais de 280 vezes no custo por milhão de tokens para atingir desempenho equivalente ao GPT-3.5 no MMLU entre novembro de 2022 e outubro de 2024. O menor modelo acima de 60% no mesmo benchmark caiu de 540 bilhões para 3,8 bilhões de parâmetros.
2. **A fronteira muda de mãos.** O [AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026_chapter_2_technical.pdf) mostra fornecedores líderes muito próximos em alguns rankings, benchmarks saturando rapidamente e desempenho ainda irregular entre capacidades.
3. **Produtos físicos expiram.** Os históricos oficiais de deprecação da [OpenAI](https://developers.openai.com/api/docs/deprecations) e da [Anthropic](https://platform.claude.com/docs/en/about-claude/model-deprecations) tornam inadequado tratar um identificador de modelo como fundamento permanente da arquitetura.

A consequência não é “todos os modelos são iguais”. É outra: **o nome físico do modelo deve deixar de ser o lugar onde a empresa guarda seu contrato, sua política e sua memória**.

## O recorte correto de substituibilidade

Substituibilidade é uma propriedade operacional de um workload:

```text
modelo candidato
+ capabilities declaradas
+ adapter compatível
+ conjunto de evals representativo
+ thresholds de qualidade, segurança, custo e latência
= candidato promovível para uma classe de tarefa
```

Ela não é uma promessa universal. Dois modelos podem aceitar o mesmo JSON e divergir em escolha de tool, obediência a instruções, uso de contexto, structured output, segurança ou variância. Adapter prova a forma. Eval prova o comportamento.

O [RouteLLM](https://arxiv.org/abs/2406.18665) demonstrou que routing pode reduzir custo mantendo qualidade em workloads avaliados; também mostrou que routers desalinhados com os dados podem ficar próximos ou abaixo do aleatório. O workload local continua sendo a unidade de verdade.

Substituibilidade amadurece por níveis: ID físico isolado, adapter sintático, contrato de capabilities, gate comportamental e rollout reversível. Somente a interface comum prova forma. Shadow, canary, fallback e rollback transformam fitness offline em capacidade operacional de troca.

## O que “thin harness” quer dizer

Harness fino não é um loop frágil. É um plano de controle que evita duplicar inteligência que o modelo já adquiriu, mas mantém invariantes que não podem depender de comportamento probabilístico:

- contrato de entrada e saída;
- capabilities e tools permitidas;
- autenticação, autorização e aprovações;
- budgets, timeout, retries e stop rules;
- estado de execução e idempotência;
- traces, outcome graders e rollback;
- routing, fallback e promoção de modelos.

A [Anthropic](https://www.anthropic.com/engineering/building-effective-agents) recomenda começar por padrões simples e compostos. Em [Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps), a equipe mostra que partes do scaffolding codificam hipóteses sobre limitações do modelo; quando essas limitações desaparecem, o scaffolding pode ser removido. O que fica não é a compensação para um modelo antigo. Ficam os invariantes operacionais.

O artigo [Decoupling the brain from the hands](https://www.anthropic.com/engineering/managed-agents) reforça a separação entre brain/harness, hands e session por interfaces independentes. A divisão reduz acoplamento entre raciocínio, ambiente e ciclo de vida da execução.

### Instrução persistente também deprecia

Na [entrevista da Y Combinator](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=412s), Boris Cherny recomenda que usuários de Claude Code testem a remoção semestral de `CLAUDE.md`, skills e hooks. O contexto completo é ablação: versionar, retirar, usar o modelo, observar falhas e devolver apenas a instrução que corrige tropeço repetido. A fala não cita `AGENTS.md`; aplicar o mesmo teste a ele é inferência arquitetural, não atribuição nominal.

A Anthropic recomenda [revisão trimestral e remoção de conteúdo stale](https://support.claude.com/en/articles/14553240-give-claude-context-claude-md-and-better-prompts). Também reportou a [remoção de mais de 80% do system prompt do Claude Code](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models) para modelos Claude 5, sem perda mensurável nos evals internos de código. O princípio é progressive disclosure: mapa curto always-on; procedimentos e referências sob demanda.

A OpenAI relata [prompts mais enxutos](https://developers.openai.com/api/docs/guides/latest-model#favor-leaner-prompts) com melhora direcional de 10–15% em evals internos, redução de 41–66% em tokens e de 33–67% em custo. O efeito não é universal. Estudos de `AGENTS.md` divergem: [CTXbench](https://arxiv.org/abs/2602.11988) encontrou custo maior sem ganho significativo; [outro estudo de 124 PRs](https://arxiv.org/abs/2601.20404) encontrou runtime e output tokens menores. A única regra sustentável é avaliar arquivo + modelo + repo + tarefa.

## O cérebro modular da empresa

O company brain é conhecimento institucional fora dos pesos do modelo. “Modular” significa separar jobs, autoridade e ritmo de atualização. Um desenho mínimo distingue:

1. **Fontes canônicas** — documentos, dados e eventos que podem provar uma afirmação.
2. **Camada de fatos e sínteses** — claims normalizados, decisões e relações com proveniência.
3. **Memória procedural** — SOPs, rubricas, contratos, skills e exemplos aprovados.
4. **Memória episódica** — o que aconteceu em execuções, com identidade, tempo e outcome.
5. **Projeções recuperáveis** — índice lexical, vetorial ou grafo, todos reconstruíveis a partir das fontes.
6. **Governança** — ACL, validade, supersessão, conflito, retenção, exclusão e auditoria.

O paper [CoALA](https://arxiv.org/abs/2309.02427) posiciona o language model dentro de uma arquitetura maior com memória de trabalho, episódica, semântica e procedural. O [paper original de RAG](https://arxiv.org/abs/2005.11401) separa memória paramétrica de memória não paramétrica recuperável.

Janela longa e recuperação são complementares. [Lost in the Middle](https://arxiv.org/abs/2307.03172) mostra que o uso da informação depende da posição no contexto. Mais tokens não resolvem ACL, staleness, conflito ou proveniência. O brain deve entregar uma projeção pequena, atual, autorizada e citável — não o depósito inteiro.

O caminho de escrita exige mais cautela que o de leitura. Runs produzem observações, traces e candidatos a memória; não devem escrever output cru diretamente como verdade. Classificação, proveniência, validação, aprovação, versão, supersessão e reconstrução dos índices pertencem à governança do brain.

## Fronteiras de interoperabilidade

O [MCP](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) padroniza descoberta e invocação de tools e dados por schemas. Isso reduz cola, mas não padroniza o modelo, a memória, o loop, os evals nem a política completa de autorização. A fronteira técnica ainda precisa de contrato semântico local.

Protocolos ajudam a trocar componentes. Não eliminam diferenças de capability ou modos de falha. A interoperabilidade útil é conquistada por contrato + teste + observabilidade.

## Protocolo de promoção

Uma troca segura controla variáveis em sequência:

```text
baseline reproduzível
→ capability check
→ eval offline com casos retidos e múltiplos trials
→ shadow sem efeitos
→ canary com blast radius explícito
→ promoção versionada do alias
→ observação + rollback
```

O modelo pode ser promovido numa rota e rejeitado em outra. Qualidade média não compensa violação crítica de segurança, autoridade ou acesso.

## Limites e contraexemplos

- Workflow determinístico e regulado pode justificar um harness mais explícito.
- Capability exclusiva pode justificar lock-in consciente atrás de uma fronteira e com dívida de saída documentada.
- Protótipo reversível não precisa antecipar uma plataforma multi-provider.
- Brain pequeno pode começar em arquivos versionados e busca simples.
- “Thin harness” é uma definição operacional desta síntese; faltam comparações independentes e longitudinais contra harnesses espessos.

A regra é preservar a opção de troca sem pagar antecipadamente por todas as trocas imagináveis.

## Invariantes da arquitetura

- O modelo não é fonte da verdade da empresa.
- O harness não vira um segundo modelo codificado em regras frágeis.
- O brain não recebe autoridade global por conveniência.
- A projeção de busca não substitui a fonte original.
- A troca de modelo não é promovida por leaderboard.
- Resultado no mundo vale mais que a declaração “concluído” do agente.
- Toda escrita relevante registra autor, tempo, fonte e possibilidade de reversão.

## Gate mínimo de troca

Um modelo candidato só substitui o atual quando:

1. possui as capabilities obrigatórias;
2. mantém o contrato de entrada e saída;
3. passa casos representativos e retidos;
4. preserva segurança e autoridade;
5. atinge o outcome no ambiente, não apenas um texto plausível;
6. tem custo e latência dentro do alvo;
7. foi testado em múltiplos trials quando há variância;
8. possui fallback e rollback operacionais;
9. sua promoção fica versionada e observável.

## Navegação

[Aula 21b](../aulas/21b-modelos-substituiveis-harness-fino-cerebro-modular.md) · [Aula 19 — Routing](../aulas/19-routing-de-modelos.md) · [Aula 21 — Harness](../aulas/21-harness.md) · [Aula 12f — Menor cérebro](../aulas/12f-menor-cerebro-suficiente.md) · [FONTES](../FONTES.md) · [Curso](../README.md)
