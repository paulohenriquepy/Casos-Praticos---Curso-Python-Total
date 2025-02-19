from random import randint

numero_aleatorio = randint(1, 100)

# Tenho a vaga lembrança de que esse while vem aqui em cima

nome = input("Qual teu nome, amigo? ")
print(f"Então, amigo {nome}. Você tem 8 chances para acertar um número entre 1 e 100.")

tentativas = 1

while tentativas < 9:

    numero_ingressado = int(input("Diz o número, amigo: "))

    if numero_ingressado < 1 or numero_ingressado > 100:
        print("Esse valor não é permitido. Diga um número entre 1 e 100.")

        tentativas = tentativas + 1

    elif numero_ingressado < numero_aleatorio:
        print("Errou. Você disse um número menor do que o número secreto.")
        tentativas = tentativas + 1

    elif numero_ingressado > numero_aleatorio:
        print("Errou. Você disse um número maior do que o número secreto.")
        tentativas = tentativas + 1

    elif numero_ingressado == numero_aleatorio:
        print(f"Você acertou em {tentativas} tentativas. Arrasou, veado!")
        tentativas = 9
else:
    print(f"O número secreto era {numero_aleatorio}.")


