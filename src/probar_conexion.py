"""Verifica conectividad (ping) y permisos reales de lectura/escritura.

El ping solo prueba la conexión; por eso también se escribe y se lee un documento.
"""
from datetime import datetime, timezone

from conexion import conectar


def main():
    cliente, db = conectar()
    try:
        print("Ping:", db.command("ping"))
        print("Base de datos:", db.name)

        col = db["conexion_prueba"]
        col.update_one(
            {"_id": "PRUEBA-001"},
            {"$set": {"verificado_en": datetime.now(timezone.utc)}},
            upsert=True,
        )
        print("Lectura/escritura OK:", col.find_one({"_id": "PRUEBA-001"}))
    finally:
        cliente.close()


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        # Solo el mensaje: nunca se imprime la URI (contiene la contraseña).
        print("Error de conexión:", err)
        raise SystemExit(1)
