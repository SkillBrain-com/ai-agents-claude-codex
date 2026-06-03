# 02 — Prerequizite

> **Estimare timp setup total:** ~45 minute. **Cost:** ~$60/lună pentru abonamente.

---

## 1. Hardware

| Item | Minim | Recomandat |
|---|---|---|
| OS | macOS 12+, Windows 10+, Ubuntu 22.04+ | macOS 14+ / Win 11 |
| RAM | 8 GB | 16 GB (pentru OpenClaw + browser + VSCode simultan) |
| Disk liber | 10 GB | 50 GB |
| Internet | Stabil (rulezi API calls frecvent) | — |

⚠️ **Important:** scheduled tasks în Claude Cowork rulează **doar când laptop-ul e treaz și Claude Desktop e deschis**. Dacă închizi laptop-ul peste noapte, task-urile de la 06:00 nu rulează. Vezi M3 pentru workarounds.

---

## 2. Software (gratuit)

### VSCode (5 min)
Download: [code.visualstudio.com](https://code.visualstudio.com/)

Acceptă default-urile. La final, deschide VSCode și verifică în terminal:
```bash
code --version
# 1.95.x sau mai nou
```

### Node.js 24 (5 min — necesar pentru OpenClaw în Modulul 4)
Download: [nodejs.org](https://nodejs.org/)  → versiunea LTS (24.x).

Verifică:
```bash
node --version   # v24.x.x
npm --version    # 11.x sau mai nou
```

### Git (probabil deja instalat)
```bash
git --version    # 2.40+ recomandat
```
Dacă nu îl ai: macOS via `xcode-select --install`, Windows via [git-scm.com](https://git-scm.com/).

### Extensia Claude Code în VSCode (2 min)
1. Deschide VSCode
2. `Cmd+Shift+X` (Mac) sau `Ctrl+Shift+X` (Win/Linux)
3. Caută `Claude Code`
4. Click `Install` pe extensia publicată de Anthropic
5. La prima utilizare îți cere autentificare (browser se deschide automat)

Docs oficiale: [code.claude.com/docs/en/vs-code](https://code.claude.com/docs/en/vs-code)

---

## 3. Abonamente AI (~$60/lună)

| Serviciu | Cost | Necesar pentru | Link |
|---|---|---|---|
| Claude Pro sau Max | $20/lună (Pro) sau $100/lună (Max) | M1-M5 — model principal | [claude.com/plans](https://www.claude.com/plans) |
| ChatGPT Plus | $20/lună | M1 (comparație), M3 (creative), M4 (routing) | [chat.openai.com](https://chat.openai.com/) |
| Gemini Advanced | $20/lună | M1 (comparație), M4 (multimodal + research) | [gemini.google.com](https://gemini.google.com/) |

**Sfat:** dacă ai buget restrâns, mergi numai cu **Claude Pro** ($20) — îți permite să termini complet 80% din curs. ChatGPT și Gemini sunt necesare doar pentru exercițiile de comparație (M1.3, M4.6).

### API keys (necesar de la M4 încolo)

Pentru OpenClaw ai nevoie de cel puțin o cheie API. **Anthropic** e cea mai simplă:

1. Mergi la [console.anthropic.com](https://console.anthropic.com/)
2. Sign up cu același email ca pe Claude Pro
3. Settings → API Keys → Create key
4. Copiază cheia (începe cu `sk-ant-...`)
5. Pune-o în `.env` ca `ANTHROPIC_API_KEY=sk-ant-...`

⚠️ **Cost API separate de abonament!** Tipic: $5-30/lună suplimentar. Setează un budget cap în Anthropic console: Settings → Usage → Set monthly limit ($50 recomandat).

---

## 4. Conturi opționale (utile dar nu blocante)

| Serviciu | Pentru ce | Cost |
|---|---|---|
| **Notion** | Dashboard (M5.4), audit-uri (M2) | Gratuit pentru personal use |
| **WhatsApp Business** | Interfață OpenClaw (M4) | Gratuit, dar test only |
| **GitHub** | Fork-uiește acest repo + commit-uiește progres | Gratuit |
| **Discord** sau **Slack** | Comunitatea cohortei | Gratuit |

---

## 5. Cunoștințe presupuse

✅ **Trebuie să știi:**
- Să folosești file explorer (mută/redenumește fișiere)
- Să copy-paste între aplicații
- Să urmărești instrucțiuni pas cu pas

❌ **NU trebuie să știi:**
- Programare (Python, JavaScript, etc.)
- Linia de comandă (învățăm minimum necesar în M1)
- Cum funcționează LLM-urile intern
- Git/GitHub avansat (basic clone + commit + push, învățăm în M1)

---

## 6. Checklist pre-Day 1

Înainte de prima lecție, asigură-te că:

- [ ] Am VSCode instalat și pornește (`code --version` funcționează)
- [ ] Am Node.js 24 instalat (`node --version`)
- [ ] Am Git instalat
- [ ] Am abonamentul Claude Pro activ (verific la claude.com → Settings → Subscription)
- [ ] Am extensia Claude Code activă în VSCode
- [ ] Am cont GitHub și am clonat repo-ul ăsta
- [ ] Am `.env` creat (copiat din `.env.example`) cu cel puțin `ANTHROPIC_API_KEY`

---

## Next step

Treci la [03-cum-incep.md](03-cum-incep.md) pentru walkthrough-ul de Ziua 1.
