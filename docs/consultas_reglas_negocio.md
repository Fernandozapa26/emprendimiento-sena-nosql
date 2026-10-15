
# Actividad A3 - Consultas y reglas de negocio

## Unidad de Emprendimiento del SENA

## 1. Objetivo

Definir las consultas y reglas necesarias para gestionar
emprendedores, iniciativas y asesorías antes de diseñar
las colecciones de MongoDB.

Las frecuencias indicadas son hipótesis de uso, no
estadísticas reales de la Unidad de Emprendimiento.

## 2. Consultas del sistema

### Q01. Iniciativas activas por sector y etapa

Necesidad: Como asesor, quiero consultar las iniciativas
activas de un sector y una etapa para organizar el
acompañamiento.

- Actor: Asesor.
- Filtros: estado = activa, sector y etapa.
- Salida: codigo, nombre, sector, etapa, emprendedor_codigo.
- Orden: nombre ascendente y codigo ascendente.
- Frecuencia estimada: diaria (hipótesis).
- Entrada de ejemplo: sector = tecnologia,
  etapa = validacion.
- Resultado esperado: lista de iniciativas que cumplan
  los tres filtros. Si no hay coincidencias, lista vacía.

### Q02. Detalle de una iniciativa

Necesidad: Como asesor, quiero consultar una iniciativa
para conocer su propuesta de valor y sus atributos
específicos.

- Actor: Asesor.
- Filtro: codigo de iniciativa.
- Salida: codigo, nombre, propuesta_valor, sector,
  etapa, estado, emprendedor_codigo y atributos.
- Orden: no aplica, porque se consulta un registro.
- Frecuencia estimada: varias veces al día (hipótesis).
- Entrada de ejemplo: INI-001.
- Resultado esperado: información completa de la
  iniciativa, incluidos sus atributos particulares.
  Si el código no existe, se informa que no fue encontrada.

### Q03. Iniciativas de un emprendedor por estado

Necesidad: Como responsable de la unidad, quiero
consultar las iniciativas asociadas a un emprendedor
para revisar su estado.

- Actor: Responsable de la unidad.
- Filtros: emprendedor_codigo y estado.
- Salida: codigo, nombre, sector, etapa y estado.
- Orden: codigo ascendente.
- Frecuencia estimada: semanal (hipótesis).
- Entrada de ejemplo: EMP-001 y activa.
- Resultado esperado: iniciativas activas cuyo
  responsable sea EMP-001.

### Q04. Asesorías pendientes por fecha y modalidad

Necesidad: Como coordinador, quiero consultar las
asesorías programadas dentro de un periodo para
organizar la agenda de atención.

- Actor: Coordinador.
- Filtros: estado = programada, modalidad y rango
  de fecha_programada.
- Salida: codigo, iniciativa_codigo, asesor_codigo,
  modalidad y fecha_programada.
- Orden: fecha_programada ascendente y codigo ascendente.
- Frecuencia estimada: diaria (hipótesis).
- Entrada de ejemplo: del 2026-10-08 al 2026-10-09,
  modalidad = virtual.
- Resultado esperado: asesorías programadas dentro
  del periodo y con la modalidad solicitada.
- Convención: el inicio del rango se incluye y el
  límite final se excluye. Las fechas se almacenan
  como instantes y se interpretan según la zona
  horaria correspondiente.

### Q05. Historial de asesorías de una iniciativa

Necesidad: Como asesor, quiero consultar las asesorías
de una iniciativa para conocer su seguimiento,
incluidas las sesiones realizadas y canceladas.

- Actor: Asesor.
- Filtro: iniciativa_codigo.
- Salida: codigo, asesor_codigo, temas, estado,
  modalidad, fecha_programada y fecha_realizacion.
- Orden: fecha_programada descendente y codigo
  ascendente para desempatar.
- Frecuencia estimada: cada vez que se revisa
  el acompañamiento (hipótesis).
- Entrada de ejemplo: INI-001.
- Resultado esperado: historial de asesorías
  relacionadas con INI-001, sin eliminar las sesiones
  por estar canceladas o archivada la iniciativa.

### Q06. Cantidad de asesorías realizadas por sector y mes

Necesidad: Como responsable de la unidad, quiero
conocer cuántas asesorías se realizaron en cada sector
durante un mes para revisar el acompañamiento.

- Actor: Responsable de la unidad.
- Filtros: estado = realizada y fecha_realizacion
  dentro del mes solicitado.
- Agrupación: sector de la iniciativa al momento
  de realizar la asesoría y mes de realización.
- Salida: mes, sector y cantidad.
- Orden: mes ascendente y sector ascendente.
- Frecuencia estimada: mensual (hipótesis).
- Entrada de ejemplo: octubre de 2026.
- Resultado esperado: cantidad de asesorías realizadas
  por sector durante ese mes. Las programadas y
  canceladas no se cuentan.

Decisión de diseño para Q06:
Se propone guardar el sector vigente cuando se realiza
la asesoría en el campo sector_al_realizar.
Así, un cambio posterior de sector no modifica
los resultados históricos.

Para el reporte mensual se utilizará la zona horaria
America/Bogota, convirtiendo los límites del periodo
a UTC cuando se realicen las consultas.

## 3. Reglas de negocio

### RN01. Identificadores únicos

Cada emprendedor, iniciativa y asesoría debe tener
un código único dentro de su entidad.

### RN02. Responsable de una iniciativa

Cada iniciativa debe estar asociada a un emprendedor
existente. Un emprendedor puede ser responsable
de varias iniciativas.

### RN03. Relación de asesorías

Cada asesoría debe estar asociada a una iniciativa
existente y registrar el código ficticio del asesor
que la atiende.

### RN04. Sectores y etapas

Sectores de ejemplo:
- tecnologia
- alimentos
- economia_circular

Etapas didácticas:
- idea
- validacion
- puesta_en_marcha

Estas etapas son categorías del ejercicio académico,
no categorías oficiales de un programa del SENA.

### RN05. Estados permitidos

Estados de iniciativa:
- activa
- archivada

Estados de asesoría:
- programada
- realizada
- cancelada

### RN06. Registro de fechas

Toda asesoría debe registrar fecha_programada.

Cuando se realice, también debe registrar
fecha_realizacion.

La fecha real puede ser diferente de la programada
y no debe modificarse para ocultar una reprogramación.

### RN07. Evitar cruces de asesorías

No se deben programar dos asesorías para el mismo
asesor en la misma franja de atención.

Para este laboratorio se propone una franja de
60 minutos por asesor, pendiente de confirmación.

Esta es una regla funcional. Su garantía ante
solicitudes simultáneas se implementará y probará
en una etapa posterior.

### RN08. Conservación del historial

Archivar una iniciativa no debe eliminar
automáticamente su historial de asesorías.

Se propone revisar las asesorías pendientes antes
de archivar una iniciativa y evitar nuevas
programaciones mientras permanezca archivada.

## 4. Preguntas para el responsable de la unidad

1. ¿Cuál es la duración real de las asesorías y
   qué horarios se utilizan para programarlas?

2. ¿Qué debe suceder con las asesorías pendientes
   cuando una iniciativa cambia de estado a archivada?

Estas respuestas permitirán ajustar las reglas
antes de implementar el sistema.

## 5. Riesgo identificado

Riesgo: duplicidad de asesorías para un mismo asesor
en el mismo horario.

Consecuencia: conflictos en la agenda y posibles
incumplimientos en la atención a emprendedores.

Medida propuesta: validar la disponibilidad antes
de registrar una asesoría y, posteriormente,
implementar un mecanismo que controle las
solicitudes simultáneas.

## 6. Diferencia entre reglas e implementación

Las reglas de negocio describen lo que debe
cumplir el sistema.

Los mecanismos técnicos, como validaciones,
índices, controles de concurrencia y consultas
MongoDB, se diseñarán e implementarán después.

Por ahora estamos definiendo las necesidades
funcionales, no afirmando que estas reglas ya
estén implementadas.

## 7. Conclusión

Esta actividad me permitió identificar las consultas
que necesita la Unidad de Emprendimiento del SENA
y establecer reglas para mantener la información
organizada y coherente.

Definir estas necesidades antes de programar facilita
el diseño de las colecciones y ayuda a prevenir
errores durante el desarrollo.
