vida_pikachu = 100
vida_bulbasaur = 100
vida_charmander = 80
vida_squirtle = 90
dano_pikachu_chispazo = 10
dano_pikachu_voltio = 12
dano_bulbasaur = 10
dano_charmander = 7
dano_squirtle = 8
dano_enemigo = 0
nombre_pokemon = 0
print("Bienvenido a la batalla pokemon")
print("a Bulbasaur b Squirtle c Charmander")
pokemon_del_usuario = input ("Jugaras con pikachu. Elige tu contrincante").upper()
vida_enemigo = 0
if pokemon_del_usuario == "A":
    print("Has escogido a Bulbasaur")
    vida_enemigo = vida_bulbasaur
    dano_enemigo = dano_bulbasaur
    nombre_pokemon = "Bulbasaur"
elif pokemon_del_usuario == "B":
    print("Has escogido a Squirtle")
    vida_enemigo = vida_squirtle
    dano_enemigo = dano_squirtle
    nombre_pokemon = "Squirtle"

elif pokemon_del_usuario == "C":
    print("Has escogido a Charmander")
    vida_enemigo = vida_charmander
    dano_enemigo = dano_charmander
    nombre_pokemon = "Charmander"

else:
    print("Reinicia, y escribe solo la letra")

while vida_pikachu > 0 and vida_enemigo > 0:
    print("Turno de Pikachu")
    ataque_elegido = input("Elige ataque a-Chispazo(10) b-Bola voltio(12)").upper()
    if ataque_elegido == "A":
        ataque_elegido = dano_pikachu_chispazo
        vida_enemigo -= ataque_elegido
        vida_pikachu -= dano_enemigo

        print("Pikachu ha usado Chispazo")

        print("{} tiene {} puntos de vida".format(nombre_pokemon, vida_enemigo))

        print("{} te ha atacado y te ha quitado {} puntos de vida".format(vida_enemigo, dano_enemigo))

        print("Pikachu tiene {} puntos de vida".format(vida_pikachu))

    elif ataque_elegido == "B":
        ataque_elegido = dano_pikachu_voltio
        vida_enemigo -= ataque_elegido
        vida_pikachu -= dano_enemigo

        print("Pikachu ha usado Bola Voltio")

        print("{} tiene {} puntos de vida".format(nombre_pokemon, vida_enemigo))

        print("{} te ha atacado y te ha quitado {} puntos de vida".format(nombre_pokemon, dano_enemigo))

        print("Pikachu tiene {} puntos de vida".format(vida_pikachu))

    else:
        vida_pikachu -= dano_enemigo

print("El combate ha terminado")
if vida_pikachu > vida_enemigo:
    print("Has ganado")
else:
    print("Has perdido")