# formularios.py
# Las preguntas que hay que contestar escribiendo. Usa la libreria QUESTIONARY,
# que se encarga de pedir el dato, mostrar el error si esta mal y volver a pedirlo.
# Todas devuelven None si el usuario cancela con Ctrl+C.

import questionary

from consola import consola, encabezado, GRIS
from validaciones import (revisar_nombre, revisar_positivo, revisar_entero, quitar_tildes,
                          CONTINENTES)
from banderas import nombres_conocidos

# colores de las preguntas, para que combinen con el resto del programa
ESTILO = questionary.Style([("qmark", "fg:#5FD7D7 bold"), ("question", "bold"),
                            ("answer", "fg:#5FD787 bold"), ("pointer", "fg:#5FD7D7 bold"),
                            ("highlighted", "fg:#5FD7D7 bold"), ("instruction", "fg:#808080")])


# Limpia la pantalla y pone el titulo arriba de las preguntas
def empezar_formulario(titulo):
    consola.clear()
    consola.print(encabezado(titulo, "Ctrl+C cancela"))
    consola.print()


# Pide el nombre de un pais. Mientras se escribe sugiere los paises que conoce.
def pedir_nombre():
    texto = questionary.autocomplete("Nombre del pais:", choices=nombres_conocidos(),
                                     validate=revisar_nombre, ignore_case=True,
                                     qmark="›", style=ESTILO).ask()
    if texto is None:
        return None
    return quitar_tildes(texto.strip()).title()


# Pide un numero entero mayor a 0. "ahora" es el valor que aparece ya escrito.
def pedir_positivo(mensaje, ahora=""):
    texto = questionary.text(mensaje, default=ahora, validate=revisar_positivo,
                             qmark="›", style=ESTILO).ask()
    if texto is None:
        return None
    return int(texto.strip())


# Pide un numero entero que puede ser 0
def pedir_entero(mensaje):
    texto = questionary.text(mensaje, validate=revisar_entero, qmark="›", style=ESTILO).ask()
    if texto is None:
        return None
    return int(texto.strip())


# Deja elegir el continente con las flechas. "sugerido" es el que aparece marcado.
def pedir_continente(sugerido):
    if sugerido not in CONTINENTES:
        sugerido = CONTINENTES[0]
    return questionary.select("Continente:", choices=CONTINENTES, default=sugerido,
                              qmark="›", style=ESTILO, instruction="(flechas y Enter)").ask()


# Muestra un error y espera un Enter
def avisar_error(texto):
    consola.print()
    consola.print("  × " + texto, style="#FF6B6B")
    consola.input("[" + GRIS + "]  Enter para seguir...[/]")
