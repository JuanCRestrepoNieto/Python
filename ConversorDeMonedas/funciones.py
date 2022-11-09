def conversar(mensaje):
    print("Hola, cómo estás?")
    print("Elegiste la opción "+ mensaje)

opcion = input("Elige una opción (1, 2, 3): ")
if opcion == '1':
    conversar('1')
elif opcion == '2':
    conversar('2')
elif opcion == '3':
    conversar('3')