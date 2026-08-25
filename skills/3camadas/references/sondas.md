# Sondas de disco

Procure evidência. Não procure o vocabulário da aula. Um arquivo chamado `brain` sem leitor não é company brain.

Comece por `scripts/probe.py`. Depois leia. Habitat (manifesto) só diz **onde olhar primeiro**, não marca ponto. Hit em `cursos/`, `README` ou `SKILL.md` costuma ser vocabulário, não runtime.

| Manifesto | Olhe primeiro |
|-----------|----------------|
| `package.json` | `src/`, `lib/`, scripts, plugins, `*.mjs` |
| `pyproject.toml` / `requirements.txt` | pacote Python, `src/`, adapters |
| `go.mod` / `Cargo.toml` | `cmd/`, `internal/` |
| `AGENTS.md` / `CLAUDE.md` | harness persistente — ainda precisa de leitor e hipótese |
| `prisma/` / `migrations/` | dados; não é brain sozinho |
| Nenhum manifesto + pasta enorme | se não achar um arquivo por pilar, saia para `code-anatomist` |

## Modelo

| Sinal | Onde costuma aparecer | Cuidado |
|-------|-----------------------|---------|
| ID físico isolado | `.env.example`, `config/models*`, router, adapter | `gpt-4o` hardcoded em prompt, skill ou teste = Q1 não |
| Alias de capability | `review-seguranca`, `bulk-mecanico`, rota por tarefa | Um único “default model” para tudo = contrato ausente |
| Adapter | cliente LLM, normalização de erro/schema | Um adapter sem segundo candidato testado = nível 1 no máximo |
| Eval local | fixtures, golden cases, regressões, casos adversariais | Leaderboard público não substitui Q6 |
| Shadow / canary / rollback | flags, traffic split, runbook, teste de volta | Comentário “depois a gente faz canary” = Q7 não |

Pergunta de ouro: **trocar o modelo obriga a reescrever política, memória ou autoridade?**

## Harness

| Sinal | Onde costuma aparecer | Cuidado |
|-------|-----------------------|---------|
| Autoridade | approval, ACL de tool, caps, deny-by-default | “Seja cuidadoso” no system prompt não é T1 |
| Quatro planos | execução, controle, evidência, mudança em módulos distintos | Um `agent.py` que aprova, chama modelo e grava memória = grosso |
| Ablação | hipótese + métrica + `remover_quando` em apoio de raciocínio | `CLAUDE.md` / `AGENTS.md` longos sem dono nem revisão = Q9 não |
| Prova de outcome | check no ambiente depois do “concluído” | Texto final do modelo como prova = harness cego |
| Scaffolding vencido | decomposição fixa, parsers, validadores duplicados | Pode existir; sem condição de remoção vira arqueologia |

Pergunta de ouro: **“thin” está medindo linhas ou motivos diferentes de mudança?**

## Company brain

| Sinal | Onde costuma aparecer | Cuidado |
|-------|-----------------------|---------|
| Fonte canônica | docs versionados, ledger, CMS com vigência | Pasta `docs/` morta ou Drive inteiro no prompt = dump |
| ACL antes da busca | filtro de identidade **antes** do retrieve | ACL só no harness depois do chunk no contexto = B2 não |
| Write-back | fila de revisão, PR, gate humano | Memória automática da resposta do agente = B3 não |
| Validade | `valid_from` / `supersedes` / TTL | “Pega o mais recente” apaga o caso da Ana |
| Conflito | claim em disputa explícito | Resolver pelo embedding mais parecido = consenso fabricado |
| Dossiê | seleção pequena, atual, autorizada, citável | Long context com o corpus inteiro = bibliotecária ausente |

Pergunta de ouro: **write-back entra como candidato ou como verdade?**

## O que não contar

- README que promete a tese sem código que a cumpra
- Skill ou aula deste acervo copiada para o repo auditado e nunca lida
- Adapter de um único fornecedor apresentado como “agnóstico”
- Vault de estudo (`aiox-brain`) apresentado como company brain
- MCP, janela longa ou “temos RAG” como prova de pilar
