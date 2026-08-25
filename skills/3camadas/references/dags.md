# DAGs e workflows

O relatório não é só score. Ele mostra **como o trabalho corre hoje**. Roubado do review editorial (swimlane + mermaid da mesma execução). Não copie paleta, nomes nem slugs de outro laboratório.

Dois diagramas são obrigatórios. Um terceiro só se o disco tiver troca de modelo.

## Legenda na página (humano)

| Classe CSS | O dono lê | Marca |
|------------|-----------|-------|
| `modelo` | O motor (a IA) | lima |
| `harness` | O painel | ink |
| `brain` | Memória da empresa | fundo escuro |
| `humano` | Você decide | borda lima |
| `gap` | Ainda não existe | tracejado |
| `vazamento` | Caminho errado | vermelho |

Nó sem path = `gap`. Aresta vermelha = caminho errado (regra dentro do prompt, busca antes de checar acesso, aprendizado virando fato sozinho).

Nó sem path = `gap`. Aresta vermelha = vazamento (política no prompt, ACL depois da busca, write-back como verdade).

## 1. DAG das três camadas (AS-IS)

Mermaid `flowchart LR` ou `TD`. Uma caixa por pilar **como o disco está**, não como a aula desenha.

```text
brain[o que o disco realmente entrega]
  --> harness[o que o disco realmente governa]
  --> adapter[se existir]
  --> modelo[como o ID é escolhido]
  --> eval[se existir]
  --> writeback[candidato ou verdade]
```

Se o pilar não tem arquivo: caixa `gap` com o nome do que falta. Não invente o adapter “para o diagrama ficar bonito”.

## 2. Workflow de uma execução

Uma corrida real que o disco permite (pedido, arquivo, job, tool). Duas vistas do **mesmo** caminho:

1. **Swimlane HTML** — colunas por dono (humano / harness / brain / modelo). Cartões curtos.
2. **DAG Mermaid** — a mesma ordem, com um losango de decisão se houver gate.

Tabela de três colunas embaixo:

| O disco já diz | A máquina faz sem perguntar | Ela recusa sozinha |

Se não achar nenhuma execução: prior-art + swimlane com um único cartão `gap`. Não desenhe o fluxo da aula.

## 3. DAG de substituição (só se houver evidência)

Shadow → canary → promoção / rollback. Sem Q7, omita. Não desenhe o protocolo da aula como se fosse o repo.

## Regras

- Um diagrama que precisa de parágrafo para ser lido deve ser redesenhado.
- Antes/depois dos candidatos continua separado: estes DAGs são o **AS-IS do sistema**, não a proposta.
- Mermaid via CDN, `securityLevel: "strict"`. Tokens AIOX se o HTML for deste acervo.
- Não nasça orquestrador no desenho. Aprofunde o caminho que o probe achou.
- Aresta tracejada vermelha = caminho proibido (ex.: “perguntar antes de processar”, write-back como verdade, ACL depois da busca).

## classDef canônico

Cole no fim de cada `flowchart`. Nó sem path recebe `:::gap`.

```text
classDef modelo fill:#D1FF00,stroke:#050505,color:#050505
classDef harness fill:#050505,stroke:#050505,color:#F4F4E8
classDef brain fill:#111111,stroke:#D1FF00,color:#F4F4E8
classDef humano fill:#F4F4E8,stroke:#D1FF00,color:#050505
classDef gap fill:#F4F4E8,stroke:#050505,stroke-dasharray:5 5,color:#050505
classDef vazamento fill:#F4E8E8,stroke:#B42318,color:#B42318
```

## Swimlane

Quatro colunas, nesta ordem, salvo se o sistema tiver outro dono:

1. **Você** — pedido, veto, o que vira fato
2. **Painel** — porta, plano, prova, recusa
3. **Memória** — fonte, gaveta, acesso, candidato
4. **Motor** — a IA, atrás da porta comum

Cartão = um passo. Rótulo na página = a tabela de cima. Não escreva harness/brain/adapter no cartão.
