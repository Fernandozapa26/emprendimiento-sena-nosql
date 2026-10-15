"""Conexión autenticada a MongoDB.

Las credenciales se leen de variables de entorno (.env), nunca del código.
"""
import os
from urllib.parse import quote_plus

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()


def construir_uri():
    host = os.getenv("MONGO_HOST", "127.0.0.1")
    puerto = os.getenv("MONGO_PORT", "27017")
    base = os.getenv("MONGO_DB", "emprendimiento_sena_lab")
    usuario = os.getenv("MONGO_USER")
    clave = os.getenv("MONGO_PASSWORD")
    base_auth = os.getenv("MONGO_AUTH_DB", base)

    if not usuario or not clave:
        raise RuntimeError(
            "Faltan MONGO_USER o MONGO_PASSWORD. Copia .env.example a .env y complétalo."
        )

    # quote_plus evita errores si la contraseña tiene caracteres especiales
    return (
        f"mongodb://{quote_plus(usuario)}:{quote_plus(clave)}"
        f"@{host}:{puerto}/{base}?authSource={base_auth}"
    )


def conectar():
    """Retorna (cliente, db). Recuerda cerrar el cliente con cliente.close()."""
    # tz_aware=True: las fechas vuelven como datetime con zona UTC
    cliente = MongoClient(
        construir_uri(), serverSelectionTimeoutMS=5000, tz_aware=True
    )
    db = cliente[os.getenv("MONGO_DB", "emprendimiento_sena_lab")]
    return cliente, db
