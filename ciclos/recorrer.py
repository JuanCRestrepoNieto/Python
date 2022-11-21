def solicitarNombre():
    nombre = input('Ingrese tu nombre: ')
    return nombre


def recorrerCadena(cadena):
    for letra in cadena:
        print(letra)


def run():
    nombre = solicitarNombre()
    recorrerCadena(nombre)


if __name__ == '__main__':
    run()