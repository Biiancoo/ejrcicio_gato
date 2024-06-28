import random


def inicializar_tablero():
    return [[str(3 * i + x + 1) for x in range(3)] for i in range(3)]


def mostrar_tablero(tablero):
    print("+-------+-------+-------+")
    for fila in tablero:
        print("|       |       |       |")
        print("|   " + "   |   ".join(fila) + "   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")


def ganador(tablero, jugador):
    for fila in tablero:
        es_ganador = True
        for espacio in fila:
            if espacio != jugador:
                es_ganador = False
                break
        if es_ganador:
            return True

    for col in range(3):
        es_ganador = True
        for fila in range(3):
            if tablero[fila][col] != jugador:
                es_ganador = False
                break
        if es_ganador:
            return True

    es_ganador = True
    for i in range(3):
        if tablero[i][i] != jugador:
            es_ganador = False
            break
    if es_ganador:
        return True

    es_ganador = True
    for i in range(3):
        if tablero[i][2 - i] != jugador:
            es_ganador = False
            break
    if es_ganador:
        return True

    return False

def empate(tablero):
    for fila in tablero:
        for espacio in fila:
            if espacio not in ['X', 'O']:
                return False
    return True


def movi_jugador(tablero):
    while True:
        movimiento = input("Ingresa tu movimiento (1-9): ")
        if not movimiento.isdigit():
            print("ERROR. Por favor, introduce un número del 1 al 9.")
            continue

        movimiento = int(movimiento)
        if movimiento < 1 or movimiento > 9:
            print("ERROR. Intenta de nuevo.")
            continue

        fila = (movimiento - 1) // 3
        columna = (movimiento - 1) % 3
        if tablero[fila][columna] in ['X', 'O']:
            print("El cuadro ya está ocupado. Intenta de nuevo.")
        else:
            return fila, columna



def movimiento_maquina(tablero):
    movimientos_validos = [(i, j) for i in range(3) for j in range(3) if tablero[i][j] not in ['X', 'O']]
    
    if movimientos_validos:
        return random.choice(movimientos_validos)
    else:
        return None  


def jugar_tic_tac_toe():
    tablero = inicializar_tablero()

    tablero[1][1] = 'X'
    mostrar_tablero(tablero)

    while True:

        fila, columna = movi_jugador(tablero)
        tablero[fila][columna] = 'O'
        mostrar_tablero(tablero)

        if ganador(tablero, 'O'):
            print("Has ganado!")
            break
        if empate(tablero):
            print("El juego termino en empate.")
            break


        fila, columna = movimiento_maquina(tablero)
        tablero[fila][columna] = 'X'
        print(f"La máquina elige el cuadro {fila * 3 + columna + 1}")
        mostrar_tablero(tablero)

        if ganador(tablero, 'X'):
            print("La máquina gano, suerte para la proxima")
            break
        if empate(tablero):
            print("Has empatado con la maquina")
            break



jugar_tic_tac_toe()