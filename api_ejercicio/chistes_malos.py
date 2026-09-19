
import requests
seguir = True 
 
def obtener_chiste():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
 
while seguir:
    chiste = obtener_chiste()
    print(chiste["setup"])
    print(chiste["punchline"])
 
    respuesta = input("\nQuieres otro chiste? (s/n): ")
 
    if respuesta.lower() != "s":
        seguir = False  # con esto se rompe el while
 
print("Listo, hasta luego")
 


