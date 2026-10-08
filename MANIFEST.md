# Manifiesto recomendado

Este manifiesto describe una arquitectura objetivo. No implica que todos los componentes deban instalarse.

## Skills compartidas

Ubicación preferida: `~/.agents/skills`.

Categorías sugeridas:

- Privacidad y cumplimiento.
- Edición de imágenes y video.
- Bases de datos y Supabase.
- Escritura y documentación.
- Accesibilidad y calidad web, cuando ambas plataformas soporten la misma skill.

Cada skill compartida debe tener:

- Un único directorio canónico.
- Un `SKILL.md` válido.
- Fuente y licencia verificables.
- Nombre único o namespace claro.
- Activadores que no se solapen de manera ambigua.

## Skills exclusivas de Codex

Ubicación: `~/.codex/skills`.

Ejemplos de categorías:

- Documentación y configuración de productos OpenAI.
- Creación e instalación de skills de Codex.
- Revisión de cambios delegada específicamente a Codex.
- Capacidades integradas de generación de imágenes.

## Skills exclusivas de Claude

Ubicación: `~/.claude/skills`.

Mantener aquí solamente las skills que dependan de:

- Herramientas exclusivas de Claude Code.
- Convenciones o hooks propios de Claude.
- Plugins que no sean compatibles con el formato compartido.

## Plugins e integraciones

Clasificación recomendada:

- Nube y despliegue: Render, Vercel o Netlify.
- Datos: Supabase y PostgreSQL.
- Diseño: Figma.
- Documentos: PDF, hojas de cálculo y presentaciones.
- Control de aplicaciones: computer use y navegador.
- Seguridad: auditoría, validación y corrección de hallazgos.
- Desarrollo de agentes: SDKs y APIs oficiales.

Reglas:

- Mantener una sola distribución activa por proveedor y función.
- Evitar instalar simultáneamente forks equivalentes.
- No contar el contenido de marketplaces o cachés como activo.
- Verificar la disponibilidad desde una sesión nueva.

## Agentes y delegación

Los perfiles de rescate o segunda opinión deben ser opt-in:

- No ejecutarse por hooks automáticos.
- No activarse porque otro agente esté “atascado”.
- Requerir una petición explícita del usuario en el mensaje actual.
- Documentar qué proveedor o runtime consumen.

Los agentes empaquetados dentro de plugins deben distinguirse de los subagentes genéricos y de los agentes personalizados persistentes.

## Criterios de aceptación

- No hay skills duplicadas con el mismo contenido.
- Toda colisión de nombres está namespaced o documentada.
- Cada plugin activo tiene una finalidad clara.
- No hay invocaciones automáticas entre proveedores de modelos.
- No se almacenan secretos en el repositorio.
- La lista observada en sesiones nuevas coincide con el manifiesto aprobado.

