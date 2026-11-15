# animaciones.py
# Las dos animaciones del programa, hechas con "Live" de la libreria rich:
#   - la presentacion del principio (el mapa aparece y los paises se encienden)
#   - el ordenamiento: se ve como trabaja el metodo burbuja, paso a paso

import time

from rich.console import Group
from rich.live import Live
from rich.text import Text

from consola import consola, encabezado, color_de_continente, hay_panel, GRIS, VERDE, AMARILLO, BLANCO
from teclado import leer_tecla
from banderas import bandera_angosta
from mapa import dibujar_mapa, ANCHO_MAPA

ALTO_BARRAS = 10       # renglones que mide la barra mas alta


# Presentacion: el mapa se dibuja de izquierda a derecha y despues
# los paises del CSV se van encendiendo de a uno.
def presentacion(paises):
    if not hay_panel():
        return
    with Live(console=consola, screen=True, auto_refresh=False) as live:
        for hasta in range(0, ANCHO_MAPA + 1, 4):
            live.update(Group(encabezado("Gestion de paises", "leyendo paises.csv"), Text(""),
                              dibujar_mapa([], "", "", hasta)), refresh=True)
            time.sleep(0.03)
        nombres = []
        for pais in paises:
            nombres.append(pais["nombre"])
            aviso = Text(f"\n  Cargando {pais['nombre']}...   {len(nombres)} de {len(paises)}", style=GRIS)
            live.update(Group(encabezado("Gestion de paises", "leyendo paises.csv"), Text(""),
                              dibujar_mapa(nombres, pais["nombre"]), aviso), refresh=True)
            time.sleep(0.07)
        aviso = Text(f"\n  √ Se cargaron {len(paises)} paises", style=VERDE)
        live.update(Group(encabezado("Gestion de paises", ""), Text(""),
                          dibujar_mapa(nombres, ""), aviso), refresh=True)
        time.sleep(0.6)


# True si las barras de todos los paises entran en la ventana (cada pais usa 4 letras de ancho)
def se_puede_animar(cantidad):
    return cantidad >= 2 and cantidad * 4 + 4 <= consola.size.width and consola.size.height >= 22


# Cuanto se espera entre un paso y el siguiente, para que toda la animacion dure unos 6 segundos
def calcular_espera(cantidad):
    pasos = cantidad * (cantidad - 1) / 2 * 1.5
    espera = 6 / pasos
    if espera > 0.25:
        espera = 0.25
    return espera


# Devuelve un numero para decidir que tan alta es la barra de un pais
def valor_para_barra(pais, campo):
    if campo == "nombre":
        # por nombre: la A es la mas bajita y la Z la mas alta
        return "abcdefghijklmnopqrstuvwxyz".find(pais["nombre"][0].lower()) + 2
    # se usa la raiz cuadrada para que los paises chicos no queden invisibles al lado de los gigantes
    return pais[campo] ** 0.5


# Dibuja una barra por pais. "marcados" son las dos posiciones que se estan comparando.
def dibujar_barras(paises, campo, marcados, color_marcados):
    maximo = 0
    for pais in paises:
        if valor_para_barra(pais, campo) > maximo:
            maximo = valor_para_barra(pais, campo)
    alturas = []
    for pais in paises:
        altura = int(valor_para_barra(pais, campo) * ALTO_BARRAS / maximo)
        if altura < 1:
            altura = 1
        alturas.append(altura)

    texto = Text()
    # se dibuja de arriba para abajo: en cada renglon van las barras que llegan hasta ahi
    for renglon in range(ALTO_BARRAS, 0, -1):
        texto.append("  ")
        for i in range(len(paises)):
            if alturas[i] >= renglon:
                if i in marcados:
                    color = color_marcados
                else:
                    color = color_de_continente(paises[i]["continente"])
                texto.append("███", style=color)
            else:
                texto.append("   ")
            texto.append(" ")
        texto.append("\n")
    # abajo de cada barra va la bandera del pais (son 2 renglones)
    for renglon in range(2):
        texto.append("  ")
        for pais in paises:
            texto.append_text(bandera_angosta(pais["nombre"]).split("\n")[renglon])
            texto.append(" ")
        texto.append("\n")
    return texto


# Abre la pantalla de la animacion y la devuelve, para ir actualizandola en cada paso
def empezar_ordenamiento():
    animacion = Live(console=consola, screen=True, auto_refresh=False)
    animacion.start()
    return animacion


# Muestra un paso del metodo burbuja. tipo es "COMPARAR" o "INTERCAMBIAR".
def mostrar_paso(animacion, paises, titulo, campo, j, tipo, pasada, comparaciones, intercambios, espera):
    if tipo == "COMPARAR":
        color = "white"
        accion = f"comparando {paises[j]['nombre']} con {paises[j + 1]['nombre']}"
    else:
        color = AMARILLO
        accion = f"se intercambian {paises[j + 1]['nombre']} y {paises[j]['nombre']}"
    abajo = Text()
    abajo.append(f"  Pasada {pasada} de {len(paises) - 1}:  ", style=BLANCO)
    abajo.append(accion + "\n")
    abajo.append(f"  Comparaciones: {comparaciones}     Intercambios: {intercambios}", style=GRIS)
    animacion.update(Group(encabezado(titulo, "metodo burbuja"), Text(""),
                           dibujar_barras(paises, campo, [j, j + 1], color), abajo), refresh=True)
    time.sleep(espera)


# Muestra como quedo todo ordenado, espera una tecla y cierra la pantalla de la animacion
def terminar_ordenamiento(animacion, paises, titulo, campo, comparaciones, intercambios):
    abajo = Text()
    abajo.append("  √ Lista ordenada\n", style=VERDE)
    abajo.append(f"  Comparaciones: {comparaciones}     Intercambios: {intercambios}\n\n", style=GRIS)
    abajo.append("  Pulsa una tecla para ver la lista", style=GRIS)
    animacion.update(Group(encabezado(titulo, "metodo burbuja"), Text(""),
                           dibujar_barras(paises, campo, [], "white"), abajo), refresh=True)
    leer_tecla()
    animacion.stop()
