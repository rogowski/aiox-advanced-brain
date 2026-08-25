---
type: template
course: company-brain
status: canonical
canonical_scope: cursos/Company-Brain
---

# Matriz ACL

Use na [aula 09](../aulas/09-acl-e-autoridade.md). Um case por ficha. Treino: [Atlas Assist](../casos/atlas-assist.md). Não invente ator sem declarar.

```yaml
case: ""
workload: ""

atores:
  - id: ""
    papel: ""

modulos:
  - fontes
  - claims
  - procedural
  - episodica
  - projecoes

operacoes:
  - ler
  - escrever
  - revogar

celulas:
  - ator: ""
    modulo: ""
    operacao: "" # ler | escrever | revogar
    permitido: false
    recusa: ""

dado_restrito:
  id: MARGEM-CLIENTE
  quem_le: []
  quem_nao_le: []

escrita_de_fato:
  quem_escreve_fato: []
  quem_escreve_candidato: []
  agent_escreve_fato: false

revogacao:
  quem_revoga: []

efeito:
  brain_dispara_efeito: false
  autoridade_de_efeito: harness
  efeitos_proibidos_ao_brain: []

acl_antes_do_retrieve: ""
```
