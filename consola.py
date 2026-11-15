# consola.py
# Cosas basicas para mostrar en pantalla. Usa la libreria RICH, que se encarga
# de los colores, las tablas y de acomodar el texto.

from rich.console import Console
from rich.text import Text

# "consola" es el objeto de rich con el que se imprime todo
consola = Console()

# colores (rich acepta nombres o codigos como los de las paginas web)
GRIS = "grey58"
ROJO = "#FF6B6B"
VERDE = "#5FD787"
AMARILLO = "#FFD75F"
CELESTE = "#5FD7D7"
BLANCO = "bold white"
FONDO_TITULO = "#1C3A6E"
FONDO_ELEGIDO = "#282C3C"

# color de cada continente, para que se distingan
COLOR_CONTINENTE = {"America": "#46C873", "Europa": "#5F91FF", "Asia": "#F5CD46",
                    "Africa": "#F5695F", "Oceania": "#50D7D7"}

ANCHO_IZQUIERDA = 46      # ancho de la parte izquierda cuando al lado va el mapa


# Devuelve el color que le toca a un continente (gris si no lo conocemos)
def color_de_continente(continente):
    if continente in COLOR_CONTINENTE:
        return COLOR_CONTINENTE[continente]
    return GRIS


# True si la ventana es lo bastante grande para mostrar el mapa al costado
def hay_panel():
    return consola.size.width >= 114 and consola.size.height >= 22


# Devuelve la franja azul con el titulo. "derecha" es un texto chico que va del otro lado.
def encabezado(titulo, derecha=""):
    izquierda = "  " + titulo.upper()
    # se rellena con espacios para que la franja ocupe todo el ancho de la ventana
    espacios = consola.size.width - len(izquierda) - len(derecha) - 2
    if espacios < 1:
        espacios = 1
    franja = Text(izquierda + " " * espacios, style="bold white on " + FONDO_TITULO)
    franja.append(derecha + "  ", style=CELESTE + " on " + FONDO_TITULO)
    return franja


# Pasa 45376763 a "45.376.763" para que se lea mejor
def con_puntos(numero):
    return f"{numero:,}".replace(",", ".")


# Devuelve una barra de color. El largo depende de cuanto vale "valor" comparado con "maximo"
def barra(valor, maximo, largo, color):
    cantidad = 0
    if maximo > 0:
        cantidad = int(valor * largo / maximo)
        if cantidad == 0 and valor > 0:
            cantidad = 1
    texto = Text("█" * cantidad, style=color)
    texto.append("░" * (largo - cantidad), style="grey30")
    return texto
