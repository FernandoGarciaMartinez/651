import random

def elegir_palabra():
    palabras = ["python", "java", "javascript", "ruby", "html", "css"]
    return random.choice(palabras)

def mostrar_tablero(palabra, letras_adivinadas):
    resultado = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado.strip()

def jugar_ahorcado():
    palabra_secreta = elegir_palabra()
    letras_adivinadas = []
    intentos_maximos = 6
    intentos_realizados = 0

    print("¡Bienvenido al Juego del Ahorcado!")
    print("Palabra a adivinar:", mostrar_tablero(palabra_secreta, letras_adivinadas))

    while True:
        letra = input("Ingresa una letra: ").lower()

        if letra.isalpha() and len(letra) == 1:
            if letra in letras_adivinadas:
                print("Ya has adivinado esa letra. Intenta con otra.")
                continue

            letras_adivinadas.append(letra)

            if letra not in palabra_secreta:
                intentos_realizados += 1
                print("Incorrecto. Te quedan {} intentos.".format(intentos_maximos - intentos_realizados))
                if intentos_realizados == intentos_maximos:
                    print("Perdiste. La palabra era: {}".format(palabra_secreta))
                    break
            else:
                print("¡Correcto!")

            print("Palabra actual:", mostrar_tablero(palabra_secreta, letras_adivinadas))

            if "_" not in mostrar_tablero(palabra_secreta, letras_adivinadas):
                print("¡Felicidades! ¡Has ganado!")
                break
        else:
            print("Ingresa una letra válida.")

if __name__ == "__main__":
    jugar_ahorcado()
