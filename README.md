# Agentes y skills para Claude Code

Marketplace de plugins para **Claude Code** con 11 agentes especialistas y 2 skills de auditoría y seguridad. Ningún componente delega en otros modelos ni se activa por hooks.

## Instalar (dos comandos)

Dentro de cualquier sesión de Claude Code:

```text
/plugin marketplace add Theshooter21/codex-claude-agents-skills
/plugin install agents-skills@codex-claude-agents-skills
```

Después abre una sesión nueva. Si prefieres que una sesión de Claude lo haga por ti, pégale el prompt de [`INSTALL_PROMPT.md`](INSTALL_PROMPT.md).

Desde un terminal, con la CLI de Claude:

```bash
claude plugin marketplace add Theshooter21/codex-claude-agents-skills
claude plugin install agents-skills@codex-claude-agents-skills
```

## Qué incluye

**Agentes (11)**, en [`plugins/agents-skills/agents`](plugins/agents-skills/agents):
`software-architect`, `backend-architect`, `frontend-developer`, `ui-designer`, `ux-architect`, `security-engineer`, `technical-writer`, `growth-hacker`, `proposal-strategist`, `sales-engineer` y `triage-lead` (solo lectura: recomienda qué agentes usar).

**Skills (2)**, en [`plugins/agents-skills/skills`](plugins/agents-skills/skills):
- `agent-setup-audit`: inventario de solo lectura de skills, agentes y plugins (duplicados, colisiones, qué está activo).
- `skill-security-review`: revisión defensiva de skills/agentes de terceros antes de instalarlos (`ALLOW` / `REVIEW` / `BLOCK`).

## Uso

- Claude elige los agentes por su descripción, o los pides por nombre: "usa el agente `security-engineer` para revisar este login".
- Para una tarea grande, pide primero a `triage-lead` que recomiende qué agentes usar.
- Skills: "audita mis skills y agentes" o "revisa si es seguro instalar esta skill".

## Skills de terceros

No se redistribuyen copias de skills ajenas. Las recomendadas están listadas con su fuente en [`THIRD_PARTY.md`](THIRD_PARTY.md).

## Desarrollo

```bash
python scripts/build_agents.py   # regenera los agentes desde scripts/_agents_data.py
python scripts/validate.py       # JSON, frontmatter y datos privados
python scripts/install.py --local   # instala desde este clon (pruebas)
claude plugin validate .         # validación oficial del marketplace
```

Más: [`MANIFEST.md`](MANIFEST.md) · [`SECURITY.md`](SECURITY.md) · [`LICENSE`](LICENSE) (MIT).
