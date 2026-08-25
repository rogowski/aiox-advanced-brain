---
type: template
course: company-brain
status: canonical
canonical_scope: cursos/Company-Brain
---

# Inventário de fontes

Use na [aula 04](../aulas/04-fontes-canonicas.md). Um case por ficha. Treino: [Atlas Assist](../casos/atlas-assist.md). Não invente ID sem declarar.

```yaml
case: ""
outcome_observavel: ""

fontes:
  - id: ""
    tipo: documento # documento | dado | evento
    o_que_prova: ""
    vigente: "" # sim | nao | nao_se_aplica
    dono_da_vigencia: ""
    locator: ""
    o_que_nao_pode_provar: ""

recusados:
  - id: ""
    aparenta_fonte: ""
    por_que_nao_e: "" # copia | sintese | computado_sem_origem | pesos | projecao | resolucao_privada
    vira_fonte_se: ""

dado_computado:
  afirmacao: ""
  planilha_origem: ""
  recusa_se_faltar_origem: ""
```
