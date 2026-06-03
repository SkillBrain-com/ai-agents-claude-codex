# dashboard/

> **Module 5.4 deliverable.** Dashboard unificat care monitorizează cele 3 automation.

## De ce dashboard

Fără dashboard, automation-urile sunt invizibile. Cu dashboard:

- Vezi status live ✅ Healthy / ⚠️ Warning / ❌ Down
- Vezi ultima rulare reușită
- Vezi erori cumulate 7d
- Vezi impact măsurat (ore economisite / săptămână)

## Implementare recomandată: Notion database

### Schema database

| Coloană | Tip Notion | Exemplu |
|---|---|---|
| Name | Title | `morning-brief` |
| Status | Select (Healthy/Warning/Down) | Healthy |
| Last successful run | Date | 2026-06-03 07:31 |
| Next scheduled run | Date | 2026-06-04 07:30 |
| Errors 7d | Number | 0 |
| Impact h/wk | Number | 1.75 |
| Notes | Rich text | „Crashed 2× pe 2026-05-28 din cauza Notion API down" |

Vezi [notion-database-schema.md](notion-database-schema.md) pentru schema completă + cum o creezi.

## Pattern: skill care actualizează dashboard

În fiecare flow al tău, ultimul step face PATCH la row-ul corespunzător din Notion:

```python
# Pseudo-cod în _scripts/push_status.py (exemplu)
push_status({
    "automation_name": "morning-brief",
    "status": "Healthy",  # sau "Warning" / "Down"
    "last_run": now(),
    "errors_7d": count_recent_errors(),
    "impact_hours": estimated_impact(),
})
```

Vezi [_scripts/push_status.py.example](_scripts/push_status.py.example) — copiază + setezi token Notion + database ID.

## Alerting

Dincolo de dashboard, setează alerting activ:

1. **Slack DM la owner** când `Status = Down`
2. **Email săptămânal** cu summary toate automation
3. **WhatsApp ping** când `impact_hours` > target săptămânal

Detalii M5.4.
