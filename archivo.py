# archivo.py
# Todo lo que tiene que ver con el archivo CSV: leerlo y guardarlo.

from validaciones import quitar_tildes, esta_repetido

ARCHIVO_CSV = "paises.csv"
ENCABEZADO = "nombre,poblacion,superficie,continente"


# convierte una linea del CSV en un diccionario
# devuelve None si la linea no tiene el formato correcto
def convertir_linea(linea):
    campos = linea.split(",")
    if len(campos) != 4:
        return None
    nombre = quitar_tildes(campos[0].strip()).title()
    poblacion = campos[1].strip()
    superficie = campos[2].strip()
    continente = quitar_tildes(campos[3].strip()).capitalize()
    if nombre == "" or continente == "":
        return None
    if not poblacion.isdecimal() or not superficie.isdecimal():
        return None
    if int(poblacion) <= 0 or int(superficie) <= 0:
        return None
    return {"nombre": nombre,
            "poblacion": int(poblacion),
            "superficie": int(superficie),
            "continente": continente}


# lee el CSV y devuelve dos cosas: la lista de paises y una lista de avisos
# los avisos son los problemas que encontro (lineas mal escritas, repetidos, etc)
def cargar_paises():
    paises = []
    avisos = []

    try:
        with open(ARCHIVO_CSV, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
    except FileNotFoundError:
        avisos.append("No se encontro paises.csv. Se empieza con la lista vacia.")
        return paises, avisos
    except UnicodeDecodeError:
        avisos.append("No se pudo leer paises.csv (guardarlo como UTF-8). Se empieza con la lista vacia.")
        return paises, avisos

    if len(lineas) == 0:
        avisos.append("El archivo paises.csv esta vacio.")
        return paises, avisos

    # se arranca en 1 para saltear el encabezado
    for i in range(1, len(lineas)):
        linea = lineas[i].strip()
        if linea != "":
            pais = convertir_linea(linea)
            if pais is None:
                avisos.append(f"Linea {i + 1} con formato invalido, se ignora: {linea}")
            elif esta_repetido(paises, pais["nombre"]):
                avisos.append(f"Linea {i + 1}: el pais '{pais['nombre']}' esta repetido, se ignora.")
            else:
                paises.append(pais)
    return paises, avisos


# escribe toda la lista de paises en el CSV
# devuelve True si pudo guardar y False si no
def guardar_paises(paises):
    try:
        with open(ARCHIVO_CSV, "w", encoding="utf-8") as archivo:
            archivo.write(ENCABEZADO + "\n")
            for pais in paises:
                archivo.write(f"{pais['nombre']},{pais['poblacion']},{pais['superficie']},{pais['continente']}\n")
        return True
    except PermissionError:
        return False
