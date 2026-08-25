---
type: glossary-term
course: aiox-advanced
tags:
- glossario
- aiox
- course-brain
updated: '2026-08-25'
status: reference
canonical_scope: cursos/AIOX Advanced
freq:
  aiox_advanced: 22
  aiox_advanced_squads: 0
  total: 22
  counted_at: '2026-08-25'
---
# Gauntlet Loop

Arquitetura de iteração que compara um artefato real com uma barra explícita, separa construção de avaliação, usa evidência antes da opinião, corrige o maior gap e encerra por regra de parada.

## Como é usado

Use **Gauntlet Loop** quando o erro evitado justifica mais de uma execução e existe artefato, referência legítima, checks, crítico separado, budget e autoridade de aceite.

**Exemplo prático:** na aula [[77-gauntlet-loop]], o aluno preserva uma baseline, roda checks, entrega o artefato a um crítico em contexto novo, aplica um único patch e compara antes/depois antes de decidir `STOP`, `CONTINUE` ou `ESCALATE`.

**Não confunda:** Gauntlet não é “pedir até ficar perfeito”, fan-out obrigatório nem nome genérico para qualquer loop. [[Goal vs Loop]] define destino e repetição; Gauntlet acrescenta barra, separação builder–crítico, ratchet, regressão e freio.

**Frequência nos cursos:** **22** menções (AIOX Advanced: 22 · AIOX Advanced Squads: 0).

## Aulas

- [[77-gauntlet-loop]]
- [[11-goal-vs-loop]]
- [[21-deterministico-primeiro-llm-onde-gera-ouro]]
- [[50-rider-modo-elicitacao]]

## Ver também

- [[No-self-review]]
- [[Stop rule]]
- [[Determinismo Progressivo]]
- [[Evidência]]
- [[Glossário AIOX Advanced]]
