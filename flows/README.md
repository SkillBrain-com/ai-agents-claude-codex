# flows/

> **Module 4-5 deliverable.** Task Flows OpenClaw — fluxuri multi-pas cu state tracking + error handling.

## Diferența flow vs skill

| Aspect | Skill | Flow |
|---|---|---|
| **Scop** | 1 acțiune | Secvență multi-pas |
| **State** | Stateless | Persistent (state file per rulare) |
| **Resume on fail** | NU | DA (de la step-ul unde a picat) |
| **Folder** | `areas/*/skills/` | `flows/` |
| **Învățat în** | M1 | M4.3 |

## Structura unui flow

```
flows/
├── README.md
├── _examples/                       ← exemple gata făcute
│   └── customer-support-flow/
│       ├── SKILL.md                 ← definirea celor 4 steps
│       └── README.md
├── briefing-cu-dashboard/           ← flow real al tău
│   ├── SKILL.md
│   └── _state/                      ← runs istoric (gitignored)
└── ...
```

## Convenție steps

| Pattern | Use cases |
|---|---|
| `classify → fetch → reason → act` | Email triage, customer support, document review |
| `collect → analyze → format → deliver` | Reports, summaries, dashboards |
| `monitor → alert → escalate` | Health checks, anomaly detection |

Vezi M4.3 pentru pattern-uri complete.

## Cum rulez un flow

```bash
# Start
openclaw tasks flow start {flow-name} --input @path/to/input.json

# Verifică status
openclaw tasks flow show {flow_id}

# Resume dacă a picat
openclaw tasks flow resume {flow_id}
```

## Error handling

Fiecare flow trebuie să aibă în SKILL.md o secțiune `ERROR HANDLING`:

```yaml
ERROR HANDLING per step:
- Retry pe 429/500/503: 3 încercări cu backoff exponențial (5s, 10s, 20s)
- Hard fail pe 400/401/403: log + alert owner via Slack
- Fallback: skip step + continuă, sau abort total
```

Vezi M4.4 pentru pattern-ul complet.
