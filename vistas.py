# vistas.py
# Las pantallas interactivas del programa, hechas con la libreria RICH:
#   elegir()    un menu que se mueve con las flechas
#   explorar()  una lista de paises con su bandera, para recorrer, buscar o elegir
#   ficha()     todos los datos de un pais con la bandera grande
# Todas usan "Live" de rich, que deja volver a dibujar la pantalla sin que parpadee.

from rich.console import Group
from rich.live import Live
from rich.padding import Padding
from rich.table import Table
from rich.text import Text

from consola import (consola, encabezado, barra, con_puntos, color_de_continente, hay_panel,
                     GRIS, VERDE, AMARILLO, CELESTE, BLANCO, FONDO_ELEGIDO,
                     COLOR_CONTINENTE, ANCHO_IZQUIERDA)
from teclado import leer_tecla
from banderas import bandera_grande, bandera_chica
from mapa import dibujar_mapa, esta_en_mapa


# Devuelve la lista con los nombres de los paises (es lo que necesita el mapa)
def nombres_de(paises):
    nombres = []
    for pais in paises:
        nombres.append(pais["nombre"])
    return nombres


# Renglon que va abajo del mapa en los menus: cuantos paises hay de cada continente
def resumen(paises):
    texto = Text()
    for continente in COLOR_CONTINENTE:
        cantidad = 0
        for pais in paises:
            if pais["continente"] == continente:
                cantidad += 1
        texto.append("■ ", style=COLOR_CONTINENTE[continente])
        texto.append(f"{continente} {cantidad}   ", style=GRIS)
    texto.append("\nEn color: los paises cargados en paises.csv", style=GRIS)
    return texto


# Devuelve el puesto de un pais en poblacion y los valores mas grandes de la lista
# (se usan para las barras). Devuelve tres cosas.
def datos_de(todos, pais):
    puesto = 1
    max_poblacion = pais["poblacion"]
    max_superficie = pais["superficie"]
    for otro in todos:
        if otro["poblacion"] > pais["poblacion"]:
            puesto += 1                       # el puesto es 1 + los que tienen mas poblacion
        if otro["poblacion"] > max_poblacion:
            max_poblacion = otro["poblacion"]
        if otro["superficie"] > max_superficie:
            max_superficie = otro["superficie"]
    return puesto, max_poblacion, max_superficie


# Los datos de un pais con sus barras (va abajo del mapa en las listas, y en la ficha)
def detalle(todos, pais, largo):
    puesto, max_poblacion, max_superficie = datos_de(todos, pais)
    densidad = round(pais["poblacion"] / pais["superficie"], 1)
    texto = Text()
    texto.append(pais["nombre"].upper(), style=BLANCO)
    texto.append("   " + pais["continente"] + "\n", style=color_de_continente(pais["continente"]))
    texto.append(f"Puesto {puesto} de {len(todos)} en poblacion\n\n", style=GRIS)
    texto.append("Poblacion   ")
    texto.append_text(barra(pais["poblacion"], max_poblacion, largo, VERDE))
    texto.append("  " + con_puntos(pais["poblacion"]) + " hab\n")
    texto.append("Superficie  ")
    texto.append_text(barra(pais["superficie"], max_superficie, largo, CELESTE))
    texto.append("  " + con_puntos(pais["superficie"]) + " km2\n")
    texto.append(f"Densidad    {densidad} habitantes por km2", style=GRIS)
    if not esta_en_mapa(pais["nombre"]):
        texto.append("   (no esta en el mapa)", style=GRIS)
    return texto


# Arma una pantalla completa: titulo arriba, "izquierda" a la izquierda y,
# si la ventana es grande, el mapa a la derecha con "abajo_mapa" debajo.
def pantalla(titulo, derecha, izquierda, mapa, abajo_mapa, pie):
    partes = [encabezado(titulo, derecha), Text("")]
    if hay_panel():
        columnas = Table.grid(padding=(0, 3))
        columnas.add_column(width=ANCHO_IZQUIERDA)
        columnas.add_column()
        columnas.add_row(izquierda, Group(mapa, Text(""), abajo_mapa))
        partes.append(columnas)
    else:
        partes.append(izquierda)
    partes.append(Text(""))
    partes.append(Text("  " + pie, style=GRIS))
    return Group(*partes)


# Menu con flechas. Recibe el titulo, la lista de opciones y una lista con la
# explicacion de cada una. Devuelve la POSICION de la opcion elegida, o -1 si se vuelve atras.
#   info: renglon extra que va arriba de las opciones
#   son_continentes: True si las opciones son continentes (se resalta en el mapa el que se mira)
def elegir(titulo, opciones, ayudas, paises, info="", son_continentes=False):
    elegido = 0
    listo = False
    with Live(console=consola, screen=True, auto_refresh=False) as live:
        while not listo:
            izquierda = Text()
            if info != "":
                izquierda.append("  " + info + "\n\n", style=VERDE)
            for i in range(len(opciones)):
                if i == elegido:
                    # la opcion donde estamos parados va con fondo y una flecha
                    izquierda.append(f"  ► {opciones[i]:<38}\n", style="bold white on " + FONDO_ELEGIDO)
                else:
                    izquierda.append("    " + opciones[i] + "\n", style=GRIS)
            izquierda.append("\n  " + ayudas[elegido], style=AMARILLO)

            continente = ""
            if son_continentes:
                continente = opciones[elegido]
            mapa = dibujar_mapa(nombres_de(paises), "", continente)
            derecha = f"{len(paises)} paises"
            live.update(pantalla(titulo, derecha, izquierda, mapa, resumen(paises),
                                 "↑ ↓ mover    Enter elegir    Esc volver"), refresh=True)

            tecla = leer_tecla()
            if tecla == "ARRIBA":
                elegido -= 1
                if elegido < 0:
                    elegido = len(opciones) - 1     # si se pasa de arriba, va a la ultima
            elif tecla == "ABAJO":
                elegido += 1
                if elegido == len(opciones):
                    elegido = 0                     # si se pasa de abajo, vuelve a la primera
            elif tecla == "ENTER":
                listo = True
            elif tecla == "ESC" or tecla == "IZQUIERDA":
                elegido = -1
                listo = True
    return elegido


# Arma lo que se ve en la ficha de un pais
def armar_ficha(todos, pais, mensaje):
    izquierda = Text()
    if mensaje != "":
        izquierda.append("  √ " + mensaje + "\n\n", style=VERDE)
    cuerpo = Table.grid(padding=(0, 2))
    cuerpo.add_row(Text("  "), bandera_grande(pais["nombre"]))
    largo = 12
    if not hay_panel():
        largo = 24
    contenido = Group(izquierda, cuerpo, Text(""), Padding(detalle(todos, pais, largo), (0, 0, 0, 2)))
    mapa = dibujar_mapa(nombres_de(todos), pais["nombre"])
    return pantalla("Ficha del pais", "", contenido, mapa, resumen(todos), "Pulsa una tecla para volver")


# Muestra la ficha de un pais y espera una tecla. "mensaje" es un aviso que va arriba (puede ser "").
def ficha(todos, pais, mensaje=""):
    with Live(armar_ficha(todos, pais, mensaje), console=consola, screen=True, auto_refresh=False) as live:
        live.refresh()
        leer_tecla()


# Muestra un aviso en una pantalla aparte y espera una tecla
def pausa(titulo, texto):
    contenido = Group(encabezado(titulo), Text(""), Text("  ! " + texto, style=AMARILLO),
                      Text(""), Text("  Pulsa una tecla para volver", style=GRIS))
    with Live(contenido, console=consola, screen=True, auto_refresh=False) as live:
        live.refresh()
        leer_tecla()


# Devuelve el nombre del pais con la parte que coincide con la busqueda resaltada
def resaltar(nombre, buscado, estilo):
    texto = Text(nombre, style=estilo)
    if buscado != "":
        lugar = nombre.lower().find(buscado)
        if lugar != -1:
            texto.stylize("bold black on " + AMARILLO, lugar, lugar + len(buscado))
    return texto


# Lista de paises para recorrer con las flechas. Cada pais tiene su bandera chica al lado.
# "todos" es la lista completa y "lista" son los paises que hay que mostrar.
# Tiene tres modos:
#   "VER"     solo se recorre. Con Enter se abre la ficha del pais.
#   "BUSCAR"  ademas se puede escribir: la lista se achica con cada letra.
#   "ELEGIR"  igual que BUSCAR, pero con Enter se devuelve el pais elegido.
# Devuelve dos cosas: el pais elegido (o None) y el texto que se busco.
def explorar(todos, lista, titulo, modo):
    if len(lista) == 0:
        pausa(titulo, "No se encontraron paises.")
        return None, ""
    elegido = 0
    primero = 0           # posicion del primer pais que se ve en pantalla
    buscado = ""
    resultado = None
    salir = False
    with Live(console=consola, screen=True, auto_refresh=False) as live:
        while not salir:
            # con lo que se escribio se arma la lista de los que coinciden
            visibles_lista = []
            for pais in lista:
                if buscado in pais["nombre"].lower():
                    visibles_lista.append(pais)
            if elegido >= len(visibles_lista):
                elegido = len(visibles_lista) - 1
            if elegido < 0:
                elegido = 0

            # cuantos paises entran depende del alto de la ventana (cada uno usa 3 renglones)
            cuantos = (consola.size.height - 8) // 3
            if cuantos < 2:
                cuantos = 2
            # la "ventana" se corre para que el pais elegido siempre se vea
            if elegido < primero:
                primero = elegido
            if elegido >= primero + cuantos:
                primero = elegido - cuantos + 1
            ultimo = primero + cuantos
            if ultimo > len(visibles_lista):
                ultimo = len(visibles_lista)

            tabla = Table.grid(padding=(0, 1))
            tabla.add_column(width=2)
            tabla.add_column(width=6)
            tabla.add_column(width=17)
            tabla.add_column(justify="right")
            for i in range(primero, ultimo):
                pais = visibles_lista[i]
                if i == elegido:
                    marca = Text("►", style=CELESTE)
                    estilo = BLANCO
                    estilo_datos = "white"
                else:
                    marca = Text(" ")
                    estilo = "none"
                    estilo_datos = GRIS
                nombre = resaltar(pais["nombre"][:17], buscado, estilo)
                nombre.append("\n" + pais["continente"] + "\n", style=color_de_continente(pais["continente"]))
                datos = Text(con_puntos(pais["poblacion"]) + " hab\n" + con_puntos(pais["superficie"]) + " km2",
                             style=estilo_datos)
                tabla.add_row(marca, bandera_chica(pais["nombre"]), nombre, datos)

            arriba = Text()
            if modo != "VER":
                arriba.append("  Buscar: ", style=CELESTE)
                arriba.append(buscado + "▌\n", style=BLANCO)
            if len(visibles_lista) == 0:
                arriba.append("\n  No hay paises que coincidan.", style=AMARILLO)
            abajo = Text()
            if primero > 0:
                abajo.append(f"  ▲ {primero} mas arriba   ", style=GRIS)
            if ultimo < len(visibles_lista):
                abajo.append(f"  ▼ {len(visibles_lista) - ultimo} mas abajo", style=GRIS)
            izquierda = Group(arriba, tabla, abajo)

            if len(visibles_lista) > 0:
                actual = visibles_lista[elegido]
                mapa = dibujar_mapa(nombres_de(visibles_lista), actual["nombre"])
                abajo_mapa = detalle(todos, actual, 22)
                derecha = f"{elegido + 1} de {len(visibles_lista)}"
            else:
                mapa = dibujar_mapa([], "")
                abajo_mapa = Text("")
                derecha = "0 paises"
            if modo == "VER":
                pie = "↑ ↓ mover    Enter ver ficha    Esc volver"
            elif modo == "BUSCAR":
                pie = "Escribi para buscar    ↑ ↓ mover    Enter ver ficha    Esc volver"
            else:
                pie = "Escribi para buscar    ↑ ↓ mover    Enter elegir    Esc volver"
            live.update(pantalla(titulo, derecha, izquierda, mapa, abajo_mapa, pie), refresh=True)

            tecla = leer_tecla()
            if tecla == "ARRIBA":
                if elegido > 0:
                    elegido -= 1
            elif tecla == "ABAJO":
                if elegido < len(visibles_lista) - 1:
                    elegido += 1
            elif tecla == "ESC":
                salir = True
            elif tecla == "ENTER":
                if len(visibles_lista) > 0:
                    if modo == "ELEGIR":
                        resultado = visibles_lista[elegido]
                        salir = True
                    else:
                        # se frena esta pantalla un momento para mostrar la ficha
                        live.stop()
                        ficha(todos, visibles_lista[elegido])
                        live.start()
            elif modo != "VER":
                # en los modos de busqueda, las letras se van sumando a lo que se busca
                if tecla == "BORRAR":
                    buscado = buscado[:-1]
                elif len(tecla) == 1 and (tecla.isalpha() or tecla == " ") and len(buscado) < 20:
                    buscado += tecla.lower()
                    elegido = 0
                    primero = 0
    return resultado, buscado
