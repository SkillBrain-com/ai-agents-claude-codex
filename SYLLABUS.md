# 🎓 ai-agents-claude-codex — Syllabus complet

<aside>
🎯 <b>Big promise:</b> Construiește și pune în producție 3 automatizări AI end-to-end care îți economisesc minim 5h/săptămână.
</aside>

> **Format:** 5 module · 24 lecții · 622 min conținut + ~50h practică · 8 săptămâni
> **Audiență:** BEGINNER non-tehnic · Limba: română · Stack: VSCode, Claude, ChatGPT, Gemini, Cowork, OpenClaw

---

## 📚 Modulele

| # | Modul | Durată | Lecții | Săptămâni |
|---|---|---|---|---|
| **1** | Set-up rapid: VSCode + conturi AI + primul skill | 107 min | 4 | W1 |
| **2** | Research: harta ta personală de automatizări | 106 min | 4 | W2 |
| **3** | Concepte tehnice: prompting + Cowork + arhitectură multi-agent | 123 min | 5 | W3 |
| **4** | OpenClaw deep-dive: agent runtime + ClawHub skills | 151 min | 6 | W4.1 · W4.2 · W4.3 |
| **5** | Implementare: 3 automatizări + dashboard + demo în comunitate | 135 min | 5 | W5.1 · W5.2 |

---

## 📆 Distribuirea pe săptămâni

Fiecare săptămână are **o singură temă livrabilă** — un artefact concret pe care mentorul îl poate inspecta în repo, în Notion sau în comunitate. Nu sunt checklist-uri abstracte, sunt **proiecte cu output verificabil**.

| Săpt | Cod | Tema săptămânii — artefactul livrat | Unde o vede mentorul |
|---|---|---|---|
| 1 | **W1** | Repo personal pe GitHub cu **primul skill custom** invocat cu success | `github.com/{tu}/...` — commit + SKILL.md valid + demo în live call |
| 2 | **W2** | **Harta personală de automatizări** (≥8 procese audit-uite, top 3 prioritizate) | `audits/{data}_automation-map.md` în repo + post peer-review în Discord |
| 3 | **W3** | **Scheduled Cowork task** rulând 3 zile consecutive + **un orchestrator** de 2 skills în secvență | Screenshot Cowork sidebar cu 3 successful runs + skill orchestrator în repo |
| 4 | **W4.1** | Primul **Task Flow OpenClaw cu 4 pași** end-to-end (classify → fetch → reason → reply) | Live demo `openclaw tasks flow show` cu 4 steps validi + SKILL.md în `flows/` |
| 5 | **W4.2** | **Flow refactored cu retry+fallback** + **skill care procesează un PDF de 100+ pagini** | Inspecție SKILL.md cu secțiunea `ERROR HANDLING` + demo PDF real |
| 6 | **W4.3** | **Capstone OpenClaw integrat** (2 connectors ClawHub + Claude long-doc + model routing + error handling) prezentat live în 3 min | Capstone show & tell — mentor + cohorta scorează pe rubric |
| 7 | **W5.1** | **Automatizarea #1 LIVE** — minim 3 rulări successive verificate + commitment public pe #2 și #3 | Logs OpenClaw + post Discord cu plan-ul celorlalte 2 |
| 8 | **W5.2** | **3 automatizări live + dashboard + screencast 2 min** + iterație post-feedback | Dashboard public (Notion/Sheet) + Loom link + thread cu ≥3 feedback-uri și 1 revision |

> **Principiul de evaluare:** la finalul fiecărei săptămâni, dacă mentorul **nu poate să dea click pe artefact** și să-l vadă funcționând, săptămâna nu e închisă. Fără excepții.

---

## 🕒 Ritmul săptămânal

```
Săpt:     W1     W2     W3    W4.1   W4.2   W4.3   W5.1   W5.2
Effort:   5h     6h     7h     5h     6h     6h     7h     8h
          ↑              ↑                                  ↑
       easy           peak                              peak
       ramp-up        intelectual                       execution
```

| Eveniment live | Săptămână | Durată | Rol |
|---|---|---|---|
| 🎬 Kickoff call | W1 (Luni) | 60 min | Demo stack live + buddy pairing |
| 🗺️ Map review | W2 (Sâmbătă) | 60 min | Peer review pe harta de automatizări |
| 🔧 OpenClaw clinic | W4.2 (Miercuri seara) | 90 min | Debug session — toți aduc flow-uri stuck |
| 🏆 Capstone show & tell | W4.3 (Sâmbătă) | 90 min | Fiecare prezintă capstone-ul în 3 min |
| 🛠️ Build standup | W5.1 (Miercuri) | 60 min | 30 sec/persoană: progres #1, blocaje #2 |
| 🎤 Demo day | W5.2 (Vineri seara) | 120 min | Prezentări 2-min + feedback + certs |
| ☕ Office hours | W1 → W5.2 | 60 min/săpt | Drop-in async pe Discord |

---

## 🗓️ Modul 1 — W1: Set-up rapid

<aside>
📋 Pornește de la zero — instalează tooling-ul, configurează cele 3 modele frontier, construiește structura de skill pe care vei adăuga TOT ce urmează.
</aside>

> ### 🏁 Tema W1 — artefact livrabil
> **Repo personal pe GitHub cu primul skill custom invocat cu success de Claude Code în VSCode.**
>
> **Cum verifică mentorul:**
> 1. Open `github.com/{cursant}/ai-agents-claude-codex` — există ca fork
> 2. Există commit cu `areas/personal/skills/{nume-skill-al-cursantului}/SKILL.md`
> 3. SKILL.md trece linter-ul automat (frontmatter valid: name kebab-case ≤64ch, description ≤1024ch)
> 4. În live call, cursantul rulează skill-ul în Claude Code și output-ul apare în ≤30 sec
>
> **DoD (Definition of Done):** mentorul poate executa skill-ul pe repo-ul cursantului fără config suplimentar.

### Lecții

- **L1.1 — Construiește prima ta structură de skill în VSCode** (40 min · APPLY)

  **Obiectiv:** Creează un skill nou de la zero cu name kebab-case ≤64 ch + description cu verbe de acțiune, și invocă-l cu success
  **Slug:** `vscode-claude-code-skill-structure`

  ### Chapters
  - HOOK — De ce ai nevoie de VSCode dacă nu programezi
  - CORE — Anatomia unui skill: SKILL.md + references/ + scripts/
  - PRACTICE — Duplică starter-template și rulează first skill
  - TRANSFER — Aceeași structură = OpenClaw skills, Claude Code skills, MCP skills

- **L1.2 — Configurează mediul: conturi, abonamente, custom instructions** (22 min · APPLY)

  **Obiectiv:** Activează cele 3 conturi (Claude Pro / ChatGPT Plus / Gemini Advanced) și setează custom instructions identice pe toate
  **Slug:** `configureaza-mediul`

  ### Chapters
  - HOOK — De ce 3 modele, nu unul
  - CORE — Custom instructions ca prim system prompt
  - PRACTICE — Setează profilul tău pe toate 3 platforme
  - TRANSFER — Custom instructions vs. Claude Projects vs. Custom GPTs

- **L1.3 — Activează Claude, ChatGPT, Gemini — primul prompt pe toate 3** (25 min · APPLY)

  **Obiectiv:** Rulează același prompt pe Claude / ChatGPT / Gemini și catalogă diferențele într-un mini-tabel
  **Slug:** `activeaza-claude-chatgpt-gemini`

  ### Chapters
  - HOOK — Același prompt, 3 răspunsuri diferite — care e bun?
  - CORE — Cele 6 strength-zones (Claude=long-doc, Gemini=multimodal, ChatGPT=creative)
  - PRACTICE — Rulează 3 task-uri reale și marchează câștigătorul
  - TRANSFER — Routing principle pentru cursul tot: ce model pentru ce task

- **L1.4 — Verifică tot stack-ul cu un mini-task end-to-end** (20 min · APPLY)

  **Obiectiv:** Construiește un pipeline simplu: ChatGPT cercetează → Claude sintetizează → tu salvezi într-un Markdown în VSCode
  **Slug:** `verifica-stack-end-to-end`

  ### Chapters
  - HOOK — Cele mai multe automatizări sunt: research → sinteză → output
  - PRACTICE — Run 3-step manual pipeline cu task real
  - TRANSFER — Asta e schema oricărei automatizări viitoare

---

## 🗓️ Modul 2 — W2: Research

<aside>
📋 Pune AI-ul să te auditeze. Doi agenți de audit te ghidează prin viața personală și job pentru a identifica procesele care merită automatizate.
</aside>

> ### 🏁 Tema W2 — artefact livrabil
> **Harta personală de automatizări** cu minim 8 procese audit-uite și top 3 prioritizate prin impact × fezabilitate, în repo-ul cursantului.
>
> **Cum verifică mentorul:**
> 1. Există fișier `audits/{YYYY-MM-DD}_automation-map.md` în repo
> 2. Fișierul conține ≥8 procese, fiecare cu scor impact (1-5) și fezabilitate (1-5)
> 3. Exact 3 procese marcate explicit ca „Top 3" în zona high-impact × high-feasibility
> 4. Pentru fiecare top-3: o frază cu stack tehnic propus (ex: „Cowork scheduled + Gmail integration")
> 5. Cursantul a postat un thread în Discord/Slack cohortă cu harta + 3 cereri specifice de feedback
>
> **DoD:** mentorul poate spune după 2 min de citit: „știu exact ce vrea acest cursant să construiască în M5".

### Lecții

- **L2.1 — Diferențiază procesele automatizabile de cele non-automatizabile** (20 min · UNDERSTAND)

  **Obiectiv:** Aplică filtrul high-volume + rule-based + clear trigger + predictable output
  **Slug:** `automatizabil-vs-non-automatizabil`

  ### Chapters
  - HOOK — Studiu de caz: ce a AUTOMATIZAT greșit cineva
  - CORE — Cele 4 criterii + 2 anti-criterii
  - PRACTICE — Clasifică 10 procese din viața ta
  - TRANSFER — Același filtru, contexte diferite

- **L2.2 — Agentul de audit pe viața ta personală** (28 min · APPLY)

  **Obiectiv:** Rulează agentul de audit-personal pe ultimele 7 zile și obține minim 5 procese candidate
  **Slug:** `audit-viata-personala`

  ### Chapters
  - HOOK — AI-ul vede pattern-uri pe care tu nu le vezi
  - CORE — Cum funcționează agentul de audit (structura prompt)
  - PRACTICE — Loghează 7 zile + rulează agentul
  - TRANSFER — De la audit la decizie

- **L2.3 — Agentul de audit pe procesele de la job** (28 min · APPLY)

  **Obiectiv:** Identifică minim 5 procese candidate de la job marcate cu high-volume/rule-based/error-prone/bottleneck
  **Slug:** `audit-job`

  ### Chapters
  - HOOK — Procesele job-ului sunt diferite de cele personale
  - CORE — 4 etichete de prioritizare
  - PRACTICE — Loghează 1 săpt de la job + rulează audit
  - TRANSFER — Sensibilitate la confidențialitate

- **L2.4 — Construiește harta ta personalizată de automatizări** (30 min · APPLY)

  **Obiectiv:** Sintetizează cele 2 liste într-o hartă cu ≥8 procese + 3 prioritizate prin impact × fezabilitate
  **Slug:** `harta-automatizari`

  ### Chapters
  - HOOK — De ce ai nevoie de hartă, nu doar de listă
  - CORE — Scorul impact × fezabilitate
  - PRACTICE — Sintetizează harta în Notion / Markdown
  - TRANSFER — Harta = input pentru Modulul 5

---

## 🗓️ Modul 3 — W3: Concepte tehnice

<aside>
📋 Înveți tehnicile care fac modelul fiabil: rol/context/memorie, few-shot, chain-of-thought, scheduled vs event triggers, orchestrator.
</aside>

> ### 🏁 Tema W3 — artefact livrabil
> **Un scheduled Claude Cowork task care a rulat 3 zile consecutive** + **un orchestrator** care apelează 2 skills în secvență.
>
> **Cum verifică mentorul:**
> 1. Screenshot Cowork sidebar cu task-ul activ + minim 3 entries în „Past runs" cu Status: Success
> 2. Repo conține skill orchestrator (ex: `areas/personal/skills/research-then-synthesize/SKILL.md`) care apelează explicit alte 2 skills în corpul SKILL.md
> 3. Demo live: cursantul invocă orchestrator-ul, vede output-ul agregat
> 4. Prompt-urile interne (mai ales pentru audit/research) conțin minim 3 `<example>` tags (few-shot) — dovadă de aplicare L3.2
>
> **DoD:** orchestrator-ul rulează fără cursant prezent + scheduled task-ul a livrat 3 output-uri în 3 zile.

### Lecții

- **L3.1 — Prompting: roluri, context, memorie** (22 min · UNDERSTAND)

  **Obiectiv:** Explică cum system role + context window + memorie afectează output-ul
  **Slug:** `prompting-rol-context`

  ### Chapters
  - HOOK — De ce același prompt produce răspunsuri diferite
  - CORE — Stack-ul prompt: system / context / user / examples
  - PRACTICE — Rescrie 1 prompt cu rol explicit
  - TRANSFER — Context budget = resursă finită

- **L3.2 — Few-shot + chain-of-thought pe task real** (28 min · APPLY)

  **Obiectiv:** Rescrie un prompt nestructurat ca prompt few-shot cu 3 exemple și măsoară consistența
  **Slug:** `few-shot-cot`

  ### Chapters
  - HOOK — Câștigul de 30% accuracy cu 3 exemple
  - CORE — `<example>` tags + CoT prompt
  - PRACTICE — Aplică pe task de audit
  - TRANSFER — Few-shot la orice prompt repetitiv

- **L3.3 — Cowork triggers — modelul mental** (20 min · UNDERSTAND)

  **Obiectiv:** Diferențiază scheduled vs event-driven triggers și alege corect pe scenariu
  **Slug:** `cowork-modelul-mental`

  ### Chapters
  - HOOK — De ce briefing-ul tău nu trebuie să-l pornești tu
  - CORE — Scheduled vs Event-driven
  - PRACTICE — Clasifică 5 idei propuse
  - TRANSFER — Pattern-ul se aplică la orice unealtă cu triggers

- **L3.4 — Construiește prima automatizare cu Cowork trigger** (28 min · APPLY)

  **Obiectiv:** Configurează 1 scheduled task (daily 07:30) care rulează 3 zile fără intervenție
  **Slug:** `prima-automatizare-cowork`

  ### Chapters
  - HOOK — Briefing de dimineață — primul tău angajat AI
  - CORE — Cum creezi un scheduled task pas-cu-pas
  - PRACTICE — Construiește + verifică 3 zile
  - TRANSFER — Event-driven următorul pas

- **L3.5 — Arhitectură: Skills, Orchestrator, fluxuri multi-agent** (25 min · APPLY)

  **Obiectiv:** Construiește un mini-orchestrator care apelează 2 skills în secvență
  **Slug:** `arhitectura-skills-orchestrator`

  ### Chapters
  - HOOK — De ce un skill mare e mai fragil decât 3 mici
  - CORE — Team-lead + teammates pattern
  - PRACTICE — Construiește orchestrator cu 2 skills
  - TRANSFER — Pattern-ul scalează: 2 skills → 20 skills

---

## 🗓️ Modul 4 — W4.1 · W4.2 · W4.3: OpenClaw deep-dive

<aside>
📋 Pui agentul tău local în producție: instalare, anatomie, flow multi-pas, connectors, error handling, model routing. Distribuit pe 3 săptămâni pentru a permite consolidarea fiecărui pattern înainte de M5.
</aside>

### W4.1 — Foundations

> ### 🏁 Tema W4.1 — artefact livrabil
> **Primul Task Flow OpenClaw cu 4 pași end-to-end** (classify → fetch → reason → reply), cu state tracking inspectabil prin `openclaw tasks flow show`.
>
> **Cum verifică mentorul:**
> 1. Cursantul rulează în live call comanda `openclaw tasks flow show {flow_id}` și apar 4 steps cu Status: Success
> 2. Repo conține `flows/{nume}/SKILL.md` cu cele 4 steps clari + tipurile de input/output per step
> 3. Cel puțin 1 connector instalat din ClawHub (vetted — verified badge sau >1000 instalări)
> 4. Flow-ul rulează pe input real (nu mock data)
>
> **DoD:** mentorul poate trimite un input nou și obține output corect prin 4 steps.

#### Lecții W4.1

- **L4.1 — Activează OpenClaw: cont, plan, prim test** (18 min · APPLY)

  **Obiectiv:** Instalează OpenClaw local + API key + primul mesaj de test
  **Slug:** `openclaw-setup`

  ### Chapters
  - HOOK — De ce OpenClaw schimbă regulile pentru non-developeri
  - CORE — Cerințe: Node 24 + API key + cont
  - PRACTICE — Install + first message
  - TRANSFER — Local-first vs cloud trade-off

- **L4.2 — Anatomia OpenClaw: Skills, Tools, ClawHub** (25 min · UNDERSTAND)

  **Obiectiv:** Explică cum Skills + Tools + ClawHub formează un agent autonom
  **Slug:** `openclaw-anatomy`

  ### Chapters
  - HOOK — De ce OpenClaw e diferit de ChatGPT
  - CORE — Skills + Tools + ClawHub marketplace
  - PRACTICE — Instalează 2 skills din ClawHub
  - TRANSFER — Marketplace economics + risk

- **L4.3 — Construiește un flux multi-pas end-to-end** (30 min · APPLY)

  **Obiectiv:** Task Flow cu 4 pași: classify → fetch → reason → reply
  **Slug:** `flux-multi-pas`

  ### Chapters
  - HOOK — De ce un step = o acțiune
  - CORE — Task Flow + state tracking
  - PRACTICE — Build 4-step flow real
  - TRANSFER — Pattern reproducibil pentru orice domeniu

---

### W4.2 — Deepen

> ### 🏁 Tema W4.2 — artefact livrabil
> **Flow-ul din W4.1 refactored cu retry+fallback complet** (3-state error model) + **un skill nou care procesează un PDF de 100+ pagini** cu Claude long-doc reasoning.
>
> **Cum verifică mentorul:**
> 1. SKILL.md al flow-ului refactored conține section `ERROR HANDLING` pe FIECARE step cu retry strategy + fallback explicit
> 2. Mentorul forțează deliberat o eroare (revoke API key temporar) și verifică că flow-ul intră în fallback fără să crash-uiască
> 3. Există skill nou (`contract-reviewer`, `paper-summarizer`, sau similar) care primește un PDF real ≥30 pagini și returnează analiza structurată
> 4. Analiza conține minim 3 secțiuni distincte (ex: parties, risk_clauses, recommendation)
>
> **DoD:** flow-ul supraviețuiește la o defecțiune simulată și skill-ul de long-doc rulează pe un document de minim 30 pagini.

#### Lecții W4.2

- **L4.4 — Conectori avansați + gestiune de erori** (28 min · APPLY)

  **Obiectiv:** Adaugă retry × 2 + fallback explicit la fiecare connector
  **Slug:** `connectors-error-handling`

  ### Chapters
  - HOOK — Primul 429 — și ce faci cu el
  - CORE — 3-state model: success / retry / hard-fail
  - PRACTICE — Implementează retry + fallback
  - TRANSFER — Patternul = software engineering 101

- **L4.5 — OpenClaw + Claude: raționament + documente lungi** (25 min · APPLY)

  **Obiectiv:** Construiește un skill care procesează un PDF de 100+ pagini
  **Slug:** `openclaw-claude-long-docs`

  ### Chapters
  - HOOK — 200k tokens = ~500 pagini
  - CORE — Cum trimiți long-doc la Claude prin OpenClaw
  - PRACTICE — Sumarizează un PDF real
  - TRANSFER — Pattern pentru contract review, paper review etc.

---

### W4.3 — Integration (Capstone)

> ### 🏁 Tema W4.3 — artefact livrabil
> **Capstone OpenClaw integrat** — 1 flow care combină **2 connectors ClawHub + Claude long-doc + model routing intenționat + retry/fallback complet** — prezentat live în 3 min show-and-tell.
>
> **Cum verifică mentorul:**
> 1. Cursantul prezintă live (3 min) capstone-ul cu input real, mentor + cohorta urmăresc execuția pas cu pas
> 2. Capstone-ul satisface rubric-ul de 5 puncte:
>    - ✅ 2 connectors ClawHub diferiți
>    - ✅ minim un step cu Claude pe long-doc / reasoning serios
>    - ✅ minim 2 modele AI diferite în flow (routing intenționat, ex: Gemini pentru research, Claude pentru sinteză)
>    - ✅ retry + fallback explicit pe minim un step critic
>    - ✅ state tracking funcțional (inspectabil prin CLI)
> 3. Mentorul + cohorta scorează 0-5 pe fiecare punct → minim 4/5 pentru passing
>
> **DoD:** capstone-ul rulează live, satisface rubric-ul de 5 puncte, și e fork-able (poate fi rulat de altcineva pe propriul cont).

#### Lecții W4.3

- **L4.6 — OpenClaw + ChatGPT + Gemini: ce model unde** (25 min · APPLY)

  **Obiectiv:** Implementează routing-ul în 1 flow real (3 modele, 1 flow)
  **Slug:** `model-routing`

  ### Chapters
  - HOOK — De ce un singur model = costuri inutile
  - CORE — Routing matrix: task → model
  - PRACTICE — Implementează routing în flow
  - TRANSFER — Routing principle în viața ta

**+ Capstone project (5-6h build)** — scenarii sugerate:
1. **Email inbox triage** — classify + auto-reply + log Notion
2. **Meeting recap** — transcript → summary + action items → Slack
3. **Content radar** — search 3 surse → sumarizare → propune draft post

---

## 🗓️ Modul 5 — W5.1 · W5.2: Implementare

<aside>
📋 Construiești 3 automatizări reale din harta ta, le integrezi, le pui sub dashboard și prezinți public proiectul final.
</aside>

### W5.1 — Sprint 1: Production build

> ### 🏁 Tema W5.1 — artefact livrabil
> **Automatizarea #1 LIVE** cu minim 3 rulări successive verificate + **commitment public** pe celelalte 2 (cu date estimate de finalizare).
>
> **Cum verifică mentorul:**
> 1. Logs OpenClaw (`openclaw tasks flow show`) arată ≥3 successful runs ale #1 în ultimele 3 zile
> 2. Sau (echivalent pentru Cowork scheduled): Cowork sidebar arată 3+ runs cu Status: Success
> 3. Cursantul a postat în Discord/Slack cohortă commitment-ul public cu format-ul:
>    - Automation #1 (LIVE) — nume + descriere scurtă + impact estimat
>    - Automation #2 (planned) — nume + dată estimată finalizare
>    - Automation #3 (planned) — nume + dată estimată finalizare
> 4. Impact estimat al #1 e cuantificat (ex: „economisesc 1.5h/săpt prin {ce}")
>
> **DoD:** #1 rulează autonom fără cursant și echipa cohortei știe ce vine în W5.2.

#### Lecții W5.1

- **L5.1 — Selectezi primele 3 automatizări de construit** (20 min · APPLY)

  **Obiectiv:** Alege 3 automatizări cu cel mai bun raport impact×fezabilitate din hartă
  **Slug:** `selecteaza-primele-3`

  ### Chapters
  - HOOK — De ce 3 (nu 1, nu 10)
  - CORE — Criteriile de selecție finală
  - PRACTICE — Selectează și commit-uie în comunitate
  - TRANSFER — Aceeași logică la deciziile tale viitoare

- **L5.2 — Construiește automatizarea #1 cu tot stack-ul** (30 min · APPLY)

  **Obiectiv:** Pune în producție automatizarea #1 (skill + Cowork trigger + OpenClaw flow + 1 connector ClawHub)
  **Slug:** `build-automatizare-1`

  ### Chapters
  - HOOK — Prima ta automatizare reală
  - CORE — End-to-end build checklist
  - PRACTICE — Build complet + test live
  - TRANSFER — Build-pattern reusable

---

### W5.2 — Sprint 2: Integrare + dashboard + demo

> ### 🏁 Tema W5.2 — artefact livrabil
> **3 automatizări LIVE** + **dashboard unificat** (Notion sau echivalent) + **screencast 2 min** publicat în comunitate + **1 round de iterație** vizibilă post-feedback.
>
> **Cum verifică mentorul:**
> 1. Dashboard accesibil prin link public (Notion shared, Sheet public, sau pagina hostată)
> 2. Pe dashboard: 3 rânduri/widget-uri cu Status: Healthy + Last Run recent + Impact h/wk cuantificat
> 3. Screencast Loom (sau YouTube/Vimeo) ≤4 min care arată cele 3 automation rulând live
> 4. Thread în comunitate cu post-ul demo + minim 3 feedback-uri primite + 1 comment de la cursant cu „am aplicat X, Y, Z" + commit cu iterația
> 5. Cele 3 automation sunt **integrate** (output #1 → input #2 sau shared state) — nu 3 silos
>
> **DoD:** dashboard-ul rulează autonom + există dovada feedback → iterație vizibilă.

#### Lecții W5.2

- **L5.3 — Construiește #2 și integreaz-o cu #1** (30 min · APPLY)

  **Obiectiv:** Output-ul #1 devine input-ul #2 (sau share state)
  **Slug:** `build-automatizare-2-integrat`

  ### Chapters
  - HOOK — Integrarea = exponențială, nu liniară
  - CORE — Patterns de integrare (chained / shared-state)
  - PRACTICE — Build #2 + integrare
  - TRANSFER — Composability principle

- **L5.4 — Construiește #3 + dashboard unificat** (30 min · APPLY)

  **Obiectiv:** 3 automatizări sub un dashboard cu status live + ultima rulare + erori cumulate
  **Slug:** `build-3-dashboard`

  ### Chapters
  - HOOK — Fără dashboard, automatizările sunt invizibile
  - CORE — Metrice esențiale + alerting
  - PRACTICE — Build dashboard + alerting
  - TRANSFER — Dashboards la orice sistem critic

- **L5.5 — Pregătești și prezinți proiectul final în comunitate** (25 min · APPLY)

  **Obiectiv:** Screencast 2 min + prezentare live cu 1 round de feedback
  **Slug:** `demo-final`

  ### Chapters
  - HOOK — Demo > documentație
  - CORE — Structura prezentării (problem → audit → 3 automations → impact)
  - PRACTICE — Înregistrează + prezintă + iterează
  - TRANSFER — Identitate nouă: constructor de agenți

---

## 🏆 Certificare

<aside>
🎓 Cursantul primește certificat „<b>Constructor de agenți AI — Claude & Codex</b>" emis de SkillBrain la îndeplinirea simultană a:
<br><br>
✅ Toate 8 teme săptămânale livrate (W1 → W5.2) cu DoD validat de mentor<br>
✅ Capstone OpenClaw (W4.3) cu scor ≥4/5 pe rubric<br>
✅ 3 automation LIVE și integrate la finalul W5.2<br>
✅ Demo prezentat public + minim 1 round de iterație post-feedback
</aside>

> **Notă pentru mentori:** dacă o temă săptămânală nu îndeplinește DoD-ul, **nu o marca completed**. Solicitați cursantului să închidă tema în săptămâna următoare (cu impact pe pacing-ul restului — dar mai bine recovery decât „skip"). Capstone W4.3 sub 4/5 = obligatoriu refacere înainte de M5.

---

## 📎 Referințe

- [README.md](README.md) — overview repo
- [docs/01-overview-curs.md](docs/01-overview-curs.md) — context pedagogic
- [docs/02-prerequisite.md](docs/02-prerequisite.md) — ce instalezi și plătești
- [docs/03-cum-incep.md](docs/03-cum-incep.md) — Day 1 walkthrough
- [docs/04-structura-skill.md](docs/04-structura-skill.md) — anatomia SKILL.md
- [docs/05-troubleshooting.md](docs/05-troubleshooting.md) — erori comune
- [docs/06-cum-prezint-proiectul.md](docs/06-cum-prezint-proiectul.md) — demo final
