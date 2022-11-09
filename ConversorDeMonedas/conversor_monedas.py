def convertir_moneda(valor_dolar):
    dinero = float(input("¿Cuánto dinero quieres cambiar?"))
    dolares = dinero/valor_dolar
    print("Tienes en total "+ str(round(dolares, 2))+ " dólares")

menu = """"
            Bienvenido al conversor de monedas🐱‍🐉
            1. Peso colombiano
            2. Peso argentino
            3. Peso mexicano
            Elige una opción
        """
print(menu)

opcion = input()

if(int(opcion) == 1):
    convertir_moneda(4960.79)
elif (int(opcion) == 2):
    convertir_moneda(160.05)
elif (int(opcion) == 3):
    convertir_moneda(19.59)
else:
    print("No escogiste ninguna opción")
