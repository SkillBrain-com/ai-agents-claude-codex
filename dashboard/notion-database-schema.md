# Notion Database Schema — Automation Status

> Schema completă pentru dashboard-ul tău din M5.4. Cum o creezi pas cu pas.

---

## Pasul 1 — Creează database

În Notion:
1. Crează o pagină nouă: `🤖 My Automations Dashboard`
2. Tastează `/database` → Database — Full page
3. Numește-l `Automation Status`

## Pasul 2 — Configurează coloanele

Adaugă următoarele properties:

| Property name | Type | Configurare |
|---|---|---|
| `Name` | Title | (există default) |
| `Status` | Select | Options: `🟢 Healthy`, `🟡 Warning`, `🔴 Down`, `⚪ Paused` |
| `Last successful run` | Date | Include time: ON |
| `Next scheduled run` | Date | Include time: ON |
| `Errors 7d` | Number | Format: number |
| `Impact h/wk` | Number | Format: number, 1 decimal |
| `Type` | Select | Options: `personal`, `work`, `shared` |
| `Stack` | Multi-select | Options: `cowork`, `openclaw`, `claude-direct`, `chatgpt`, `gemini` |
| `Trigger` | Select | Options: `scheduled`, `event-driven`, `manual` |
| `Notes` | Rich text | (incidents, observations) |
| `Repo path` | URL | (link la SKILL.md în GitHub) |

## Pasul 3 — Adaugă view-urile

Default view (Table): toate

Plus:

### View „🚨 Probleme"
- Filter: `Status` is not `🟢 Healthy`
- Sort: `Errors 7d` descending

### View „📊 Impact"
- Sort: `Impact h/wk` descending
- Display only: Name, Impact h/wk, Last successful run

### View „📅 Schedule"
- Sort: `Next scheduled run` ascending
- Display: Name, Next scheduled run, Trigger

## Pasul 4 — Setează initial rows

Adaugă manual cele 3 automation ale tale:

| Name | Status | Type | Stack | Trigger |
|---|---|---|---|---|
| `morning-brief` | 🟢 Healthy | personal | cowork, claude-direct | scheduled |
| `invoice-processor` | 🟢 Healthy | work | openclaw, claude-direct | event-driven |
| `weekly-recap` | 🟢 Healthy | shared | openclaw, claude-direct, gemini | scheduled |

## Pasul 5 — Setup integration pentru push automat

1. Mergi la [notion.so/profile/integrations](https://notion.so/profile/integrations)
2. Click `New integration`
3. Numește: `My Automation Push`
4. Workspace: alege workspace-ul tău
5. Copy `Internal Integration Token` → pune în `.env` ca `NOTION_TOKEN=secret_...`

Apoi share database-ul cu integrarea:
1. Deschide database-ul în Notion
2. Click `⋯` dreapta-sus → `Connections` → adaugă `My Automation Push`

## Pasul 6 — Folosește scriptul de push

Vezi [_scripts/push_status.py.example](_scripts/push_status.py.example).

Setează în `.env`:
```
NOTION_TOKEN=secret_...
NOTION_DATABASE_ID=...   # din URL-ul database-ului: notion.so/{database_id}?v=...
```

Apoi în SKILL.md-ul fiecărui flow, ultimul step apelează:
```bash
python3 dashboard/_scripts/push_status.py \
  --name morning-brief --status healthy --impact 1.75
```

## Alternative

Dacă nu vrei Notion:
- **Google Sheets:** la fel de simplu, push prin Sheets API
- **Local Markdown:** un singur `dashboard/STATUS.md` actualizat de fiecare flow (commit + push în git)
- **Tools dedicate:** [bika.ai](https://bika.ai/), [vellum.ai](https://www.vellum.ai/) — overkill pentru personal
