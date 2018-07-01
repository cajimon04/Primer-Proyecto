numero_ganador = 13
numero_del_usuario = int(input("Dime un numero del 1 al 15: "))
if numero_del_usuario == numero_ganador:
    print ("Has ganado")

else:
    print ("Te quedan 4 intentos")
numero_del_usuario_2 = int(input("Dime un numero del 1 al 15: "))

if numero_del_usuario_2 == numero_ganador:
    print("Has ganado")

else:
    print("Te quedan 3 intentos")
numero_del_usuario_3 = int(input("Dime un numero del 1 al 15: "))

if numero_del_usuario_3 == numero_ganador:
    print("Has ganado")

else:
    print(" Te quedan 2 intentos")
numero_del_usuario_4 = int (input("Dime un numero del 1 al 15: "))

if numero_del_usuario_4 == numero_ganador:
    print("Has ganado")

else:
    print("Es tu ultimo intento")
numero_del_usuario_5 = int (input("Dime un número del 1 al 15: "))

if numero_del_usuario_5 == numero_ganador:
    print ("Has ganado")

else:
    print("Has perdido")