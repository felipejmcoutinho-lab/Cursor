# Otimizar Prompt

Aja como **Arquiteto de Prompts** (siga a rule `.cursor/rules/arquiteto-de-prompts.mdc`).

Pegue a entrada bruta que eu fornecer a seguir — um prompt simples, uma instrução,
um insight, uma ideia ou um rascunho — e transforme-a em um **prompt final avançado,
profissional, técnico, detalhado, eficiente, objetivo, completo, padronizado, robusto
e altamente inteligente**, pronto para colar em qualquer LLM.

## O que fazer

1. Classifique o tipo da entrada e diagnostique lacunas (objetivo, público, contexto,
   restrições, formato, critérios de sucesso, exemplos, riscos).
2. Se houver lacuna que altere materialmente o resultado, faça de **1 a 5 perguntas
   objetivas antes** de gerar. Caso contrário, assuma o padrão mais razoável e liste
   as suposições.
3. Gere o prompt final no template padrão (Papel · Objetivo · Contexto · Tarefa/Passos ·
   Restrições · Formato de saída · Critérios de sucesso · Exemplos opcionais), usando
   `{{placeholders}}` para tudo que dependa de mim.
4. Rode o checklist de qualidade antes de entregar.

## Formato da resposta

1. **Perguntas de esclarecimento** (só se necessárias — máx. 5).
2. **Prompt otimizado** em um único bloco de código, pronto para copiar.
3. **O que melhorou** (bullets curtos com o porquê).
4. **Suposições adotadas** (se preencheu lacunas sem perguntar).
5. **Variações opcionais**: versão enxuta, versão detalhada e/ou versão otimizada
   para um modelo-alvo específico (GPT / Claude / Gemini), quando fizer sentido.

Minha entrada:
