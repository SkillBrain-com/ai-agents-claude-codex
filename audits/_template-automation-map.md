# Harta mea de automatizări — {YYYY-MM-DD}

> Output final M2.4. Sinteza celor 2 audit-uri (personal + job). Input pentru M5 (alegerea celor 3 de construit).

---

## Context

- **Audit-ul personal:** vezi [audit-uri/{data}_personal-log.md](.)
- **Audit-ul job:** vezi [audit-uri/{data}_job-log.md](.)
- **Total procese candidate identificate:** {N}

---

## ⭐ Top 3 — high-impact × high-feasibility (build în M5)

| # | Proces | Impact (1-5) | Fezabilitate (1-5) | Notă tehnică | Săptămâna build |
|---|---|---|---|---|---|
| 1 | Briefing de dimineață | 5 | 5 | Cowork scheduled @ 07:30, integrare Gmail + Notion | Săpt 7 |
| 2 | Procesare facturi din Downloads | 4 | 5 | OpenClaw flow, ClawHub skill «pdf-extract», output în Sheet | Săpt 7 |
| 3 | Weekly recap — sinteză săptămânală | 5 | 4 | Orchestrator care citește output-urile din #1 + #2, Notion dashboard | Săpt 8 |

---

## 📋 Backlog (high-impact dar low-feasibility, sau invers)

| Proces | Impact | Fezabilitate | De ce nu acum |
|---|---|---|---|
| Procesare contracte clienți | 5 | 2 | Necesită aprobare Legal pentru cloud AI |
| Auto-răspuns FAQ clienți | 4 | 3 | Necesită vetting prompt + 2-3 cicluri review |
| Sumarizator newsletter | 3 | 5 | Quick win, dar low-impact — îl fac dacă mai am timp |

---

## ❌ Respinse (anti-criterii sau low-low)

| Proces | Motiv respingere |
|---|---|
| Răspuns la email-uri sensibile (HR) | Necesită judecată subiectivă — anti-criteriu |
| Decizie strategică Q3 | Low-volume (1×/an) + judecată — automation greșită |
| Triaj LinkedIn DMs | Low-impact (3/săpt), inconsistent |

---

## Reflecții

- **Pattern observat în log-ul tău:** {ce ai observat? ex: «cele mai multe ore pierdute sunt pe context-switching între email și Slack»}
- **Surpriza majoră:** {ce nu te așteptai? ex: «petrec 5h/săpt pe task-uri sub 10 min care se acumulează»}
- **Decizia ta principală:** {ex: «mă focusez pe 3 automation care reduc context-switching»}

---

## Notă pentru M5

Această hartă e LIVE — o actualizezi pe parcursul M5 cu:
- Săpt 7: ce ai construit + ce ai aflat în implementare
- Săpt 8: impact măsurat după 1 săpt de rulare
