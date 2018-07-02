
apetece_helado_input = input("¿Te apetece un helado? ¿Si/No?: ").upper()

if apetece_helado_input == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
else:
    print("Te he dicho que me digas si o no. Como no te entiendo pondre no")
    apetece_helado = False
tienes_dinero_input = input("¿Tienes dinero para un helado? ¿Si/No?: ").upper()

if tienes_dinero_input == "SI":
    tienes_dinero = True
elif tienes_dinero_input == "NO":
    tienes_dinero = False
else:
    print("Te he dicho que me digas si o no. Como no te entiendo pondre no")
    tienes_dinero = False


hay_helados_input = input("¿Hay helados? ¿Si/No?: ").upper()

if hay_helados_input == "SI":
    hay_helados = True
elif hay_helados_input == "NO":
    hay_helados = False
else:
    print("Te he dicho que me digas si o no. Como no te entiendo pondre no")
    hay_helados = False

esta_tu_tia_input = input("¿Estas con tu tia? ¿Si/No?: ").upper()

if esta_tu_tia_input == "SI":
    esta_tu_tia = True
elif esta_tu_tia_input == "NO":
    esta_tu_tia = False
else:
    print("Te he dicho que me digas si o no. Como no te entiendo pondre no")
    esta_tu_tia = False

puedes_permitirtelo = tienes_dinero_input == "SI" or esta_tu_tia_input == "SI"

if apetece_helado == True and puedes_permitirtelo == True and hay_helados == True:
    print("Pues cometelo")
else:
    print("Pues na")
