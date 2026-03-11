# PDFs Bloqueados pelo Google Drive File Stream

**Data:** 2026-03-11  
**Projeto:** Parador AG7  
**Problema:** Arquivos em modo "disponível sob demanda" → deadlock ao tentar ler

---

## Paisagismo - Implantação (Espécies Vegetais)

**Status:** ❌ 5 PDFs bloqueados (TODOS os arquivos de implantação com legendas de espécies)

1. **PAR-PAI-EX-0010-IM-IMP-R01.pdf** (6,4 MB)
   - Path: `~/Library/CloudStorage/.../24. Paisagismo/04. Executivo/PDF/`
   - Conteúdo esperado: Legendas de espécies vegetais (torre/implantação)

2. **PAR-PAI-EX-0020-IM-IMP-R00.pdf** (62 MB)
   - Path: `~/Library/CloudStorage/.../24. Paisagismo/04. Executivo/PDF/`
   - Conteúdo esperado: Implantação principal com lista completa de espécies

3. **PAR-PAI-EX-0030-IM-IMP-R00.pdf** (20 MB)
   - Path: `~/Library/CloudStorage/.../24. Paisagismo/04. Executivo/PDF/`
   - Conteúdo esperado: Legendas de espécies (setor específico)

4. **PAR-PAI-EX-0060-TO-N01-R00.pdf** (tamanho TBD)
   - Path: `~/Library/CloudStorage/.../24. Paisagismo/04. Executivo/PDF/`
   - Conteúdo esperado: Legendas de espécies (torre N01)

5. **PAR-PAI-EX-0110-IM-IMP-R00.pdf** (37 MB)
   - Path: `~/Library/CloudStorage/.../24. Paisagismo/04. Executivo/PDF/`
   - Conteúdo esperado: Implantação com legendas de espécies

---

## Impacto no Orçamento

**Disciplina afetada:** Paisagismo  
**Dados já extraídos:** Drenagem, irrigação, pisos externos, equipamentos (26 items)  
**Dados pendentes:** Lista completa de espécies vegetais (nomes científicos, quantidades)

**Ação necessária:** Leo enviará os 5 PDFs localmente após conclusão da extração automática.

---

## Outras Disciplinas com Possíveis Bloqueios

**Nota:** Elétrico teve 70% dos arquivos bloqueados anteriormente (processamento parcial).  
Hidrossanitário e Arquitetura também tiveram alguns timeouts relacionados a deadlocks.
