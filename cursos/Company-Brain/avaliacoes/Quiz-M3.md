---
type: quiz
course: company-brain
module: M3
status: canonical
canonical_scope: cursos/Company-Brain
questions: 4
---

# Quiz M3 — Interface: o brain alimentando agents

Este quiz fecha o M3. Faça depois das aulas 13–15.

[Módulo M3](../modulos/M3-interface-o-brain-alimentando-agents.md) · [Avaliações](../Assessments.md)

### 1. Qual pipeline descreve uma política de contexto suficiente?

A. Corpus inteiro → prompt → “o modelo filtra”
B. Fine-tune semanal → prompt vazio, porque a política “já está nos pesos”
C. Janela máxima → esperança de que Lost in the Middle não se aplique a este vendor
D. Query → filtro → ACL → projeção → tamanho máximo

### 2. O contrato brain↔harness precisa declarar no mínimo:

A. Entrada (query + ACL + actor), saída (claim + fonte + citação) e fallback
B. O identificador físico do modelo vencedor do mês, como se fosse o locator
C. Um servidor MCP, porque o protocolo já seria a memória da empresa
D. Autoridade de efeito no brain (pagar, fechar ticket) para “não depender do harness”

### 3. Quando um aprendizado pode voltar ao brain?

A. Sempre que o agent marcar o ticket como concluído
B. Depois de um gate de aprovação; falha bruta não vira fato
C. Quando o transcript for semanticamente parecido com a SOP informal
D. Quando o custo de tokens daquela run estiver baixo o bastante para “valer gravar”

### 4. MCP, neste curso, padroniza o quê?

A. O company brain inteiro — memória, ACL e supersessão inclusas
B. O loop, a memória e a política completa de autorização institucional
C. Descoberta e invocação de tools por schema — e não o resto
D. A equivalência entre todos os modelos, o que tornaria o contrato desnecessário

<details>
<summary>Gabarito comentado</summary>

1. **D.** Política é recorte governado. Pesos, dump e janela-como-prova são recusas.
2. **A.** Interface estável. Modelo, MCP e mãos no brain não são o contrato.
3. **B.** Sem gate, similaridade e “concluído” envenenam o retrieve.
4. **C.** Protocolo reduz cola. Não substitui memória, loop, eval nem ACL.

</details>

## Transferência

Desenhe o contrato da **cotação** em [Norte Log](../casos/norte-log.md): o que o harness pergunta, o que o brain devolve se CUSTO-ROTA aparecer, e o que acontece se POL-PRAZO-2024 for a única “fonte” vigente no wiki.

[↑ M3](../modulos/M3-interface-o-brain-alimentando-agents.md) · [↑ Curso](../README.md)
