---
name: agent-setup-audit
description: Auditoría de solo lectura de skills, agentes y plugins instalados para Claude y Codex. Úsala cuando el usuario pida "auditar mis skills/agentes", revisar duplicados, colisiones de nombres o qué está realmente activo.
---

# Agent setup audit

Inventario **de solo lectura** de skills, agentes y plugins. No instala, mueve ni borra nada.

## Reglas

- No leas ni muestres archivos de credenciales (`auth.json`, `.credentials.json`, `.env`, tokens).
- Una copia en caché de plugins **no** es un componente activo. Distingue activo / instalado pero deshabilitado / solo caché.
- No propongas cambios hasta presentar el inventario; ejecuta cambios solo con aprobación explícita.

## Ubicaciones a examinar (si existen)

| Qué | Claude | Codex | Compartido |
|---|---|---|---|
| Skills | `~/.claude/skills` | `~/.codex/skills` | `~/.agents/skills` |
| Agentes | `~/.claude/agents` | `~/.codex/agents` | — |
| Plugins | `~/.claude/plugins` (estado en `installed_plugins.json`) | `~/.codex/plugins`, `config.toml` | — |

Los proyectos pueden tener además `.claude/` y `.codex/` propios.

## Procedimiento

1. **Listar** cada componente: nombre, tipo (skill/agente/plugin), plataforma, ruta, versión y fuente si consta en el frontmatter.
2. **Hashear** el contenido de cada skill (por ejemplo SHA-256 de `SKILL.md` más sus archivos ordenados) para detectar duplicados idénticos entre ubicaciones.
3. **Detectar colisiones**: mismo `name:` con contenido distinto.
4. **Validar** cada `SKILL.md`: frontmatter con `name` y `description`, y `name` igual al directorio.
5. **Revisar delegación**: agentes cuya descripción invite a invocarse "proactivamente" o que llamen a otro modelo (Codex, AGY, otros). Márcalos si las reglas del usuario exigen petición explícita.
6. **Clasificar** cada componente: compartido recomendado · exclusivo de Claude · exclusivo de Codex · duplicado idéntico · colisión · solo caché · deshabilitado · fuente/licencia no verificable.

## Salida

Tabla con: componente, plataforma, estado, hallazgo y acción propuesta. Después, lista corta de decisiones que requieren al usuario (por ejemplo, qué variante conservar en una colisión).

Para revisar la seguridad de un componente de terceros usa la skill `skill-security-review`.
