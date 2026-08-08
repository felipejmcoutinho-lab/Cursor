# Template de prompt elaborado

Use esta estrutura interna ao construir prompts. Adapte seções conforme o tipo; omita seções irrelevantes.

## Estrutura canônica

```markdown
# [Título descritivo do prompt]

## Papel
Você é [especialista/função] com expertise em [domínio]. Seu foco é [resultado principal].

## Contexto
[Informações de fundo necessárias para executar a tarefa — projeto, stack, público, estado atual]

## Objetivo
[Uma frase clara: o que deve ser alcançado ao final da execução]

## Tarefas
1. [Passo ordenado e verificável]
2. [Passo ordenado e verificável]
3. ...

## Restrições
- DEVE: [obrigatório]
- NÃO DEVE: [proibido]
- PREFERIR: [desejável mas não bloqueante]

## Formato de saída
[Schema exato: markdown, JSON, tabelas, seções obrigatórias, idioma]

## Critérios de sucesso
- [ ] [Critério verificável 1]
- [ ] [Critério verificável 2]

## Edge cases
- Se [condição], então [comportamento esperado]
- Se informação insuficiente, [ação: perguntar X / assumir Y / abortar]

## Exemplos (opcional)
### Entrada
[exemplo]

### Saída esperada
[exemplo]
```

## Variantes por tipo

### System prompt (agente)

```markdown
## Papel
[Persona técnica]

## Capacidades
- [O que o agente pode fazer]

## Limites
- [O que o agente não deve fazer]

## Fluxo de trabalho
1. [Fase de análise]
2. [Fase de execução]
3. [Fase de validação/entrega]

## Comunicação
- Tom: [profissional/técnico/didático]
- Idioma: [pt-BR]
- Estrutura de resposta: [seções fixas]
```

### Cursor rule (.mdc)

```markdown
---
description: [Frase de roteamento — "Use quando..."]
globs: [opcional]
alwaysApply: [true/false]
---

[Instruções concisas, imperativas, sem redundância]
```

### Skill (SKILL.md)

```markdown
---
name: [kebab-case]
description: [O que faz + quando usar — frase de roteamento]
---

# [Nome]

## Quando usar
- [Gatilho 1]

## Fluxo
1. [Passo]

## Referências
- [arquivo](references/...)
```

### User prompt (tarefa pontual)

```markdown
## Contexto
[1–3 frases]

## Tarefa
[Verbo imperativo + objeto + critério de done]

## Entrada
[dados, arquivos, links]

## Saída esperada
[formato + exemplo se útil]
```

## Regras de escrita

1. **Imperativo** nas instruções operacionais ("Analise", "Gere", "Valide")
2. **Específico** em restrições ("máximo 500 linhas" > "seja conciso")
3. **Verificável** em critérios de sucesso (checkbox ou métrica)
4. **Hierárquico** — informação crítica antes de detalhes
5. **Sem contradição** — revise DEVE vs NÃO DEVE antes de entregar
