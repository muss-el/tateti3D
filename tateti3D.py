################################
# Se importa el modulo "os" para manipular la consola.
import os
################################
#Se crea una función para limpiar la consola sin importar el sistema operativo.
################################
def clear():
    if os.name in ("ce", "nt", "dos"):
        os.system("cls")
    else:
        os.system("clear")
################################
# Función para dibujar el tablero con las posiciones guardadas en la lista "pos".
# La lista "pos" tiene las posiciones ordenadas númericamente desde la esquina
# izquierda superior trasera hasta la esquina opuesta.
################################
def mostrarTablero(pos):
    print(f"""          ________________________
         /       /       /       /|
        /  {pos[0]}  /  {pos[1]}  /  {pos[2]}  / |
       /_______/_______/_______/  |
      /       /       /       /   |
     /  {pos[3]}  /  {pos[4]}  /  {pos[5]}  /    |
    /_______/_______/_______/     |
   /       /       /       /      |
  /  {pos[6]}  /  {pos[7]}  /  {pos[8]}  /       |
 /_______/_______/_______/        |
|         |                       |
|         |_______________________|
|        /       /       /       /|
|       /  {pos[9]}  /  {pos[10]}  /  {pos[11]}  / |
|      /_______/_______/_______/  |
|     /       /       /       /   |
|    /  {pos[12]}  /  {pos[13]}  /  {pos[14]}  /    |
|   /_______/_______/_______/     |
|  /       /       /       /      |
| /  {pos[15]}  /  {pos[16]}  /  {pos[17]}  /       |
|/_______/_______/_______/        |
|         |                       |
|         |_______________________|
|        /       /       /       /
|       /  {pos[18]}  /  {pos[19]}  /  {pos[20]}  /
|      /_______/_______/_______/
|     /       /       /       /
|    /  {pos[21]}  /  {pos[22]}  /  {pos[23]}  /
|   /_______/_______/_______/
|  /       /       /       /
| /  {pos[24]}  /  {pos[25]}  /  {pos[26]}  /
|/_______/_______/_______/""")
################################
# Esta función guarda las jugadas ganadoras en listas que contienen un valor booleano y
# una posición del tablero. El primero verifica sí, según una combinación de posiciones,
# hay tres casilleros iguales, dando un "True", y, sí no hay casilleros iguales,
# entregará un "False". El otro valor de las listas es la primera posicion
# del tablero de las tres que hay en la jugada. Esto sirve para saber, en caso de
# que haya un "True" (tres casilleros iguales), quien está ocupando esos casilleros.
# La ultima lista "jugadas" guarda todas las jugadas para poder iterar sobre ellas facilmente.
################################
def jugadasGanadoras(pos):
    jugada1 = [pos[0] == pos[1] == pos[2], pos[0]]
    jugada2 = [pos[0] == pos[3] == pos[6], pos[0]]
    jugada3 = [pos[0] == pos[4] == pos[8], pos[0]]
    jugada4 = [pos[1] == pos[4] == pos[7], pos[1]]
    jugada5 = [pos[2] == pos[5] == pos[8], pos[2]]
    jugada6 = [pos[3] == pos[4] == pos[5], pos[3]]
    jugada7 = [pos[6] == pos[7] == pos[8], pos[6]]
    jugada8 = [pos[2] == pos[4] == pos[6], pos[2]]
    jugada9 = [pos[9] == pos[10] == pos[11], pos[9]]
    jugada10 = [pos[9] == pos[12] == pos[15], pos[9]]
    jugada11 = [pos[9] == pos[13] == pos[17], pos[9]]
    jugada12 = [pos[10] == pos[13] == pos[16], pos[10]]
    jugada13 = [pos[11] == pos[14] == pos[17], pos[11]]
    jugada14 = [pos[12] == pos[13] == pos[14], pos[12]]
    jugada15 = [pos[15] == pos[16] == pos[17], pos[15]]
    jugada16 = [pos[11] == pos[13] == pos[15], pos[11]]
    jugada17 = [pos[18] == pos[19] == pos[20], pos[18]]
    jugada18 = [pos[18] == pos[22] == pos[26], pos[18]]
    jugada19 = [pos[18] == pos[21] == pos[24], pos[18]]
    jugada20 = [pos[19] == pos[22] == pos[25], pos[19]]
    jugada21 = [pos[20] == pos[23] == pos[26], pos[20]]
    jugada22 = [pos[21] == pos[22] == pos[23], pos[21]]
    jugada23 = [pos[24] == pos[25] == pos[26], pos[24]]
    jugada24 = [pos[20] == pos[22] == pos[24], pos[20]]
    jugada25 = [pos[0] == pos[9] == pos[18], pos[0]]
    jugada26 = [pos[1] == pos[10] == pos[19], pos[1]]
    jugada27 = [pos[2] == pos[11] == pos[20], pos[2]]
    jugada28 = [pos[3] == pos[12] == pos[21], pos[3]]
    jugada29 = [pos[4] == pos[13] == pos[22], pos[4]]
    jugada30 = [pos[5] == pos[14] == pos[23], pos[5]]
    jugada31 = [pos[6] == pos[15] == pos[24], pos[6]]
    jugada32 = [pos[7] == pos[16] == pos[25], pos[7]]
    jugada33 = [pos[8] == pos[17] == pos[26], pos[8]]
    jugada34 = [pos[0] == pos[10] == pos[20], pos[0]]
    jugada35 = [pos[2] == pos[10] == pos[18], pos[2]]
    jugada36 = [pos[2] == pos[14] == pos[26], pos[2]]
    jugada37 = [pos[8] == pos[14] == pos[20], pos[8]]
    jugada38 = [pos[8] == pos[16] == pos[24], pos[8]]
    jugada39 = [pos[6] == pos[16] == pos[26], pos[6]]
    jugada40 = [pos[6] == pos[12] == pos[18], pos[6]]
    jugada41 = [pos[24] == pos[12] == pos[0], pos[24]]
    jugada42 = [pos[1] == pos[13] == pos[25], pos[1]]
    jugada43 = [pos[7] == pos[13] == pos[19], pos[7]]
    jugada44 = [pos[5] == pos[13] == pos[21], pos[5]]
    jugada45 = [pos[3] == pos[13] == pos[23], pos[3]]
    jugada46 = [pos[0] == pos[13] == pos[26], pos[0]]
    jugada47 = [pos[2] == pos[13] == pos[24], pos[2]]
    jugada48 = [pos[8] == pos[13] == pos[18], pos[8]]
    jugada49 = [pos[6] == pos[13] == pos[20], pos[6]]
    jugadas = [jugada1, jugada2, jugada3, jugada4, jugada5,
            jugada6, jugada7, jugada8, jugada9, jugada10,
            jugada11, jugada12, jugada13, jugada14, jugada15,
            jugada16, jugada17, jugada18, jugada19, jugada20,
            jugada21, jugada22, jugada23, jugada24, jugada25,
            jugada26, jugada27, jugada28, jugada29, jugada30,
            jugada31, jugada32, jugada33, jugada34, jugada35,
            jugada36, jugada37, jugada38, jugada39, jugada40,
            jugada41, jugada42, jugada43, jugada44, jugada45,
            jugada46, jugada47, jugada48, jugada49]
    ################################
    # Se itera sobre cada jugada.
    for jugada in jugadas:
        ################################
        # Sí hay un "True" (tres casilleros iguales),
        # la función termina y devuelve el jugador que ganó.
        if jugada[0]:
            return jugada[1]
        ################################
        # Sino, continuará iterando buscando algún "True" en las listas de jugadas.
        else:
            continue
    ################################
    # Sí no hay jugadas ganadoras, la función termina
    # devuelve un "False"
    return False
    ################################


LETRAS = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ") # Lista con el abecedario.
JUGADORES = ("1", "2", "3")

################################
# Se crea un bucle para seguir el juego en caso de que se haya terminado.
################################
while True:

    ################################
    #Listas para guardar las posiciones según se requieran.
    posicionesMostradas = list()
    posicionesVacias = list()
    posiciones = list()
    ################################
    # Itera sobre el abecedario creado.
    for letra in LETRAS:
        ################################
        # Solo muestra los casilleros en los que haya jugadores.
        posicionesVacias.append("   ")
        ################################
        # Guarda las posiciones de los jugadores para mejor uso en el futuro.
        posiciones.append(f"{letra}")
        ################################
        # Guarda las posiciones de los casilleros para mejor visualización en el tablero.
        posicionesMostradas.append(f" {letra} ")
    ################################
    # Contador.
    x = 0
    ################################
    # Un bucle anidado para iniciar el juego y mantenerlo hasta que alguien gane.
    while True:
        ################################
        # Se muestra el tablero (con los casilleros ocupados por
        # las letras del abecedario) y se le pide a los jugadores indicar una posición.
        mostrarTablero(posicionesMostradas)
        print (f"Turno del jugador {JUGADORES[x]}.")
        print ("Ingrese una posición valida:")
        posicion = input(">>> ").upper() # Convierte cualquier letra en mayusculas.
        ################################
        # Verifica sí la posición es valida.
        if posicion in LETRAS:
            ################################
            # Si es valida, guarda el indice de la posición elegida.
            indicePosicion = LETRAS.index(posicion)
            ################################
            # Pero, si la posición elegida ya estaba ocupada por otro jugador,
            # Vuelve a comenzar el bucle anidado.
            if posiciones[indicePosicion] in JUGADORES:
                clear()
                continue
        ################################
        # Si la posición no es valida, vuelve a comenzar el bucle anidado.
        else:
            clear()
            continue
        ################################
        # Actualiza los valores de las listas con la posicion elegida y la rellena
        # con el jugador actual.
        posiciones[indicePosicion] = JUGADORES[x]
        posicionesVacias[indicePosicion] = "(" + JUGADORES[x] + ")"
        posicionesMostradas[indicePosicion] = "(" + JUGADORES[x] + ")"
        ################################
        # Cambia al jugador siguiente.
        if x == 2:
            x = 0
        else:
            x = x + 1
        ################################
        # Inicia el analisis de posiciones en busca de jugadas ganadoras.
        # Guarda el resultado en la variable "ganador".
        ganador = jugadasGanadoras(posiciones)
        ################################
        # Si hay ganador, muestra el tablero con los casilleros vacios, excepto por
        # los de los jugadores, e indica que jugador ganó.
        # Sí no hay ganador, entonces "ganador" tendrá el valor de "False" y el if
        # no se cumplirá.
        if ganador:
             clear()
             mostrarTablero(posicionesVacias)
             print(f"Ganó el jugador {ganador}.")
             ################################
             #Termina el bucle anidado para terminar el juego.
             break
        ################################
        # Como no hay ganador, limpia la consola y vuelve a comenzar el bucle anidado.
        clear()
    ################################
    # Le pregunta al usuario si continua el juego o quiere salir.
    print ("Continuar jugando?")
    print("Escribe \"si\" para continuar, o cualquier otra cosa para salir:")
    opcion = input(">>> ")
    ################################
    # Sí respondio con algunas de las opciones afirmativas, el bucle comenzará devuelta.
    if opcion in ("si", "SI", "Si"):
        clear()
        continue
    ################################
    # Sino, se romperá el bucle y se termina el programa.
    else:
        clear()
        break
exit()
################################
