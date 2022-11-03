print("¿Qué deseas realizar?\n")
print("Opción 1: De peso colombiano a Dolar\n")
print("Opción 2: De dolar a peso colombiano\n")
opcion = input()

dinero = float(input("¿Cuánto dinero quieres cambiar?"))
if(int(opcion) == 1):
    valor_dolar = 4900
    dolares = dinero / valor_dolar
    print("Tienes en total "+ str(round(dolares, 2))+ " dólares")
elif int(opcion)==2:
    peso_colombiano = 1/4900
    pesos_colombianos = dinero / peso_colombiano
    print("Tienes en total "+ str(round(pesos_colombianos, 2))+ " pesos colombianos")
else:
    print("No escogiste ninguna de las opciones")
