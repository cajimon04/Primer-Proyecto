operacion = input("Que operacion quieres hacer (Sumar / Restar / Multiplicar / Dividir)").upper()
if operacion == "SUMAR":
    primer_valor = int(input("Introduzca el primer valor"))
    segundo_valor = int(input("Introduzca el segundo valor"))
    print("Primer valor: {}".format(primer_valor))
    print("Segundo valor: {}".format(segundo_valor))
    resultado = primer_valor + segundo_valor
    print("Resultado: {}".format(resultado))
if operacion == "RESTAR":
    primer_valor = int(input("Introduzca el primer valor"))
    segundo_valor = int(input("Introduzca el segundo valor"))
    print("Primer valor: {}".format(primer_valor))
    print("Segundo valor: {}".format(segundo_valor))
    resultado = primer_valor - segundo_valor
    print("Resultado: {}".format(resultado))
if operacion == "MULTIPLICAR":
    primer_valor = int(input("Introduzca el primer valor"))
    segundo_valor = int(input("Introduzca el segundo valor"))
    print("Primer valor: {}".format(primer_valor))
    print("Segundo valor: {}".format(segundo_valor))
    resultado = primer_valor * segundo_valor
    print("Resultado: {}".format(resultado))
if operacion == "DIVIDIR":
    primer_valor = int(input("Introduzca el primer valor"))
    segundo_valor = int(input("Introduzca el segundo valor"))
    print("Primer valor: {}".format(primer_valor))
    print("Segundo valor: {}".format(segundo_valor))
    resultado = primer_valor / segundo_valor
    print("Resultado: {}".format(resultado))
print("FIN")