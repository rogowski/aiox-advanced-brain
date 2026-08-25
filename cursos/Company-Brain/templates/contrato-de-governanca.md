---
type: template
course: company-brain
status: canonical
canonical_scope: cursos/Company-Brain
---

# Contrato de governança

Use na [aula 12](../aulas/12-ciclo-de-vida.md). Fecha o M2 com as fichas das [aulas 09](../aulas/09-acl-e-autoridade.md)–[11](../aulas/11-conflito-e-proveniencia.md). Treino: [Atlas Assist](../casos/atlas-assist.md).

```yaml
case: ""
workload: ""

acl:
  ficha: matriz-acl
  antes_do_retrieve: true
  margem_no_chamador_proposta: false

validade:
  ficha: politica-de-validade
  revoga_sem_apagar: true
  slack_supersede: false

conflito:
  ficha: resolver-policy
  ledger_aberto: true
  modelo_escolhe: false

ciclo:
  ingestao_aprovada: ""
  recusados_de_ingestao:
    - id: T-8841
      entra_como: episodio
      nao_entra_como: sop
  retencao: ""
  exclusao: ""
  auditoria:
    quem_leu: ""
    quem_escreveu: ""
    quem_revogou: ""
    quem_ingestou: ""

efeito:
  brain_executa: false
  harness_executa: true

lacuna_de_benchmark: ""
```
