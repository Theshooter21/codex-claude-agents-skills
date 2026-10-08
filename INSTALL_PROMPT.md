# Prompt para que una sesión de Claude lo instale

Pega esto en una sesión de Claude Code en la máquina donde quieras instalarlo.

```text
Instala el plugin de https://github.com/Theshooter21/codex-claude-agents-skills en este Claude Code.

Pasos:
1. Ejecuta: claude plugin marketplace add Theshooter21/codex-claude-agents-skills
   (si la CLI `claude` no está disponible, dime que ejecute /plugin marketplace add Theshooter21/codex-claude-agents-skills)
2. Ejecuta: claude plugin install agents-skills@codex-claude-agents-skills
3. Ejecuta: claude plugin list y confirma que agents-skills aparece como enabled.
4. Dime que abra una sesión nueva y qué debería ver:
   agentes: software-architect, backend-architect, frontend-developer, ui-designer, ux-architect, security-engineer, technical-writer, growth-hacker, proposal-strategist, sales-engineer, triage-lead
   skills: agent-setup-audit, skill-security-review

Reglas:
- No leas ni muestres credenciales, tokens ni archivos de autenticación.
- No modifiques otra configuración ni desinstales o reemplaces nada existente.
- No actives hooks, tareas programadas ni delegaciones automáticas a otros modelos o herramientas.
- Si algo falla, muestra el error exacto y no improvises alternativas destructivas.
```

Para actualizar más adelante: `claude plugin marketplace update codex-claude-agents-skills` y `claude plugin update agents-skills@codex-claude-agents-skills`.
