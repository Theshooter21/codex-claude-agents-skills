# Manifiesto

## Estructura del repo

```text
.claude-plugin/marketplace.json        marketplace de Claude Code
plugins/agents-skills/
  .claude-plugin/plugin.json           manifiesto del plugin
  agents/*.md                          11 agentes (Claude), generados
  skills/<nombre>/SKILL.md             skills (formato compartido Claude/Codex)
codex/agents/*.toml                    los mismos agentes en formato Codex, generados
scripts/_agents_data.py                fuente única de los agentes
scripts/build_agents.py                genera .md y .toml
scripts/install.py                     instalador (Claude vía CLI, Codex copiando archivos)
scripts/validate.py                    validaciones
```

## Dónde queda cada cosa tras instalar

| Qué | Claude | Codex |
|---|---|---|
| Skills | dentro del plugin (`agents-skills:<skill>`) | `~/.agents/skills/<skill>` |
| Agentes | dentro del plugin | `~/.codex/agents/<agente>.toml` |

## Reglas de diseño

- Una sola fuente por agente; los formatos de Claude y Codex se generan, no se editan a mano.
- Cada skill tiene un `SKILL.md` válido y `name` igual a su directorio.
- Los agentes son opt-in: ninguno invoca a otro modelo ni se activa por hooks. `triage-lead` solo lee y recomienda.
- No se redistribuye contenido de terceros (ver `THIRD_PARTY.md`).
- Sin credenciales, historiales, rutas privadas ni datos de proyectos concretos; `scripts/validate.py` lo comprueba.

## Criterios de aceptación

- `python scripts/validate.py` termina con `OK`.
- En una sesión nueva de Claude Code aparecen los 11 agentes y las 2 skills del plugin.
- No hay delegación automática ni hooks añadidos.
