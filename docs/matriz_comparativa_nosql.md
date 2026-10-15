
# Actividad A2 - Comparación de necesidades y modelos NoSQL

## Objetivo

Comparar diferentes modelos de bases de datos NoSQL
para identificar cuál se adapta mejor a las necesidades
de cada situación planteada en la Unidad de
Emprendimiento del SENA.

## Matriz comparativa

| Caso | Modelo propuesto | Razón vinculada a una consulta | Límite o costo | Alternativa |
|---|---|---|---|---|
| Iniciativas de varios sectores | Documental - MongoDB | Permite consultar iniciativas de tecnología, alimentos y economía circular, conservando atributos particulares de cada sector dentro de documentos flexibles. | Se deben validar los campos y controlar la duplicación de información y las referencias. | Base de datos SQL con tablas especializadas por sector. |
| Sesiones temporales | Clave-valor - Redis | Permite recuperar rápidamente una sesión mediante un identificador y configurar su vencimiento automático con TTL. | No resulta tan adecuado para consultas complejas sobre múltiples atributos y requiere definir la persistencia necesaria. | SQL con una tabla de sesiones y fechas de expiración. |
| Recorridos de relaciones | Grafos - Neo4j | Permite consultar las relaciones entre emprendedores, mentores y habilidades para encontrar personas que puedan apoyar una iniciativa. | Requiere aprender un modelo de consultas especializado y puede ser excesivo para relaciones sencillas. | SQL con tablas de relación entre emprendedores, mentores y habilidades. |
| Lecturas por dispositivo y periodo | Columnas anchas - Cassandra | Permite consultar grandes cantidades de lecturas de sensores por dispositivo y rango de tiempo, utilizando particiones diseñadas para esas consultas. | Requiere planificar las claves de partición y evitar particiones demasiado grandes. | Base de datos de series temporales o SQL particionado. |

## Situación en la que conservaría SQL

Conservaría una base de datos SQL para gestionar
operaciones financieras, como pagos, facturas y
movimientos contables.

En este caso considero importante mantener relaciones
claras entre las tablas, utilizar claves foráneas
y garantizar la consistencia de las operaciones.

Aunque MongoDB también permite utilizar transacciones,
SQL puede ser una buena elección cuando el sistema
requiere numerosas consultas relacionales y reglas
estrictas de integridad.

## Justificación individual

Considero que no existe un único modelo de base de
datos que sea el mejor para todas las situaciones.

Para registrar iniciativas de emprendimiento utilizaría
MongoDB, porque los atributos pueden cambiar según
el sector al que pertenezca cada iniciativa.

Para manejar sesiones temporales elegiría Redis;
para consultar relaciones complejas utilizaría Neo4j;
y para grandes volúmenes de lecturas de sensores
consideraría Cassandra.

La elección depende principalmente de cómo se
organizan los datos, qué consultas se necesitan
y cuáles son las limitaciones de cada tecnología.

## Conclusión

Esta actividad me permitió comprender que los
diferentes modelos NoSQL responden a necesidades
distintas.

Para el caso principal de la Unidad de Emprendimiento
del SENA considero adecuado utilizar MongoDB,
porque facilita el almacenamiento de documentos
con atributos variables.
