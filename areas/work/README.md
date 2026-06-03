# areas/work/

Skills care folosesc **conturile de la job** (Slack work, Gmail work, CRM, etc.).

## ⚠️ Atenție compliance

Înainte să pui aici primul skill care atinge date de la companie:

- [ ] Verifică **politica AI internă** (ai voie să trimiți date la Claude/ChatGPT/Gemini?)
- [ ] Confirmă cu **IT/Security** că folosirea cloud AI e OK pentru tipul tău de date
- [ ] Pentru date sensibile (clienți, financial, HR): consideră varianta **local-only** (Ollama + OpenClaw, vezi M4.5)

Dacă răspunsul e „nu e OK cloud AI": nu construi aici. Construiește doar local cu modele open-source.

## Ce skill-uri pun aici (exemple)

- `inbox-triage/` — triaj automat Slack/email work
- `meeting-summarizer/` — sumarizează transcript-uri din ședințe
- `invoice-extractor/` — procesare facturi din folder Downloads → Sheet
- `crm-update-bot/` — auto-update HubSpot/Pipedrive după calls
- `job-audit/` — agentul de audit din M2.3

## Configurare credentiale

```bash
cp areas/work/.env.work.example areas/work/.env.work
# Adaugă tokens de la HubSpot, Slack, etc.
```

`.env.work` e gitignored.

## Best practices

- **Niciodată nu hardcoda email-uri de clienți** în SKILL.md (sunt în git history apoi)
- **Folosește placeholder-uri**: `{CLIENT_EMAIL}` în SKILL.md, valoarea reală vine din `.env` sau prompt
- **Loghează minim:** output-urile nu trebuie să conțină nume de clienți / date private. Anonimizează dacă vrei history.
