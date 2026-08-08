# Padrões Cursor — referência para elaboração de prompts

## Mecanismos de configuração

| Mecanismo | Arquivo | Quando usar no prompt elaborado |
|-----------|---------|--------------------------------|
| **Rule** | `.cursor/rules/*.mdc` | Padrões persistentes; alwaysApply ou globs |
| **Skill** | `.cursor/skills/<nome>/SKILL.md` | Workflow repetível; referências sob demanda |
| **Subagent** | `.cursor/agents/<nome>.md` | Tarefas longas com contexto isolado |
| **AGENTS.md** | raiz ou aninhado | Instruções de repo/cloud; escopo por diretório |

## Frontmatter — rule (.mdc)

```yaml
---
description: Frase de roteamento — "Use quando o usuário..."
globs: "**/*.ts, src/**"   # opcional
alwaysApply: false         # true = sempre ativo
---
```

## Frontmatter — skill (SKILL.md)

```yaml
---
name: kebab-case          # deve igualar nome da pasta
description: O que faz + quando usar (sinal de roteamento)
paths:                    # opcional — escopo por arquivo
  - ".cursor/**"
disable-model-invocation: false  # true = só via /nome
---
```

## Frontmatter — subagent

```yaml
---
name: kebab-case
description: Quando delegar a este subagent
model: inherit            # ou modelo específico
readonly: true            # opcional — só análise
---
```

## Boas práticas para prompts Cursor

1. **`description` é roteamento** — invista na frase "Use quando..."
2. **Progressive disclosure** — SKILL.md curto; detalhes em `references/`
3. **Regras < 500 linhas** — dividir em regras compostas
4. **`@arquivo`** em vez de colar conteúdo longo
5. **Sem segredos** em arquivos versionados — usar Dashboard → Secrets
6. **AGENTS.md** — só notas duráveis de operação cloud/repo

## Mapeamento: pedido do usuário → artefato

| Pedido típico | Artefato recomendado |
|---------------|---------------------|
| "Sempre faça X neste projeto" | Rule com `alwaysApply: true` |
| "Quando editar arquivos Y, siga Z" | Rule com `globs` |
| "Workflow para criar deploys" | Skill com scripts/references |
| "Revisar prompt complexo em profundidade" | Subagent readonly |
| "Instruções para Cloud Agents" | AGENTS.md |

## Invocação

- Skill: automática por relevância ou `/prompt-elaboracao`
- Subagent: `/prompt-elaborador` ou "use o subagent prompt-elaborador"
- Rule: automática por alwaysApply/globs/relevância
