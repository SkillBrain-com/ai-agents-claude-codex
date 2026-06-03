# ai-agents-claude-codex

> **Curs SkillBrain** — Automatizează-ți viața și locul de muncă folosind Claude, ChatGPT, Gemini, Claude Cowork și OpenClaw. Fără cod.

[![Course](https://img.shields.io/badge/curs-8%20săptămâni-blue)](docs/01-overview-curs.md)
[![Audience](https://img.shields.io/badge/audience-beginner-green)](docs/02-prerequisite.md)
[![Language](https://img.shields.io/badge/limba-română-yellow)](#)

---

## Ce este acest repo

Acesta e **punctul tău de plecare** pentru cursul *ai-agents-claude-codex*. Conține structura de foldere recomandată + un skill exemplu funcțional pe care îl duplici și-l personalizezi pe parcursul cursului.

La finalul celor 8 săptămâni vei avea în acest repo:
- ✅ **3 automatizări** rulând autonom (1 personală, 1 de la job, 1 integrată)
- ✅ **Hartă de automatizări** cu procesele tale candidate (output Modul 2)
- ✅ **Dashboard unificat** care monitorizează automation-urile (Modul 5)
- ✅ **Skills custom** care lucrează pentru tine zilnic

---

## Quick start (15 minute)

```bash
# 1. Clonează acest repo
git clone https://github.com/SkillBrain-com/ai-agents-claude-codex.git my-ai-agents
cd my-ai-agents

# 2. Copiază template-ul de .env
cp .env.example .env

# 3. Adaugă API keys în .env (cel puțin ANTHROPIC_API_KEY)
#    Generează la: https://console.anthropic.com/settings/keys

# 4. Deschide în VSCode
code .

# 5. Citește documentația de start
open docs/03-cum-incep.md
```

Detalii pas-cu-pas în [docs/03-cum-incep.md](docs/03-cum-incep.md).

---

## Structura repo-ului

```
ai-agents-claude-codex/
│
├── README.md                ← ești aici
├── .env.example             ← template chei API (copiază ca .env, NU commitate)
├── .gitignore
├── .vscode/                 ← settings + extensii recomandate
│
├── docs/                    ← documentație pas-cu-pas
│   ├── 01-overview-curs.md
│   ├── 02-prerequisite.md
│   ├── 03-cum-incep.md     ← citește ASTA prima
│   ├── 04-structura-skill.md
│   ├── 05-troubleshooting.md
│   └── 06-cum-prezint-proiectul.md
│
├── areas/                   ← skills împărțite pe arii de viață
│   ├── personal/            ← skill-uri cu cont Gmail/Notion personal
│   │   └── skills/my-first-skill/  ← exemplu funcțional, START AICI
│   ├── work/                ← skill-uri pentru job (Slack, CRM, etc.)
│   └── shared/              ← orchestratoare care folosesc ambele
│
├── audits/                  ← log-uri și harta de automatizări (output M2)
├── flows/                   ← Task Flows OpenClaw (M4-M5)
├── dashboard/               ← dashboard unificat (M5.4)
├── decisions/               ← decizii personale documentate (M1.4 onwards)
```

Detalii despre fiecare folder în [docs/01-overview-curs.md](docs/01-overview-curs.md).

---

## Mapare modul → foldere modificate

| Modul | Săpt | Foldere unde lucrezi | Deliverable |
|---|---|---|---|
| **M1** Set-up rapid | 1 | `areas/personal/skills/my-first-skill/` | Primul skill custom funcțional |
| **M2** Research | 2-3 | `audits/` | Hartă cu 8+ procese candidate + 3 prioritizate |
| **M3** Concepte tehnice | 3-4 | `areas/*/skills/`, `flows/` | Skill orchestrator + scheduled Cowork task |
| **M4** OpenClaw deep-dive | 5-6 | `flows/`, `areas/*/skills/` | Flux 4 pași + error handling + model routing |
| **M5** Implementare | 7-8 | `flows/`, `dashboard/`, `decisions/` | 3 automation live + dashboard + demo |

---

## Prerequizite

- Mac, Windows sau Linux
- Node.js 24+ ([nodejs.org](https://nodejs.org/))
- VSCode ([code.visualstudio.com](https://code.visualstudio.com/))
- Abonamente AI (~$60/lună combinat):
  - Claude Pro / Max
  - ChatGPT Plus
  - Gemini Advanced (opțional pentru M2-M4)
- Cont GitHub (pentru a-ți face fork la acest repo)

Detalii complete: [docs/02-prerequisite.md](docs/02-prerequisite.md).

---

## Documentație

Toate ghidurile sunt în [`docs/`](docs/):

| Fișier | Pentru ce |
|---|---|
| [01-overview-curs.md](docs/01-overview-curs.md) | Ce înveți, durată, structură pe stadii |
| [02-prerequisite.md](docs/02-prerequisite.md) | Ce instalezi și plătești înainte să începi |
| [03-cum-incep.md](docs/03-cum-incep.md) | Ziua 1: setup walkthrough pas cu pas |
| [04-structura-skill.md](docs/04-structura-skill.md) | Anatomia SKILL.md + exemple |
| [05-troubleshooting.md](docs/05-troubleshooting.md) | Erori comune și soluții |
| [06-cum-prezint-proiectul.md](docs/06-cum-prezint-proiectul.md) | Demo final în comunitate (M5.5) |

---

## Comunitate + suport

- **Întrebări tehnice:** [Issues](../../issues) — folosește template-ul „Help"
- **Sugestii / feedback:** [Discussions](../../discussions)
- **Demo final M5.5:** vezi [docs/06-cum-prezint-proiectul.md](docs/06-cum-prezint-proiectul.md) pentru cum postezi în comunitate
- **Cohorta ta:** discord/Slack link va fi distribuit la start de curs

---

## Securitate — REGULĂ ABSOLUTĂ

⚠️ **NU urca niciodată fișierul `.env` în git.** Conține API keys care, scurse, costă bani reali (cineva îți poate consuma cota Claude / ChatGPT).

`.gitignore` îl exclude deja, dar verifică înainte de fiecare `git push`:

```bash
git status | grep -E '\.env$' && echo "⚠️ STOP — .env e în staged!"
```

Mai multe reguli: [docs/05-troubleshooting.md#securitate](docs/05-troubleshooting.md#securitate).

---

## Licență

MIT — vezi [LICENSE](LICENSE). Conținutul cursului (lecții, video) e proprietate SkillBrain și se distribuie prin platformă, nu prin acest repo.
