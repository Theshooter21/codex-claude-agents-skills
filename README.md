# Codex + Claude Agents & Skills Setup

Plantilla pública para organizar skills, plugins y agentes de Codex y Claude sin activar delegaciones automáticas entre modelos.

## Objetivos

- Mantener skills compartidas en `~/.agents/skills`.
- Separar las skills exclusivas de Codex y Claude.
- Evitar duplicados y colisiones de nombres.
- Instalar plugins únicamente desde fuentes oficiales o verificadas.
- Impedir que Codex, Claude u otros revisores se invoquen automáticamente.
- Conservar credenciales, historiales y configuración privada fuera del repositorio.

## Contenido

- [`INSTALL_PROMPT.md`](INSTALL_PROMPT.md): prompt completo para realizar la instalación de forma asistida.
- [`MANIFEST.md`](MANIFEST.md): clasificación y estructura recomendadas.
- [`SECURITY.md`](SECURITY.md): límites de seguridad y privacidad.

## Uso rápido

1. Clona este repositorio.
2. Abre `INSTALL_PROMPT.md`.
3. Copia el prompt en Codex o Claude.
4. Revisa el plan que produzca el agente.
5. Autoriza explícitamente cualquier instalación, eliminación o reemplazo.

Este repositorio no distribuye copias de plugins o skills de terceros. El instalador debe obtenerlos desde sus fuentes oficiales y respetar sus licencias.

## Filosofía de instalación

```text
~/.agents/skills   -> skills compartidas
~/.codex/skills    -> skills exclusivas de Codex
~/.claude/skills   -> skills exclusivas de Claude
plugins oficiales  -> integraciones mantenidas por sus proveedores
```

La presencia de un archivo en una caché no significa que el componente esté activo. La validación final debe hacerse desde una sesión nueva de cada aplicación.

