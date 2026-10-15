# Unidad de Emprendimiento del SENA — Bases de Datos NoSQL (Semana 1)

Programa: Tecnología en Análisis y Desarrollo de Software (ADSO) · Centro CTMA
Instructor: Wilson Castro Gil
Aprendiz(ces): _(escribir nombre(s))_ · Ficha: _(por definir)_

Proyecto de ejemplo de la **Semana 1** (diagnóstico y fundamentos NoSQL). Simula el registro de emprendedores, iniciativas y asesorías de una Unidad de Emprendimiento. **Todos los datos son ficticios**; no representan procesos reales del SENA.

## Contenido del repositorio

```
├── README.md              ← este archivo
├── entorno.md             ← registro del entorno (versiones, comandos, resultados)
├── .env.example           ← plantilla de variables (sin secretos)
├── .gitignore
├── requirements.txt
├── src/
│   ├── conexion.py        ← conexión autenticada a MongoDB (pymongo)
│   ├── probar_conexion.py ← ping + prueba de lectura/escritura
│   └── explorar.py        ← inserta y verifica los documentos demo
├── scripts/
│   └── 01_explorar.js     ← versión para mongosh (sección 5.7 de la guía)
├── docs/
│   ├── matriz_modelos.md  ← A2: comparación de modelos NoSQL
│   ├── consultas_Q01_Q06.md ← A3: consultas previstas
│   └── reglas.md          ← A3: reglas, preguntas a la unidad y riesgo
└── evidencias/            ← resultados y capturas (sin secretos)
```

## Requisitos

- Python 3.9 o superior
- MongoDB autenticado con una cuenta de práctica (preparada por el instructor)
- `mongosh` (opcional pero recomendado) y MongoDB Compass (opcional)

## Cómo ejecutarlo

1. Crear el entorno virtual e instalar dependencias:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate      # En Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Crear el archivo de variables y completar la contraseña (**no se sube a Git**):
   ```bash
   cp .env.example .env
   ```
3. Probar la conexión (ping + lectura/escritura):
   ```bash
   python3 src/probar_conexion.py
   ```
4. Insertar y verificar los documentos demostrativos:
   ```bash
   python3 src/explorar.py
   ```
5. Alternativa con mongosh (escribe la contraseña en el prompt, no en el comando):
   ```bash
   mongosh "mongodb://127.0.0.1:27017/emprendimiento_sena_lab" \
     --username aprendiz_nosql \
     --authenticationDatabase emprendimiento_sena_lab \
     --file scripts/01_explorar.js
   ```

**Resultado esperado:** el documento `ASE-DEMO-001` mostrado, conteo `1` y `true` al comprobar que `fecha_programada` es `Date`.

## Seguridad

- Las credenciales están solo en `.env`, que está en `.gitignore`.
- Se usa la cuenta de práctica `aprendiz_nosql`, no la cuenta administrativa.
- Nunca se imprime ni se comparte una URI con credenciales.

## Entregables de la Semana 1 (E01)

| Entregable | Dónde está |
| --- | --- |
| Matriz de selección de modelos (A2) | `docs/matriz_modelos.md` |
| Consultas Q01–Q06 (A3) | `docs/consultas_Q01_Q06.md` |
| Reglas, dos preguntas a la unidad y un riesgo (A3) | `docs/reglas.md` |
| Registro del entorno (A4) | `entorno.md` |
| Script de exploración | `scripts/01_explorar.js` y `src/explorar.py` |
| README | este archivo |

## Preguntas del diagnóstico teórico (A1 — Parte A)

> Respuestas propias, escritas antes de consultar soluciones. Si no sé algo, indico qué parte no comprendo.

**1. ¿Qué representan una tabla, una fila y una clave primaria? Utiliza un ejemplo relacionado con las iniciativas de emprendimiento.**

Respuesta: _(escribir)_

**2. ¿Para qué sirve una clave foránea? ¿Qué problema genera una iniciativa que referencia a un emprendedor inexistente?**

Respuesta: _(escribir)_

**3. Explica qué devuelve `SELECT codigo FROM iniciativas WHERE sector = 'tecnologia';`. ¿Modifica registros?**

Respuesta: _(escribir)_

**4. Diferencia una lista y un diccionario en Python. ¿Qué estructura utilizarías para una iniciativa y para varias iniciativas?**

Respuesta: _(escribir)_

**5. ¿Son equivalentes `false` y `"false"` en JSON? Explica el tipo de cada valor.**

Respuesta: _(escribir)_

**6. Diferencia un campo ausente, un campo con `null` y un campo con una cadena vacía. Propón un ejemplo.**

Respuesta: _(escribir)_

**7. ¿Qué ventaja tiene una función que retorna datos frente a otra que únicamente los imprime?**

Respuesta: _(escribir)_

**8. Si falla la lectura de un archivo JSON, ¿qué revisarías antes de cambiar el programa?**

Respuesta: _(escribir)_

**9. ¿Qué información reconoces en `2026-10-06T13:00:00Z`? ¿Qué ambigüedades evita frente a `06/10/26 8:00`?**

Respuesta: _(escribir)_

**10. Se publicó por error una contraseña en Git. ¿Qué acciones propondrías? ¿Es suficiente borrarla del archivo actual?**

Respuesta: _(escribir)_

## Preguntas de la exploración en MongoDB (A4 y sección 5)

**a. Identifica la cadena, el booleano, el arreglo, el subdocumento y la fecha del documento `ASE-DEMO-001`.**

Respuesta: _(escribir)_

**b. ¿Por qué la colección `asesorias_demo` no es todavía el modelo definitivo de emprendedores/iniciativas/asesorías?**

Respuesta: _(escribir)_

**c. Propón un atributo específico para una iniciativa de alimentos y otro para una de software.**

Respuesta: _(escribir)_

**d. Identifica una regla que el documento por sí solo no impone (por ejemplo, que la modalidad pertenezca a un conjunto acordado).**

Respuesta: _(escribir)_

**e. Transferencia (`ASE-DEMO-002`): ¿qué campos cambian y cuáles conservan su tipo?**

Respuesta: _(escribir)_

## Dificultad resuelta

_(describir un problema real que encontraste y cómo lo resolviste)_

## Autoevaluación

- Puedo realizar: _(completar)_
- Necesito reforzar: _(completar)_
- Mi primera acción de mejora será: _(completar)_

## Uso de herramientas de IA

Según la guía, si se usa IA después del diagnóstico se declara para qué y qué se verificó.

- Se usó IA para: estructura inicial del proyecto, código de conexión y borrador de la documentación de `docs/`.
- Lo que verifiqué/modifiqué yo: _(completar después de ejecutar y revisar)_

## Fuentes

- MongoDB. BSON Types: https://www.mongodb.com/docs/manual/reference/bson-types/
- MongoDB. Data Modeling: https://www.mongodb.com/docs/manual/data-modeling/
- MongoDB. mongosh Options: https://www.mongodb.com/docs/mongodb-shell/reference/options/
