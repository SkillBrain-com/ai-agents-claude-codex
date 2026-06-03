# 07 — Teme săptămânale

> Fiecare săptămână are o **temă** care comprimă obiectivul săptămânii într-un titlu scanabil. Folosește-le în comunicările cu cohorta (email, slide, calendar) și ca anchor pentru tracking-ul progresului.

**Naming convention:** `W{M}.{săpt-din-modul}` — ex: `W4.2` = a doua săptămână din Modulul 4. Săptămânile cu modul scurt sunt doar `W1`, `W2`, `W3`.

---

## Overview

| Cod | Săpt | Tema | Modul |
|---|---|---|---|
| **W1**   | 1 | Setup mediu și primul skill custom              | M1 — Setup rapid |
| **W2**   | 2 | Audit procese și hartă de automatizări          | M2 — Research |
| **W3**   | 3 | Prompting avansat și orchestrare multi-agent    | M3 — Concepte tehnice |
| **W4.1** | 4 | OpenClaw: setup local și primul Task Flow       | M4 — Foundations |
| **W4.2** | 5 | Connectors, error handling, long-doc reasoning  | M4 — Deepen |
| **W4.3** | 6 | Capstone OpenClaw integrat                      | M4 — Integration |
| **W5.1** | 7 | Production build — automatizarea #1             | M5 — Sprint 1 |
| **W5.2** | 8 | Integrare, dashboard și demo final              | M5 — Sprint 2 |

---

## W1 — Setup mediu și primul skill custom

**Modul:** M1 — Setup rapid
**Lecții:** L1.0, L1.1, L1.2, L1.3 (107 min)
**Effort estimat:** ~5h

**Outcome măsurabil:**
- VSCode + extensia Claude Code funcționale
- Cele 3 conturi AI (Claude / ChatGPT / Gemini) cu custom instructions identice
- Primul SKILL.md custom invocat cu success

**Deliverable:** repo personal clonat, `.env` configurat, primul skill custom commit-uit pe GitHub.

**Activități cheie:**
- Day 1 walkthrough complet (vezi [03-cum-incep.md](03-cum-incep.md))
- Test stack pe 3 task-uri identice (sumarizare / email / factual cu sursă)
- Mini-pipeline manual research → sinteză → salvare

---

## W2 — Audit procese și hartă de automatizări

**Modul:** M2 — Research
**Lecții:** L2.1, L2.2, L2.3, L2.4 (106 min)
**Effort estimat:** ~6h

**Outcome măsurabil:**
- Log de timp 7 zile complet (personal + job)
- Minim 8 procese candidate identificate de agenții de audit
- 3 procese prioritizate prin matricea impact × fezabilitate

**Deliverable:** [audits/{data}_automation-map.md](../audits/) — harta finală care devine input pentru M5.

**Activități cheie:**
- Logging zilnic 5-7 min (paralel cu lecțiile)
- Rularea agenților de audit (personal + job) cu prompt-urile oficiale
- Peer review pe harta finală (sesiune live săpt 2, sâmbătă)

---

## W3 — Prompting avansat și orchestrare multi-agent

**Modul:** M3 — Concepte tehnice
**Lecții:** L3.1, L3.2, L3.3, L3.4, L3.5 (123 min)
**Effort estimat:** ~7h

**Outcome măsurabil:**
- Înțelegere prompt stack (role / context / memory / few-shot)
- Diferențiere scheduled vs event-driven triggers
- Pattern orchestrator + 2 sub-skills implementat

**Deliverable:**
- Scheduled Claude Cowork task care rulează 3 zile fără intervenție manuală
- Mini-orchestrator cu 2 skills în secvență

**Activități cheie:**
- Rescriere prompt nestructurat ca few-shot cu 3 exemple în `<example>` tags
- Setup primul scheduled task (briefing de dimineață 07:30)
- Build orchestrator research-then-synthesize

---

## W4.1 — OpenClaw: setup local și primul Task Flow

**Modul:** M4 — Foundations
**Lecții:** L4.1, L4.2, L4.3 (73 min)
**Effort estimat:** ~5h

**Outcome măsurabil:**
- OpenClaw instalat local (Node 24, gateway pornit, prim chat OK)
- Înțelegere arhitectură: Skills + Tools + ClawHub
- Primul Task Flow cu 4 steps (classify → fetch → reason → reply)

**Deliverable:** flow OpenClaw funcțional în `flows/{nume}/` cu state tracking verificabil prin `openclaw tasks flow show`.

**Activități cheie:**
- Install + autentificare API
- Vetting + install 2 skills din ClawHub (verified)
- Build flow 4 pași cu inputs reali

---

## W4.2 — Connectors, error handling, long-doc reasoning

**Modul:** M4 — Deepen
**Lecții:** L4.4, L4.5 (53 min)
**Effort estimat:** ~6h

**Outcome măsurabil:**
- Pattern retry × N + backoff exponențial + fallback implementat
- 3-state error model (success / retry-able / hard-fail) aplicat
- Skill care procesează un PDF de 100+ pagini cu Claude

**Deliverable:**
- Refactor flow-ul din W4.1 cu error handling complet pe fiecare step
- Skill contract-reviewer (sau echivalent) care rulează pe document real

**Activități cheie:**
- Test deliberat cu eroare simulată (429) — verifică retry-ul
- Optimizare context budget pentru long-doc (~70k tokens efectivi din 200k)
- Mid-build clinic (sesiune live săpt 5, miercuri seara)

---

## W4.3 — Capstone OpenClaw integrat

**Modul:** M4 — Integration
**Lecții:** L4.6 (25 min) + capstone project
**Effort estimat:** ~6h

**Outcome măsurabil:**
- Implementare model routing (3 modele într-un singur flow)
- Capstone OpenClaw care combină tot ce s-a învățat în M4

**Deliverable:** capstone — 1 flow OpenClaw care:
1. Folosește **2 connectors ClawHub** (vetted)
2. Are **minim un step cu Claude pe long-doc / reasoning**
3. Implementează **model routing intenționat** (Claude / Gemini / ChatGPT per step)
4. Are **retry + fallback** pe minim un step critic
5. Salvează **state** verificabil

**Scenarii capstone (alege unul):**
- Email inbox triage (classify + auto-reply + log Notion)
- Meeting recap (transcript → summary + action items → Slack)
- Content radar (search 3 surse → sumarizare → propune draft)

**Activitate cheie:** capstone show & tell — fiecare prezintă 3 min (repetiție pentru demo M5.5).

---

## W5.1 — Production build — automatizarea #1

**Modul:** M5 — Sprint 1
**Lecții:** L5.1, L5.2 (50 min)
**Effort estimat:** ~7h

**Outcome măsurabil:**
- Selecție finală 3 automation din hartă (commit public în comunitate)
- Automatizarea #1 LIVE — rulează autonom cu input-uri reale

**Deliverable:**
- Public commitment cu cele 3 automation + dată estimată de finalizare
- Automation #1 în production (spec → build → verify → deploy complet)
- Spec ready pentru #2

**Activități cheie:**
- Re-evaluare hartă M2 cu lentila OpenClaw (ce skills ClawHub acoperă deja 80%?)
- Build sprint focusat pe #1 (4 etape: spec, build, verify, deploy)
- Build standup midweek (sesiune live săpt 7, miercuri)

---

## W5.2 — Integrare, dashboard și demo final

**Modul:** M5 — Sprint 2
**Lecții:** L5.3, L5.4, L5.5 (85 min)
**Effort estimat:** ~8h

**Outcome măsurabil:**
- Automatizarea #2 LIVE și integrată cu #1 (chain / shared state / event)
- Automatizarea #3 LIVE
- Dashboard unificat în Notion cu status + ultima rulare + erori + impact
- Screencast 2 min de demo prezentat public

**Deliverable:**
- 3 automation rulând autonom
- Dashboard live cu alerting setat
- Screencast publicat în comunitate cu 3 cereri specifice de feedback
- 1 round de iterație post-feedback

**Activități cheie:**
- Integration pattern: alegere între chain / shared state / event queue
- Build dashboard Notion + script de status push (vezi [dashboard/](../dashboard/))
- Demo day live (sesiune săpt 8, vineri seara)

---

## Cum folosești temele

### În comunicarea cu cohorta

**Email săptămânal — subject:**
```
Săpt {N}: {tema}
```

Exemplu: `Săpt 3: Prompting avansat și orchestrare multi-agent`

### Pe slide-ul de kickoff al fiecărui live call

Slide #1 = `{cod} — {tema}` + outcome măsurabil.

### Ca anchor pentru tracking progres

În Notion dashboard al cohortei, fiecare student are coloane `W1` … `W5.2` cu status:
- ✅ Completed (deliverable bifat)
- 🟡 In progress
- ⚪ Not started

Ratele de completion per săptămână = indicator de health al cohortei.

### Pe certificatul final

Timeline cu 8 entries (W1 → W5.2), bifate cele finalizate. Certificat „AI Agents — Claude & Codex" emis la 8/8.

### În jurnalul cursantului (opțional)

Template săptămânal:

```
## {cod} — {tema}

### Outcome propus
{copy din docs/07-teme-saptamani.md}

### Ce am livrat


### Ce a mers neașteptat de bine


### Ce m-a blocat și cum am ieșit


### Ce schimb la abordarea mea pentru săpt următoare
```
