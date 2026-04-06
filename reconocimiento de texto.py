import requests
import PyPDF2
import tkinter as tk
from tkinter import filedialog

def guardar_resultado(texto):
    with open("resultado.txt", "w", encoding="utf-8") as archivo:
        archivo.write(texto)

def analizar_pdf():
    ruta = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    
    if not ruta:
        return
    
    texto = ""
    with open(ruta, "rb") as archivo:
        lector = PyPDF2.PdfReader(archivo)
        for pagina in lector.pages:
            contenido = pagina.extract_text()
            if contenido:
                texto += contenido

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
    resultado = data["response"].strip()

    resultado_texto.delete(1.0, tk.END)
    resultado_texto.insert(tk.END, resultado)

    guardar_resultado(resultado)

# Ventana
ventana = tk.Tk()
ventana.title("Analizador de Documentos con IA")
ventana.geometry("600x500")

# Botón
btn = tk.Button(ventana, text="Seleccionar PDF y Analizar", command=analizar_pdf)
btn.pack(pady=10)

# Área de texto
resultado_texto = tk.Text(ventana, wrap="word")
resultado_texto.pack(expand=True, fill="both")

ventana.mainloop()