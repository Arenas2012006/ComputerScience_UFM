from random import choice, random, sample 
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


def damage(pokemon: dict, hp_lost: int):
    pokemon['hp'] = max(0, pokemon['hp'] - hp_lost)


def calcular_efectividad(tipo_atacante: str, tipo_defensor: str) -> float:
    return TABLA_TIPOS[tipo_atacante][tipo_defensor]


def attack(atacante: dict, rival: dict):
    ataque = ATAQUES[atacante['tipo']]
    print(f"\n({atacante['nombre']}) usa {ataque}!")

    if random() < PROB_FALLO:
        print(f"¡El ataque de {atacante['nombre']} falló!")
        return


    efectividad = calcular_efectividad(atacante['tipo'], rival['tipo'])
    dano = atacante['ad'] * efectividad

    es_critico = random() < PROB_CRITICO
    if es_critico:
        dano = dano * MULT_CRITICO
 
    dano = int(dano)
    damage(rival, dano)

    if es_critico:
        print('¡Golpe crítico!')
    if efectividad > 1:
        print('¡Es súper eficaz!')
    elif efectividad < 1:
        print('No es muy eficaz...')

    print(f"-{dano} HP para {rival['nombre']}")


    








