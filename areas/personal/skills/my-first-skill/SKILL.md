---
name: my-first-skill
description: Briefing de dimineață — agregă vremea, ora curentă și un quote motivațional. Folosește când utilizatorul cere «briefing de dimineață», «good morning», sau pornește scheduled task de dimineață.
---

# my-first-skill — Briefing de dimineață

> **Pentru cine:** primul tău skill în VSCode. Funcționează out-of-the-box fără API keys externe (Open-Meteo e gratuit, fără cheie).

## Ce face

Generează un briefing scurt (~80 cuvinte) cu:

1. 🌤️ Vremea de azi pentru orașul tău
2. ⏰ Ora curentă
3. 💡 Un quote scurt despre productivitate / focus / învățare

## Cum îl invoc

- **Direct în Claude Code:** „Rulează skill-ul my-first-skill"
- **Cu locație custom:** „Rulează my-first-skill pentru Cluj-Napoca"
- **Scheduled (după M3.4):** se invocă automat zilnic la 07:30

## Pași de execuție

1. **Citește orașul** din [references/profile.md](references/profile.md) (default: București). Dacă user-ul a specificat alt oraș în mesaj, folosește-l pe acela.
2. **Apelează scriptul de vreme:**
   ```bash
   python3 areas/personal/skills/my-first-skill/scripts/get_weather.py "{oraș}"
   ```
   Output exemplu: `19.4°C în București`
3. **Generează quote-ul.** Alege 1 quote scurt (max 20 cuvinte) despre productivitate / focus / învățare. Variază între rulări — nu repeta același quote 2 zile la rând.
4. **Asamblează output-ul** în formatul de mai jos:

```
Bună dimineața!

🌤️  Vremea: {output_script_vreme}
⏰  E acum: {ora_curenta} ({zi_saptamana})

💡 {quote_motivational}

Ai o zi productivă!
```

## Exemple de output bun

<examples>
  <example>
    <input>Rulează my-first-skill</input>
    <output>
Bună dimineața!

🌤️  Vremea: 19.4°C în București
⏰  E acum: 07:32 (marți)

💡 „Cel mai bun moment pentru a începe a fost ieri. Al doilea cel mai bun e acum."

Ai o zi productivă!
    </output>
  </example>
  <example>
    <input>Rulează my-first-skill pentru Cluj-Napoca</input>
    <output>
Bună dimineața!

🌤️  Vremea: 17.1°C în Cluj-Napoca
⏰  E acum: 06:45 (miercuri)

💡 „Focus-ul nu e despre a spune da; e despre a spune nu la o sută de lucruri."

Ai o zi productivă!
    </output>
  </example>
</examples>

## Erori comune

| Caz | Soluție |
|---|---|
| Scriptul de vreme returnează „N/A" (oraș negăsit) | Afișează „Vremea N/A pentru {oraș}" și continuă la pașii următori |
| Lipsește `references/profile.md` | Folosește default „București" |
| Nu există Python 3 instalat | Cere user-ului să-l instaleze; oferă alternativă manuală |

## Cum îl personalizezi

Asta e versiunea minimă. Adaugă incremental:

- **Email-uri:** integrează cu Gmail (necesită OAuth — vezi `clawhub install gmail-official` în M4)
- **Task-uri Notion:** integrează cu Notion API (M3.4 sau direct cu clawhub)
- **Calendar de azi:** integrează cu Google Calendar
- **Limba și ora local:** ajustează `references/profile.md`

## Note

- Output-ul nu se trimite nicăieri — doar îl vezi în chat. Pentru WhatsApp/Telegram, înlănțuie cu skill-ul `send-to-{platform}` (M4-M5).
- Quote-urile sunt generate de model, nu hardcodate — variază natural.
- Scriptul Python nu necesită niciun API key extern. Open-Meteo e gratuit.
