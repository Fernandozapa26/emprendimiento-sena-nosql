
import json

# JSON original con errores
texto_original = '{"codigo":"INI-001", "activa":True, "intereses":["Validar mercado",]}'

print("=== JSON ORIGINAL ===")

try:
    json.loads(texto_original)
except json.JSONDecodeError as error:
    print("Error encontrado:", error)

# JSON corregido
texto_corregido = '{"codigo":"INI-001", "activa":true, "intereses":["Validar mercado"]}'

datos = json.loads(texto_corregido)

print("\n=== JSON CORREGIDO ===")
print("Codigo:", datos["codigo"])
print("Activa:", datos["activa"])
print("Tipo de codigo:", type(datos["codigo"]).__name__)
print("Tipo de activa:", type(datos["activa"]).__name__)

print("\n=== EXPLICACION ===")
print("Se cambio True por true porque JSON utiliza booleanos en minuscula.")
print("Se elimino la coma adicional del arreglo intereses.")
