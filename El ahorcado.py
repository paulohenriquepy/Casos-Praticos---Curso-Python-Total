from random import choice

def sortear_palavras():

    frutas = ['manga', 'abacaxi', 'banana', 'graviola', 'sapoti']

    palavra_secreta = choice(frutas)
    numero_de_linhas = '-' * len(palavra_secreta)

    print(f"Olha esta dica sobre a palavra secreta: {numero_de_linhas}")
    print("Você terá 6 tentativas para acertar.")


    return palavra_secreta

def pedir_letra():

    alfabeto = 'a b c d e f g h i j l m n o p q r s t u v x z'
    alfabeto_separado = alfabeto.split()
    lista_alfabeto = list(alfabeto_separado)

    letra_ingressada = 'y'

    while letra_ingressada not in lista_alfabeto:
        letra_ingressada = input("Diga apenas uma letra do alfabeto brasileiro (sem k, w ou y): ")

        if len(letra_ingressada) > 1:
            letra_ingressada = input("Diga apenas uma letra do alfabeto brasileiro (sem k, w ou y): ")
    else:
        print("Espere. Eu vou analisar a letra que você inseriu.")

    return letra_ingressada

def conferir_letra(letra_ingressada, palavra_secreta, letras_incorretas, numero_de_vidas, revelacao):


    linhas_em_listas = list(revelacao)
    resultado = revelacao

    if letra_ingressada in palavra_secreta:

        indices = [i for i, letra in enumerate(palavra_secreta) if letra == letra_ingressada]
        for indice in indices:
            linhas_em_listas[indice] = letra_ingressada
            resultado = ''.join(linhas_em_listas)

        print(f"Você agora possui {numero_de_vidas} vidas.")


    else:
        letras_incorretas.append(letra_ingressada)
        print(f"A letra {letra_ingressada} não faz parte da palavra secreta.")
        print(f"As letras incorretas são {letras_incorretas}.")
        numero_de_vidas = numero_de_vidas - 1
        print(f"Você agora possui {numero_de_vidas} vidas.")

    lista = numero_de_vidas, resultado

    return lista

def verificar_vitoria(lista, palavra):

    numero_de_vidas = lista[0]
    palavra_intermediaria = lista[1]

    if palavra_intermediaria == palavra:
        print("Parabéns. Você acertou a palavra secreta.")
        return True

    else:
        print("Você ainda não acertou a palavra secreta.")

        return False


letras_incorretas = []

numero_de_vidas = 6

palavra = sortear_palavras()
revelacao = '-' * len(palavra)


while numero_de_vidas > 0:
     letra = pedir_letra()
     vidas = conferir_letra(letra, palavra, letras_incorretas, numero_de_vidas, revelacao)
     numero_de_vidas = vidas[0]
     revelacao = vidas[1]
     print(revelacao)
     verificacao = verificar_vitoria(vidas, palavra)

     if verificacao == True:
         print("Parabéns. Você acertou")
         break

     if numero_de_vidas == 0:
         print("Fim de jogo")
         break















