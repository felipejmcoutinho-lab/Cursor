---
name: prompt-engineering
description: Elabora, otimiza e padroniza prompts avançados a partir de inputs simples (prompts, instruções, insights, ideias). Use quando o usuário pedir para melhorar, detalhar, profissionalizar ou criar um prompt.
---

# Skill: Prompt Engineering

## Quando usar

Use esta skill quando o usuário fornecer um input bruto e quiser um prompt superior para LLM, Cursor Agent, automação ou fluxo técnico.

## Protocolo rápido

1. Diagnosticar intenção, destinatário e lacunas.
2. Montar o prompt no template padrão (ver regra `.cursor/rules/prompt-engineer.mdc`).
3. Endurecer com restrições, critérios, anti-padrões e edge cases.
4. Entregar: Diagnóstico → Prompt (copiável) → Variantes úteis → Notas.

## Checklist de robustez

Antes de entregar, verifique:

- [ ] Objetivo único e verificável
- [ ] Role adequada ao domínio
- [ ] Escopo inclui / fora de escopo
- [ ] Formato de saída explícito
- [ ] Critérios de qualidade mensuráveis
- [ ] Anti-padrões e edge cases
- [ ] Hipóteses marcadas (se houver)
- [ ] Variáveis `{{CLARAS}}` para o que o usuário precisa preencher
- [ ] Sem contradições nem fluff

## Perfis de destinatário

| Destinatário | Ênfase |
|---|---|
| Cursor / Cloud Agent | arquivos, passos, validação, critérios de done, git/PR se couber |
| LLM chat genérico | role, contexto, formato, exemplos |
| Análise / consultoria | método, evidências, riscos, trade-offs |
| Redação / conteúdo | tom, público, estrutura, length |
| Ops / runbook | precondições, comandos, rollback, verificação |

## Modos de entrega

- **Padrão:** diagnóstico + prompt completo + notas
- **Compacto:** só o essencial, alta densidade
- **Agent-ready:** passos executáveis + validação
- **Bilingue:** sob pedido — prompt em EN, meta em PT

## Não fazer

- Não executar o prompt a menos que o usuário peça.
- Não substituir a intenção do usuário por outra “melhor”.
- Não gerar dezenas de variantes — no máximo 2–3.
- Não pedir questionário longo antes de elaborar.
