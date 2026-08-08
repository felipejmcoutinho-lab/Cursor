# Biblioteca de prompts elaborados

Pasta opcional para versionar prompts refinados por este agente.

## Convenção de nomes

```
prompts/
├── [dominio]/
│   └── [nome-descritivo].md
```

Exemplo: `prompts/engenharia/revisor-python.md`

## Estrutura de arquivo

```markdown
---
titulo: Nome do prompt
tipo: system | user | rule | skill | subagent
idioma: pt-BR
origem: rascunho do usuário em [data ou referência]
versao: 1.0
---

## Prompt

[conteúdo copiável]

## Notas

[contexto, variantes, histórico de iterações]
```

## Uso

1. Elabore o prompt na conversa com o agente
2. Copie o resultado para um arquivo aqui se quiser versionar
3. Peça ao agente: "Salve este prompt em `prompts/...`" quando quiser persistir no repo
