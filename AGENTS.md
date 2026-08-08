# Agent instructions

## Project overview

Repositório de configuração e documentação para integração entre Cursor local e Cloud Agents no projeto `felipejmcoutinho-lab/Cursor`.

## Cursor Cloud specific instructions

### Ambiente

- Este repositório não tem dependências de pacote. O script `install` em `.cursor/environment.json` só valida o ambiente.
- Não há servidor de desenvolvimento, banco de dados ou Docker neste repo.

### Fluxo local ↔ cloud

1. Alterações locais chegam ao Cloud Agent apenas via **Git** (`commit` + `push`).
2. Cloud Agents trabalham em branch separada e abrem PR no GitHub.
3. Para continuar localmente após um Cloud Agent: `git fetch origin` e checkout da branch do PR.

### Branches

- Use o prefixo `cursor/` para branches criadas por agentes (ex.: `cursor/<descricao>-092d`).
- Branch base para PRs: `main`.

### Testes e validação

- Não há suite de testes automatizada neste repositório.
- Valide alterações revisando markdown e JSON (`.cursor/environment.json`).

### Segredos

- Não commite credenciais. Use [Dashboard → Cloud Agents → Secrets](https://cursor.com/dashboard/cloud-agents).

## Agente de elaboração de prompts

Este repositório está parametrizado como **chat/agente de engenharia de prompts**. O objetivo é transformar ideias, rascunhos e instruções simples do usuário em prompts avançados, profissionais e padronizados.

### Recursos

| Recurso | Caminho | Função |
|---------|---------|--------|
| Rule (sempre ativa) | `.cursor/rules/prompt-elaborador.mdc` | Define o modo elaborador neste projeto |
| Skill | `.cursor/skills/prompt-elaboracao/` | Workflow, template, rubrica e exemplos |
| Subagent | `.cursor/agents/prompt-elaborador.md` | Elaboração profunda (`/prompt-elaborador`) |
| Biblioteca | `prompts/` | Versionar prompts elaborados (opcional) |

### Uso rápido

1. Envie qualquer rascunho, ideia ou instrução curta na conversa
2. O agente elabora o prompt no formato padronizado (Diagnóstico → Prompt → Metadados → Checklist)
3. Para sessões longas ou revisão profunda: `/prompt-elaborador`
4. Para invocar só o workflow: `/prompt-elaboracao`

### Formato de entrega

Toda resposta de elaboração segue a estrutura definida em `.cursor/skills/prompt-elaboracao/SKILL.md` e valida com `references/rubrica-qualidade.md`.
