from random import choice

def lanzar_dados():
    """
    Esta función lanza dos dados
    """
    lanzamiento1 = choice(list(range(1, 7)))
    lanzamiento2 = choice(list(range(1, 7)))
    return lanzamiento1, lanzamiento2

def evaluar_jugada(num1, num2):
    """
    Esta función suma los dos lanzamientos y retorna una evaluación
    """
    suma_dados = num1 + num2

    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif 6 < suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

# Simulación de la jugada
dado1, dado2 = lanzar_dados()
resultado = evaluar_jugada(dado1, dado2)

print(resultado)  # Agora o resultado é retornado corretamente
