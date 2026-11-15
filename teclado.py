# teclado.py
# Lee UNA tecla sin tener que apretar Enter, usando la libreria READCHAR.
# Le pone a cada tecla especial un nombre facil de usar en el resto del programa.

import readchar


# Devuelve "ARRIBA", "ABAJO", "IZQUIERDA", "DERECHA", "ENTER", "ESC", "BORRAR" o la letra que se apreto
def leer_tecla():
    tecla = readchar.readkey()
    if tecla == readchar.key.UP:
        return "ARRIBA"
    if tecla == readchar.key.DOWN:
        return "ABAJO"
    if tecla == readchar.key.LEFT:
        return "IZQUIERDA"
    if tecla == readchar.key.RIGHT:
        return "DERECHA"
    if tecla == readchar.key.ENTER or tecla == "\r" or tecla == "\n":
        return "ENTER"
    if tecla == readchar.key.ESC or tecla == readchar.key.ESC + readchar.key.ESC:
        return "ESC"
    if tecla == readchar.key.BACKSPACE or tecla == "\x08" or tecla == "\x7f":
        return "BORRAR"
    return tecla
