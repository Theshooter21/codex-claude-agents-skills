# Prompt de instalación

Copia el siguiente prompt completo en Codex o Claude desde el equipo donde deseas realizar la instalación.

```text
Configura una instalación limpia y segura de agentes, skills y plugins para Codex y Claude usando este repositorio como guía.

Repositorio de referencia:
https://github.com/Theshooter21/codex-claude-agents-skills

Objetivos:
- Usar ~/.agents/skills como ubicación canónica para skills compatibles con ambos agentes.
- Mantener en ~/.codex/skills únicamente las skills exclusivas de Codex.
- Mantener en ~/.claude/skills únicamente las skills exclusivas de Claude.
- Instalar plugins solo desde marketplaces, repositorios o proveedores oficiales verificables.
- No permitir invocaciones automáticas entre Codex, Claude, AGY u otros revisores.
- No copiar credenciales, sesiones, tokens, historiales, memorias, cachés ni configuraciones privadas al repositorio.

Reglas obligatorias:
1. Trabaja primero en modo de auditoría de solo lectura.
2. Lee los archivos globales de instrucciones que existan antes de proponer cambios.
3. No interpretes una copia en caché como un plugin activo.
4. Distingue entre componentes activos, instalados pero deshabilitados, compartidos, duplicados y obsoletos.
5. No instales, desinstales, elimines, reemplaces ni muevas archivos hasta presentar el plan y recibir mi aprobación explícita.
6. No muestres ni leas en voz alta secretos, tokens o archivos de credenciales.
7. Antes de modificar configuración, crea una copia de seguridad recuperable y registra su ubicación.
8. No subas información local o privada a GitHub.
9. Si una skill no tiene licencia o fuente verificable, detén su instalación y repórtala.
10. No actives tareas programadas, hooks de delegación o revisiones externas automáticas.

Fase 1: inventario
- Examina las ubicaciones de skills de Codex, Claude y la biblioteca compartida.
- Examina la configuración de plugins sin abrir archivos de credenciales.
- Enumera agentes persistentes y agentes empaquetados por plugins.
- Para cada componente indica: nombre, tipo, plataforma, fuente, versión, estado y ruta lógica.
- Calcula hashes para detectar duplicados idénticos.
- Señala colisiones donde dos skills tienen el mismo nombre pero contenido diferente.

Fase 2: clasificación
Clasifica cada componente como:
- Compartido y recomendado.
- Exclusivo de Codex.
- Exclusivo de Claude.
- Plugin oficial activo.
- Instalado pero deshabilitado.
- Duplicado idéntico.
- Colisión con contenido diferente.
- Solo caché o catálogo.
- Incompatible con las reglas de delegación.
- Fuente o licencia no verificable.

Fase 3: plan
- Usa MANIFEST.md como arquitectura objetivo, no como autorización para modificar el sistema.
- Propón la lista exacta de archivos y configuraciones que cambiarías.
- Conserva una sola fuente canónica para cada skill compartida.
- No reemplaces variantes de Supabase u otras skills con contenido diferente sin comparar sus reglas y pedirme una decisión.
- Mantén una sola distribución activa de cada integración, como Render.
- Desactiva la ejecución automática de perfiles de rescate o delegación; consérvalos solo si requieren una orden explícita del usuario.
- Si un plugin diseñado para invocar Codex desde Claude está habilitado dentro de Codex, repórtalo como potencialmente autorreferencial.

Fase 4: ejecución, únicamente después de mi aprobación
- Realiza solo los cambios aprobados.
- Usa instaladores oficiales cuando existan.
- No edites directamente cachés administradas por las aplicaciones.
- Valida la sintaxis y metadatos de cada SKILL.md.
- No elimines copias de seguridad durante esta tarea.

Fase 5: verificación
- Inicia o solicita una sesión nueva de Codex y Claude cuando sea necesario.
- Comprueba cuáles skills aparecen realmente disponibles.
- Verifica que no haya delegación automática, hooks inesperados o plugins duplicados activos.
- Entrega una tabla final con el estado anterior, cambio aplicado, estado final y evidencia.
- Enumera cualquier paso manual pendiente.

Empieza únicamente con la Fase 1 y el plan. No realices todavía cambios destructivos ni instalaciones.
```

