# Contributing

> Acest repo e **template-ul de start** pentru cursanții *AI pentru Viața Ta*. Cum contribui depinde de rolul tău.

---

## Sunt cursant — cum să contribui

### 1. Fork → fă-l al tău

```bash
# Pe GitHub: Fork repo-ul în contul tău personal
# Apoi local:
git clone https://github.com/{tu}/ai-agents-claude-codex.git my-agents
cd my-agents
git remote add upstream https://github.com/SkillBrain-com/ai-agents-claude-codex.git
```

Fork-ul tău e SPAȚIUL TĂU. Construiește, experimentează, share-uiește cu cohorta.

### 2. Sync-uiește îmbunătățiri din upstream

Când SkillBrain adaugă template-uri noi sau fix-uri în upstream:

```bash
git fetch upstream
git merge upstream/main
# Rezolvă conflicte dacă există (de obicei nu — modificările tale sunt în areas/* și audits/*, noi modificăm doar docs/*)
```

### 3. Share skill-urile tale cu comunitatea

Dacă ai construit un skill grozav, share-uiește:

- **Discord/Slack cohortă:** post cu link la fork-ul tău + descriere
- **Pull Request la `_examples/`:** dacă vrei să-l includem ca exemplu în repo-ul oficial (vezi mai jos)

---

## Vreau să contribui la repo-ul oficial

Mulțumesc! Acceptăm PR-uri pentru:

### ✅ Bune candidaturi pentru PR

- **Skill-uri exemplu** (pentru `_examples/`) — funcționale, generice, non-personale
- **Îmbunătățiri docs** — clarificări, fix-uri typo, traduceri
- **Templates noi** (audit, decision, flow patterns)
- **Troubleshooting entries** — erori comune pe care le-ai întâlnit + soluții
- **Workflows GitHub Actions** — linting SKILL.md, validare structură

### ❌ Nu acceptăm PR-uri pentru

- Skill-uri personale (acelea trăiesc în fork-ul tău)
- Audit-urile tale (datele tale)
- Materiale curs (proprietate SkillBrain — distribuite prin Notion)
- Schimbări în structura `areas/` (e convenția stabilită)

---

## Proces PR

1. **Issue mai întâi** (pentru schimbări mari): deschide un Issue cu propunerea
2. **Branch:** `feat/{ce-adaugi}` sau `fix/{ce-fixezi}` sau `docs/{ce-actualizezi}`
3. **Commit message:** [Conventional Commits](https://www.conventionalcommits.org/):
   - `feat: add invoice-extractor skill template`
   - `fix: typo in docs/03-cum-incep.md`
   - `docs: add troubleshooting entry for openclaw 429`
4. **PR description:** include
   - Ce schimbi
   - De ce
   - Cum poate cineva testa
5. **Review:** un maintainer SkillBrain face review în 3-5 zile

---

## Checklist pre-PR

- [ ] Nu am modificat fișiere din `areas/personal/` sau `areas/work/` (cu excepția exemple generice)
- [ ] Nu am `.env` sau date sensibile în commits (verifică cu `git log --all --oneline`)
- [ ] Documentația nouă/modificată folosește română cu diacritice
- [ ] Am testat schimbarea pe propriul setup
- [ ] Commit message-ul urmează Conventional Commits

---

## Code of Conduct

Acest proiect urmează [Code of Conduct](CODE_OF_CONDUCT.md). Pe scurt:
- Fii ok cu colegii (toți suntem în diferite stadii de învățare)
- Critică ideile, nu oamenii
- Răspunsuri „nu știu" sunt OK — niciun întrebare nu e prostească

Raportare violare: contact@skillbrain.com.

---

## Comunicare

| Canal | Pentru ce |
|---|---|
| [Issues](../../issues) | Bug-uri, request-uri feature, întrebări tehnice |
| [Discussions](../../discussions) | Idei, sfaturi, conversații libere |
| Discord cohortă | Live chat zilnic |
| support@skillbrain.com | Probleme cu acces, plată, escalări |

Mulțumesc că contribui! 🦞
