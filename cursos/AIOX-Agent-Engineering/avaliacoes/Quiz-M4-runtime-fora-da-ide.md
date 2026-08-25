---
type: quiz
course: aiox-agent-engineering
module: M4
question_count: 4
passing_score: 80
status: canonical
canonical_scope: cursos/AIOX-Agent-Engineering
---
# Quiz M4 — Runtime fora da IDE

[Módulo M4](../modulos/M4-runtime-fora-da-ide.md) · [Avaliações](../Assessments.md)

### 1. Qual arranjo permite trocar o modelo sem perder a memória nem a governança da capacidade?

A. Guardar regras e fatos no prompt do modelo principal
B. Usar qualquer API compatível e dispensar avaliações
C. Separar modelo, thin harness e company brain, promovendo candidatos por evals
D. Duplicar o conhecimento em cada provider

### 2. Qual é a primeira etapa segura fora da IDE?

A. A menor interface que preserve contratos e produza logs reproduzíveis
B. Um SaaS completo
C. Autonomia sem supervisão
D. Multi-tenant global

### 3. Por que usar uma escada progressiva de runtime?

A. Para evitar documentação
B. Para aumentar autonomia conforme evidência e controles amadurecem
C. Para trocar de modelo semanalmente
D. Para remover humans-in-the-loop

### 4. Qual artefato prova que a capacidade saiu da IDE?

A. Uma captura do chat
B. Um prompt exportado
C. Uma lista de ferramentas
D. Uma execução acionável com contrato, logs e resultado recuperável

<details>
<summary>Gabarito comentado</summary>

1. **C.** O modelo fica substituível porque operação e conhecimento possuem contratos próprios; adapter sem eval não prova equivalência.
2. **A.** A primeira interface deve preservar o que já foi validado.
3. **B.** Autonomia cresce com confiança conquistada.
4. **D.** Fora da IDE significa execução reproduzível, não apenas prompt portátil.

</details>

## Transferência

Defina o primeiro degrau de runtime da sua capacidade e o log mínimo necessário.
