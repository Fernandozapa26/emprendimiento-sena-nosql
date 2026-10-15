"""Equivalente en Python de scripts/01_explorar.js (sección 5.7 de la guía).

Inserta documentos demostrativos en asesorias_demo y verifica los tipos.
"""
import json
from datetime import datetime, timezone

from conexion import conectar

FECHA = datetime(2026, 10, 8, 13, 0, 0, tzinfo=timezone.utc)  # 2026-10-08T13:00:00Z

DEMOS = [
    {
        "_id": "ASE-DEMO-001",
        "emprendedor_alias": "Emprendedor ficticio 01",
        "iniciativa": {
            "codigo": "INI-DEMO-001",
            "nombre": "EcoEmpaque",
            "sector": "economia_circular",
        },
        "temas": ["propuesta de valor", "validacion de clientes"],
        "modalidad": "virtual",
        "estado": "programada",
        "requiere_seguimiento": True,
        "fecha_programada": FECHA,
        "fecha_realizacion": None,
    },
    # Transferencia (sección 5.7): ASE-DEMO-002 con otra iniciativa y sector
    {
        "_id": "ASE-DEMO-002",
        "emprendedor_alias": "Emprendedor ficticio 02",
        "iniciativa": {
            "codigo": "INI-DEMO-002",
            "nombre": "Sabores Locales",
            "sector": "alimentos",
        },
        "temas": ["propuesta de valor", "canales de venta"],
        "modalidad": "virtual",
        "estado": "programada",
        "requiere_seguimiento": True,
        "fecha_programada": FECHA,
        "fecha_realizacion": None,
    },
]


def main():
    cliente, db = conectar()
    try:
        col = db["asesorias_demo"]
        for d in DEMOS:
            # Chequeo previo como en la guía (no es una solución de concurrencia).
            if col.count_documents({"_id": d["_id"]}) == 0:
                col.insert_one(d)
            doc = col.find_one({"_id": d["_id"]})
            print(json.dumps(doc, indent=2, ensure_ascii=False, default=str))
            print("Conteo por _id:", col.count_documents({"_id": d["_id"]}))
            print("fecha_programada es datetime (Date en BSON):",
                  isinstance(doc["fecha_programada"], datetime))
            print("---")
    finally:
        cliente.close()


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print("Error:", err)
        raise SystemExit(1)
