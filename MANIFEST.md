# Manifiesto

## Estructura del repo

```text
.claude-plugin/marketplace.json        marketplace de Claude Code
plugins/agents-skills/
  .claude-plugin/plugin.json           manifiesto del plugin
  agents/*.md                          11 agentes, generados
  skills/<nombre>/SKILL.md             2 skills
scripts/_agents_data.py                fuente única de los agentes
scripts/build_agents.py                genera agents/*.md
scripts/install.py                     instalador (CLI de Claude; --local para pruebas)
scripts/validate.py                    validaciones
```

## Reglas de diseño

- Una sola fuente por agente; los `.md` se generan, no se editan a mano.
- Las descripciones del frontmatter van entre comillas (los `: ` sin comillas rompen el YAML).
- Cada skill tiene un `SKILL.md` válido y `name` igual a su directorio.
- Los agentes son opt-in: ninguno invoca a otros modelos ni se activa por hooks. `triage-lead` solo lee (Read, Grep, Glob) y recomienda.
- No se redistribuye contenido de terceros (ver `THIRD_PARTY.md`).
- Sin credenciales, historiales, rutas privadas ni datos de proyectos concretos; `scripts/validate.py` lo comprueba.

## Criterios de aceptación

- `python scripts/validate.py` termina con `OK` y `claude plugin validate .` pasa.
- Tras instalar, `claude plugin list` muestra `agents-skills` habilitado.
- En una sesión nueva aparecen los 11 agentes y las 2 skills con su descripción completa.
