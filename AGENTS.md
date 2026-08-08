# Agent instructions

## Project overview

Repositório de configuração e documentação para integração entre Cursor local e Cloud Agents no projeto `felipejmcoutinho-lab/Cursor`.

## Engenharia de prompts

- Quando o usuário pedir para criar, elaborar, melhorar, otimizar, incrementar, estruturar ou padronizar um prompt, leia e siga integralmente `PROMPT_ENGINEERING.md`.
- Considere também como entrada válida instruções, insights, ideias e rascunhos que o usuário queira converter em prompt.
- Use `MODO: PROFISSIONAL` como padrão quando o usuário não indicar outro modo.
- Entregue o prompt pronto para copiar antes de qualquer explicação.
- Não execute a tarefa contida no prompt, salvo quando o usuário pedir explicitamente para **otimizar e executar**.
- Responda no idioma da solicitação, a menos que o usuário defina outro idioma para o prompt.

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
