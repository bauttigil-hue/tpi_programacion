# estadisticas.py
# Calcula y muestra las estadisticas de los paises.

from rich.console import Group
from rich.live import Live
from rich.table import Table
from rich.text import Text

from consola import consola, barra, con_puntos, color_de_continente, GRIS, BLANCO, CELESTE
from teclado import leer_tecla
from banderas import bandera_chica
from mapa import dibujar_mapa
from vistas import pantalla, pausa, resumen, nombres_de


# Opcion "Estadisticas": mayor y menor poblacion, promedios y cantidad de paises por continente
def mostrar_estadisticas(paises):
    if len(paises) == 0:
        pausa("Estadisticas", "No hay paises cargados.")
        return
    mayor = paises[0]
    menor = paises[0]
    total_poblacion = 0
    total_superficie = 0
    continentes = {}
    # con un solo recorrido se saca todo
    for pais in paises:
        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais
        if pais["poblacion"] < menor["poblacion"]:
            menor = pais
        total_poblacion += pais["poblacion"]
        total_superficie += pais["superficie"]
        # el diccionario se usa como contador: la clave es el continente
        if pais["continente"] in continentes:
            continentes[pais["continente"]] += 1
        else:
            continentes[pais["continente"]] = 1
    promedio_poblacion = round(total_poblacion / len(paises), 2)
    promedio_superficie = round(total_superficie / len(paises), 2)

    # --- de aca para abajo es solo mostrar los resultados ---
    destacados = Table.grid(padding=(0, 1))
    for dato in [["Mayor poblacion", mayor], ["Menor poblacion", menor]]:
        texto = Text(dato[0] + "\n", style=GRIS)
        texto.append(dato[1]["nombre"], style=BLANCO)
        texto.append("  " + con_puntos(dato[1]["poblacion"]) + " hab\n")
        destacados.add_row(Text(""), bandera_chica(dato[1]["nombre"]), texto)

    promedios = Text()
    promedios.append("  Promedio de poblacion   ")
    promedios.append(str(promedio_poblacion), style=BLANCO)
    promedios.append(" hab\n  Promedio de superficie  ")
    promedios.append(str(promedio_superficie), style=BLANCO)
    promedios.append(" km2\n\n")
    promedios.append("  Paises por continente\n", style=CELESTE)

    # se busca el continente con mas paises para saber cuanto mide la barra mas larga
    maximo = 0
    for continente in continentes:
        if continentes[continente] > maximo:
            maximo = continentes[continente]
    barras = Text()
    for continente in continentes:
        cantidad = continentes[continente]
        barras.append(f"  {continente:<10}")
        barras.append_text(barra(cantidad, maximo, 26, color_de_continente(continente)))
        barras.append(f"  {cantidad}\n")

    izquierda = Group(destacados, promedios, barras)
    todo = pantalla("Estadisticas", f"{len(paises)} paises", izquierda,
                    dibujar_mapa(nombres_de(paises), mayor["nombre"]), resumen(paises),
                    "Pulsa una tecla para volver")
    with Live(todo, console=consola, screen=True, auto_refresh=False) as live:
        live.refresh()
        leer_tecla()
