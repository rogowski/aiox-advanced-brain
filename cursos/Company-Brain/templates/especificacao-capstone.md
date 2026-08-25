---
type: template
course: company-brain
status: canonical
canonical_scope: cursos/Company-Brain
---

# Especificação do capstone

Use na [aula 18](../aulas/18-projeto-integrador.md). Oito seções + replay da [Rubrica](../Rubrica.md). Case real preferido; [Atlas Assist](../casos/atlas-assist.md) só como treino; [Norte Log](../casos/norte-log.md) para transferência. Sem cluster, sem vendor como fundação.

```yaml
# 1. Case e justificativa
case:
  nome: ""
  sintoma_institucional: ""
  agents_que_apontam_o_mesmo_locator: []
  decisao: "" # construir | veto
  por_que_a_12f_nao_basta: ""
  condicao_de_reabertura: ""

# 2. Mapa de módulos
modulos:
  - job: fontes
    autoridade: ""
    ritmo: ""
    fronteira: ""
  - job: fatos_e_sinteses
    autoridade: ""
    ritmo: ""
    fronteira: ""
  - job: procedural
    autoridade: ""
    ritmo: ""
    fronteira: ""
  - job: episodico
    autoridade: ""
    ritmo: ""
    fronteira: ""
  - job: projecoes
    autoridade: ""
    ritmo: ""
    fronteira: ""
  - job: governanca
    autoridade: ""
    ritmo: ""
    fronteira: ""

# 3. Ledger de proveniência
claims:
  - id: ""
    afirmacao: ""
    fonte: ""
    data: ""
    uso: ""
    status: "" # pronto | gap | recusado
  - id: ""
    afirmacao: ""
    fonte: ""
    data: ""
    uso: ""
    status: ""
  - id: ""
    afirmacao: ""
    fonte: ""
    data: ""
    uso: ""
    status: ""
conflito:
  fontes: []
  resolver_policy: ""

# 4. Contrato de governança
governanca:
  acl:
    - ator: ""
      le: []
      escreve: []
      revoga: []
  validade: ""
  supersessao: ""
  conflito: ""
  retencao: ""
  exclusao: ""
  auditoria: ""

# 5. Política de contexto
politicas:
  - workload: ""
    query: ""
    filtro: ""
    acl: ""
    projecao: ""
    teto: ""
    fallback_insuficiente: ""

# 6. Contrato brain↔harness
contrato:
  entrada:
    query: ""
    acl: ""
    actor: ""
  saida:
    claim: ""
    fonte: ""
    citacao: ""
    conflito_ou_buraco: ""
  citacao_obrigatoria: true
  latencia_alvo:
    intencao: ""
    nao_e_sla_de_produto: ""
  fallback: ""
  brain_sem_maos: ""

# 7. Gate de aprendizado
gate:
  candidato_exemplo: ""
  classificacao: ""
  aprovador: ""
  versao: ""
  projecao_reconstruida: ""
  o_que_nao_volta: []

# 8. Anti-padrões
antipadroes:
  dump: {aparece: false, justificativa: ""}
  vector_oracle: {aparece: false, justificativa: ""}
  janela_como_prova: {aparece: false, justificativa: ""}
  autoridade_global: {aparece: false, justificativa: ""}
  harness_brain: {aparece: false, justificativa: ""}
  modelo_como_verdade: {aparece: false, justificativa: ""}
  escrita_sem_gate: {aparece: false, justificativa: ""}
  vendor_como_fundacao: {aparece: false, justificativa: ""}

# Replay de mesa (prova transversal obrigatória; não é a nona seção — sem cluster)
replay:
  claim_autorizado:
    actor: ""
    query: ""
    saida: {claim: "", fonte: "", citacao: "", data: ""}
    prova_que_o_contrato_fechou: ""
  tentativa_sem_acl:
    actor: ""
    dado_restrito: ""
    recusa_antes_do_retrieve: true
    o_que_nao_entra_no_prompt: ""
  conflito_ou_buraco:
    vozes: []
    o_que_o_brain_devolve: "" # conflito | buraco
    modelo_desempata: false
  feedback_recusado:
    candidato: ""
    classificacao: ""
    por_que_o_gate_barra: ""
    nao_vira: "" # sop | claim_vigente | dump
```
