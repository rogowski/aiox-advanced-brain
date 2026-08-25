---
type: template
course: company-brain
status: canonical
canonical_scope: cursos/Company-Brain
---

# Resolver policy

Use na [aula 11](../aulas/11-conflito-e-proveniencia.md). Mesmo case das [aulas 09](../aulas/09-acl-e-autoridade.md)–[10](../aulas/10-validade-e-supersessao.md). Treino: [Atlas Assist](../casos/atlas-assist.md).

```yaml
case: ""
dominio: "" # ex.: prazo de reembolso

candidatos:
  - id: ""
    afirmacao: ""
    tipo: "" # documento | resolucao_privada | pesos
    status: "" # vigente | revogado | gap | recusado

regra:
  prioridade: []
  fecha_quando: ""
  o_que_nao_faz:
    - modelo_escolhe_a_melhor
    - media_dos_tres
    - fine_tune_desempata
  buraco_se_nao_fechar: ""

ledger_aberto:
  visivel_para: []
  escondido_do_chamador: []
  texto_do_conflito: ""

lacuna_de_benchmark: ""
```
