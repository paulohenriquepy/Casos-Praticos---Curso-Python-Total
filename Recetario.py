from pathlib import Path
import os
from os import system
import shutil

diretorio_raiz = Path("C:/Users/Paulo/Recetas")

def perguntar_categoria():

    conjunto_pastas = set()

    for dir_, _, _ in os.walk(diretorio_raiz):
        rel_dir = os.path.relpath(dir_, diretorio_raiz)
        if rel_dir != '.':
            conjunto_pastas.add(rel_dir)

    print("Nós temos as seguintes categorias:")
    for nome in conjunto_pastas:
      print(nome.lower())

    categoria = input("Qual categoria você quer escolher? ").lower()

    while categoria not in conjunto_pastas:
        print(f"Sinto muito, não temos essa categoria.")
        categoria = input("Qual categoria você quer escolher? ").lower()

    return categoria

def mostrar_receitas(categoria):

    conjunto_arquivos = list()
    diretorio_atual = Path(diretorio_raiz, categoria)

    # Enumerando e imprimindo todos os arquivos

    for txt in Path(diretorio_atual).glob('*.txt'):
        conjunto_arquivos.append(txt.stem)

    print(f"Nós temos as seguintes receitas de {categoria.lower()}:")
    for i, nome in enumerate(conjunto_arquivos, start = 1):
        print(f"Número {i}: {nome}")

    total = len(conjunto_arquivos)

    # Os números válidos são um range de 1 até o comprimento do conjunto de arquivos

    numeros_validos = range(1, total + 1)

    conjunto_numeros_validos = []

    for i in numeros_validos:
        conjunto_numeros_validos.append(i)

    receita = int(input("Diga o número da receita que você quer: "))

    while receita not in conjunto_numeros_validos:
        print("Não temos uma receita com este número.")
        receita = int(input("Diga o número da receita que você quer: "))

    posicao_arquivo_desejado = receita - 1

    return conjunto_arquivos[posicao_arquivo_desejado]


def ler_receita():

    categoria = perguntar_categoria()
    receita = mostrar_receitas(categoria)
    print(receita)

    nome_do_arquivo = receita + '.txt'

    caminhos = list(diretorio_raiz.rglob(nome_do_arquivo))

    # Se encontrar o arquivo, abrir

    if caminhos:
        with open(caminhos[0], encoding="utf-8") as f:
            conteudo = f.read()
            print(conteudo)
            
    else:
        print("Arquivo não encontrado.")


def criar_receita():

    categoria = perguntar_categoria()

    diretorio_atual = Path(diretorio_raiz, categoria)

    receita_nova = input("Diga o nome da receita que você quer criar: ").lower()

    while not receita_nova.isalpha() == True:
        print("O nome da receita deve conter apenas caracteres alfabéticos.")
        print("Insira outro nome, por favor.")
        receita_nova = input("Diga o nome da receita que você quer criar: ").lower()

    else:
        print("Perfeito. Você introduziu um nome válido.")


    nome_do_arquivo = receita_nova + '.txt'

    print("Insira um texto resumido contendo a receita desejada.")
    print("Ao terminar, digite 'FIM', dessa forma em maiúsculo.")
    print("Pode inserir o texto: ")

    # Obtendo uma lista a partir do texto inserido

    linhas = []
    while True:
        linha = input()
        if linha == 'FIM':
            break
        linhas.append(linha)

    # Convertendo a lista a uma string
    # Substituindo os pontos finais por ponto final + quebra de linhas

    texto = ''.join(str(x) for x in linhas).replace('.', '.\n')

    # Salvando arquivo no diretório desejado

    diretorio_do_arquivo = os.path.join(diretorio_atual, nome_do_arquivo)

    with open(diretorio_do_arquivo, "w") as output:
        output.write(texto)

    return None


# Eliminar receita

def eliminar_receita():

    categoria = perguntar_categoria()

    mostrar_receitas(categoria)

    diretorio_atual = Path(diretorio_raiz, categoria)

    receita_eliminada = input("Diga o nome da receita que você quer eliminar: ").lower()

    nome_do_arquivo = receita_eliminada + '.txt'

    diretorio_do_arquivo = os.path.join(diretorio_atual, nome_do_arquivo)

    # Conferindo se o arquivo existe

    if os.path.exists(diretorio_do_arquivo):
        print("A receita existe na pasta desejada. Vou eliminá-la.")
        os.remove(diretorio_do_arquivo)
    else:
        print("A receita nao existe na categoria desejada.\n Verifique se você inseriu o nome adequadamente")

    return None

def criar_categoria():

    nova_categoria = input("Diga o nome da nova categoria que você quer criar: ").lower()

    novo_diretorio = Path(diretorio_raiz, nova_categoria)

    # Se não existe um diretório com este nome, criá-lo

    if not os.path.exists(novo_diretorio):
        os.makedirs(novo_diretorio)
        print(f"Perfeito! Criamos a categoria {nova_categoria}.")

    return None

# Eliminar categoria

def eliminar_categoria():

    categoria_a_eliminar = input("Diga o nome da nova categoria que você quer eliminar: ").capitalize()

    diretorio_completo = Path(diretorio_raiz, categoria_a_eliminar)

    # Verificando se a categoria a ser eliminada existe

    if os.path.exists(diretorio_completo):
        shutil.rmtree(diretorio_completo)
        print(f"Perfeito! Eliminamos a categoria {categoria_a_eliminar}.")

    else:
        print("Sinto muito. Não temos essa categoria.\nVerifique se você digitou adequadamente.")

    return None


def limpar_tela():

    system('cls')

    return None

#Código principal

print("Bem vindo ao seu caderno de receitas!")


print(f"Suas receitas estão no seguinte diretório: ", diretorio_raiz)

# Percorrendo recursivamente os arquivos dentro do diretório desejado

set_de_arquivos = set()

for diretorio, nome_de_diretorio, nomes_de_arquivos in os.walk(diretorio_raiz):
    for arquivo in nomes_de_arquivos:
     set_de_arquivos.add(arquivo)

numero_de_arquivos = len(set_de_arquivos)

print(f"Seu caderno possui {numero_de_arquivos} receitas diferentes.")

def perguntar():

  acao = int(input('''Escolha uma das seguintes opções (Basta pressionar o número desejado):

[1] - Ler receita
[2] - Criar receita
[3] - Criar categoria
[4] - Eliminar receita
[5] - Eliminar categoria
[6] - Finalizar programa

'''))

  return acao




acao = perguntar()

while acao != 6:

     if acao == 1:
         ler_receita()
         limpar_tela()
         acao = perguntar()

     elif acao == 2:
         criar_receita()
         limpar_tela()
         acao = perguntar()


     elif acao == 3:
         criar_categoria()
         limpar_tela()
         acao = perguntar()

     elif acao == 4:
         eliminar_receita()
         limpar_tela()
         acao = perguntar()


     elif acao == 5:
         eliminar_categoria()
         limpar_tela()
         acao = perguntar()


     elif acao == 6:
         print("Fechamos o seu caderno de receita.\nAté breve!")
         limpar_tela()
         break















