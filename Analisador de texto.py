# Caso prático 3 - Analisador de texto

print("------------------------")
print("Vamos brincar de analisador de textos?")
texto = input("Escreva um pequeno texto que você gostaria de analisar: ")
print("Em seguida, preciso que você me diga três letras uma de cada vez.")
primeira_letra = input("Me diga a primeira letra: ")
segunda_letra = input("Me diga a segunda letra: ")
terceira_letra = input("Me diga a terceira letra: ")


texto = texto.lower()
primeira_letra = primeira_letra.lower()
segunda_letra = segunda_letra.lower()
terceira_letra = terceira_letra.lower()

primeira_letra_texto = texto[0]
ultima_letra_texto = texto[-1]

texto_dividido = texto.split()

total_palavras = len(texto_dividido)

texto_invertido = texto_dividido[::-1]
texto_invertido_unido = " ".join(texto_invertido)

contagem_primeira_letra = texto.count(primeira_letra)
contagem_segunda_letra = texto.count(segunda_letra)
contagem_terceira_letra = texto.count(terceira_letra)

verificar_palavra = "python" in texto
dicionario = {"A palavra Python está no texto?": True}
dicionario["A palavra Python está no texto?"] = verificar_palavra



print(f"O seu texto possui um total de {total_palavras} palavras.")
print(f"A primeira letra do texto é {primeira_letra_texto}")
print(f"A última letra do texto é {ultima_letra_texto}")
print(f"O seu texto invertido fica assim: {texto_invertido_unido}")
print(f"A primeira letra aparece no seu texto {contagem_primeira_letra} vezes.")
print(f"A segunda letra aparece no seu texto {contagem_segunda_letra} vezes.")
print(f"A terceira letra aparece no seu texto {contagem_terceira_letra} vezes.")
print(dicionario)
print("Finalizamos a brincadeira.")
print("-------------------------")

