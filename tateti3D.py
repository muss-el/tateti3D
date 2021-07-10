import os
def mostrarTablero(pos):
    print(f"""          __________________
         /     /     /     /|
        /  {pos[0]}  /  {pos[1]}  /  {pos[2]}  / |
       /_____/_____/_____/  |
      /     /     /     /   |
     /  {pos[3]}  /  {pos[4]}  /  {pos[5]}  /    |
    /_____/_____/_____/     |
   /     /     /     /      |
  /  {pos[6]}  /  {pos[7]}  /  {pos[8]}  /       |
 /_________________/        |
|         |                 |
|         |_________________|
|        /     /     /     /|
|       /  {pos[9]}  /  {pos[10]}  /  {pos[11]}  / |
|      /_____/_____/_____/  |
|     /     /     /     /   |
|    /  {pos[12]}  /  {pos[13]}  /  {pos[14]}  /    |
|   /_____/_____/_____/     |
|  /     /     /     /      |
| /  {pos[15]}  /  {pos[16]}  /  {pos[17]}  /       |
|/_________________/        |
|         |                 |
|         |_________________|
|        /     /     /     /
|       /  {pos[18]}  /  {pos[19]}  /  {pos[20]}  /
|      /_____/_____/_____/
|     /     /     /     /
|    /  {pos[21]}  /  {pos[22]}  /  {pos[23]}  /
|   /_____/_____/_____/
|  /     /     /     /
| /  {pos[24]}  /  {pos[25]}  /  {pos[26]}  /
|/_________________/""")
letras = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
posiciones = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
turnoDe = ("*", "°", "+")
x = 0

mostrarTablero(posiciones)

while True:
    posicion = input(">>> ")
    if posicion in letras:
        indicePosicion = letras.index(posicion)
    else:
        continue
    posiciones[indicePosicion] = turnoDe[x]
    if x == 2:
        x = 0
    else:
        x = x + 1
    os.system("cls")
    mostrarTablero(posiciones)
