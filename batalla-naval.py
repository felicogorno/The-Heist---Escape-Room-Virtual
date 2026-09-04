import random

#TOMAS SALVATIERRA

tamanio_tablero = 5
cantidad_barcos = 3
max_disparos = 20



def crear_tablero(valor_inicial):
    tablero = []

    for fila in range(tamanio_tablero):
        nueva_fila = []

        for columna in range(tamanio_tablero):
            nueva_fila.append(valor_inicial)

        tablero.append(nueva_fila)

    return tablero






def posicion_valida_barco(tablero, fila, columna,barco):

    if tablero[fila][columna] == barco:
        return False

    for f in range(fila - 1, fila + 2): #usa la fila anterior y la siguiente 

        for c in range(columna - 1, columna + 2): # usa la columna anterior y la siguiente 
 
            if f >= 0 and f < tamanio_tablero and c >= 0 and c < tamanio_tablero: # verifica que la fila y columna estén dentro del tablero( si pongo un 0 0 no va a probar con 0 -1)

                if tablero[f][c] == barco:
                    return False

    return True

def generar_barcos(tablero):
    barcos_colocados = 0
    

    while barcos_colocados < cantidad_barcos:
        fila=random.randint(0,tamanio_tablero-1)
        columna=random.randint(0,tamanio_tablero-1)
        validar=False
        while validar==False:
            validar=posicion_valida_barco(tablero,fila,columna,1)
            if validar==False:
                fila=random.randint(0,tamanio_tablero-1)
                columna=random.randint(0,tamanio_tablero-1)
        tablero[fila][columna]=1
        barcos_colocados+=1


def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join([str(celda) for celda in fila]))
        


def validar_enteros(minimo,maximo,mensaje,error):
    respuesta=input(mensaje)
    while not respuesta.isdigit() or int(respuesta) < minimo or int(respuesta) > maximo:
        print(error)
        respuesta=input(mensaje)
    return int(respuesta)

def ingresar_cordenadas(tablero_visible):
    comprobar=False
    while comprobar==False:
        fila = validar_enteros(1, tamanio_tablero, "Ingrese la fila (1-5): ", "Fila inválida. Intente nuevamente.")
        columna = validar_enteros(1, tamanio_tablero, "Ingrese la columna (1-5): ", "Columna inválida. Intente nuevamente.")
        fila -= 1  # Ajustar a índice de lista (0-4)
        columna -= 1  # Ajustar a índice de lista (0-4)
        comprobar=posicion_disponible(tablero_visible, fila, columna)
    return fila, columna


def posicion_disponible(tablero, fila, columna):
    if tablero[fila][columna] != ".":
        print("Ya atacaste esa posición. Intenta nuevamente.")
        return False
    
    return True


def realizar_disparo(tablero_barcos, tablero_visible, fila, columna,aciertos,intentos):
    if tablero_barcos[fila][columna] == 1:
        tablero_visible[fila][columna] = "X"
        print("¡IMPACTO! Barco hundido.")
        aciertos += 1
        
    else:
        tablero_visible[fila][columna] = "O"
        print("AGUA")

    intentos += 1
    return aciertos, intentos

def mostrar_tablero_final(tablero):
    for fila in tablero:
        fila_visible = ["X" if celda == 1 else "." for celda in fila]
        print(" ".join(fila_visible))

def mostrar_estado(aciertos, intentos):
    print("Barcos hundidos:", aciertos)
    print("Barcos restantes:", cantidad_barcos - aciertos)
    print("Disparos disponibles:", max_disparos - intentos)

def jugar_batalla_naval():
    tablero_barcos = crear_tablero(0)
    tablero_visible = crear_tablero(".")
    generar_barcos(tablero_barcos)
    aciertos = 0
    intentos = 0

    while aciertos < cantidad_barcos and intentos < max_disparos:
        print("\nTablero visible:")
        mostrar_tablero(tablero_visible)
        fila, columna = ingresar_cordenadas(tablero_visible)
        aciertos, intentos = realizar_disparo(tablero_barcos, tablero_visible, fila, columna, aciertos, intentos)
        mostrar_estado(aciertos, intentos)


    
    if aciertos == cantidad_barcos:
        print("¡Felicidades! Has hundido todos los barcos.")
        mostrar_tablero(tablero_visible)
        return True
    else:
        print("Se acabaron los intentos. ¡Mejor suerte la próxima vez!")
        print("Tablero de barcos:")
        mostrar_tablero_final(tablero_barcos)
        return False

jugar_batalla_naval()