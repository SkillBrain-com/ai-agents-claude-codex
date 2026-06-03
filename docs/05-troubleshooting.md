# 05 — Troubleshooting & FAQ

> Erori comune și soluții. Caută pe pagină cu `Ctrl+F` / `Cmd+F`.

---

## Securitate

### `.env` apare în git status

🛑 **OPREȘTE-TE.** Înainte de orice push:

```bash
git reset HEAD .env       # scoate-l din staged
echo ".env" >> .gitignore  # confirmă că e gitignored
git status                 # verifică din nou
```

Dacă l-ai pushat deja:
1. Rotește IMEDIAT API key-urile (le invalidezi pe cele vechi)
2. Generează altele noi în Anthropic Console / OpenAI / Google
3. Actualizează `.env` local
4. `git rm --cached .env` + commit + push

### Ce să faci dacă vezi consum API neașteptat

1. Mergi în [console.anthropic.com → Usage](https://console.anthropic.com/settings/usage)
2. Verifică timestamps + endpoints
3. Dacă vezi calls suspecte → rotește key
4. Setează **monthly limit** pe cont ($50 recomandat la început)

---

## Setup & instalare

### `code: command not found` (Mac)

În VSCode:
1. `Cmd+Shift+P`
2. Tastează `Shell Command: Install 'code' command in PATH`
3. Restart Terminal

### `git: command not found`

| OS | Soluție |
|---|---|
| macOS | `xcode-select --install` (~10 min) |
| Windows | Download de la [git-scm.com](https://git-scm.com/) |
| Linux | `sudo apt install git` / `sudo dnf install git` |

### `node: command not found` după instalare

- Restart Terminal
- Verifică PATH: `echo $PATH | grep node`
- Re-instalează cu installer-ul oficial (NU prin brew dacă e prima oară)

---

## Claude Code (extensia VSCode)

### „You don't have access to this feature"

- Verifică abonamentul activ: [claude.com → Settings → Subscription](https://www.claude.com/settings)
- Sign out + sign in în extensie (Cmd+Shift+P → „Claude Code: Sign Out")
- Dacă persistă: verifică că folosești cont-ul corect (Pro/Max e nominal — nu se share-uiește)

### Claude Code nu invocă skill-ul meu automat

3 cauze posibile, în ordine:

1. **`description` prea vagă** — schimbă cu verbe de acțiune clare („Folosește când..."). Vezi M1.0.
2. **Skill-ul nu e în folder vizibil** — verifică că e sub `skills/`, nu `archived/` sau `_backup/`
3. **`name` invalid** — verifică kebab-case, max 64 chars, fără spații/caractere speciale

Workaround manual:
```
@areas/personal/skills/my-skill/SKILL.md  Rulează skill-ul
```

### Extensia nu apare după instalare

```
Cmd+Shift+P → Developer: Reload Window
```

### Skill-ul rulează dar primesc răspuns generic

- Verifică că corpul SKILL.md are pași clari (nu doar frontmatter)
- Verifică că `references/` și `scripts/` sunt menționate în SKILL.md (Claude le încarcă la cerere)

---

## Claude Cowork (scheduled tasks)

### Scheduled task nu a rulat la ora setată

| Cauză | Soluție |
|---|---|
| Laptop închis la ora setată | Cowork rulează doar când e treaz. Lasă-l pornit sau folosește event triggers |
| Claude Desktop app închis | Trebuie să fie deschis (poate în background) |
| Auth Gmail/Notion expirat | Re-autorizează din Cowork Settings |

### „Could not access Gmail/Notion"

- Re-autorizează: Cowork → Settings → Connectors → Gmail → Reconnect
- Verifică că ai dat scope-urile corecte (read messages + send)

---

## OpenClaw (M4-M5)

### `openclaw: command not found` după `npm install -g openclaw`

```bash
# Verifică unde-l pune npm global
npm config get prefix
# Adaugă acel path la PATH-ul tău

# Mac/Linux
echo 'export PATH="$(npm config get prefix)/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# Windows: adaugă manual în Environment Variables
```

### `openclaw start` pică cu „Cannot find module"

```bash
# Re-instalează clean
npm uninstall -g openclaw
npm cache clean --force
npm install -g openclaw@latest
```

### Skill-ul OpenClaw nu vede API key-ul

`.env` trebuie să fie în **workspace-ul OpenClaw**, nu în repo-ul cursului:

```bash
cd ~/openclaw-agents  # workspace-ul tău OpenClaw
ls .env               # trebuie să existe aici
```

Dacă rulezi din folderul cursului, exportă explicit:
```bash
export ANTHROPIC_API_KEY=$(grep ANTHROPIC_API_KEY .env | cut -d= -f2)
openclaw start
```

### ClawHub skill conține malware?

Vezi M4.2 pentru vetting checklist. Pe scurt:
- Verified badge ✓
- >1000 instalări
- Citit SKILL.md ÎNAINTE de install (pe GitHub)
- Search „{skill-name} security review"

Dacă suspectezi: `openclaw skill remove {nume}` + raportează pe forum.

---

## API costs

### Cum verific cât am cheltuit luna asta

| Provider | Dashboard |
|---|---|
| Anthropic | [console.anthropic.com/settings/usage](https://console.anthropic.com/settings/usage) |
| OpenAI | [platform.openai.com/usage](https://platform.openai.com/usage) |
| Google | [aistudio.google.com](https://aistudio.google.com/) → Usage |

### Cum setez budget limit (RECOMANDAT)

**Anthropic:**
1. Console → Plans → Monthly limit
2. Pune $50 la început, crește dacă e nevoie
3. Alert la 80% e default

**OpenAI:**
1. Settings → Billing → Usage limits
2. Hard limit + soft limit (alert)

### Skill-ul meu costă $5 per rulare — e normal?

Probabil NU. Verifică:
- Trimiți context inutil? (PDF întreg când ai nevoie de 1 pagină)
- Folosești model premium când Haiku/Flash e suficient? (M4.6)
- Loops de retry care nu se opresc?

Quick fix: pune un `print("Tokens used: X")` în logs și optimizează cele mai mari calls.

---

## Git & GitHub

### „Permission denied (publickey)"

```bash
# Verifică-ți SSH key
ssh -T git@github.com

# Dacă nu merge: setează HTTPS în loc de SSH
git remote set-url origin https://github.com/SkillBrain-com/ai-agents-claude-codex.git
```

### Am pushat ceva ce nu trebuia (ex: .env)

1. **Rotește IMMEDIATE credentialele** (key-urile expuse sunt deja compromise)
2. Apoi curăță istoria:
   ```bash
   git rm --cached .env
   echo ".env" >> .gitignore
   git commit -m "fix: remove .env from tracking"
   git push
   ```
3. **Notă:** datele rămân în history. Pentru repos sensibile, contactează SkillBrain admin pentru hard delete.

### „Updates were rejected"

Cineva (sau tu de pe alt laptop) a pushat ceva nou. Pull înainte:

```bash
git pull --rebase origin main
git push
```

---

## VSCode

### Extensiile recomandate nu apar

Click pe `.vscode/extensions.json` și verifică conținutul. VSCode propune extensiile **doar prima dată** când deschizi workspace-ul. Forțează:
- `Cmd+Shift+P` → „Extensions: Show Recommended Extensions"

### Markdown preview nu arată corect

- `Cmd+Shift+V` deschide preview side-by-side
- Pentru diagrame Mermaid, instalează extensia „Markdown Preview Mermaid Support"

---

## Comunitate

### Nu mă pot conecta la Discord/Slack-ul cohortei

Link-ul vine pe email la începutul cursului. Dacă nu l-ai primit:
- Verifică folderul Spam / Promotions
- Contactează **support@skillbrain.com**

### Cum cer ajutor în comunitate

Format care primește răspuns rapid:
1. **Ce încerc să fac** (1 propoziție)
2. **Ce am încercat** (3 bullets)
3. **Eroarea exactă** (screenshot SAU error message)
4. **Versiunile** (`node --version`, `code --version`, OS)

**NU întreba „de ce nu merge?" fără context.** Răspunsul va întârzia.

---

## Nu găsesc răspunsul aici?

- [Issues GitHub](../../issues) — folosește template-ul „Help"
- [Discussions GitHub](../../discussions) — pentru întrebări mai puțin urgente
- Discord cohortă — pentru întrebări live cu colegii
- Email **support@skillbrain.com** — pentru blocaje cu plata / acces
