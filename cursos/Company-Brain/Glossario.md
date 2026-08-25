---
type: glossary
course: company-brain
status: canonical
canonical_scope: cursos/Company-Brain
---

# Glossário — Company Brain

## Distinções obrigatórias

**Company brain** — conhecimento institucional fora dos pesos do modelo, modular por job, autoridade e ritmo, capaz de entregar projeção a agents. Analogia do curso: **biblioteca viva**, não o motor nem o chassis.

**Vault de estudo / aiox-brain** — segundo cérebro do aluno neste acervo. Não é o cérebro da empresa. Dono: `cursos/Obsidian-IA/` e `skills/aiox-brain/`.

**Memória da capacidade** — o que um workload precisa lembrar para fechar a própria story. Dono: módulo M1b em `cursos/AIOX-Agent-Engineering/`.

## Termos centrais

**ACL** — quem pode ler, escrever ou revogar um módulo. Não é “permissão” vaga.

**Claim** — afirmação normalizada que aponta para fonte, data e uso permitido.

**Fonte canônica** — documento, dado ou evento que prova um claim. Cópia e síntese não são fonte.

**Governança** — ACL, validade, supersessão, conflito, retenção, exclusão e auditoria.

**Harness** — plano de controle da execução: contrato, autoridade, tools, budget, prova. Não guarda a empresa.

**Ledger de proveniência** — registro claim → fonte → data → uso.

**Modelo substituível** — motor de raciocínio para uma classe de tarefa. Não é fonte da verdade.

**Projeção** — recorte recuperável (lexical, vetorial ou grafo) reconstruível a partir das fontes. Não é oráculo.

**Promessa do brain** — entregar contexto pequeno, atual, autorizado e citável; recusar dump.

**Supersessão** — um claim substitui formalmente outro, sem fingir que o antigo nunca existiu.

**Vector-oracle** — anti-padrão: tratar um índice como o cérebro.

**Acoplamento de relógio** — uma mudança obrigatória que força modelo, harness e brain a se moverem juntos. Sinal de monolith com três nomes.

**Esteira de contexto** — query → filtro → ACL → projeção → teto → saída → buraco. É a promessa operacional do M0.

**Habitat da perda** — pesos, documento sem dono, cabeça de gente ou store-oráculo. Nenhum é company brain.

**Memória paramétrica** — o que ficou nos pesos: opaca, cara de atualizar, difícil de revogar.

**Memória recuperável** — o que se busca e se edita. Só vira brain com dono, validade e citação.

**Pacote dump / pacote janela / pacote projeção** — três jeitos de montar contexto; só o terceiro cumpre a promessa.

**Política de contexto** — a esteira do M0 nomeada por workload/agent: query, filtro, ACL, projeção, teto, fallback. Uma esteira para todos os agents é depósito.

**Contrato brain↔harness** — interface: entrada (query + ACL + actor), saída (claim + fonte + citação + conflito|buraco). Latência é intenção, não SLA de produto. MCP não é este contrato.

**Gate de aprendizado** — candidato → classificação → aprovação → versão → projeção reconstruída. Feedback não é fato. T-8841 não atravessa como política.

**Menor brain suficiente (empresa)** — escada arquivo versionado → ledger de claims → módulos + governança. Distinta da escada de capacidade da aula 12f em Agent Engineering.

**Brain sem mãos** — o brain não dispara efeito no mundo. Estorno, e-mail e fechar ticket são harness.

**Dump** — anti-padrão: o depósito entra no prompt.

**Janela-como-prova** — anti-padrão: capacidade nominal de contexto como curadoria.

**Autoridade global** — anti-padrão: um store, todos leem tudo; ACL só no prompt.

**Harness-brain** — anti-padrão: regra de negócio institucional no `if` do runner.

**Modelo-como-verdade** — anti-padrão: pesos (fine-tune) como locator.

**Escrita-sem-gate** — anti-padrão: run grava memória; falha bruta vira SOP.

**Vendor-como-fundação** — anti-padrão: produto como módulo mental do brain.

**Replay de mesa** — quatro jogadas no papel que provam coerência do YAML: claim autorizado, tentativa sem ACL, conflito ou buraco, feedback recusado pelo gate. Sem cluster.

**Norte Log** — caso inédito de transferência (SLA 48h/24h, CUSTO-ROTA, T-2207). Não misturar IDs com a Atlas.
