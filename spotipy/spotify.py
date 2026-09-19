import requests
import webbrowser
import base64
import time
from api_key_spotify import CLIENT_ID
from api_key_spotify import SECRET_CLIENT

CLIENT_ID = CLIENT_ID 
CLIENT_SECRET = SECRET_CLIENT 
REDIRECT_URI = "http://127.0.0.1:8888/callback"
 
SCOPES = (
    "user-read-currently-playing "
    "user-modify-playback-state "
    "user-top-read"
)
 
url_login = (
    "https://accounts.spotify.com/authorize"
    "?client_id=" + CLIENT_ID +
    "&response_type=code"
    "&redirect_uri=" + REDIRECT_URI +
    "&scope=" + SCOPES
)
 
print("Se va a abrir el navegador, inicia sesion y da permiso")
webbrowser.open(url_login)
 
print("La pagina va a dar error, no importa, copia la URL de arriba")
url_con_code = input("Pega la URL aqui: ")
code = url_con_code.split("code=")[1]
 
auth = base64.b64encode((CLIENT_ID + ":" + CLIENT_SECRET).encode()).decode()
 
respuesta_token = requests.post(
    "https://accounts.spotify.com/api/token",
    headers={"Authorization": "Basic " + auth},
    data={
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
    },
)
 
token = respuesta_token.json()["access_token"]
headers = {"Authorization": "Bearer " + token}
 
historial = []
cancion_anterior = ""
id_cancion_actual = None
 
 
def mostrar_cancion_actual():
    global cancion_anterior, id_cancion_actual
 
    r = requests.get(
        "https://api.spotify.com/v1/me/player/currently-playing",
        headers=headers,
    )
 
    if r.status_code != 200 or r.text == "":
        print("No hay nada sonando ahorita")
        id_cancion_actual = None
        return
 
    data = r.json()
    nombre = data["item"]["name"]
    artista = data["item"]["artists"][0]["name"]
    album = data["item"]["album"]["name"]
    id_cancion_actual = data["item"]["id"]
 
    progreso_ms = data["progress_ms"]
    duracion_ms = data["item"]["duration_ms"]
    min_prog = progreso_ms // 60000
    seg_prog = (progreso_ms // 1000) % 60
    min_dur = duracion_ms // 60000
    seg_dur = (duracion_ms // 1000) % 60
 
    porcentaje = progreso_ms / duracion_ms
    llenado = int(porcentaje * 20)
    barra = "#" * llenado + "-" * (20 - llenado)
 
    print("\n" + "=" * 40)
    print(" AHORA SUENA")
    print("=" * 40)
    print(" Cancion:", nombre)
    print(" Artista:", artista)
    print(" Album:  ", album)
    print(" [" + barra + "]", f"{min_prog}:{seg_prog:02d} / {min_dur}:{seg_dur:02d}")
    print("=" * 40)
 
    if nombre != cancion_anterior:
        historial.append(nombre + " - " + artista)
        cancion_anterior = nombre
 
 
def pausar():
    requests.put("https://api.spotify.com/v1/me/player/pause", headers=headers)
    print("Pausado")
 
 
def reanudar():
    requests.put("https://api.spotify.com/v1/me/player/play", headers=headers)
    print("Reanudado")
 
 
def siguiente_cancion():
    requests.post("https://api.spotify.com/v1/me/player/next", headers=headers)
    print("Saltando a la siguiente cancion")
 
 
def ver_top_canciones():
    r = requests.get(
        "https://api.spotify.com/v1/me/top/tracks?limit=5",
        headers=headers,
    )
    data = r.json()
    print("\nTus 5 canciones mas escuchadas:")
    for i, cancion in enumerate(data["items"], start=1):
        print(f" {i}. {cancion['name']} - {cancion['artists'][0]['name']}")
 
 
def mostrar_resumen():
    print("\n" + "=" * 40)
    print(" RESUMEN DE LA SESION")
    print("=" * 40)
    print(" Canciones distintas escuchadas:", len(historial))
    for cancion in historial:
        print(" -", cancion)
    print("=" * 40)
 
 
while True:
    mostrar_cancion_actual()
 
    print("\nQue quieres hacer?")
    print(" [enter] = revisar cancion de nuevo")
    print(" p = pausar")
    print(" r = reanudar")
    print(" n = siguiente cancion")
    print(" t = ver mis top 5 canciones")
    print(" q = salir")
 
    opcion = input("Opcion: ").lower()
 
    if opcion == "p":
        pausar()
    elif opcion == "r":
        reanudar()
    elif opcion == "n":
        siguiente_cancion()
    elif opcion == "t":
        ver_top_canciones()
    elif opcion == "q":
        mostrar_resumen()
        break
 