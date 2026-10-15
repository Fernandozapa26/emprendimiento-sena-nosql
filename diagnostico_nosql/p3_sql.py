
import sqlite3

# Crear base de datos temporal en memoria
conexion = sqlite3.connect(":memory:")

# Crear tablas e insertar datos
conexion.executescript("""
CREATE TABLE emprendedores(
    id INTEGER PRIMARY KEY,
    alias TEXT
);

CREATE TABLE iniciativas(
    id INTEGER PRIMARY KEY,
    emprendedor_id INTEGER,
    estado TEXT
);

INSERT INTO emprendedores VALUES
(1, 'Emprendedor A'),
(2, 'Emprendedor B'),
(3, 'Emprendedor C');

INSERT INTO iniciativas VALUES
(101, 1, 'activa'),
(102, 2, 'archivada'),
(103, 1, 'activa');
""")

# Consultar iniciativas activas y sus responsables
consulta = """
SELECT iniciativas.id, emprendedores.alias
FROM iniciativas
INNER JOIN emprendedores
ON iniciativas.emprendedor_id = emprendedores.id
WHERE iniciativas.estado = 'activa'
ORDER BY iniciativas.id;
"""

print("=== INICIATIVAS ACTIVAS ===")

resultados = conexion.execute(consulta).fetchall()

for resultado in resultados:
    print(resultado)

print("\n=== EXPLICACION ===")
print("Se utilizo INNER JOIN para relacionar las dos tablas.")
print("La relacion se realiza mediante emprendedor_id.")
print("WHERE permite mostrar solamente las iniciativas activas.")
print("ORDER BY organiza los resultados por identificador.")

conexion.close()
