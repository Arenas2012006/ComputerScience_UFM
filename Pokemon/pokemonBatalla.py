from random import choice 
from time import sleep


def esperar():
    print("\n...")
    sleep(1)


ATAQUES = { 
    "electrico": "Impactrueno",
    "planta": "Latigo cepa", 
    "fuego": "Ascuas",
    "agua": "Pistola agua",
}


TABLA_TIPOS = {
    'electrico': {'electrico': 0.5, 'planta': 0.5, 'fuego': 1.0, 'agua': 2.0},
    'planta':    {'electrico': 1.0, 'planta': 0.5, 'fuego': 0.5, 'agua': 2.0},
    'fuego':     {'electrico': 1.0, 'planta': 2.0, 'fuego': 0.5, 'agua': 0.5},
    'agua':      {'electrico': 1.0, 'planta': 0.5, 'fuego': 2.0, 'agua': 0.5},
}


PROB_CRITICO = 0.10    
MULT_CRITICO = 1.5
PROB_FALLO = 0.10


def crear_pokemon(nombre: str, tipo: str, hp: int, ad: int) -> dict:
    return {
        'nombre': nombre.capitalize(),
        'tipo': tipo.capitalize(),
        'hp': hp,
        'hp_max': hp,
        'ad': ad,
    }







