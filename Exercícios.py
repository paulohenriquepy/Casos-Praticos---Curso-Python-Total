# Ejercicio 1


def devolver_distintos(num1, num2, num3):

    lista_numeros = [int(num1), int(num2), int(num3)]

    valor_mayor = max(lista_numeros)

    valor_menor = min(lista_numeros)

    valor_intermedio = sorted(lista_numeros)[1]

    if sum(lista_numeros) > 15:
        return valor_mayor

    elif sum(lista_numeros) < 10:
        return valor_menor

    else:
        return valor_intermedio



# Ejercicio 2

def fatiar_palabra(palabra):

    palabra_fatiada = list(palabra)

    letras_ordenadas = sorted(palabra_fatiada)

    lista_final = []

    for letra in letras_ordenadas:
        if letra not in lista_final:
            lista_final.append(letra)


    return lista_final


def verificacion(*args):

    sequencia = list(args)

    for i in range(len(sequencia) - 1):  # Garante que i+1 não ultrapasse o tamanho da lista
        if sequencia[i] == 0 and sequencia[i + 1] == 0:
            return True  # Retorna True assim que encontrar dois zeros consecutivos

    return False  # Retorna False se não encontrar dois zeros consecutivos


def contar_primos(numero):

    primos = [2]

    iteracion = 3

    if numero < 2:
        return 0

    while iteracion <= numero:

        for n in range(3, iteracion, 2):

            if iteracion % n == 0:
                iteracion += 2
                break


        else:
            primos.append(iteracion)
            iteracion += 2

    print(primos)

    return len(primos)





