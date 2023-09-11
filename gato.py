tablero = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def imprimir_instrucciones():
    print("Vamos a jugar al gato")
    print("El tablero tiene la siguiente estructura")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")

def dibujar_tablero(tablero):
    print(" %c | %c | %c " % (tablero[0], tablero[1], tablero[2]))
    print("---+---+---+")
    print(" %c | %c | %c " % (tablero[3], tablero[4], tablero[5]))
    print("---+---+---+")
    print(" %c | %c | %c " % (tablero[6], tablero[7], tablero[8]))

def estado_juego(tablero):
    ## Revisar horizontales
    if (tablero[0] == tablero[1] == tablero[2] != ' '):
        estado_actual = "ganador"
    elif (tablero[3] == tablero[4] == tablero[5] != ' '):
        estado_actual = "ganador"
    elif (tablero[6] == tablero[7] == tablero[8] != ' '):
        estado_actual = "ganador"

    ## Revisar verticales
    elif (tablero[0] == tablero[3] == tablero[6] != ' '):
        estado_actual = "ganador"
    elif (tablero[1] == tablero[4] == tablero[7] != ' '):
        estado_actual = "ganador"
    elif (tablero[2] == tablero[5] == tablero[8] != ' '):
        estado_actual = "ganador"

    ## Revisar diagonales
    elif (tablero[0] == tablero[4] == tablero[8] != ' '):
        estado_actual = "ganador"
    elif (tablero[6] == tablero[4] == tablero[2] != ' '):
        estado_actual = "ganador"

    else:
        estado_actual = "jugando"

    return estado_actual

jugador_actual = "x"
estado_actual = "jugando"
turno = 1
imprimir_instrucciones()

while (True):
    print("El turno del jugador %s " % jugador_actual)
    posicion = int(input("Elija la posicion a jugar (1-9)")) - 1
    if 0 <= posicion <= 8:
        ## Meter en arreglo al jugador
        if tablero[posicion] != " ":
            print("la posicion %s ya esta ocupada, elija otra " % str(posicion))
            continue
        else:
            tablero[posicion] = jugador_actual
            turno = turno + 1
    else:
        print("Posicion no valida")
        continue

    dibujar_tablero(tablero)
    estado_actual = estado_juego(tablero)

    ## Determina si se sigue jugando o se gana
    if estado_actual == "jugando":

        ## Cambiar de turno X o O
        if jugador_actual == "X":
            jugador_actual = "O"
        else:
            jugador_actual = "X"

    elif estado_actual == "ganador":
        print("El jugador %s es el GANADOR" % jugador_actual)
        break

    ## Salir si los turnos se acaban
    if turno >= 9:
        print("ya no hay mas casillas, juego empatado")
        break
