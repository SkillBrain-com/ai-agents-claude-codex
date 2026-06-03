# areas/ — Skill-uri împărțite pe arii de viață

Aici trăiesc skill-urile tale. Le împărțim pe **3 arii** (personal / work / shared) pentru:

1. **Izolare credentiale.** Gmail-ul tău personal NU se amestecă cu Gmail-ul de la job. Fiecare arie are propriul `.env`.
2. **Mental clarity.** Când lucrezi la skill-uri de la job, deschizi doar `areas/work/`. Mai puțină distragere.
3. **Output separat.** Briefing-urile personale nu se amestecă cu rapoartele de la muncă.

---

## Structura

```
areas/
├── personal/
│   ├── README.md
│   ├── skills/
│   │   ├── my-first-skill/       ← exemplu funcțional (M1)
│   │   └── {skill-urile tale}/
│   ├── output/                    ← rezultatele rulărilor (gitignored)
│   └── .env.personal.example      ← chei specifice (Gmail personal etc.)
│
├── work/
│   ├── README.md
│   ├── skills/
│   ├── output/
│   └── .env.work.example
│
└── shared/
    ├── README.md
    ├── skills/                    ← orchestratoare care folosesc skills din ambele arii
    └── output/
```

---

## Când pun un skill în `personal/` vs `work/`?

| Întrebare | Personal | Work |
|---|---|---|
| Datele atinse sunt ale tale sau ale companiei? | Tale | Ale companiei |
| Folosește contul tău Gmail/Notion personal? | DA | NU |
| Output-ul îl folosești la job? | NU | DA |
| Ai voie legal să rulezi cu cloud AI? | DA întotdeauna | Cere acord IT/Legal |

Exemple:

| Skill | Arie |
|---|---|
| Briefing de dimineață cu vremea + email personal | `personal/` |
| Audit rutină personală (M2) | `personal/` |
| Triaj inbox Slack de la job | `work/` |
| Procesare facturi work | `work/` |
| Orchestrator care combină brief personal + status work (M5) | `shared/` |

---

## Convenția de naming pentru skill folders

- `kebab-case` (litere mici + cratime)
- Descriptiv, scurt: `morning-brief`, `invoice-processor`, `weekly-recap`
- **NU** generice ca: `helper`, `utility`, `misc`
- **NU** brand-uri în nume: NU `claude-helper`, da `text-summarizer`

---

## Cum împart un skill „universal" (ex: weather)

Dacă ai un skill care e util peste tot (ex: vremea, ora, conversie monetară), pune-l în:

- `areas/shared/skills/get-weather/` — și apelează-l din orchestratoarele tale

Pattern recomandat M3.5.
