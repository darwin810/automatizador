import requests

sintomas = input("ingrese sintomas del pasiente:")
prompt = f"Eres un sistema médico. Analiza los síntomas y responde SOLO con la especialidad médica NO expliques nada: {sintomas}"
response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }
)
data = response.json()
especialidad = data["response"]

medico = ("DR.pepe diaz")
hora = ("10:00am")

print("\n--- Cita General---")
print("Especialidad:", especialidad.strip())
print("Doctor:", medico)
print("Hora:", hora)