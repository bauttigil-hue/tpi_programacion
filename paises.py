# paises.py
# Las operaciones con los paises: agregar, actualizar, buscar, filtrar y ordenar.
# Cada una devuelve un texto corto con lo que se hizo, para mostrarlo en el menu.
# Si no se hizo nada (se cancelo o hubo un error) devuelven None.

from consola import con_puntos
from validaciones import esta_repetido, CONTINENTES
from archivo import guardar_paises
from vistas import elegir, explorar, ficha, pausa
from formularios import (empezar_formulario, pedir_nombre, pedir_positivo, pedir_entero,
                         pedir_continente, avisar_error)
from mapa import continente_segun_mapa
from animaciones import (se_puede_animar, calcular_espera, empezar_ordenamiento,
                         mostrar_paso, terminar_ordenamiento)


# Guarda el CSV. Devuelve el texto que se le muestra al usuario.
def guardar(paises, texto):
    if guardar_paises(paises):
        return texto + " y guardado en paises.csv"
    return texto + ", pero NO se pudo guardar el CSV"


# Opcion "Agregar pais"
def agregar_pais(paises):
    empezar_formulario("Agregar pais")
    # se pide el nombre hasta que no este repetido (o hasta que se cancele)
    nombre = pedir_nombre()
    while nombre is not None and esta_repetido(paises, nombre):
        avisar_error(f"{nombre} ya existe en la lista.")
        empezar_formulario("Agregar pais")
        nombre = pedir_nombre()
    if nombre is None:
        return None
    poblacion = pedir_positivo("Poblacion:")
    if poblacion is None:
        return None
    superficie = pedir_positivo("Superficie (km2):")
    if superficie is None:
        return None
    # si es un pais conocido, ya aparece marcado su continente
    continente = pedir_continente(continente_segun_mapa(nombre))
    if continente is None:
        return None
    pais = {"nombre": nombre, "poblacion": poblacion,
            "superficie": superficie, "continente": continente}
    paises.append(pais)
    ficha(paises, pais, guardar(paises, "Agregado"))
    return f"Se agrego {nombre}"


# Opcion "Actualizar pais": cambia la poblacion y la superficie
def actualizar_pais(paises):
    # primero se elige el pais de la lista (se puede escribir para buscarlo)
    pais, texto = explorar(paises, paises, "Actualizar: elegi el pais", "ELEGIR")
    if pais is None:
        return None
    empezar_formulario("Actualizar " + pais["nombre"])
    # las preguntas arrancan con el dato que el pais tiene ahora ya escrito
    poblacion = pedir_positivo("Nueva poblacion:", str(pais["poblacion"]))
    if poblacion is None:
        return None
    superficie = pedir_positivo("Nueva superficie (km2):", str(pais["superficie"]))
    if superficie is None:
        return None
    pais["poblacion"] = poblacion
    pais["superficie"] = superficie
    ficha(paises, pais, guardar(paises, "Actualizado"))
    return f"Se actualizo {pais['nombre']}"


# Opcion "Buscar pais": por nombre completo o por una parte.
# La busqueda se hace en la lista: con cada letra que se escribe quedan menos paises.
def buscar_pais(paises):
    pais, texto = explorar(paises, paises, "Buscar pais", "BUSCAR")
    if texto == "":
        return None
    return f"Se busco '{texto}'"


# Opcion "Filtrar paises": por continente, rango de poblacion o rango de superficie
def filtrar_paises(paises):
    filtro = elegir("Filtrar paises",
                    ["Por continente", "Por rango de poblacion", "Por rango de superficie"],
                    ["Solo los paises de un continente",
                     "Entre un minimo y un maximo de habitantes",
                     "Entre un minimo y un maximo de km2"], paises)
    if filtro == -1:
        return None
    encontrados = []
    if filtro == 0:
        ayudas = []
        for continente in CONTINENTES:
            ayudas.append(f"Muestra solo los paises de {continente}")
        posicion = elegir("Filtrar por continente", CONTINENTES, ayudas, paises, "", True)
        if posicion == -1:
            return None
        for pais in paises:
            if pais["continente"].lower() == CONTINENTES[posicion].lower():
                encontrados.append(pais)
        detalle = CONTINENTES[posicion]
    else:
        # poblacion y superficie se filtran igual, solo cambia que dato se mira
        if filtro == 1:
            campo = "poblacion"
        else:
            campo = "superficie"
        # se piden el minimo y el maximo hasta que el rango este bien
        rango_bien = False
        while not rango_bien:
            empezar_formulario(f"Filtrar por {campo}")
            minimo = pedir_entero(f"{campo.capitalize()} minima:")
            if minimo is None:
                return None
            maximo = pedir_entero(f"{campo.capitalize()} maxima:")
            if maximo is None:
                return None
            if minimo > maximo:
                avisar_error("El minimo no puede ser mayor al maximo.")
            else:
                rango_bien = True
        for pais in paises:
            if pais[campo] >= minimo and pais[campo] <= maximo:
                encontrados.append(pais)
        detalle = f"{campo} {con_puntos(minimo)} a {con_puntos(maximo)}"
    explorar(paises, encontrados, "Filtro: " + detalle, "VER")
    return f"Filtro: {detalle}"


# Devuelve una copia de la lista ordenada con el metodo burbuja.
#   campo: "nombre", "poblacion" o "superficie"      descendente: True o False
#   animacion: la pantalla donde se va mostrando cada paso (None si no se anima)
# Devuelve tres cosas: la lista ordenada, cuantas comparaciones hizo y cuantos intercambios.
def ordenar_lista(paises, campo, descendente, animacion, titulo):
    ordenados = []
    for pais in paises:
        ordenados.append(pais)
    comparaciones = 0
    intercambios = 0
    espera = calcular_espera(len(ordenados))
    for i in range(len(ordenados) - 1):
        for j in range(len(ordenados) - 1 - i):
            a = ordenados[j][campo]
            b = ordenados[j + 1][campo]
            if campo == "nombre":
                a = a.lower()
                b = b.lower()
            comparaciones += 1
            intercambiar = False
            if descendente:
                if a < b:
                    intercambiar = True
            else:
                if a > b:
                    intercambiar = True
            if animacion is not None:
                mostrar_paso(animacion, ordenados, titulo, campo, j, "COMPARAR", i + 1,
                             comparaciones, intercambios, espera)
            if intercambiar:
                aux = ordenados[j]
                ordenados[j] = ordenados[j + 1]
                ordenados[j + 1] = aux
                intercambios += 1
                if animacion is not None:
                    mostrar_paso(animacion, ordenados, titulo, campo, j, "INTERCAMBIAR", i + 1,
                                 comparaciones, intercambios, espera)
    return ordenados, comparaciones, intercambios


# Opcion "Ordenar paises": se elige por que dato y en que sentido
def ordenar_paises(paises):
    if len(paises) < 2:
        pausa("Ordenar paises", "Hacen falta al menos 2 paises para ordenar.")
        return None
    campos = ["nombre", "poblacion", "superficie"]
    posicion = elegir("Ordenar paises", ["Por nombre", "Por poblacion", "Por superficie"],
                      ["Orden alfabetico", "Segun la cantidad de habitantes", "Segun los km2"], paises)
    if posicion == -1:
        return None
    campo = campos[posicion]
    sentido = elegir(f"Ordenar por {campo}", ["Ascendente", "Descendente"],
                     ["De menor a mayor (o de la A a la Z)", "De mayor a menor (o de la Z a la A)"], paises)
    if sentido == -1:
        return None
    if sentido == 1:
        texto_sentido = "descendente"
    else:
        texto_sentido = "ascendente"
    titulo = f"Por {campo} ({texto_sentido})"
    animacion = None
    if se_puede_animar(len(paises)):
        animacion = empezar_ordenamiento()
    ordenados, comparaciones, intercambios = ordenar_lista(paises, campo, sentido == 1, animacion, titulo)
    if animacion is not None:
        terminar_ordenamiento(animacion, ordenados, titulo, campo, comparaciones, intercambios)
    explorar(paises, ordenados, titulo, "VER")
    return f"Orden por {campo} {texto_sentido}"
