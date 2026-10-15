# A3. Reglas del ejercicio

## Reglas funcionales

1. Los códigos de emprendedores, iniciativas y asesorías son únicos.
2. Cada iniciativa tiene un emprendedor responsable existente; una persona puede ser responsable de varias iniciativas.
3. Cada asesoría se vincula con una iniciativa existente y registra el código ficticio del asesor que la atiende.
4. Sectores: `tecnologia`, `alimentos`, `economia_circular`. Etapas didácticas: `idea`, `validacion`, `puesta_en_marcha` (no son categorías oficiales).
5. Estado de iniciativa: `activa` o `archivada`. Estado de asesoría: `programada`, `realizada` o `cancelada`.
6. Se registra `fecha_programada` y, al realizarse la sesión, `fecha_realizacion`. Esta no se altera para ocultar una reprogramación.
7. No se programan dos asesorías para el mismo asesor en la misma franja.
   - **Franja definida para el laboratorio:** bloques de 1 hora (por ejemplo 08:00–09:00 hora de Colombia).
   - Esto es una **regla funcional**; garantizarla ante solicitudes simultáneas es un mecanismo que se estudiará más adelante.
8. Archivar una iniciativa no elimina automáticamente su historial de asesorías.

## Ajuste propuesto

- `fecha_realizacion: null` significa "aún no realizada". Si el campo falta, se interpreta como dato incompleto y no como "no realizada".

## Dos preguntas para la persona responsable de la unidad

1. ¿Una asesoría reprogramada debe conservar el historial de sus fechas anteriores o basta con la última?
2. ¿Se necesita que una iniciativa tenga más de un emprendedor (equipos) en un futuro cercano?

## Un riesgo

Dos coordinadores podrían programar al mismo asesor en la misma franja al mismo tiempo y el sistema no lo detectaría si solo se valida antes de insertar (condición de carrera).

## Reglas funcionales vs. mecanismos

| Regla funcional (qué) | Mecanismo (cómo, se aprende después) |
| --- | --- |
| Códigos únicos | Índices únicos |
| Estados y sectores permitidos | Validación de esquema |
| Sin doble programación del asesor | Control de concurrencia / índice único por asesor + franja |
