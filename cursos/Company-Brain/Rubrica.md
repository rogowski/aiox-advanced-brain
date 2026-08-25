---
type: rubric
course: company-brain
status: canonical
canonical_scope: cursos/Company-Brain
---

# Rubrica

Protocolo: [aula 18](aulas/18-projeto-integrador.md) · Artefato: [Projeto Integrador](Projeto-Integrador.md) · Schema: [especificacao-capstone](templates/especificacao-capstone.md).

## Dimensões e níveis (capstone)

| Dimensão | Insuficiente | Suficiente | Exemplar |
|----------|-------------|-----------|---------|
| **Mapa de módulos** | Faltam módulos ou não tem autoridade/ritmo | Seis módulos com job, autoridade e ritmo | Módulos com fronteira entre si e justificativa de separação |
| **Ledger de proveniência** | Claims sem fonte ou fonte genérica | 3+ claims com claim → fonte → data → uso | Conflito documentado + resolver policy |
| **Contrato de governança** | Sem ACL ou sem validade/supersessão | ACL, TTL e supersessão especificados | Inclui trilha de auditoria e gatilhos de exclusão |
| **Política de contexto** | Manda o depósito inteiro ou não há filtro | Pipeline de recuperação com filtro de ACL | Tamanho máximo justificado + fallback quando contexto insuficiente |
| **Contrato brain↔harness** | Ausente ou vago | Entrada, saída e latência-intenção especificados | Inclui fallback e citação obrigatória |
| **Menor mecanismo** | Não aplicado ou ignorado | Escada aplicada com veto ou justificativa | Veto auditável com condição de reabertura |
| **Anti-padrões** | Anti-padrões presentes sem justificativa | Rubrica preenchida sem anti-padrão residual | Justificativas explícitas para cada recusa |
| **Replay de mesa** | Ausente, ou uma jogada contradiz ACL/gate/contrato | Quatro jogadas preenchidas e coerentes com as seções 3–7 | Inclui IDs do case e recusa explícita em cada jogada negativa |

Latência no contrato é **intenção de recorte**, não SLA de produto.

## Falhas críticas (bloqueiam aprovação)

- Ausência de mecanismo de ACL em qualquer módulo.
- Nenhuma fonte canônica identificada (tudo inferido do modelo ou do índice).
- Política de contexto é "enviar tudo" (dump explícito).
- Nenhum mecanismo de supersessão (claims não expiram nunca).
- Gate de aprendizado ausente (toda falha bruta vira verdade).
- Vendor específico como fundação do modelo mental (não como opção de implementação futura).
- Replay de mesa ausente ou incoerente (claim sem cadeia; ACL só no output; modelo desempata; falha bruta vira fato).

## Evidência aceitável

- Especificação textual (Markdown, YAML ou combinação) que outro humano consiga auditar.
- Não precisa de cluster, banco ou código rodando.
- Bloqueio de ambiente é estado honesto, não aprovação.
- Atlas Assist só como treino declarado; Norte Log só como transferência declarada.

## Lote M0 (ainda útil como entrada)

| Dimensão | Insuficiente | Suficiente |
|----------|-------------|------------|
| Diagnóstico | Culpa o modelo ou pede ferramenta | Nomeia onde o conhecimento vive e recusa um vizinho |
| Camadas | Mistura brain, harness e modelo | A próxima mudança cai em uma camada |
| Promessa | “Mandar o conhecimento” | Quatro adjetivos + uma recusa + um claim citável |

[Curso](README.md)
