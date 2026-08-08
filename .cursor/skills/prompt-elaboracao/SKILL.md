---
name: prompt-elaboracao
description: Elabora prompts avançados, profissionais e técnicos a partir de ideias simples. Use quando o usuário fornecer instruções, insights, rascunhos ou pedir para otimizar, melhorar, incrementar ou padronizar prompts para agentes, regras, skills ou tarefas de IA.
---

# Elaboração de Prompts

Transforme entradas simples do usuário em prompts completos, robustos e prontos para uso.

## Quando usar

- O usuário envia uma ideia, rascunho, bullet points ou instrução curta
- Pedidos de otimizar, melhorar, incrementar, padronizar ou profissionalizar prompts
- Criação de system prompts, regras Cursor, skills, subagents ou instruções de agente
- Refatoração de prompts existentes para maior clareza, precisão ou eficiência

## Fluxo obrigatório

1. **Receber** — Aceite qualquer formato: texto livre, lista, pergunta, código, link, nota mental
2. **Diagnosticar** — Identifique em silêncio:
   - Objetivo final (o que o prompt deve fazer acontecer)
   - Público-alvo (agente, humano, modelo específico)
   - Contexto e restrições implícitas
   - Lacunas, ambiguidades e suposições não declaradas
3. **Perguntar só se necessário** — Faça no máximo 3 perguntas objetivas quando faltar informação crítica; caso contrário, declare suposições explicitamente e prossiga
4. **Elaborar** — Produza o prompt usando o template em `references/template-saida.md`
5. **Validar** — Aplique a rubrica em `references/rubrica-qualidade.md` antes de entregar
6. **Entregar** — Resposta estruturada conforme seção "Formato de saída" abaixo

## Princípios de elaboração

| Princípio | Aplicação |
|-----------|-----------|
| **Objetivo** | Uma intenção principal por prompt; sem redundância |
| **Completo** | Contexto, papel, tarefa, restrições, formato de saída e critérios de sucesso |
| **Técnico** | Terminologia precisa; evite adjetivos vazios sem critério mensurável |
| **Eficiente** | Menor número de tokens que preserve robustez; progressive disclosure |
| **Padronizado** | Mesma estrutura em toda entrega; nomes e seções consistentes |
| **Robusto** | Antecipe edge cases, ambiguidade e falhas comuns |
| **Inteligente** | Inclua raciocínio implícito (chain-of-thought quando útil), exemplos few-shot quando agregam valor |

## Formato de saída (sempre nesta ordem)

```markdown
## Diagnóstico rápido
- **Objetivo inferido:** ...
- **Suposições:** (se houver)
- **Lacunas tratadas:** ...

## Prompt elaborado
[código markdown com o prompt completo, pronto para copiar]

## Metadados
| Campo | Valor |
|-------|-------|
| Tipo | system / user / rule / skill / subagent |
| Idioma | pt-BR / en / ... |
| Tokens estimados | ~N |
| Variantes | sim/não |

## Variantes (opcional)
- **Curta:** versão mínima para contexto limitado
- **Longa:** versão com exemplos e edge cases

## Checklist de qualidade
- [ ] Objetivo único e mensurável
- [ ] Papel e contexto definidos
- [ ] Restrições explícitas
- [ ] Formato de saída especificado
- [ ] Sem contradições internas
```

## Tipos de prompt suportados

- **Agente / system prompt** — persona, capacidades, limites, fluxo de trabalho
- **User prompt** — tarefa pontual com contexto e deliverables
- **Cursor rule (.mdc)** — frontmatter + instruções com globs/alwaysApply
- **Skill (SKILL.md)** — frontmatter + workflow + referências
- **Subagent** — frontmatter + prompt de delegação
- **Chain / multi-step** — sequência numerada com checkpoints
- **Eval / rubric** — critérios de avaliação para outputs de IA

## Referências

- Template de saída: [references/template-saida.md](references/template-saida.md)
- Rubrica de qualidade: [references/rubrica-qualidade.md](references/rubrica-qualidade.md)
- Padrões Cursor: [references/padroes-cursor.md](references/padroes-cursor.md)
- Exemplos: [references/exemplos.md](references/exemplos.md)

## O que NÃO fazer

- Não entregue apenas comentários sobre o rascunho — sempre produza o prompt elaborado
- Não infle o prompt com texto genérico ("seja útil", "seja preciso") sem critério operacional
- Não altere o idioma do usuário sem motivo (mantenha pt-BR por padrão)
- Não inclua segredos, credenciais ou dados sensíveis nos prompts gerados
