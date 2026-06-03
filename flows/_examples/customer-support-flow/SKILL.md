---
name: customer-support-flow
description: Procesează un mesaj nou primit de la client în Slack #customer-support. Classify intent → fetch context CRM → reason cu Claude → reply automat sau escalează. Folosește la fiecare mesaj nou cu @bot mention.
---

# customer-support-flow (EXEMPLU)

> Pattern canonic M4.3 — classify → fetch → reason → reply, cu state tracking + error handling.

## Steps

### Step 1: classify (skill «message-classifier»)

**Input:** mesaj raw text + sender email
**Output JSON:**
```json
{
  "intent": "support | sales | complaint | other",
  "urgency": 1-5,
  "sentiment": "positive | neutral | negative"
}
```

**Error handling:**
- Retry pe 429/500/503 → backoff exponențial (5s, 10s, 20s, max 3 tries)
- Hard fail → fallback la `intent=other, urgency=3` și log warning

---

### Step 2: fetch (ClawHub skill «hubspot-contact-fetch»)

**Input:** sender email
**Output JSON:**
```json
{
  "contact_found": true,
  "last_3_tickets": [...],
  "account_value": 5400,
  "csat_score": 4.2
}
```

**Error handling:**
- 404 (contact nu există): NU e hard-fail, returnează `{contact_found: false}` și continuă
- 429/500: retry × 3
- 401 (auth expirat): hard fail + alert owner pentru re-auth

---

### Step 3: reason (Claude direct, model sonnet-4.6)

**Input:** classify output + fetch output + mesajul original
**Output JSON:**
```json
{
  "draft_reply": "...",
  "escalation_needed": false,
  "tags_to_add": ["billing", "urgent"]
}
```

**Logic:**
- Dacă `urgency >= 4` SAU `account_value > 10000` → `escalation_needed = true`
- Dacă `contact_found = false` → reply generic + flag pentru sales team
- Dacă `sentiment = negative` AND `urgency >= 3` → escalation_needed = true

**Error handling:**
- Retry × 2 pe API errors
- Hard fail → escalate manual cu mesajul original ne-procesat

---

### Step 4: reply (ClawHub skill «slack-reply»)

**Input:** draft_reply + escalation_needed
**Logic:**
- Dacă `escalation_needed = true`:
  - Postează în #support-escalation cu @manager mention
  - Postează thread reply: «Cazul tău e escalat unui senior, primești răspuns în 2h»
- Dacă `escalation_needed = false`:
  - Postează `draft_reply` ca thread reply

**Error handling:**
- Retry × 2 pe network errors
- Hard fail: email backup direct la sender + alert owner

---

## State tracking

Fiecare step salvează automat input + output în `_state/{flow_id}/step_{n}.json`.

Pentru resume după crash:
```bash
openclaw tasks flow resume {flow_id}
# Pornește de la step-ul care a picat, NU de la step 1
```

## Monitoring

- Logs: `openclaw tasks flow show {flow_id}`
- Alerting: Slack DM la owner pe orice hard fail
- Metrics săptămânale: agregate ore economisite + erori cumulate (vezi `dashboard/`)

## Cum îl personalizezi

Acest flow e un schelet. Pentru cazul TĂU specific:
1. Înlocuiește `hubspot-contact-fetch` cu CRM-ul tău (Pipedrive, Salesforce, etc.)
2. Ajustează logica de `escalation_needed` cu praguri specifice business-ului
3. Schimbă `#customer-support` cu canalul tău Slack
4. Personalizează template-ul de reply în step 3 reason
