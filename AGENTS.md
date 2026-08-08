# Agent instructions

## Project overview

Repositório de configuração e documentação para integração entre Cursor local e Cloud Agents no projeto `felipejmcoutinho-lab/Cursor`.

Também hospeda o **Modo Prompt Engineer**: elaboração de prompts avançados a partir de sementes simples.

## Modo Prompt Engineer

Quando o usuário fornecer prompt simples, instrução, insight, ideia ou pedir otimizar/melhorar/elaborar um prompt:

1. Siga `.cursor/rules/prompt-engineer.mdc` e a skill `.cursor/skills/prompt-engineer/SKILL.md`.
2. **Elabore** o prompt; **não execute** a tarefa da semente, salvo pedido explícito de execução.
3. Entregue: diagnóstico breve → prompt final copiável → metadados → variantes/perguntas só se necessário.
4. Use templates em `.cursor/skills/prompt-engineer/references/templates.md` quando ajudarem.
5. Guia de uso: `docs/prompt-engineering.md`.

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
