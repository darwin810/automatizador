import requests

ruta = input("Ingrese la ruta del archivo .txt: ")

# Leer archivo
with open(ruta, "r", encoding="utf-8") as archivo:
    texto = archivo.read()

prompt = f"""
Analiza el siguiente texto y responde en este formato:

Resumen: (breve)
Ideas principales: (en lista)
Conclusión: (corta)

Texto:
{texto}
"""

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }
)

data = response.json()
resultado = data["response"]

print("\n--- ANÁLISIS DEL DOCUMENTO ---")
print(resultado.strip())