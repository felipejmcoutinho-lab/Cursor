# Agent instructions

## Project overview

Repositório de configuração e documentação para integração entre Cursor local e Cloud Agents no projeto `felipejmcoutinho-lab/Cursor`.

## Regras do projeto (`.cursor/rules`)

- `.cursor/rules/engenharia-de-prompts.mdc`: ative este modo sempre que o usuário
  pedir para otimizar, incrementar, melhorar ou profissionalizar um prompt,
  instrução, insight ou ideia (ou ao invocar `@engenharia-de-prompts`). Nesse modo,
  o objetivo é **projetar o prompt final** — não executar a tarefa nele descrita —
  seguindo o template padronizado e a checklist de qualidade definidos na regra.

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
