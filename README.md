# Codex + Claude: agentes y skills

Marketplace de plugins para **Claude Code** con agentes y skills listos para instalar, más los equivalentes para **Codex**. Ningún componente delega en otro modelo de forma automática.

## Instalar en Claude Code (dos comandos)

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

## Codex

Los mismos agentes en formato Codex están en [`codex/agents`](codex/agents) (`.toml`) y las skills usan el mismo formato `SKILL.md`. Para copiarlos a tu máquina (con copia de seguridad, sin borrar nada):

```bash
git clone https://github.com/Theshooter21/codex-claude-agents-skills
python codex-claude-agents-skills/scripts/install.py --target codex
```

Esto deja las skills en `~/.agents/skills` y los agentes en `~/.codex/agents`. Los agentes se generan desde una única fuente (`scripts/_agents_data.py`) con `python scripts/build_agents.py`, así que Claude y Codex no se desincronizan.

## Skills de terceros

No se redistribuyen copias de skills ajenas. Las recomendadas (Supabase, accesibilidad, calidad web, etc.) están listadas con su fuente oficial en [`THIRD_PARTY.md`](THIRD_PARTY.md).

## Desarrollo

```bash
python scripts/build_agents.py   # regenera agentes de Claude y Codex
python scripts/validate.py       # JSON, frontmatter, TOML, sincronía y datos privados
```

Más: [`MANIFEST.md`](MANIFEST.md) (arquitectura y rutas) · [`SECURITY.md`](SECURITY.md) · [`LICENSE`](LICENSE) (MIT).
