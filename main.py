"""
Interaccion con Gemini desde la terminal

Documentacion oficial: https://ai.google.dev/gemini-api/docs
"""

import requests
from api_key import API_KEY




# CONSTANTES 
MODEL = "gemini-3.6-flash"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"
VERBOSE = False

# print de configuracion API KEY
if VERBOSE:
    print(f'\n================================')
    print(f'API KEY: {API_KEY}')
    print(f'GEMINI MODEL: {MODEL}')
    print(f'\n================================')


# Construir header con API KEY
headers = {
    "Content-Type": "application/json",
    "x-goog-api-key": API_KEY,
}


# ------------ Arriba: constante | abajo: dinamico o variante 

# ciclo interactivo con Gemini
while True:
    print ('\n=============== Gemini ===============')
    user_prompt = input('En qué piensas? (Ingresa tu prompt o "salir" para terminar la sesion): ')

    # revisa si el usuario desea salir
    if user_prompt.lower().strip() == "salir":
        print("Saliendo de la sesion...")
        break


    # Construir el body del request. 
    body = {
        "contents": [
            {
                "parts": [
                    {"text": user_prompt}
                ]
            }
        ]
    }

    # Realizar request POST 
    respuesta = requests.post(URL, headers=headers, json=body)


    if VERBOSE:
        print("Status code:", respuesta.status_code)

    if respuesta.status_code != 200:
        print("Algo salio mal:")
        print(respuesta.text)
    else:
        datos = respuesta.json()

        # La respuesta de Gemini viene anidada varios niveles:
        # datos -> candidates -> [0] -> content -> parts -> [0] -> text
        respuesta_gemini = datos["candidates"][0]["content"]["parts"][0]["text"]
        print("\nRespuesta de Gemini:\n")
        print(respuesta_gemini)




