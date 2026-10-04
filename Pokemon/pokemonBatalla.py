from random import choice 
from time import sleep


def esperar():
    print("\n...")
    sleep(1)



def elegir_pokemon(nombre: str, tipo: str, hp: int, ad: int) -> dict:
    return {
        "nombre": nombre.capitalize(),
        "tipo": tipo.capitalize(),
        "hp": hp,
        "ad": ad
    }


def damage(pokemon: dict, hp_lost: int):
    pokemon["hp"] = pokemon["hp"] - hp_lost



def attack(atacante: dict, rival: dict):
 
    if atacante['tipo'] == 'electrico':
        ataque = 'Impactrueno'
    elif atacante['tipo'] == 'planta':
        ataque = 'látigo cepa'
    elif atacante['tipo'] == 'fuego':
        ataque = 'ascuas'
    else:
        ataque = 'pistola agua'
 
    damage(rival, atacante['ad'])
 
    print(f"\n({atacante['nombre']}) Ataca con {ataque} | -{atacante['ad']}")



pikachu = elegir_pokemon('pikachu', 'electrico', 35, 55)
bulbasaur = elegir_pokemon('bulbasaur', 'planta', 45, 65)
charmander = elegir_pokemon('charmander', 'fuego', 39, 60)
squirtle = elegir_pokemon('squirtle', 'agua', 44, 50)

















