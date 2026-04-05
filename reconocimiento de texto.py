import requests
import PyPDF2

ruta = input("Ingrese la ruta del archivo PDF: ")

# Leer PDF
texto = ""
with open(ruta, "rb") as archivo:
    lector = PyPDF2.PdfReader(archivo)
    
    for pagina in lector.pages:
        texto += pagina.extract_text()

# Prompt
prompt = f"""
Analiza el siguiente documento y responde en este formato:

Resumen: (breve)
Ideas principales: (en lista)
Conclusión: (corta)

Documento:
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

print("\n--- ANÁLISIS DEL PDF ---")
print(resultado.strip())