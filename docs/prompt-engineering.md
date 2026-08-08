# Modo Prompt Engineer

Este repositório está parametrizado para **elaborar prompts avançados** a partir de sementes simples (ideias, insights, instruções curtas).

## Como usar

1. Abra o projeto no Cursor (local ou Cloud Agent).
2. Envie a semente, por exemplo:
   - `Elabore um prompt profissional para: revisar PRs de infraestrutura`
   - `Otimize: criar checklist de comissionamento de fibra`
   - `Melhore este insight em prompt técnico: …`
3. O agente **não executa** a tarefa da semente — devolve o **prompt pronto para copiar**.
4. Cole o prompt elaborado no chat/agente/modelo de destino.

## O que foi configurado

| Artefato | Função |
|----------|--------|
| `.cursor/rules/prompt-engineer.mdc` | Regra sempre ativa: protocolo de entrega e gatilho do modo |
| `.cursor/skills/prompt-engineer/SKILL.md` | Framework completo (diagnóstico → arquitetura → bloco canônico → checklist) |
| `.cursor/skills/prompt-engineer/references/templates.md` | Templates Standard, Agentic e Análise + exemplo semente→elaborado |
| `AGENTS.md` | Instrução lida por Cloud Agents |

## Formato de resposta esperado

1. Diagnóstico curto da semente  
2. Prompt final (bloco único copiável)  
3. Metadados (arquitetura, persona, premissas)  
4. Variantes opcionais / até 3 perguntas se bloqueante  

## Dicas para sementes melhores

- Informe o **uso final** (ChatGPT, Cursor Agent, automação, documento humano).
- Cite **domínio** e **restrições** se já souber (stack, norma, prazo, público).
- Se quiser execução depois da elaboração: diga explicitamente `agora execute este prompt`.
