---
type: quiz
course: company-brain
module: M2
status: canonical
canonical_scope: cursos/Company-Brain
questions: 4
---

# Quiz M2 — Governança

Este quiz fecha o M2. Faça depois das aulas 09–12.

[Módulo M2](../modulos/M2-governanca-a-camada-de-confiabilidade.md) · [Avaliações](../Assessments.md)

### 1. Quando a ACL deve ser aplicada?

A. Depois que o modelo já leu o documento, para “economizar” retrieve e filtrar o output
B. Só no harness (least privilege da tool); o brain pode projetar tudo e o prompt pede discrição
C. Antes da recuperação, por módulo, com least privilege
D. Nunca no retrieve: confidencialidade é um adjetivo no system prompt

### 2. O que é supersessão neste curso?

A. Apagar o histórico para o agent não se confundir
B. Trocar de modelo sem eval, levando a política no adapter
C. Manter dois claims vigentes para a mesma política e deixar o ranking decidir
D. Um claim substitui formalmente outro, com rastro do anterior

### 3. Duas fontes do mesmo domínio divergem. Qual é a resposta suficiente?

A. Registrar o conflito e a resolver policy, sem esconder o buraco
B. Pedir ao modelo para “escolher a melhor” e gravar a escolha como fato
C. Indexar as duas no mesmo store e mandar as duas no prompt, sem regra
D. Fine-tunar a fonte mais recente para o conflito “sumir dos pesos”

### 4. Qual item pertence ao ciclo de vida do brain?

A. O alias de roteamento do modelo da semana
B. Ingestão aprovada, retenção, exclusão e trilha de auditoria
C. O temperature e o cap de tokens da rota
D. A recência de crawl do índice, usada como se fosse vigência jurídica

<details>
<summary>Gabarito comentado</summary>

1. **C.** ACL tardia vaza. Prompt educado e filtro de output confessam o vazamento.
2. **D.** Revogar sem rastro apaga auditoria; conviver sem regra é conflito eterno; política no adapter rouba o relógio.
3. **A.** Conflito explícito. Média, dump e fine-tune escondem o buraco.
4. **B.** Ciclo de vida governa o conhecimento. Alias, temperature e crawl não aprovam ingestão.

</details>

## Transferência

Em [Norte Log](../casos/norte-log.md): quem lê CUSTO-ROTA? POL-PRAZO-2024 revogada apaga ou fica? O que o brain devolve enquanto 24 h não tem documento? T-2207 entra como SOP?

[↑ M2](../modulos/M2-governanca-a-camada-de-confiabilidade.md) · [↑ Curso](../README.md)
