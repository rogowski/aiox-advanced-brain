---
name: 3camadas
user-invocable: true
description: >
  Analisa e pontua um repositório real contra a tese da aula 21b:
  modelo substituível, thin harness e company brain modular. Sempre
  devolve JSON técnico para o agente e um HTML para o dono do
  sistema (chão, motor, painel, memória — sem jargão de aula).
  Use when the user invokes /3camadas or asks for architecture score,
  substituibilidade, thin harness, company brain modular, teste de
  remoção, or "quão substituível é este sistema". Não implementa a
  troca e não cria módulo novo.
---

# /3camadas

Skill da aula `cursos/AIOX-Agent-Engineering/aulas/21b-modelos-substituiveis-harness-fino-cerebro-modular.md`
(HTML: `lessons/0001-o-modelo-passa-o-sistema-fica.html`).

O modelo raciocina. O harness governa. O brain entrega contexto citável.
Você lê o disco, não o slide. **Toda execução analisa e pontua os três pilares.**

## Quando usar

- `/3camadas` neste repo ou no projeto-alvo
- “Qual o score deste repo na tese 21b?”
- “Somos substituíveis / thin / temos company brain?”
- Review com teste de remoção, costura falsa ou vazamento entre camadas

## Quando não usar

- Desenhar arquitetura do zero → `aiox-architect`
- Engenharia reversa de um sistema desconhecido → `code-anatomist`
- Especificar o company brain (ACL, validade, projeção) → `cursos/Company-Brain/`
- Mapear SOP / processo de negócio em 7 fases → `aiox-sop` (neste acervo) ou o mapper SINKRA no destino; aqui só se pontua costura
- Implementar a troca de modelo, o harness ou um módulo novo

## Entrega obrigatória

1. **JSON do agente** — `{SOURCE_PATH}/docs/reports/architecture-review-<id>.scorecard.json`: as 9 perguntas, pilares, prior-art, `round`. É o laudo. A pessoa não precisa abrir.
2. **HTML do dono** — `{SOURCE_PATH}/docs/reports/architecture-review-<id>.html`: página funcional (como ler, uma frase, três promessas, um pedido, o que já segura, um passo). Sem “tese 21b”, sem Q1–Q9, sem `rg`. Ver [references/html-report.md](references/html-report.md).
3. **Uma execução desenhada** — swimlane + mermaid do mesmo caminho. Ver [references/dags.md](references/dags.md).
4. **Um** próximo passo, em linguagem de operação.

Grave só em `docs/reports/` do projeto auditado. Crie a pasta se faltar. Não use `/tmp`. Abra o **HTML**. No chat, o path do HTML. JSON só se pedirem o laudo.

Calcule o número com `scripts/score.py` — não some de cabeça. Rubrica: [references/rubrica.md](references/rubrica.md). Sondas: [references/sondas.md](references/sondas.md). Gates: [references/gates.md](references/gates.md). DAGs: [references/dags.md](references/dags.md). Relatório: [references/html-report.md](references/html-report.md).

## Workflow

Antes do passo 1, resolva `SKILL_ROOT` na mesma sessão de shell usada pelos scripts:

```bash
if [ -z "${SKILL_ROOT:-}" ]; then
  for candidate in "$PWD/skills/3camadas" "$HOME/.codex/skills/3camadas" "$HOME/.cursor/skills/3camadas"; do
    if [ -f "$candidate/SKILL.md" ]; then SKILL_ROOT="$candidate"; break; fi
  done
fi
test -f "${SKILL_ROOT:-}/scripts/probe.py" || { echo "skill 3camadas não localizada" >&2; exit 1; }
```

1. Declare a rodada **antes** do probe: `round.id`, `round.modelo` (nome, apelido da UI e esforço — `Codex Sol · xhigh` se o SKU não veio), `round.runtime`, `round.started_at`. Classifique por sinal positivo: `leve` → pare; `medio` sem high/xhigh → avise; senão `alto` e siga. SKU oculto sem sinal leve **não** bloqueia e **não** pede override. Não abra `architecture-review-*` nem scorecard anterior até o HTML desta corrida existir. Chat que já rodou `/3camadas`: ignore aquelas respostas; recomece no disco.
2. Resolva `SOURCE_PATH` (cwd ou path local). URL/slug → pare e pergunte. O disco auditado é **somente leitura**.
3. Rode o probe e leia os hits. Sem leitura, hit não marca ponto.

   ```bash
   python3 "$SKILL_ROOT/scripts/probe.py" "$SOURCE_PATH"
   ```

   Habitat sem costura agentic visível, mas o sistema claramente tem agent/RAG/tools: **não pontue** — handoff para `code-anatomist`. Sem superfície agentic: 0/9 com contexto `não é um sistema agentic`.
4. Crie `{SOURCE_PATH}/docs/reports/` se faltar. Preencha o JSON lá (`round` + 9 respostas + espessura + brain). Todo `true` leva path + confiança (`HIGH`/`MEDIUM`). Todo `GAP`/`false` por ausência leva linha de prior-art (busca + matches). `LOW` e `REDUCED` não marcam ponto. O 0–9 é AS-IS. Rode:

   ```bash
   python3 "$SKILL_ROOT/scripts/score.py" "$SOURCE_PATH/docs/reports/architecture-review-<id>.scorecard.json"
   ```

   Sem stdout do script, não há entrega. Sem `round.modelo`, o script falha. `SKILL_ROOT` é a pasta desta skill (`~/.cursor/skills/3camadas` ou `~/.codex/skills/3camadas`).
5. Amostragem no JSON: abra dois paths citados; se não sustentarem o `true`, vire `false`, rode o score de novo. Depois escreva o HTML **para o dono** a partir do JSON — não despeje o JSON na página. Próximo passo: uma classe no JSON (`remover` / `enforcement` / `deixar`); na página, uma frase de operação.
6. Só então pode listar rodadas anteriores. Não mude as 9 respostas por causa delas. Pare. Não implemente. Pergunte se a pessoa quer explorar o primeiro movimento.

## Regras

- Avalie o disco. Doutrina no arquivo ≠ consumidor no runtime. README sem leitor é GAP.
- Não sintetize de memória. Se o path não abre, a afirmação some.
- Não invente módulo, orquestrador, fila nem “cérebro” novo. Aprofunde o que existe.
- Não copie paths, slugs ou notas de outro laboratório para o relatório.
- Afirmação só com evidência; o resto é GAP, e GAP não marca ponto.
- Veto de segurança não entra em média compensável por custo ou latência.
- O score **não** é certificação. Cada “não” localiza o próximo acoplamento.
- Protótipo descartável pode ser 0–3 e ainda ser a decisão certa. Declare processo vs missão. Não persiga +1 no HTML.
- Cada rodada carimba o modelo que a executou. Rodada sem carimbo não existe.
- Não leia a rodada anterior até concluir esta. Comparar modelos exige isolamento; senão o segundo só confirma o primeiro.
- Gateie a **classe** `analise-arquitetural-profunda`, não uma marca. Roteador leve (Luna, Terra, Haiku, flash, mini) não começa. Sonnet/médio: aviso + override. SKU oculto não bloqueia. Codex Sol / xhigh é `alto`. Não solde “só Opus”.
- HTML = dono do sistema. JSON = agente. “Tese 21b”, Q1–Q9 e `rg` não entram na página.
- No chat: o path do HTML quando existir. Sem preâmbulo de rodada, isolamento, “não vou abrir scorecard”, “em seguida leio a rubrica”. Isso é o esperado — faça, não anuncie.

## Prompt canônico

```text
/3camadas

Leia o disco deste sistema. Descubra se dá para trocar a IA sem
reescrever regra, memória ou quem manda; se o painel é fino; se a
memória da empresa tem gavetas.

Duas superfícies:
1. JSON técnico em docs/reports/ (perguntas, evidência, quem analisou)
2. HTML para o dono no mesmo docs/reports/: como ler, uma frase,
   três promessas, o que acontece quando pede, o que já segura,
   um próximo passo. Proibido na página: tese 21b, Q1–Q9, GAP, grep.
   Não grave em /tmp.

Não leia architecture-review ou scorecard anterior até este HTML existir.
Não copie o número de outra rodada nesta conversa.
Não anuncie rodada, isolamento nem “vou ler a rubrica”. Faça. No chat, o HTML.
Se este runtime for classe leve (Luna, Terra, Haiku, flash, mini), pare e peça trocar.
Classe média (Sonnet sem high): avise; só siga com override.
SKU oculto + high/xhigh/Sol/Codex: siga. Não peça override por falta de versão.

No JSON (não na página), responda com evidência:
- Trocar o motor obriga a reescrever regra, memória ou autoridade?
- O encaixe prova forma ou o teste prova comportamento?
- O acesso é checado antes da busca?
- O que a IA extraiu entra como candidato ou como fato?
```
