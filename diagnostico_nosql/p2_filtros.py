
# Ejercicio P2 - Filtrar registros con Python

iniciativas = [
    {"codigo": "INI-001", "sector": "tecnologia", "pendiente": True},
    {"codigo": "INI-002", "sector": "alimentos", "pendiente": True},
    {"codigo": "INI-003", "sector": "tecnologia", "pendiente": False},
    {"codigo": "INI-004", "sector": "tecnologia"}
]


def seleccionar_pendientes(registros, sector):
    resultado = []

    for iniciativa in registros:
        if (
            iniciativa.get("sector") == sector
            and iniciativa.get("pendiente") is True
        ):
            resultado.append(iniciativa["codigo"])

    return resultado


# Prueba 1: Con resultados
print("=== PRUEBA 1: TECNOLOGIA ===")
print(seleccionar_pendientes(iniciativas, "tecnologia"))

# Prueba 2: Sin resultados
print("\n=== PRUEBA 2: ECONOMIA CIRCULAR ===")
print(seleccionar_pendientes(iniciativas, "economia_circular"))

print("\n=== EXPLICACION ===")
print("La funcion devuelve los codigos de las iniciativas pendientes.")
print("Si falta el campo pendiente, no se considera pendiente.")
print("Se utiliza 'is True' para evitar confundir booleanos con cadenas.")
print("La lista original no se modifica.")
