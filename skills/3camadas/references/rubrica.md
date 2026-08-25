# Rubrica — score 21b

Fonte canônica: `cursos/AIOX-Agent-Engineering/aulas/21b-modelos-substituiveis-harness-fino-cerebro-modular.md`, seção **Diagnóstico — quão substituível é seu sistema?**

O número oficial desta skill é o **0–9 da aula**. Os scores por pilar são vistas derivadas, não uma escala concorrente.

## Como marcar

- `true` só com path real (e leitor no runtime, se a afirmação depender de consumo).
- `false` quando o disco contradiz ou não há evidência.
- Não existe “meio ponto”. GAP = `false`.

## Diagnóstico 21b (0–9)

| # | Pergunta (sim = 1) | Pilar |
|---|--------------------|-------|
| 1 | O nome exato do modelo está isolado em configuração ou adapter? | Modelo |
| 2 | As capacidades obrigatórias da rota estão declaradas? | Modelo |
| 3 | Ferramentas e formatos pertencem ao contrato do sistema, não ao prompt de um fornecedor? | Harness |
| 4 | Fontes canônicas e memória vivem fora dos pesos e das conversas do modelo? | Brain |
| 5 | O acesso é verificado antes de buscar contexto ou executar ação? | Brain + harness |
| 6 | Existem casos locais com resultados esperados, incluindo falhas antigas? | Modelo |
| 7 | A troca passa por sombra ou piloto, tem plano B e permite voltar? | Modelo |
| 8 | A escrita no brain passa por validação, versão e registro da origem? | Brain |
| 9 | Cada apoio de raciocínio possui hipótese, evidência e condição de remoção? | Harness |

Bandas da aula (não renegocie):

| Total | Banda | Leitura |
|------:|-------|---------|
| 0–3 | soldado | Trocar modelo provavelmente vira refactor e aposta operacional |
| 4–6 | separação parcial | A forma está separada; faltam provas ou regras de uso |
| 7–9 | troca operacional | Existe opção real, ainda condicionada à tarefa e ao teste |

## Pilar 1 — Modelo substituível (0–4)

Escada de portabilidade da aula. O nível é o **mais alto que o disco prova**; um “sim” isolado não sobe a escada.

| Nível | Nome | Evidência mínima |
|------:|------|------------------|
| 0 | Acoplamento físico | IDs de modelo espalhados em prompt, código ou chat |
| 1 | Adapter | Chamada e resposta normalizadas |
| 2 | Contrato de capability | Alias + tools + schema + limites + fallback declarados |
| 3 | Eval gate | Casos locais, thresholds, vários trials (Q6) |
| 4 | Substituição operacional | Shadow ou canary + rollback testado (Q7) |

Regra da aula: adapter prova forma; eval prova comportamento. Chegar ao nível 1 e declarar “somos agnósticos” é o erro comum.

## Pilar 2 — Thin harness (0–4)

Quatro testes de espessura da aula. Cada “a mudança não vaza” vale 1.

| # | Teste mental | Sim quando |
|---|--------------|------------|
| T1 | Troque o modelo | Política, memória e autoridade permanecem |
| T2 | Atualize uma política | Não exige redeploy do modelo nem reescrita do loop |
| T3 | Mude uma aprovação (1 → 2 pessoas) | Não exige reindexar documentos |
| T4 | Troque o ambiente de execução | Sessão e memória institucional não desaparecem |

Thin mede motivos diferentes de mudança no mesmo componente, não linhas. Q9 (ablação) não soma neste 0–4; sem ela a banda do harness não pode ser lida como “operacional”, mesmo com T1–T4 verdes. O script marca `harness_operacional_bloqueado` nesse caso.

## Pilar 3 — Company brain modular (0–4)

Quatro checks de governança da aula. Cada um vale 1.

| # | Check | Sim quando |
|---|-------|------------|
| B1 | Fonte fora dos pesos | Q4 evidenciada |
| B2 | ACL antes da busca | Q5 evidenciada na leitura, não só depois da geração |
| B3 | Write-back governado | Q8: candidato → validação → versão → origem; o modelo não cola verdade |
| B4 | Validade ou conflito explícito | Disco preserva vigência/supersessão **ou** recusa consenso silencioso |

Brain ≠ dump. Janela longa não marca ponto. Índice ou grafo sem fonte reconstruível não marca B1.

## Leitura do scorecard (ordem da aula)

1. Requisito obrigatório ausente encerra a rota — não “compensa” com custo.
2. Violação crítica de segurança é veto, não peso numa média.
3. Média global não esconde regressão num segmento crítico.
4. Resultado certo por ferramenta proibida continua sendo falha.
5. Custo e tempo só decidem entre candidatos que já passaram.

## Contexto que não infla o número

A tese defende opção de mudança, não abstração antecipada. Um protótipo reversível com 2/9 pode ser a decisão madura. Um processo financeiro com 2/9 é risco. Declare o contexto no HTML; não “ajuste” o 0–9 por simpatia.
