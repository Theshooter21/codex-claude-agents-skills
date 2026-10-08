# Prompt para que una sesión de Claude lo instale

Pega esto en una sesión de Claude Code en la máquina donde quieras instalarlo.

```text
Instala el plugin de https://github.com/Theshooter21/codex-claude-agents-skills en este Claude Code.

Pasos:
1. Ejecuta: claude plugin marketplace add Theshooter21/codex-claude-agents-skills
   (si la CLI no está disponible, indícame que ejecute /plugin marketplace add Theshooter21/codex-claude-agents-skills).
2. Ejecuta: claude plugin install agents-skills@codex-claude-agents-skills
3. Lista los plugins instalados y confirma que agents-skills está habilitado.
4. Dime que abra una sesión nueva y qué agentes y skills debería ver:
   agentes: software-architect, backend-architect, frontend-developer, ui-designer, ux-architect, security-engineer, technical-writer, growth-hacker, proposal-strategist, sales-engineer, triage-lead
   skills: agent-setup-audit, skill-security-review

Reglas:
- No leas ni muestres credenciales, tokens ni archivos de autenticación.
- No modifiques otra configuración, no desinstales ni reemplaces nada que ya exista.
- No actives hooks, tareas programadas ni delegaciones automáticas a Codex, AGY u otros modelos.
- Si algo falla, muestra el error exacto y no improvises alternativas destructivas.
```

## Solo Codex (opcional)

Si además quieres los agentes y skills en Codex, añade al prompt:

```text
Después clona el repo en un directorio nuevo y ejecuta: python scripts/install.py --target codex --dry-run
Muéstrame el resultado y, con mi aprobación, ejecútalo sin --dry-run.
```
