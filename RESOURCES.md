# Arquitetura LLM resiliente — Resources

## Knowledge

- [Stanford AI Index 2026 — Technical Performance](https://hai.stanford.edu/assets/files/ai_index_report_2026_chapter_2_technical.pdf)
  Evidência atual sobre convergência dos modelos líderes, saturação de benchmarks, inteligência irregular e falhas de agentes. Use para: explicar por que a camada de modelo é volátil e precisa de gates próprios.
- [Stanford AI Index 2025 — State of AI in 10 Charts](https://hai.stanford.edu/news/ai-index-2025-state-of-ai-in-10-charts)
  Dados sobre queda de custo e redução do tamanho necessário para atingir limiares antigos de capacidade. Use para: mostrar a velocidade da curva de preço/desempenho.
- [OpenAI API — Deprecations](https://developers.openai.com/api/docs/deprecations)
  Histórico oficial de APIs e modelos aposentados, com substitutos. Use para: provar que lifecycle de modelo precisa ser uma preocupação operacional.
- [Anthropic — Model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)
  Histórico oficial de retirement dos modelos Claude. Use para: comparar ciclos sem depender de um único fornecedor.
- [Anthropic — Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
  Princípios de patterns simples e compostos, workflows versus agents e augmented LLM. Use para: justificar harness mínimo e complexidade progressiva.
- [Anthropic — Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps)
  Experimentos sobre componentes do harness que ficam obsoletos à medida que modelos melhoram. Use para: ensinar por que “thin” é uma disciplina de remoção guiada por evidência.
- [Boris Cherny — Building Claude Code](https://www.youtube.com/watch?v=qyPCVqFUyDo)
  Entrevista primária com a recomendação semestral de retirar `CLAUDE.md`, skills e hooks e reconstruir por ablação. Use para: citar a fala com o contexto completo e não atribuí-la indevidamente a `AGENTS.md`.
- [Anthropic — The new rules of context engineering](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models)
  Relato da remoção de mais de 80% do system prompt do Claude Code e da migração para progressive disclosure. Use para: explicar overconstraint, conflito e obsolescência de scaffolding.
- [Anthropic Help Center — CLAUDE.md and better prompts](https://support.claude.com/en/articles/14553240-give-claude-context-claude-md-and-better-prompts)
  Orientação de arquivo curto, denso em sinal e revisão trimestral. Use para: diferenciar manutenção normal de uma ablação completa.
- [OpenAI — Favor leaner prompts](https://developers.openai.com/api/docs/guides/latest-model#favor-leaner-prompts)
  Resultados direcionais de evals internos com melhora de score e redução de tokens e custo. Use para: quantificar o custo possível de instrução redundante sem universalizar o efeito.
- [Evaluating AGENTS.md](https://arxiv.org/abs/2602.11988)
  CTXbench com 138 tarefas e 12 repositórios; arquivos aumentaram exploração e custo sem ganho significativo. Use para: defender requisitos humanos mínimos e revelar documentação redundante.
- [On the Impact of AGENTS.md](https://arxiv.org/abs/2601.20404)
  Estudo de 124 PRs em dez repositórios com runtime e output tokens menores quando o arquivo estava presente. Use para: mostrar o contraexemplo e impedir a tese “instrução persistente sempre atrapalha”.
- [Don't Blame the Large Language Model](https://arxiv.org/html/2607.03691v2)
  Comparação longitudinal de 35 versões de harness com LLM fixo. Use para: mostrar crescimento de custo e chamadas sem ganho correspondente e a necessidade de eval do par modelo+harness.
- [Anthropic — Scaling Managed Agents: Decoupling the brain from the hands](https://www.anthropic.com/engineering/managed-agents)
  Caso de separação entre brain/harness, hands e session por interfaces. Use para: estudar desacoplamento operacional contemporâneo.
- [Anthropic — Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
  Estrutura de evals, graders de outcome e análise de trajetórias. Use para: construir o gate de substituição de modelos.
- [OpenAI — Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
  Desenvolvimento guiado por evals, dados representativos, comparação contínua e cobertura de casos típicos, extremos e adversariais. Use para: estruturar baseline, slices e promoção de candidatos.
- [OpenAI — A practical guide to building agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
  Modelo, tools, instruções, loop e seleção por baseline/evals. Use para: uma anatomia simples e um processo de redução de custo.
- [Model Context Protocol — Tools specification](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)
  Contratos e descoberta de tools por schema. Use para: entender o que MCP desacopla e o que continua no harness.
- [NSA — MCP Security Design Considerations](https://media.defense.gov/2026/Jun/02/2003943289/-1/-1/0/CSI_MCP_SECURITY.PDF)
  Riscos de prompt injection, tool poisoning, cadeias e exfiltração. Use para: impedir que “thin” seja interpretado como ausência de segurança.
- [Cognitive Architectures for Language Agents](https://arxiv.org/abs/2309.02427)
  Taxonomia de memória de trabalho, episódica, semântica e procedural. Use para: decompor o company brain além de um vector database.
- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)
  Paper fundador que separa memória paramétrica e não paramétrica e discute atualização e proveniência. Use para: explicar por que conhecimento institucional vive fora do modelo.
- [Microsoft Research — Project GraphRAG](https://www.microsoft.com/en-us/research/project/graphrag/overview/)
  Grafos e resumos de comunidades para perguntas globais e relacionais. Use para: ensinar múltiplas projeções sem vender grafo como oráculo.
- [Lost in the Middle](https://arxiv.org/abs/2307.03172)
  Evidência de degradação conforme posição da informação em contexto longo. Use para: recusar a ideia de que uma janela grande substitui curadoria.
- [Long Context RAG Performance](https://arxiv.org/abs/2411.03538)
  Estudo de 20 modelos sob crescimento de contexto. Use para: separar capacidade nominal de uso confiável do contexto.
- [RouteLLM](https://arxiv.org/abs/2406.18665)
  Routing entre modelos forte e fraco, com ganhos e limites de transferência. Use para: mostrar que fitness depende da distribuição real.
- [Acervo AIOX — Modelo, contexto, memória, tool e skill](cursos/Introducao-a-Arquitetura-de-Sistemas/aulas/22-modelo-contexto-memoria-tool-skill.md)
  Anatomia canônica de um sistema agentic. Use para: diagnosticar a camada responsável por cada falha.
- [Acervo AIOX — Routing de modelos](cursos/AIOX-Agent-Engineering/aulas/19-routing-de-modelos.md)
  Política por task type, fitness, fallback e métricas. Use para: conectar substituição a operação.
- [Acervo AIOX — O menor cérebro suficiente](cursos/AIOX-Agent-Engineering/aulas/12f-menor-cerebro-suficiente.md)
  Escada e veto contra “instalar um cérebro” sem sintoma provado. Use para: conter complexidade de memória.
- [Acervo AIOX — Harness](cursos/AIOX-Agent-Engineering/aulas/21-harness.md)
  Runtime, auth, tools, logs e budget. Use para: distinguir laboratório de ambiente de servir.

## Wisdom (Communities)

- [MCP Working and Interest Groups](https://modelcontextprotocol.io/community/working-interest-groups)
  Grupos com governança pública, Discord e GitHub Discussions. Use para: confrontar decisões de interoperabilidade e segurança com mantenedores e praticantes.
- [Agentic AI Foundation user community](https://home.mlops.community/)
  Comunidade vendor-neutral focada em agentes em produção, MLOps e padrões abertos. Use para: validar decisões de observabilidade, evals e operação em casos reais.

## Gaps

- Não existe definição acadêmica universal de “thin harness”; a definição da aula é operacional.
- Faltam comparações independentes thin versus thick harness através de várias gerações de modelos.
- Benchmarks públicos ainda cobrem mal revogação, supersessão, deleção, conflito e permissões de um company brain real.
