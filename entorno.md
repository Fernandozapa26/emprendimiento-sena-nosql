# Registro del entorno (A4)

> Completa este archivo con tus datos reales. **No escribas contraseñas.**

| Elemento | Valor |
| --- | --- |
| Sistema operativo | _(completar)_ |
| Python | _(python3 --version)_ |
| Git | _(git --version)_ |
| mongosh | _(mongosh --version)_ |
| Servidor MongoDB | _(completar)_ |
| Base de datos | emprendimiento_sena_lab |
| Usuario (sin contraseña) | aprendiz_nosql |

## Pasos y comandos ejecutados

1. `mongosh --version` → _(resultado)_
2. Conexión:
   ```
   mongosh "mongodb://127.0.0.1:27017/emprendimiento_sena_lab" \
     --username aprendiz_nosql \
     --authenticationDatabase emprendimiento_sena_lab
   ```
   → _(resultado)_
3. `db.runCommand({ping: 1})` → _(resultado)_
4. `mongosh ... --file scripts/01_explorar.js` → _(documento, conteo 1, true)_
5. `python3 src/probar_conexion.py` → _(resultado)_
6. `python3 src/explorar.py` → _(resultado)_

## Errores encontrados y cómo se corrigieron

_(completar: al menos una dificultad resuelta)_



## Actividad A4 - Verificación del entorno MongoDB

### 1. Entorno utilizado

- Sistema operativo: Windows 10.
- Base de datos: MongoDB Server 8.0.11.
- Consola MongoDB: mongosh 2.5.3.
- Editor de código: Visual Studio Code.
- Base de datos de práctica: emprendimiento_sena_lab.
- Usuario de práctica: aprendiz_nosql.

Las versiones de Python y Git se registran mediante
los comandos de verificación correspondientes.

### 2. Conexión a MongoDB

Se realizó una conexión local a MongoDB utilizando
un usuario de práctica con permisos de lectura y
escritura sobre la base de datos del laboratorio.

La conexión se comprobó mediante una operación ping,
la consulta del nombre de la base de datos y la
inserción de un documento de prueba.

Por seguridad, no se incluyen contraseñas en
este documento ni en el repositorio.

### 3. Exploración de documentos

Se ejecutaron los siguientes archivos:

- scripts/01_explorar.js
- scripts/02_explorar_alimentos.js

Los scripts permitieron crear y consultar documentos
demostrativos de iniciativas y asesorías.

### 4. Tipos de datos identificados

- Cadena: nombre, codigo, sector y estado.
- Booleano: requiere_seguimiento.
- Arreglo: temas.
- Subdocumento: información agrupada dentro
  de un documento.
- Fecha: valor almacenado como tipo Date.

La ejecución permitió comprobar que las fechas
se almacenaron como Date y no como cadenas.

### 5. Diferencia con el modelo definitivo

Los documentos creados durante la exploración
son ejemplos utilizados para conocer MongoDB.

Todavía no representan el modelo definitivo porque
falta diseñar las colecciones de emprendedores,
iniciativas y asesorías, establecer validaciones,
relaciones y reglas de integridad.

### 6. Dificultad encontrada

Inicialmente no fue posible conectar con MongoDB
porque el servidor local no estaba iniciado.

Se solucionó preparando el directorio de datos
e iniciando el servicio mongod.

Posteriormente se configuró el usuario de práctica
y se realizó la conexión utilizando sus credenciales.

### 7. Evidencias

- evidencias/01_exploracion_mongodb.png
- evidencias/02_exploracion_alimentos.png

Las capturas muestran la ejecución de los scripts
y los resultados obtenidos.

### 8. Conclusión

Esta actividad me permitió comprender cómo conectar
con MongoDB, ejecutar scripts de exploración y
reconocer los tipos de datos utilizados en documentos.

También comprendí la importancia de proteger
las credenciales y documentar los resultados
para que otra persona pueda reproducir la práctica.

