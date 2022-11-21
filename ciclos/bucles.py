def mostrar_potencias(numero, limite):
    contador = 0
    potencia = numero**contador
    while(potencia <= limite):
        print('2 elevado a la '+str(contador)+' es igual a :'+str(potencia) + '\n')
        contador = contador + 1
        potencia = numero**contador


def run(): 
    LIMITE = 1000
    mostrar_potencias(2, LIMITE)


if __name__ == '__main__':
    run()