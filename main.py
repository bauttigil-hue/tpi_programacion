# main.py
# Archivo principal: este es el que se ejecuta.
# Solo tiene el menu. Todo lo demas esta separado en otros archivos y se importa:
#   paises.py        agregar, actualizar, buscar, filtrar y ordenar
#   estadisticas.py  estadisticas
#   archivo.py       leer y guardar el CSV
#   validaciones.py  revisar los datos que se escriben
#   formularios.py   las preguntas que se contestan escribiendo
#   vistas.py        menu con flechas, lista de paises y ficha
#   animaciones.py   presentacion y ordenamiento animado
#   banderas.py      dibujo de las banderas
#   mapa.py          dibujo del mapa
#   teclado.py       leer una tecla
#   consola.py       colores, titulos y barras
#
# Usa tres librerias que hay que instalar una vez:   pip install -r requirements.txt
#   rich         colores, tablas y pantallas
#   readchar     leer las flechas del teclado
#   questionary  preguntas con validacion

import sys

# si falta alguna libreria se avisa como instalarla, en vez de mostrar un error feo
try:
    from consola import consola, VERDE
    from archivo import cargar_paises
    from vistas import elegir, explorar, pausa
    from animaciones import presentacion
    from paises import agregar_pais, actualizar_pais, buscar_pais, filtrar_paises, ordenar_paises
    from estadisticas import mostrar_estadisticas
except ImportError as error:
    print("Falta instalar una libreria:", error.name)
    print("Para instalarlas todas, escribi en la consola:")
    print("    pip install -r requirements.txt")
    sys.exit()

OPCIONES = ["Agregar pais", "Actualizar pais", "Buscar pais", "Filtrar paises",
            "Ver todos los paises", "Ordenar paises", "Estadisticas", "Salir"]

AYUDAS = ["Carga un pais nuevo",
          "Cambia la poblacion y la superficie",
          "Busca mientras escribis el nombre",
          "Por continente, poblacion o superficie",
          "Recorre la lista completa",
          "Mira como trabaja el metodo burbuja",
          "Mayor, menor, promedios y continentes",
          "Cierra el programa"]


def main():
    paises, avisos = cargar_paises()
    # si hubo problemas al leer el CSV se muestran antes de entrar al menu
    if len(avisos) > 0:
        pausa("Aviso al leer paises.csv", "\n  ! ".join(avisos))
    presentacion(paises)

    # las pantallas se van limpiando, asi que lo ultimo que se hizo
    # se guarda en esta variable y se muestra en el menu
    ultima = ""
    seguir = True
    while seguir:
        opcion = elegir("Gestion de paises", OPCIONES, AYUDAS, paises, ultima)
        hecho = None
        if opcion == 0:
            hecho = agregar_pais(paises)
        elif opcion == 1:
            hecho = actualizar_pais(paises)
        elif opcion == 2:
            hecho = buscar_pais(paises)
        elif opcion == 3:
            hecho = filtrar_paises(paises)
        elif opcion == 4:
            explorar(paises, paises, "Todos los paises", "VER")
        elif opcion == 5:
            hecho = ordenar_paises(paises)
        elif opcion == 6:
            mostrar_estadisticas(paises)
        elif opcion == 7:
            seguir = False
        if hecho is not None:
            ultima = "√ " + hecho

    consola.print("Programa cerrado. Los cambios quedaron guardados en paises.csv", style=VERDE)


# Si se corta el programa con Ctrl+C no se muestra un error feo
try:
    main()
except KeyboardInterrupt:
    print()
    print("Programa interrumpido.")
