# audits/

> **Module 2 deliverable.** Aici trăiesc log-urile de timp și harta finală de automatizări.

## Structura recomandată

```
audits/
├── README.md
├── _template-audit.md           ← template pentru log-uri săptămânale
├── _template-automation-map.md  ← template pentru harta finală
├── 2026-06-03_personal-log.md   ← log-uri timp (input pentru agentul de audit)
├── 2026-06-10_job-log.md
└── 2026-06-15_automation-map.md ← OUTPUT FINAL M2 — harta cu 8+ procese + 3 prioritizate
```

## Workflow M2

1. **Săptămâna 2:** loghează 7 zile cu log de timp (folosește template `_template-audit.md`)
2. **Săptămâna 3:** rulează agenții de audit (M2.2 + M2.3) pe log-urile tale
3. **Final M2.4:** sintetizează harta în `automation-map.md` cu impact × fezabilitate
4. **La M5:** te întorci aici pentru a alege cele 3 procese de construit

## De ce am folder dedicat (vs `output/`)

`output/` se golește des. `audits/` rămâne — harta ta de automatizări e un artefact pe care îl rafinezi în timp și-l consulți la fiecare decizie viitoare.

## Note pentru date sensibile

Dacă log-ul tău de la job conține nume de clienți sau context confidențial:
- **NU commitez** acel fișier (adaugă în `.gitignore` local: `audits/2026-*-job-log.md`)
- Alternativ: anonimizează înainte de commit (înlocuiește nume cu CLIENT_A, PROIECT_B)
