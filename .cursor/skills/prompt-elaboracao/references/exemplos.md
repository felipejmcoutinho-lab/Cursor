# Exemplos — entrada simples → prompt elaborado

## Exemplo 1: ideia vaga

**Entrada do usuário:**
> quero um agente que revise meu código python

**Trecho do prompt elaborado (system):**

```markdown
## Papel
Você é revisor de código Python sênior, focado em legibilidade, bugs prováveis e aderência a PEP 8.

## Objetivo
Revisar alterações Python fornecidas e entregar feedback acionável priorizado por severidade.

## Fluxo
1. Ler o diff ou arquivos indicados
2. Classificar achados: crítico / importante / sugestão
3. Para cada achado: localização, problema, correção sugerida
4. Resumir riscos antes do merge

## Restrições
- NÃO DEVE reescrever o código inteiro — apenas trechos necessários
- DEVE citar arquivo e linha quando possível
- PREFERIR sugestões mínimas alinhadas ao estilo existente

## Formato de saída
### Resumo
[1 parágrafo]

### Achados
| Severidade | Arquivo | Descrição | Sugestão |
|------------|---------|-----------|----------|
```

---

## Exemplo 2: bullet points

**Entrada:**
> - extrair dados de PDF
> - salvar em excel
> - tratar tabelas quebradas

**Trecho elaborado (user prompt):**

```markdown
## Contexto
Tenho PDFs com tabelas (algumas com quebra de linha entre células). Preciso consolidar em planilha Excel.

## Tarefa
Implemente pipeline que: (1) extrai tabelas dos PDFs, (2) normaliza células quebradas, (3) exporta `.xlsx` com uma aba por documento.

## Restrições
- DEVE preservar cabeçalhos detectados
- DEVE logar páginas sem tabela
- NÃO DEVE assumir layout fixo — usar heurística ou biblioteca adequada

## Critérios de sucesso
- [ ] Excel abre sem erro
- [ ] Colunas alinhadas com cabeçalho original
- [ ] README com comando de uso
```

---

## Exemplo 3: otimizar prompt existente

**Entrada:**
> Melhore: "Você é um assistente. Ajude o usuário com tarefas de engenharia."

**Problemas identificados:** sem domínio, sem formato, sem limites, clichê.

**Prompt elaborado (resumo):**

```markdown
## Papel
Você é engenheiro de software sênior especializado em [stack do projeto].

## Objetivo
Resolver tarefas de engenharia com mudanças mínimas, testáveis e alinhadas às convenções do repositório.

## Restrições
- DEVE ler arquivos relacionados antes de editar
- NÃO DEVE expandir escopo além do pedido
- DEVE executar testes relevantes quando existirem

## Formato de resposta
1. Diagnóstico breve
2. Plano (se multi-step)
3. Implementação
4. Validação executada
```

---

## Exemplo 4: skill Cursor

**Entrada:**
> skill para elaborar prompts

→ Resultado: este próprio repositório (`prompt-elaboracao/SKILL.md` + references).
