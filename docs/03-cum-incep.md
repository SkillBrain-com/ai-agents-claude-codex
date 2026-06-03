# 03 — Cum încep (Ziua 1 walkthrough)

> **Timpul tău total:** ~45 minute. **La final:** ai primul SKILL.md custom care rulează și un commit pe GitHub.

---

## Pasul 1 — Clonează repo-ul (3 min)

Deschide Terminal-ul (Mac: Spotlight → „Terminal"; Win: Start → „cmd").

```bash
# Navighează unde vrei să trăiască repo-ul (ex: Documents)
cd ~/Documents

# Clonează repo-ul cu un nume care e al TĂU (înlocuiește "my-agents" cu ce vrei)
git clone https://github.com/SkillBrain-com/ai-agents-claude-codex.git my-agents

cd my-agents
```

✅ **Checkpoint:** rulează `ls` și ar trebui să vezi `areas/`, `audits/`, `docs/`, `flows/`, etc.

---

## Pasul 2 — Configurează `.env` (5 min)

```bash
# Copiază template-ul ca .env (acesta NU se urcă în git)
cp .env.example .env

# Deschide .env în VSCode
code .env
```

Adaugă cel puțin:

```
ANTHROPIC_API_KEY=sk-ant-...
```

Cheia o iei de la: [console.anthropic.com](https://console.anthropic.com/) → Settings → API Keys → Create key.

Salvează (`Cmd+S` / `Ctrl+S`) și închide fișierul.

⚠️ **Verifică ÎNAINTE de orice `git push`:**
```bash
git status | grep .env && echo "STOP — nu commitate .env!"
```

---

## Pasul 3 — Deschide proiectul în VSCode (2 min)

```bash
code .
```

VSCode se deschide cu toată structura. La prima rulare îți va sugera 2-3 extensii recomandate (Claude Code, YAML, Markdown) — acceptă-le.

✅ **Checkpoint:** vezi în Explorer (stânga) folderele `areas/`, `audits/`, `docs/`, etc.

---

## Pasul 4 — Rulează skill-ul exemplu (10 min)

În VSCode, deschide [areas/personal/skills/my-first-skill/SKILL.md](../areas/personal/skills/my-first-skill/SKILL.md). Citește-l. E un exemplu funcțional de briefing de dimineață.

Apoi:

1. Apasă `Cmd+Shift+P` (Mac) / `Ctrl+Shift+P` (Win/Linux) — se deschide Command Palette
2. Tastează `Claude Code: Open` și apasă Enter
3. În chat-ul Claude Code, scrie:
   ```
   Rulează skill-ul my-first-skill din @areas/personal/skills/my-first-skill/SKILL.md pe orașul București
   ```
4. Claude Code citește SKILL.md, rulează scriptul `scripts/get_weather.py`, și-ți răspunde

✅ **Checkpoint:** ai primit un briefing cu vremea pentru București.

🆘 **Dacă nu merge:** vezi [05-troubleshooting.md](05-troubleshooting.md) — secțiunea „Claude Code nu invocă skill-ul meu".

---

## Pasul 5 — Duplică și fă-l al tău (15 min)

Acum vine partea interesantă: îți construiești PROPRIUL skill.

### 5.1. Duplică folderul

În VSCode Explorer:
1. Click-dreapta pe `my-first-skill/` → `Copy`
2. Click-dreapta pe `skills/` → `Paste`
3. Redenumește copia (ex: `morning-brief/` sau `weekend-planner/` — alege ce vrei TU să facă)

### 5.2. Editează SKILL.md

Deschide `SKILL.md` din folderul nou și schimbă:

```yaml
---
name: weekend-planner          ← schimbă cu numele tău (kebab-case)
description: Planifică-mi weekend-ul pe baza vremii + 3 idei de activități. Folosește când utilizatorul cere «plan de weekend» sau pornește scheduled vineri seara.
---
```

În corpul SKILL.md, modifică pașii ca să reflecte ce vrei TU să facă (nu briefing-ul implicit). Vezi [04-structura-skill.md](04-structura-skill.md) pentru regulile complete.

### 5.3. Rulează-l

În chat-ul Claude Code:
```
Rulează skill-ul weekend-planner din @areas/personal/skills/weekend-planner/SKILL.md
```

✅ **Checkpoint:** ai propriul skill funcțional, cu numele tău.

---

## Pasul 6 — Primul tău commit (5 min)

```bash
git add areas/personal/skills/weekend-planner/

# Verifică ÎNTÂI ce urci
git status | grep .env && echo "STOP — .env e în staged!"

git commit -m "feat: primul skill custom — weekend-planner"
git push origin main
```

✅ **Checkpoint:** skill-ul tău e pe GitHub. Mergi pe github.com → repo-ul tău → vezi commit-ul.

---

## Pasul 7 — Setează configurarea pentru toate cele 3 modele (5 min — opțional acum)

Recomandat de făcut INAINTE de M1.2:
- Custom instructions identice pe Claude / ChatGPT / Gemini

Template de copy-paste e în [04-structura-skill.md#custom-instructions](04-structura-skill.md#custom-instructions).

---

## Ce ai realizat în ~45 min

- ✅ Ai repo-ul clonat și configurat
- ✅ Ai `.env` cu API key
- ✅ Ai VSCode + Claude Code funcțional
- ✅ Ai rulat skill-ul exemplu
- ✅ Ai propriul skill custom
- ✅ Ai primul commit pe GitHub

**Următorul pas:** continuă cu **M1.1** din [course Notion](https://www.notion.so/) sau treci direct la M2 dacă ai trecut deja prin M1.

---

## Erori comune

| Problemă | Soluție |
|---|---|
| `code: command not found` | În VSCode: `Cmd+Shift+P` → „Shell Command: Install 'code' command in PATH" |
| `git: command not found` | macOS: `xcode-select --install`. Windows: install de la [git-scm.com](https://git-scm.com/) |
| `node: command not found` | Re-instalează Node.js + restart terminal |
| Claude Code „You don't have access" | Verifică abonamentul activ pe claude.com → Settings |
| Skill-ul nu se invocă automat | Schimbă `description` cu verbe de acțiune clare. Vezi M1.0 |

Detalii complete: [05-troubleshooting.md](05-troubleshooting.md).
