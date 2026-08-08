# Runbook: integração e sincronização Cursor ↔ Forecast

Documento operacional (pt-BR) para acessar o agent `bc-c89c6a5b-db95-4b1e-91de-164b02f6092d`, vincular o repositório **Forecast** ao Cloud Agents e sincronizar código local ↔ remoto ↔ agents.

**Data do diagnóstico:** 2026-08-08  
**Escopo:** Cloud Agents + Agents Window + GitHub.  
**Fora de escopo:** migrar histórico completo de chats locais para a nuvem (limitação do produto).

---

## Variáveis

Preencha antes de executar o runbook:

| Variável | Significado | Valor conhecido / status |
|----------|-------------|--------------------------|
| `{{FORECAST_REPO_URL}}` | URL remota do Forecast | **Ausente** — não inventar |
| `{{FORECAST_CAMINHO_LOCAL}}` | Clone local | Hipótese: `D:\Projetos-Desktop\Forecast` |
| `{{ORG_GITHUB}}` | Org/usuário GitHub | Observado: `felipejmcoutinho-lab` |
| `{{BRANCH_BASE}}` | Branch base | Padrão: `main` |

---

## A. Diagnóstico

### Agent `bc-c89c6a5b-db95-4b1e-91de-164b02f6092d`

| Campo | Valor |
|-------|--------|
| Status | **Acessível** / `RUNNING` |
| URL | https://cursor.com/agents/bc-c89c6a5b-db95-4b1e-91de-164b02f6092d |
| Nome | Cursor local cloud |
| Repositório vinculado | `github.com/felipejmcoutinho-lab/Cursor` |
| Ambiente | `felipejmcoutinho-lab/Cursor` (`c81a84db-761f-11f1-a7d1-d6b4613131ce`) |
| Repos no ambiente | **Somente** `github.com/felipejmcoutinho-lab/Cursor` |
| Forecast no ambiente? | **Não** |
| PR associado | [#4](https://github.com/felipejmcoutinho-lab/Cursor/pull/4) (MERGED) |

**Conclusão:** este `bcId` opera no ambiente do repositório **Cursor**. Ele **não** enxerga nem clona o Forecast. Para operar o Forecast na nuvem, é necessário um **novo agent** em um ambiente que inclua `{{FORECAST_REPO_URL}}`. O chat deste `bcId` permanece acessível pela URL; o histórico **não** migra automaticamente para o novo agent.

### Forecast

| Item | Status |
|------|--------|
| Remoto em `felipejmcoutinho-lab` | **Não encontrado** na listagem acessível (só existe o repo `Cursor`) |
| Clone local `D:\Projetos-Desktop\Forecast` | **Inacessível desta VM cloud** — validar no Desktop Windows |
| Ambiente cloud Forecast | **Inexistente** neste ambiente |
| `.cursor/environment.json` do Forecast | Desconhecido (repo não disponível aqui) |

### Lacunas e hipóteses

1. **Bloqueio:** `{{FORECAST_REPO_URL}}` não foi informada e não existe repo Forecast sob `felipejmcoutinho-lab` acessível via API.
2. **Hipótese:** o clone local está (ou estará) em `D:\Projetos-Desktop\Forecast`.
3. **Hipótese incorreta a evitar:** o agent `bc-c89c6a5b-…` foi criado no contexto Forecast — o diagnóstico mostra vínculo exclusivo com **Cursor**.
4. **Hipótese:** a conta GitHub já está em Integrations; validar em https://cursor.com/dashboard/integrations.

### Agents listados no ambiente atual (Cursor)

| bcId | Nome | Status |
|------|------|--------|
| `bc-c89c6a5b-…` | Cursor local cloud | RUNNING |
| `bc-bc843704-…` | Experiência surpresa romântica | IDLE (arquivado) |
| `bc-a652c48a-…` | Detalhes venda atual | IDLE (arquivado) |
| `bc-568bcb86-…` | Instruções TIA Portal LAD/STL | IDLE (arquivado) |
| `bc-cd466cd1-…` | Conectores fibra procedimento | IDLE (arquivado) |

Nenhum agent listado aponta para Forecast.

---

## B. Arquitetura recomendada

### Diagrama textual

```
[Cursor Desktop]
  File → Open Folder → D:\Projetos-Desktop\Forecast
  Agents Window → Este Computador → Forecast
        │
        │  git commit + git push
        ▼
[Git remoto: {{FORECAST_REPO_URL}}]
        │
        │  Cloud Agent clona a branch
        ▼
[Cloud Agent VM — ambiente Forecast]
  → trabalha em branch cursor/<descricao>-xxxx
  → abre PR
        │
        │  git fetch + checkout da branch do PR
        ▼
[Cursor Desktop local — Forecast]
```

### Opção A vs B

| Opção | Descrição | Quando usar |
|-------|-----------|-------------|
| **A — Ambiente dedicado Forecast** | Um ambiente cloud só com `{{FORECAST_REPO_URL}}` | Trabalho diário no Forecast (recomendado) |
| **B — Multi-repo** | Ambiente com Cursor + Forecast | Tarefas que precisam editar/consultar os dois repos na mesma VM |

**Decisão recomendada: Opção A**, com Opção B apenas se houver dependência cruzada real.

**Não fazer:** alterar o ambiente atual do Cursor para “substituir” o Forecast. Manter ambientes separados evita sobrescrita de config e confusão de agents/`bcId`.

---

## C. Runbook de sincronização de código

Pré-requisito: remoto `{{FORECAST_REPO_URL}}` existente e clone em `{{FORECAST_CAMINHO_LOCAL}}`.

### Local → Cloud

No PowerShell (Windows):

```powershell
cd D:\Projetos-Desktop\Forecast   # ou {{FORECAST_CAMINHO_LOCAL}}
git status
git checkout {{BRANCH_BASE}}      # normalmente main
git pull origin {{BRANCH_BASE}}
# ... edite localmente ...
git add -A
git commit -m "Descrição objetiva da alteração"
git push -u origin HEAD
```

Depois: inicie ou continue um Cloud Agent no **ambiente Forecast**. O agent clona o remoto (não a pasta local).

**Antes de Move to Cloud / `/in-cloud`:** sempre `commit` + `push`. Alterações não commitadas **não** vão para a VM.

### Cloud → Local

```powershell
cd D:\Projetos-Desktop\Forecast
git fetch origin
git checkout <branch-do-pr-do-agent>   # ex.: cursor/feature-xyz-abcd
git pull origin <branch-do-pr-do-agent>
```

Ou: abra o PR no GitHub → revise → merge → `git checkout main && git pull`.

### Convenções

| Item | Convenção |
|------|-----------|
| Branches de agents | prefixo `cursor/` |
| Branch base | `{{BRANCH_BASE}}` (padrão `main`) |
| Segredos | Dashboard → Secrets — **nunca** no Git |
| Caminhos locais | `D:\Projetos-Desktop\…` (não Desktop antigo) |

### Caso extremo: Forecast só local, sem remoto

```powershell
cd D:\Projetos-Desktop\Forecast
git init
git remote add origin https://github.com/{{ORG_GITHUB}}/Forecast.git
git add -A
git commit -m "Importação inicial do Forecast"
git branch -M main
git push -u origin main
```

Só então criar o ambiente cloud (seção E).

---

## D. Runbook de acesso a agents e chats

### Abrir o `bcId` atual (Cursor — não Forecast)

1. Web: https://cursor.com/agents?selectedBcId=bc-c89c6a5b-db95-4b1e-91de-164b02f6092d  
2. Desktop: Agents Window → localizar “Cursor local cloud” ou colar a URL.  
3. Continuar o chat neste agent **apenas** para trabalho no repo Cursor.

### Operar agents no Forecast (após ambiente criado)

1. Dashboard → Environments → selecionar ambiente **Forecast**.  
2. Em https://cursor.com/agents ou Agents Window → **Cloud** → escolher repo Forecast + branch.  
3. Descrever a tarefa; o agent abre branch/PR no Forecast.  
4. Desktop local: File → Open Folder → `D:\Projetos-Desktop\Forecast` → agente em modo **local**.  
5. Delegar local→cloud: `git push` → `/in-cloud` ou **Move to Cloud**.  
6. Babysit de PR: `/babysit` no PR do Forecast.

### O que sincroniza e o que não sincroniza

| Artefato | Sincroniza? | Como |
|----------|-------------|------|
| Código versionado | Sim | Git commit/push/fetch |
| Branch/PR do agent | Sim | GitHub + checkout local |
| Ambiente (install/start) | Sim (config) | `.cursor/environment.json` + Builds |
| Histórico de chat Desktop ↔ Cloud | **Não** | Abrir pelo URL/`bcId` específico |
| Chat do `bc-c89c6a5b-…` → novo agent Forecast | **Não** | Recriar agent; contexto antigo não clona |
| MCP local → MCP cloud | **Não** automático | Configurar no Dashboard |
| Segredos | Não via Git | Dashboard → Secrets |

---

## E. Configuração a aplicar

### 1) Integrations (uma vez)

1. https://cursor.com/dashboard/integrations  
2. Conectar GitHub com leitura/escrita em `{{FORECAST_REPO_URL}}` (e Cursor, se multi-repo).

### 2) Ambiente dedicado Forecast (Opção A — recomendado)

1. https://cursor.com/dashboard/cloud-agents#environments → **New environment**.  
2. Selecionar **somente** `{{FORECAST_REPO_URL}}`.  
3. Adicionar Secrets necessários do Forecast (API keys, DB, etc.).  
4. Concluir setup guiado → aguardar **Build** bem-sucedido.  
5. Promover o Build da `main` como ativo, se aplicável.  
6. Iniciar **novo** Cloud Agent nesse ambiente (não reutilizar `bc-c89c6a5b-…` para código Forecast).

### 3) Ambiente multi-repo (Opção B — opcional)

1. New environment → selecionar **Cursor** + **Forecast**.  
2. Secrets com nomes únicos se houver colisão.  
3. Novo agent nesse ambiente multi-repo.

### 4) Conteúdo sugerido de `.cursor/environment.json` no Forecast

Ajustar após inspecionar o stack real do Forecast (Node, Python, etc.):

```json
{
  "name": "Forecast",
  "install": "echo 'Ajuste o install ao stack do Forecast (ex.: npm ci ou pip install -r requirements.txt).'"
}
```

Exemplo Node:

```json
{
  "name": "Forecast",
  "install": "npm ci"
}
```

Exemplo Python:

```json
{
  "name": "Forecast",
  "install": "python -m pip install -r requirements.txt"
}
```

Opcional: `AGENTS.md` no Forecast com seção **Cursor Cloud specific instructions**.

`repositoryDependencies`: usar **somente** se a URL do Forecast for conhecida e houver dependência versionada explícita — não preencher com placeholders.

### 5) Desktop — abrir o Forecast local

1. Cursor Desktop → **File → Open Folder**.  
2. `D:\Projetos-Desktop\Forecast`.  
3. Validar remoto:

```powershell
git -C D:\Projetos-Desktop\Forecast remote -v
git -C D:\Projetos-Desktop\Forecast status
```

---

## F. Checklist de aceite

| # | Critério | Como verificar | Resultado |
|---|----------|----------------|-----------|
| 1 | Agent `bc-c89c6a5b-…` acessível | Abrir URL do agent | Passou (RUNNING, repo Cursor) |
| 2 | Ambiente atual listado | Dashboard Environments | Passou (só Cursor) |
| 3 | Forecast **não** no ambiente deste agent | `environment-info` / repos | Passou (bloqueio confirmado) |
| 4 | `{{FORECAST_REPO_URL}}` informada | Mensagem do usuário / GitHub | **Falhou** — pendente |
| 5 | Clone local existe | File → Open Folder no Desktop | **Pendente** (VM cloud sem D:) |
| 6 | Ambiente cloud Forecast criado | Dashboard Environments | **Falhou** — pendente |
| 7 | Build Forecast SUCCEEDED | Aba Builds | Pendente |
| 8 | Novo agent no ambiente Forecast | Agents Window / cursor.com/agents | Pendente |
| 9 | Sync local→cloud | push + agent vê commit | Pendente |
| 10 | Sync cloud→local | fetch + checkout branch do PR | Pendente |
| 11 | Chat antigo não “clonado” | Novo agent sem histórico do bcId antigo | Aceito como limitação |

---

## G. Riscos e limitações

1. **Histórico de chat não sincroniza** entre Desktop e Cloud, nem entre agents/`bcId` diferentes. Acesso é por URL/`bcId`.  
2. **Este agent não opera Forecast** sem ambiente que inclua o repo.  
3. **Sem remoto Git**, Cloud Agents não clonam pasta local.  
4. **Segredos:** LGPD / ISO 27001 — apenas Dashboard Secrets; nunca commit.  
5. **Ambiente pessoal Cursor** (`environmentJsonPath: null`) é db-backed; não misturar com config do Forecast.  
6. **Caminhos:** usar `D:\Projetos-Desktop\…`, não Desktop antigo.  
7. **MCP:** configurar cloud separadamente de `.cursor/mcp.json` local.

---

## Próxima ação mínima (desbloqueio)

1. Informar `{{FORECAST_REPO_URL}}` (ou criar o remoto e fazer push inicial).  
2. Confirmar `{{FORECAST_CAMINHO_LOCAL}}` no Desktop.  
3. Criar ambiente cloud **Forecast** (Opção A) no Dashboard.  
4. Iniciar novo Cloud Agent nesse ambiente.  
5. Manter `bc-c89c6a5b-…` para trabalho no repo Cursor / este runbook.

Com a URL do Forecast, este runbook pode ser atualizado com valores concretos e, se desejado, um `.cursor/environment.json` versionado **no repositório Forecast** (não neste repo Cursor, salvo documentação).
