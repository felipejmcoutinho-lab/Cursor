# Manual Técnico TIA Portal - BLBW

Manual técnico avançado de instruções e lógica de controle para Siemens TIA Portal / Step 7 (LAD/STL).

## Documentos Gerados

| Arquivo | Descrição |
|---------|-----------|
| `docs/Manual_Tecnico_TIA_Portal_BLBW.docx` | Versão editável (Microsoft Word / LibreOffice) |
| `docs/Manual_Tecnico_TIA_Portal_BLBW.pdf` | Versão para consulta e impressão |

## Regenerar os Documentos

```bash
pip install -r requirements.txt
python3 scripts/generate_manual.py
```

## Estrutura

- `scripts/manual_content.py` — Conteúdo técnico dos 10 capítulos base
- `scripts/manual_content_extended.py` — Extensões, apêndices e instruções adicionais
- `scripts/generate_manual.py` — Gerador DOCX/PDF com padrão corporativo BLBW

**Versão atual:** Corporativa 1.1 (inclui apêndices A/B e capítulos de continuação)

## Padrão BLBW

- Identidade visual: BLBW - Be Life, Be Water
- Cores corporativas: #0066B3 (primária), #003366 (escuro), #00A0E3 (acento)
- Classificação: Documento Técnico Interno
