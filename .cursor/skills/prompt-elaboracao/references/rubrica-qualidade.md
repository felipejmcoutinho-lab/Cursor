# Rubrica de qualidade — prompts elaborados

Pontue internamente (0–2 por critério). Entregue apenas se a soma for ≥ 14/16. Se abaixo, revise antes de responder.

| # | Critério | 0 | 1 | 2 |
|---|----------|---|---|---|
| 1 | **Clareza de objetivo** | Ambíguo | Parcialmente claro | Uma intenção principal, mensurável |
| 2 | **Completude** | Faltam contexto, tarefa ou saída | Maioria presente | Contexto, tarefa, restrições, formato e sucesso |
| 3 | **Precisão técnica** | Termos vagos ou incorretos | Aceitável | Terminologia correta e específica do domínio |
| 4 | **Eficiência** | Verboso sem ganho | Alguma redundância | Conciso; cada frase agrega instrução |
| 5 | **Robustez** | Ignora edge cases | Menciona alguns | Edge cases e ambiguidade tratados |
| 6 | **Padronização** | Formato inconsistente | Parcialmente padronizado | Segue template canônico do projeto |
| 7 | **Acionabilidade** | Instruções passivas | Mistura | Passos verificáveis e ordem lógica |
| 8 | **Ausência de ruído** | Clichês ("seja útil") | Pouco ruído | Zero filler; critérios operacionais |

## Red flags (revisar obrigatoriamente)

- [ ] Duas intenções conflitantes no mesmo prompt
- [ ] "Seja criativo/preciso/útil" sem definir o que isso significa na prática
- [ ] Formato de saída ausente quando o deliverable é estruturado
- [ ] Restrições que contradizem a tarefa
- [ ] Prompt > 800 linhas sem progressive disclosure (skill/references)
- [ ] Idioma misturado sem justificativa

## Checklist rápido pré-entrega

```
[ ] Objetivo em uma frase
[ ] Papel definido (se agente/system)
[ ] Tarefas numeradas ou em fluxo
[ ] DEVE / NÃO DEVE explícitos
[ ] Formato de saída com exemplo quando útil
[ ] Critérios de sucesso verificáveis
[ ] Suposições declaradas ao usuário
[ ] Prompt copiável sem edição obrigatória
```
