---
name: prompt-engineering
description: Elabora, otimiza e padroniza prompts avançados em português brasileiro a partir de inputs simples (prompts, instruções, insights, ideias), com conformidade a normas técnicas nacionais e internacionais quando aplicável.
---

# Skill: Engenharia de Prompts

## Quando usar

Use esta skill quando o usuário fornecer um input bruto e quiser um prompt superior para LLM, Cursor Agent, automação ou fluxo técnico — **sempre em português brasileiro**.

## Protocolo rápido

1. Diagnosticar intenção, destinatário, domínio normativo e lacunas.
2. Montar o prompt no template padrão (ver regra `.cursor/rules/prompt-engineer.mdc`).
3. Incluir **Normas e conformidade** quando o domínio exigir (ABNT, ISO, IEC, ASTM, LGPD, WCAG, etc.).
4. Endurecer com restrições, critérios, anti-padrões e casos extremos.
5. Entregar: Diagnóstico → Prompt (copiável) → Variantes úteis → Notas.

## Idioma (obrigatório)

- **100% pt-BR** em diagnóstico, prompt, variantes e notas.
- Exceções: identificadores técnicos imutáveis, citações literais do usuário, pedido explícito de outro idioma.
- Evitar anglicismos quando houver termo técnico brasileiro estabelecido.

## Checklist de robustez

Antes de entregar, verifique:

- [ ] Objetivo único e verificável
- [ ] Papel adequado ao domínio
- [ ] Escopo inclui / fora de escopo
- [ ] Formato de saída explícito (em pt-BR)
- [ ] Critérios de qualidade mensuráveis
- [ ] Normas aplicáveis citadas e exigências de conformidade (se domínio exige)
- [ ] Anti-padrões e casos extremos
- [ ] Hipóteses marcadas (se houver)
- [ ] Variáveis `{{CLARAS}}` para o que o usuário precisa preencher
- [ ] Sem contradições, fluff ou inglês desnecessário na narrativa
- [ ] Ortografia e convenções pt-BR (datas, unidades SI, vírgula decimal)

## Normas por domínio (referência)

Citar apenas o que se aplica ao contexto do prompt:

| Domínio | Exemplos |
|--------|----------|
| Documentação / relatórios | ABNT NBR 14724, 6023, 6024, 6028, 10520 |
| Redação oficial | Manual de Redação da Presidência da República |
| Software | ISO/IEC/IEEE 12207, ISO/IEC 25010, ISO/IEC/IEEE 29119 |
| Segurança / dados | ISO/IEC 27001, LGPD |
| Acessibilidade | ABNT NBR 17060, WCAG 2.x |
| Engenharia / materiais | ABNT NBR, ASTM, IEC (conforme caso) |

Se a norma exata não foi informada, declarar hipótese e pedir validação no prompt.

## Perfis de destinatário

| Destinatário | Ênfase |
|---|---|
| Cursor / Cloud Agent | arquivos, passos, validação, critérios de conclusão, git/PR se couber |
| LLM genérico | papel, contexto, formato, exemplos |
| Análise / consultoria | método, evidências, riscos, trade-offs |
| Redação / conteúdo | tom, público, estrutura, extensão, normas ABNT de redação |
| Operações / runbook | pré-condições, comandos, rollback, verificação |

## Modos de entrega

- **Padrão:** diagnóstico + prompt completo + notas (pt-BR)
- **Compacto:** só o essencial, alta densidade
- **Pronto para agente:** passos executáveis + validação
- **Com normas:** expande seção Normas e conformidade

## Não fazer

- Não executar o prompt a menos que o usuário peça.
- Não substituir a intenção do usuário por outra “melhor”.
- Não gerar dezenas de variantes — no máximo 2–3.
- Não pedir questionário longo antes de elaborar.
- Não misturar inglês na narrativa sem necessidade técnica ou pedido explícito.
- Não citar normas irrelevantes ao domínio.
