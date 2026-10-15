1. ¿Qué representan una tabla, una fila y una clave primaria?
Una tabla es donde se organiza y almacena la información en una base de datos. Una fila representa un registro específico y una clave primaria es un identificador único que permite diferenciar un registro de los demás.
Por ejemplo, en una tabla de iniciativas de emprendimiento podemos guardar el código, nombre y sector de cada proyecto. Cada fila sería una iniciativa diferente y el código sería su clave primaria.
2. ¿Para qué sirve una clave foránea? ¿Qué problema genera una iniciativa que referencia a un emprendedor inexistente?
Una clave foránea sirve para relacionar la información de dos tablas. Por ejemplo, permite saber a qué emprendedor pertenece una iniciativa.
Si una iniciativa tiene registrado un emprendedor que no existe en la base de datos, se genera un problema porque la información queda relacionada incorrectamente y no podríamos identificar al responsable del proyecto. Esto afecta la integridad de los datos.
3. ¿Qué devuelve SELECT codigo FROM iniciativas WHERE sector = 'tecnologia';? ¿Modifica registros?
Esta consulta permite buscar todas las iniciativas que pertenecen al sector de tecnología y mostrar únicamente sus códigos.
No modifica ningún registro porque la instrucción SELECT solamente se utiliza para consultar información de la base de datos.

4. ¿Cuál es la diferencia entre una lista y un diccionario en Python? ¿Qué estructura utilizarías para una iniciativa y para varias iniciativas?
Una lista permite almacenar varios elementos en un orden determinado, mientras que un diccionario guarda información mediante claves y valores.
Para representar una iniciativa utilizaría un diccionario, porque puedo guardar datos como el código, nombre y sector. Para almacenar varias iniciativas utilizaría una lista de diccionarios.
5. ¿Son equivalentes false y "false" en JSON? Explica el tipo de cada valor.
No son iguales. false es un valor booleano que representa falso, mientras que "false" es una cadena de texto porque está escrita entre comillas.
Aunque se parecen, representan tipos de datos diferentes.
6. ¿Cuál es la diferencia entre un campo ausente, un campo con null y un campo con una cadena vacía?
Un campo ausente significa que ese dato no existe dentro del documento. Un campo con null indica que el campo existe, pero no tiene un valor definido. Una cadena vacía "" significa que el campo contiene un texto sin caracteres.

7. ¿Qué ventaja tiene una función que retorna datos frente a otra que únicamente los imprime?
Una función que retorna datos permite utilizar esos resultados en otras partes del programa, por ejemplo, para hacer cálculos o realizar otras operaciones. En cambio, una función que solamente imprime muestra la información en pantalla, pero no devuelve un resultado que podamos utilizar directamente.
8. Si falla la lectura de un archivo JSON, ¿qué revisarías antes de cambiar el programa?
Primero revisaría que el archivo exista y que la ruta sea correcta. Después verificaría que tenga una estructura JSON válida, que las comillas estén bien colocadas, que no existan comas adicionales y que los datos estén escritos correctamente. También revisaría el mensaje de error para identificar el problema antes de modificar el código.
9. ¿Qué información reconoces en 2026-10-06T13:00:00Z? ¿Qué ambigüedades evita frente a 06/10/26 8:00?
La primera fecha indica el 6 de octubre de 2026 a las 13:00 horas, es decir, la 1:00 de la tarde en horario UTC. En Colombia corresponde a las 8:00 de la mañana.
Este formato es más claro porque permite identificar el año, mes, día, hora y zona horaria. En cambio, 06/10/26 8:00 puede generar confusiones sobre el orden del día y el mes, además de que no especifica la zona horaria.
10. Se publicó por error una contraseña en Git. ¿Qué acciones propondrías? ¿Es suficiente borrarla del archivo actual?
Lo primero que haría sería cambiar la contraseña inmediatamente para evitar que alguien pueda utilizarla. Después revisaría el repositorio para eliminar la información sensible del historial de Git y verificaría que no se hayan realizado accesos no autorizados.

No es suficiente borrarla del archivo actual porque la contraseña podría seguir apareciendo en versiones anteriores del repositorio. También agregaría los archivos que contienen contraseñas al .gitignore para evitar que se vuelvan a subir.