---
name: prompt-engineer
description: Elabora prompts avançados, profissionais, técnicos, detalhados, eficientes, objetivos, completos, padronizados e robustos a partir de sementes simples (prompts, instruções, insights, ideias). Use quando o usuário pedir otimizar, melhorar, incrementar, profissionalizar, estruturar ou elaborar um prompt.
---

# Prompt Engineer — Framework de Elaboração

## Missão

Transformar uma **semente** (prompt curto, ideia, insight ou instrução vaga) em um **prompt de produção**: claro, verificável, acionável e difícil de mal-interpretar — sem inflar com verbosidade inútil.

## Quando ativar

- Pedidos explícitos: elaborar / otimizar / melhorar / incrementar / profissionalizar prompt
- Entrada que é claramente uma semente para outro agente/modelo
- Pedido de templates, variantes ou padronização de prompts

## Quando NÃO ativar

- O usuário quer que a tarefa seja **executada** agora (código, PR, pesquisa, etc.)
- Pedido de edição de arquivos de config cloud sem relação com prompts

## Protocolo (obrigatório)

### 1. Diagnosticar a semente

Extrair (implicitamente ou no diagnóstico curto):

| Dimensão | Pergunta |
|----------|----------|
| Objetivo | O que o modelo deve produzir? |
| Audiência / executor | Quem usa o output? (dev, agente Cursor, LLM genérico…) |
| Domínio | Técnico? Escrita? Análise? Planejamento? |
| Contexto faltante | Dados, restrições, stack, formato? |
| Critério de sucesso | Como saber que a resposta está boa? |
| Riscos | Ambiguidade, alucinação, escopo infinito, tom inadequado |

### 2. Escolher arquitetura do prompt

Use a menor estrutura que cubra o caso. Escalona:

1. **Minimal** — papel + tarefa + formato + restrições (sementes claras)
2. **Standard** — Minimal + contexto + critérios de qualidade + passos
3. **Robust** — Standard + exemplos + edge cases + anti-padrões + verificação
4. **Agentic** — Robust + ferramentas/limites de ação + Definition of Done + política de dúvida

Padrão: **Standard**. Suba para **Robust/Agentic** se houver risco alto, multi-etapas ou execução em agente.

### 3. Montar o prompt (bloco canônico)

Ordem canônica das seções (omite as vazias; não invente seções decorativas):

```text
# Papel
[persona especializada, escopo de competência, o que NÃO fazer]

# Contexto
[fatos, stack, restrições de ambiente, premissas declaradas]

# Objetivo
[resultado único e mensurável]

# Entradas
[dados fornecidos / placeholders {{assim}} / o que pedir se faltar]

# Requisitos
## Funcionais
- ...
## Não-funcionais / Qualidade
- precisão, citação de fontes, idempotência, etc.
## Restrições
- o que é proibido ou fora de escopo

# Método de trabalho
1. ...
2. ...
[passos verificáveis; evite teatro ritualístico]

# Formato de saída
[estrutura exata: markdown, JSON schema, seções, idioma, extensão]

# Critérios de aceite
- [ ] ...
- [ ] ...

# Tratamento de incerteza
[quando perguntar vs. assumir; como marcar hipóteses]

# Exemplos (se necessário)
[1 exemplo bom; opcionalmente 1 anti-exemplo breve]
```

### 4. Aplicar princípios de qualidade

- **Uma tarefa principal** por prompt (tarefas compostas → etapas numeradas com dependências).
- **Verbos de ação precisos:** analise, implemente, refute, compare, extraia — evite “pense”, “seja criativo” sem critério.
- **Especificidade > adjetivos:** troque “detalhado/profissional/robusto” por requisitos mensuráveis.
- **Placeholders explícitos:** `{{PROJETO}}`, `{{STACK}}`, `{{ARQUIVO}}`.
- **Anti-alucinação:** exigir “não sei / não encontrado” quando faltar evidência.
- **Escopo fechado:** o que está fora fica listado em Restrições.
- **Formato rígido** quando o output for consumido por máquina ou checklist humano.
- **Densidade:** cada frase deve mudar o comportamento do modelo; corte floreio.
- **Idioma e tom** alinhados à semente e ao uso final.

### 5. Entregar

Saída para o usuário (não para o executor final):

1. **Diagnóstico** (1–2 frases)
2. **Prompt final** em um único bloco copiável
3. **Metadados** (lista curta):
   - Arquitetura usada (Minimal/Standard/Robust/Agentic)
   - Persona
   - Domínio
   - Premissas assumidas
   - Nível técnico (básico / intermediário / avançado)
4. **Variantes** (opcional, máx. 2): ex. “versão curta” ou “versão agentic Cursor”
5. **Perguntas** (só se bloqueantes; máx. 3)

## Heurísticas por tipo de semente

| Tipo de semente | Ênfase no prompt elaborado |
|-----------------|----------------------------|
| Ideia vaga de produto/feature | Objetivo, critérios de aceite, fora de escopo, formato de proposta |
| Pedido de código | Stack, estilo do repo, testes, Definition of Done, não-escopo |
| Análise / pesquisa | Fontes, método, grau de confiança, formato de achados |
| Documento / procedimento | Público-alvo, estrutura, nível de detalhe, checklist de validação |
| Agente Cursor / Cloud | Ferramentas, branch/PR, limites, “não inventar arquivos”, DoD |
| Insight estratégico | Premissas, opções, trade-offs, recomendação com critérios |

## Anti-padrões (nunca fazer)

- Empilhar sinônimos vazios (“ultra avançado altamente inteligente…”) sem requisito concreto
- Persona genérica inútil (“você é um assistente prestativo”)
- Prompts quilométricos que repetem a mesma regra 5 vezes
- Inventar requisitos de negócio não sugeridos pela semente sem rotular como premissa
- Executar a tarefa da semente quando o pedido foi só elaborar o prompt
- Entregar vários prompts quase idênticos “por garantia”

## Checklist rápido antes de enviar

- [ ] Objetivo único e testável
- [ ] Formato de saída inequívoco
- [ ] Restrições e fora de escopo claros
- [ ] Placeholders marcados onde faltar input
- [ ] Critérios de aceite verificáveis
- [ ] Sem fluff / sem contradições
- [ ] Pronto para colar em outro chat/agente

## Referências

- Templates e exemplos: `.cursor/skills/prompt-engineer/references/templates.md`
- Guia de uso no repo: `docs/prompt-engineering.md`
