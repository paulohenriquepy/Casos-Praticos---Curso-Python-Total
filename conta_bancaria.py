# Programar uma conta bancária

import numpy as np

class Pessoa():

    # Atributos de instância
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


class Cliente(Pessoa):

    # Atributos de instância (cada cliente tem seus dados bancários e seu saldo)
    def __init__(self, nome, sobrenome, numero_de_conta, saldo):
        super().__init__(nome, sobrenome)
        self.numero_de_conta = numero_de_conta
        self.saldo = saldo

    # Método especial que permite imprimir o cliente e o seu saldo
    def __str__(self):
        return f'Bem vindo, {self.nome} {self.sobrenome}.\n Conta: {self.numero_de_conta}\n Seu saldo é: {self.saldo}'

    # Método sacar (método de instância)
    def sacar(self, valor):
        print(f'Você sacou {valor} reais.')
        self.saldo = self.saldo - valor
        print(f'Seu saldo agora é {self.saldo - valor} reais.')

    # Método depositar
    def depositar(self, valor):
        print(f'Você sacou {valor} reais.')
        self.saldo = self.saldo + valor
        print(f'Seu saldo agora é {self.saldo + valor} reais.')


# Função criar cliente

def criar_cliente():

    print('Bem vindo ao Banco X.')

    nome = input('Por favor, diga o seu nome: ').capitalize()
    sobrenome = input('Por favor, diga o seu último sobrenome: ').capitalize()
    nome_completo = nome + ' ' + sobrenome
    avaliar_nome_completo = nome_completo != '' and all(letra.isalpha() or letra.isspace() for letra in nome_completo)


    while avaliar_nome_completo == False:
        print('Você digitou algum símbolo incorreto.')
        print('Por favor, digite seu nome e seu sobrenome sem números ou símbolos.')
        nome = input('Por favor, diga o seu nome: ').capitalize()
        sobrenome = input('Por favor, diga o seu último sobrenome: ').capitalize()
        nome_completo = nome + ' ' + sobrenome
        avaliar_nome_completo = nome_completo != '' and all(letra.isalpha() or letra.isspace() for letra in nome_completo)

    print('Cliente registrado com sucesso.')

    print('Espere. Vamos gerar o seu número de conta.')
    rng = np.random.default_rng(12345)
    conta = rng.integers(low=11111111, high=100000000)



    saldo = 0


    pessoa = Pessoa(nome, sobrenome)
    cliente = Cliente(nome, sobrenome, conta, saldo)

    return cliente


def inicio():

    # Inicialmente, chamamos a função criar cliente
    cliente = criar_cliente()
    saldo = cliente.saldo
    print(cliente)
    print(saldo)

    # Será que eu preciso criar o objeto cliente_1 aqui dentro?
    # Como acessar o saldo aqui dentro?

    # Loop de funcionamento
    acao = input('''Escolha uma das seguintes opções (Basta teclar o número desejado):
    
    [1] - Sacar
    [2] - Depositar 
    [3] - Sair do aplicativo  
    
    ''')

    while acao.isdigit() == False:
        print('Você não digitou um número corretamente.')
        print('Digite apenas um dos três números sem espaço.')
        acao = input('''Escolha uma das seguintes opções (Basta teclar o número desejado):

            [1] - Sair do aplicativo
            [2] - Sacar 
            [3] - Depositar   

            ''')
    print('Opção escolhida corretamente.')

    while acao != '3':
        if acao == '1':
            saque = int(input('Quanto você quer sacar? '))
            if saque > cliente.saldo:
                print('Você não tem saldo suficiente para sacar este valor.')
                print(f'Seu saldo é {cliente.saldo}.')
                #Acho que aqui está errado
                acao = input('''Escolha uma das seguintes opções (Basta teclar o número desejado):

                    [1] - Sacar
                    [2] - Depositar
                    [3] - Sair do aplicativo   

                    ''')
            else:
                # Não sei uso saldo ou cliente.saldo
                cliente.saldo = cliente.saldo - saque
                print(f'Seu saldo é {cliente.saldo}.')
                acao = input('''Escolha uma das seguintes opções (Basta teclar o número desejado):

                    [1] - Sacar
                    [2] - Depositar 
                    [3] - Sair do aplicativo   

                    ''')
        if acao == '2':
            deposito = int(input('Quanto você quer depositar? '))
            cliente.saldo = cliente.saldo + deposito
            print(f'Seu saldo é {cliente.saldo}.')
            acao = input('''Escolha uma das seguintes opções (Basta teclar o número desejado):

                                [1] - Sacar
                                [2] - Depositar
                                [3] - Sair do aplicativo  

                                ''')

    print('O aplicativo foi fechado com sucesso.')



começar = inicio()





