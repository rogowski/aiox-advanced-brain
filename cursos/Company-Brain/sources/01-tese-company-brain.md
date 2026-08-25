---
type: source-brief
course: company-brain
source_id: "01"
status: canonical
canonical_scope: cursos/Company-Brain
updated: "2026-08-25"
---

# Fonte 01 — Tese operacional do company brain

Síntese autocontida do curso. O conceito “company brain” não tem definição acadêmica consolidada. A definição abaixo é **operacional** e rastreia papers e a tese já canônica do acervo.

## Definição operacional

Company brain é o conhecimento institucional **fora dos pesos do modelo**. Modular significa separar jobs, autoridade e ritmo de atualização.

Desenho mínimo:

1. Fontes canônicas — documento, dado ou evento que prova um claim
2. Fatos e sínteses — claims normalizados com proveniência
3. Memória procedural — SOP, rubrica, contrato, skill, exemplo aprovado
4. Memória episódica — execução, decisão, feedback e outcome no tempo
5. Projeções recuperáveis — lexical, vetorial ou grafo, reconstruíveis a partir das fontes
6. Governança — ACL, validade, supersessão, conflito, retenção, exclusão, auditoria

## Mecanismo que o curso precisa

**Paramétrico vs recuperável.** [Lewis et al., 2020](https://arxiv.org/abs/2005.11401) separam o que ficou nos pesos (atualização cara, opaca, lenta) do que se recupera e se edita. Fine-tune e “o modelo já sabe” são memória paramétrica. Wiki, ledger e índice são candidatos a memória recuperável — só viram brain se tiverem dono, validade e citação.

**Jobs de memória de um language agent.** [CoALA](https://arxiv.org/abs/2309.02427) posiciona o modelo dentro de uma arquitetura com memória de trabalho, episódica, semântica e procedural. O company brain é a versão institucional desses jobs: não a memória de uma sessão, a memória da empresa.

**Janela não é curadoria.** [Lost in the Middle](https://arxiv.org/abs/2307.03172) mostra que a posição no contexto altera o uso da evidência. [Long Context RAG](https://arxiv.org/abs/2411.03538) mostra que capacidade nominal de janela não é uso confiável. Mais tokens não resolvem ACL, staleness, conflito nem exclusão.

**Interface, não monolith.** [Anthropic — Decoupling the brain from the hands](https://www.anthropic.com/engineering/managed-agents) separa raciocínio, ambiente e sessão. [Harness design for long-running apps](https://www.anthropic.com/engineering/harness-design-long-running-apps) mostra que scaffolding congela hipóteses sobre o modelo; o que deve ficar são invariantes. O brain não herda autoridade de execução.

**Três camadas, três relógios.** Neste acervo a tese foi introduzida em `cursos/AIOX-Agent-Engineering/aulas/21b-modelos-substituiveis-harness-fino-cerebro-modular.md`. Este curso desenvolve o relógio lento. Não substitui o contrato de troca de modelo.

**Escrita é mais perigosa que leitura.** Run produz observação e candidato a memória. Output cru não vira fato. Classificação, aprovação, versão e supersessão pertencem à governança — aula 15.

## O que o curso não pode afirmar

- Não há benchmark público de ACL, supersessão, conflito e retenção de um company brain real.
- Não há paper que defina “company brain” como entidade multi-módulo.
- Não há comparação empírica entre estratégias de governança. O curso ensina contratos, não ranking de produtos.

## Navegação

[Aula 01](../aulas/01-empresa-vive-nos-pesos.md) · [Aula 02](../aulas/02-tres-relogios.md) · [Aula 03](../aulas/03-o-que-o-brain-entrega.md) · [Aula 15](../aulas/15-aprendizado-de-volta.md) · [Caso](../casos/atlas-assist.md) · [Fontes](../FONTES.md)
