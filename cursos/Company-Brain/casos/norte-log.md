---
type: teaching-case
course: company-brain
status: canonical
canonical_scope: cursos/Company-Brain
---

# Caso de transferência — Norte Log

Operadora B2B de frete rodoviário. Três agents já rodam. **Este caso não aparece nas aulas.** Use-o no quiz de transferência e no capstone se quiser provar que o mecanismo não depende do vocabulário da Atlas.

| Agent | Outcome | O que “sabe” hoje |
|-------|---------|-------------------|
| Roteamento | escolhe janela de coleta L1 | wiki + dump do Drive operacional |
| Cotação | rascunha preço de frete | modelo interno fine-tunado em 2025 |
| Auditoria de SLA | aceita ou recusa atraso | o que o líder de ops (Rui) decide no Slack |

## Outcome observável

Coleta classificada com SLA **vigente**, cotação **sem custo interno que o autor não pode ver**, atraso **com fonte citável**.

## Inventário (IDs próprios — não misture com a Atlas)

| ID | O que é | Habitat | Problema |
|----|---------|---------|----------|
| POL-PRAZO-2024 | página do wiki, coleta em 48 h | documento sem dono | revogada em maio; o retrieve ainda a trata como vigente |
| SLK-RUI-2026-05-08 | thread do Rui: coleta em 24 h | cabeça de gente | resolução privada; não é fonte |
| FT-NORTE-2025 | snapshot do modelo interno | pesos | deprecação em 60 dias; ainda diz 48 h |
| IDX-OPS | vector store de wiki + Drive + Slack + tickets | store-oráculo | sem ACL, sem tipo, sem gate |
| T-2207 | transcript de atraso mal justificado, colado no IDX-OPS | episódio bruto | no dia seguinte o roteamento trata como SOP |
| SOP-ATRASO | PDF na pasta do Rui, “como abrir atraso” | procedural informal | duas versões; nenhuma aprovada |
| CUSTO-ROTA | planilha de custo por rota no mesmo índice | dado restrito | estagiário da cotação vê no rascunho |

## Pessoas e papéis

| Ator | Pode ler SLA público | Pode ler custo de rota | Pode escrever claim | Pode revogar |
|------|----------------------|------------------------|---------------------|--------------|
| Agent de roteamento | sim | não | não | não |
| Agent de cotação | sim | não | não | não |
| Agent de auditoria | sim | não | candidato, não fato | não |
| Rui (ops) | sim | não | sim, com aprovação | sim |
| Estagiário comercial | sim | não | não | não |

Não invente ID. Não copie POL-REEMB-2023 para este case. Se o seu case real existir, ele vence os dois casos didáticos.

[Atlas Assist](atlas-assist.md) · [Curso](../README.md)
