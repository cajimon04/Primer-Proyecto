print("Bienvenido a la calculadora de Farenheit a Celsius")
temperatura_farenheit = int(input("Dime el numero de grados farenheit(Sin decimales): "))
temperatura_farenheit_32 = temperatura_farenheit
temperatura_farenheit_32 -= 32
resultado = temperatura_farenheit_32 / 1.8
print("Los grados Farenheit son: {} y los Celsius: {}".format(temperatura_farenheit, resultado))
