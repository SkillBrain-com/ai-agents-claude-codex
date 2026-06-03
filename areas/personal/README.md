# areas/personal/

Skills care folosesc **conturile tale personale** (Gmail personal, Notion personal, calendar personal).

## Ce skill-uri pun aici (exemple)

- `morning-brief/` — briefing zilnic cu vremea + email + task-uri (M3.4)
- `weekend-planner/` — sugestii activități pe baza vremii și liste de TODO
- `weekly-recap/` — sinteză săptămânală a productivității tale
- `personal-audit/` — agentul de audit din M2.2
- `decision-helper/` — pipeline research → sinteză → decizie (M1.4)

## Configurare credentiale

Skill-urile de aici citesc din `.env.personal` (la nivel de arie, vezi `.env.personal.example`).

```bash
# La prima rulare
cp areas/personal/.env.personal.example areas/personal/.env.personal
# Editează cu cheile TALE personale
```

`.env.personal` e gitignored prin pattern-ul `.env*` din `.gitignore` global.

## Output

Toate fișierele generate de skill-uri merg în `output/{YYYY-MM-DD}_{skill-slug}/`:

```
output/
├── 2026-06-03_morning-brief/
│   └── briefing.md
├── 2026-06-08_weekly-recap/
│   ├── analysis.json
│   └── summary.md
└── ...
```

Folder-ul `output/` e gitignored (vezi `.gitignore` global).
