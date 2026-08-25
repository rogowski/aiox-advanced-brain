---
type: project
course: company-brain
status: canonical
canonical_scope: cursos/Company-Brain
---

# Projeto integrador

Especificar um company brain mínimo para um **case real**, capaz de alimentar pelo menos um agent — preferencialmente os que compartilham o mesmo locator. Protocolo passo a passo: [aula 18](aulas/18-projeto-integrador.md). Nota: [Rubrica](Rubrica.md). Schema: [especificacao-capstone](templates/especificacao-capstone.md).

[Atlas Assist](casos/atlas-assist.md) vale como **treino**. [Norte Log](casos/norte-log.md) vale como **transferência**: IDs inéditos, mesmo mecanismo. Case real vence os dois. Marque `treino` ou `transferencia` na seção 1. Não apresente Atlas ou Norte como se fossem a sua operação.

## As oito seções + replay

1. Case e justificativa — por que um brain, ou veto com condição de reabertura.
2. Mapa dos seis módulos — job, autoridade, ritmo, fronteira.
3. Ledger de proveniência — mínimo 3 claims (claim → fonte → data → uso).
4. Contrato de governança — ACL, validade, supersessão, conflito, retenção, exclusão, auditoria.
5. Política de contexto — esteira por workload + teto + fallback.
6. Contrato brain↔harness — entrada, saída, latência como intenção, fallback, citação obrigatória.
7. Gate de aprendizado — candidato → classificação → aprovação → versão → projeção reconstruída.
8. Anti-padrões — rubrica dos oito, residual vazio.
**Replay transversal (obrigatório; não é uma nona seção)** — quatro jogadas no papel, sem cluster:
   1. claim autorizado (saída com cadeia);
   2. tentativa sem ACL (recusa antes do retrieve);
   3. conflito ou buraco (modelo não desempata);
   4. feedback recusado pelo gate de escrita.

O replay prova que ledger, governança, política e contrato **conversam**. YAML das seções 1–8 sem as quatro jogadas não fecha o M5.

## O que não precisa existir

Especificação textual (Markdown / YAML) + replay de mesa. Sem cluster, sem banco, sem retrieve no ar. Bloqueio de ambiente é estado honesto, não aprovação.

## Falhas críticas

Listadas na [Rubrica](Rubrica.md). Uma só bloqueia.

[Curso](README.md) · [M5](modulos/M5-projeto-integrador.md)
