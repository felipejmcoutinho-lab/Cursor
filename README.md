# Cursor

Repositório para configurar e documentar a integração entre **Cursor local** e **Cloud Agents**.

## Integração local ↔ cloud

O Cursor não sincroniza pastas locais com a nuvem. A integração funciona via **Git + ambiente cloud + Agents Window**.

| Recurso | Local | Cloud |
|--------|-------|-------|
| Onde roda | Sua máquina | VM isolada na nuvem |
| MCP | `.cursor/mcp.json` | [Dashboard → Integrations & MCP](https://cursor.com/dashboard/integrations) |
| Config de ambiente | Este repo | `.cursor/environment.json` (versionado) |

### Pré-requisitos

1. Plano pago do Cursor.
2. GitHub conectado em [Integrations](https://cursor.com/dashboard/integrations).
3. Ambiente cloud em [Environments](https://cursor.com/dashboard/cloud-agents#environments).

### Uso rápido

1. Abra o projeto no Cursor Desktop.
2. `Cmd+Shift+P` → **Open Agents Window**.
3. Selecione **Cloud** no dropdown do agente.
4. Para delegar da sessão local: `/in-cloud` ou **Move to Cloud** na conversa.
5. Antes de mover trabalho para cloud: `git commit` e `git push`.

### Arquivos de configuração

| Arquivo | Função |
|---------|--------|
| `.cursor/environment.json` | Ambiente cloud (install, start, snapshot) |
| `AGENTS.md` | Instruções lidas pelos Cloud Agents |
| `.cursor/rules/prompt-elaborador.mdc` | Modo elaborador de prompts (sempre ativo) |
| `.cursor/skills/prompt-elaboracao/` | Workflow de elaboração de prompts |
| `.cursor/agents/prompt-elaborador.md` | Subagent para elaboração profunda |
| `prompts/` | Biblioteca opcional de prompts elaborados |

### Agente de elaboração de prompts

Este repo pode ser usado como **chat dedicado à engenharia de prompts**: envie rascunhos, ideias ou instruções simples e o agente devolve prompts avançados, técnicos e padronizados. Invocação manual: `/prompt-elaboracao` ou `/prompt-elaborador`.

### Status da integração

| Item | Status |
|------|--------|
| `.cursor/environment.json` na `main` | ✅ |
| Build cloud (`main`) | ✅ `bld-20260804-dd809f32-8044-41b0-b37b-0c0ac870fa19` |
| Ambiente | [Dashboard](https://cursor.com/dashboard/cloud-agents/environments/e/c81a84db-761f-11f1-a7d1-d6b4613131ce) |
| CI de validação | GitHub Actions (`validate-cloud-config.yml`) |

**Promover build ativo:** no dashboard do ambiente, abra a aba **Builds** e promova o build da `main` se ainda não estiver ativo (builds draft via API não se tornam ativos automaticamente).

### Documentação oficial

- [Cloud Agents](https://cursor.com/docs/cloud-agent.md)
- [Setup de ambiente](https://cursor.com/docs/cloud-agent/setup.md)
- [Agents Window](https://cursor.com/docs/agent/agents-window.md)
- [Cloud Agents (pt-BR)](https://cursor.com/pt-BR/help/ai-features/cloud-agents.md)
