# areas/shared/

Skills **reutilizate** între personal și work, plus **orchestratoare** care apelează skills din ambele arii.

## Ce pun aici

- **Skills utilitare universale:**
  - `get-weather/` — vreme pentru orice oraș
  - `web-search/` — search wrapper
  - `text-summarizer/` — sumarizator generic
- **Orchestratoare cross-area:**
  - `daily-pulse/` — combină morning-brief (personal) + slack-triage (work) într-un dashboard
  - `weekly-review/` — agregă outputs din ambele arii

## Pattern: skill atomic vs orchestrator

| Tip | Exemplu | Mărime |
|---|---|---|
| **Atomic** (utility) | `get-weather/` | 1 file SKILL.md + 1 script |
| **Orchestrator** | `daily-pulse/` | SKILL.md care apelează 3-5 alte skills în secvență |

Vezi M3.5 pentru pattern-ul „control flow în cod, gândire în agents".

## Configurare

Skills din `shared/` citesc din `.env` global (root-ul repo-ului) când au nevoie de credentiale generale (ex: Anthropic API key).

Pentru skills care apelează skills personal + work, fiecare sub-skill își gestionează propriul `.env`.
