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

### Documentação oficial

- [Cloud Agents](https://cursor.com/docs/cloud-agent.md)
- [Setup de ambiente](https://cursor.com/docs/cloud-agent/setup.md)
- [Agents Window](https://cursor.com/docs/agent/agents-window.md)
- [Cloud Agents (pt-BR)](https://cursor.com/pt-BR/help/ai-features/cloud-agents.md)
