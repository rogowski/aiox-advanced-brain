---
type: template
course: company-brain
status: canonical
canonical_scope: cursos/Company-Brain
---

# Política de contexto

Use na [aula 13](../aulas/13-politica-de-contexto.md). Uma ficha **por workload / agent**. Não recicle a [promessa](promessa-do-brain.md) sem nomear as diferenças. Treino: [Atlas Assist](../casos/atlas-assist.md).

```yaml
case: ""
workload: "" # triagem | proposta | compliance | outro
agent: ""
politica:
  nome: ""
  query: ""
  filtro: ""
  acl:
    ator: ""
    pode_ler: []
    nao_pode_ler: []
  projecao: ""
  teto: ""
  saida: ""
  fallback_insuficiente: ""
diferenca_vs_outro_agent: ""
recusas:
  - dump
  - janela_como_prova
  - uma_politica_para_todos_os_agents
```
