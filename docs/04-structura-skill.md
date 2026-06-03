# 04 — Structura unui SKILL.md

> **Skill = unitatea atomică de automatizare.** Format unic, portabil între Claude Code, OpenClaw, Anthropic Agent Skills API.

---

## Anatomia minimă

Un skill = un folder cu cel puțin `SKILL.md`. Restul e opțional.

```
my-skill/
├── SKILL.md           ← OBLIGATORIU — frontmatter + instrucțiuni
├── references/        ← OPȚIONAL — docs auxiliare încărcate la nevoie
│   └── profile.md
└── scripts/           ← OPȚIONAL — scripturi Python/Bash apelate
    └── helper.py
```

---

## Frontmatter — partea critică

Primele rânduri din `SKILL.md` sunt YAML între `---`:

```yaml
---
name: weekend-planner
description: Planifică-mi weekend-ul pe baza vremii + 3 idei de activități. Folosește când utilizatorul cere «plan de weekend» sau pornește scheduled vineri seara.
---
```

### Reguli stricte

| Câmp | Limită | Reguli |
|---|---|---|
| `name` | max 64 caractere | kebab-case (litere mici + cifre + cratime). Fără cuvinte rezervate. |
| `description` | max 1024 caractere | Începe cu verbe de acțiune. Descrie clar CÂND să se invoce. |

### De ce contează `description`

Modelul AI **citește** `description` ca să decidă dacă skill-ul tău se potrivește cu cererea user-ului. Un description vag = skill care nu se invocă automat.

❌ **Bad descriptions:**
- „Skill pentru weekend"
- „Plan zile libere"
- „AI assistant"

✅ **Good descriptions:**
- „Planifică-mi weekend-ul pe baza vremii și 3 idei de activități. **Folosește când** utilizatorul cere «plan de weekend» sau pornește scheduled vineri seara."
- „Triază email-urile noi: identifică top 3 prioritare + sumar 1 propoziție per email. **Activează** când rulează scheduled task de dimineață sau utilizatorul cere «triaj inbox»."

**Pattern recomandat:** `{Acțiune principală}. {Acțiuni secundare}. Folosește când / Activează când {trigger condition}.`

---

## Corpul SKILL.md

După frontmatter, restul e Markdown liber cu instrucțiunile pentru AI. Structura recomandată:

```markdown
# my-skill

## Ce face

{1-2 propoziții — descriere clară pentru un user care nu te cunoaște.}

## Pași de execuție

1. {Citește orașul din references/profile.md}
2. {Apelează API-ul de vreme (vezi scripts/get_weather.py)}
3. {Generează planul cu Claude folosind template-ul de mai jos}
4. {Returnează ca markdown cu emoji-uri}

## Output

Format final:

\`\`\`
🌤️ Vremea weekend: {sumar}
🎯 Idei activități:
  1. {idee_1} — {de ce se potrivește}
  2. {idee_2} — {de ce}
  3. {idee_3} — {de ce}
💡 Bonus: {1 sfat surprinzător}
\`\`\`

## Erori comune

- Dacă API-ul de vreme cade → afișează „Vremea N/A" + skip filtrare meteo
- Dacă nu am date despre oraș în references → cere user-ului orașul

## Note

- Skill-ul nu trimite mesaje — doar pregătește textul.
- Pentru a-l trimite pe WhatsApp/Telegram, înlănțuie cu skill «send-to-telegram».
```

---

## Few-shot examples în SKILL.md

Dacă skill-ul tău produce output structurat (JSON, tabel), adaugă exemple în corp:

```markdown
## Exemple

<examples>
  <example>
    <input>orașul: București, vremea: ploaie</input>
    <output>
🌤️ Vremea weekend: ploaie ușoară 14°C
🎯 Idei activități:
  1. Cinema City Mall — comfort indoor
  2. Plimbare prin Cărturești Carusel — bookshop + cafea
  3. Gătit acasă rețetă nouă din Yotam Ottolenghi — productiv + cozy
💡 Bonus: ploaia ușoară e perfectă pentru somn — power-nap 30 min după prânz
    </output>
  </example>
</examples>
```

Few-shot prompting → vezi M3.2.

---

## Custom Instructions (pe Claude/ChatGPT/Gemini UI)

Template recomandat pentru toate cele 3 platforme — copy-paste **identic**:

```
ROL: Ești asistentul meu personal pentru muncă + viață.

CONTEXT DESPRE MINE:
- Nume: {NUMELE TĂU}
- Rol profesional: {EX: marketing manager}
- Limba primară: română (folosește diacritice)
- Fus orar: Europe/Bucharest

STIL:
- Răspunsuri concise, direct la subiect
- Bullet-uri preferate listelor lungi de proză
- Cod / scripturi cu syntax highlighting
- Niciodată nu pierde timp cu „as an AI..."

CÂND NU ȘTII RĂSPUNSUL:
- Spune explicit „nu știu / nu am date pe asta"
- Propune unde aș putea găsi răspunsul

CÂND ÎMI CERI CLARIFICĂRI:
- Maxim 1 întrebare odată
- Doar dacă e blocker real, altfel asumă cel mai probabil scenariu
```

---

## Cum se invocă skill-ul

### Manual în Claude Code (VSCode)

```
Rulează skill-ul weekend-planner din @areas/personal/skills/weekend-planner/SKILL.md
```

### Automat (model îl invocă singur dacă description e bun)

Dacă `description` se potrivește cu mesajul tău, Claude Code îl invocă fără să-l menționezi explicit:

```
User: Mi-e poftă să fac ceva diferit weekend-ul asta, ce zici?
→ Claude Code detectează «weekend» + «idei activități» → invocă weekend-planner
```

### Din scheduled task (Claude Cowork)

Vezi M3.4.

### Din alt skill (orchestrator)

Vezi M3.5.

---

## Anti-patterns frecvente la începători

| Anti-pattern | De ce e rău | Fix |
|---|---|---|
| Description = doar numele | Modelul nu știe când să invoce | Adaugă „Folosește când..." |
| SKILL.md de 500 rânduri | Modelul se pierde, calitate slabă | Sparge în 2-3 skills mai mici (M3.5) |
| Hardcoded data în SKILL.md | Skip-uire schimbări | Pune-l în `references/` |
| Nu menționezi error handling | Skill pică silent în production | Adaugă secțiunea „Erori comune" |
| Numele e `email-thing` | Nu transmite ce face | `email-triage` sau `email-auto-reply` |

---

## Resurse externe oficiale

- [Anthropic — Extend Claude with Skills](https://code.claude.com/docs/en/skills)
- [Anthropic — Agent Skills Overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Anthropic — Skill Authoring Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [Anthropic — Equipping Agents with Skills (blog)](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
