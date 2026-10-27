ARCHIVO_CSV = "paises.csv"
ENCABEZADO = "nombre,poblacion,superficie,continente"


# CSV


# lee el CSV y devuelve una lista de diccionarios con los paises
# lss lineas con errores de formato se saltean y dice cual fallo
def cargar_paises(ruta):
    paises = []

    # si el archivo no existe, se avisa y se empieza con lista vacia
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
    except FileNotFoundError:
        print("no se encontro el archivo CSV. se empieza con lista vacia.")
        return paises

    if len(lineas) == 0:
        print("el archivo CSV esta vacio. se empieza con lista vacia.")
        return paises

    
    for i in range(1, len(lineas)):
        linea = lineas[i].strip()
        if linea == "":
            continue
        pais = convertir_linea(linea)
        if pais is None:
            print(f"Linea {i + 1} con formato invalido, se ignora: {linea}")
        elif buscar_exacto(paises, pais["nombre"]) is not None:
            print(f"Linea {i + 1}: el pais '{pais['nombre']}' esta repetido, se ignora.")
        else:
            paises.append(pais)

    print(f"Se cargaron {len(paises)} paises desde el CSV.")
    return paises


# convierte una linea del CSV en diccionario
# None si la linea no tiene el formato correcto
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


# escribe la lista de paises en el CSV para que los cambios no se pierdan.
def guardar_paises(ruta, paises):
    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(ENCABEZADO + "\n")
            for pais in paises:
                archivo.write(f"{pais['nombre']},{pais['poblacion']},{pais['superficie']},{pais['continente']}\n")
    except PermissionError:
        print("Error: no se pudo guardar el CSV. Fijate que no este abierto en otro programa.")



# Funciones de entrada y validacion


# cambia las vocales con tilde por vocales sin tilde.
# America==América
def quitar_tildes(texto):
    texto = texto.replace("á", "a").replace("é", "e").replace("í", "i")
    texto = texto.replace("ó", "o").replace("ú", "u")
    texto = texto.replace("Á", "A").replace("É", "E").replace("Í", "I")
    texto = texto.replace("Ó", "O").replace("Ú", "U")
    return texto


# pide un texto que no puede estar vacio y tiene q tener solo letras y espacios.
# devuelve el texto sin tildes, o None si la entrada es invalida.
def pedir_texto(mensaje):
    texto = input(mensaje).strip()
    if texto == "":
        print("Error: no puede estar vacio.")
        return None
    if not texto.replace(" ", "").isalpha():
        print("Error: solo letras.")
        return None
    return quitar_tildes(texto)


# Pide un numero entero mayor a 0. Devuelve None si la entrada es invalida.
def pedir_entero_positivo(mensaje):
    valor = input(mensaje).strip()
    if valor == "":
        print("Error: no puede estar vacio.")
        return None
    if not valor.isdecimal() or int(valor) <= 0:
        print("Error: tiene que ser un numero entero mayor a 0.")
        return None
    return int(valor)



# Muestra los datos de un pais en una linea.
def mostrar_pais(pais):
    print(f"Nombre: {pais['nombre']}, Poblacion: {pais['poblacion']}, "
          f"Superficie: {pais['superficie']} km2, Continente: {pais['continente']}")


# Muestra todos los paises de una lista, o un aviso si esta vacia.
def mostrar_lista(paises):
    if len(paises) == 0:
        print("No se encontraron paises.")
        return
    for pais in paises:
        mostrar_pais(pais)


def buscar_exacto(paises, nombre):
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            return pais
    return None


# menu

# Agrega un pais nuevo validando que no haya campos vacios.
def agregar_pais(paises):
    nombre = pedir_texto("Ingresa el nombre del pais: ")
    if nombre is None:
        return
    nombre = nombre.title()
    if buscar_exacto(paises, nombre) is not None:
        print("Error: el pais ya existe.")
        return
    poblacion = pedir_entero_positivo("Ingresa la poblacion del pais: ")
    if poblacion is None:
        return
    superficie = pedir_entero_positivo("Ingresa la superficie del pais (km2): ")
    if superficie is None:
        return
    continente = pedir_texto("Ingresa el continente del pais: ")
    if continente is None:
        return
    paises.append({"nombre": nombre,
                   "poblacion": poblacion,
                   "superficie": superficie,
                   "continente": continente.capitalize()})
    guardar_paises(ARCHIVO_CSV, paises)
    print(f"Pais '{nombre}' agregado correctamente.")


# Actualiza la poblacion y la superficie de un pais
def actualizar_pais(paises):
    nombre = pedir_texto("Ingresa el nombre del pais a actualizar: ")
    if nombre is None:
        return
    pais = buscar_exacto(paises, nombre)
    if pais is None:
        print("Error: el pais no existe.")
        return
    poblacion = pedir_entero_positivo("Ingresa la nueva poblacion del pais: ")
    if poblacion is None:
        return
    superficie = pedir_entero_positivo("Ingresa la nueva superficie del pais (km2): ")
    if superficie is None:
        return
    pais["poblacion"] = poblacion
    pais["superficie"] = superficie
    guardar_paises(ARCHIVO_CSV, paises)
    print(f"Pais '{pais['nombre']}' actualizado correctamente.")


# Busca paises(parcial o exacto).
def buscar_pais(paises):
    texto = input("Ingresa el nombre (o parte del nombre) del pais: ").strip()
    if texto == "":
        print("Error: la busqueda no puede estar vacia.")
        return
    texto = quitar_tildes(texto).lower()
    encontrados = []
    for pais in paises:
        if texto in pais["nombre"].lower():
            encontrados.append(pais)
    mostrar_lista(encontrados)


# Filtra paises por continente, rango de poblacion o rango de superficie.
def filtrar_paises(paises):
    print("Filtrar por:")
    print("1. Continente")
    print("2. Rango de poblacion")
    print("3. Rango de superficie")
    filtro = input("Elija un filtro: ").strip()
    encontrados = []
    if filtro == "1":
        continente = pedir_texto("Ingresa el continente: ")
        if continente is None:
            return
        for pais in paises:
            if pais["continente"].lower() == continente.lower():
                encontrados.append(pais)
    elif filtro == "2" or filtro == "3":
        # Se elige que dato del pais se va a comparar
        if filtro == "2":
            campo = "poblacion"
        else:
            campo = "superficie"
        minimo = input(f"Ingresa la {campo} minima: ").strip()
        maximo = input(f"Ingresa la {campo} maxima: ").strip()
        if not minimo.isdecimal() or not maximo.isdecimal():
            print("Error: solo numeros enteros positivos.")
            return
        minimo = int(minimo)
        maximo = int(maximo)
        if minimo > maximo:
            print("Error: el minimo no puede ser mayor al maximo.")
            return
        for pais in paises:
            if pais[campo] >= minimo and pais[campo] <= maximo:
                encontrados.append(pais)
    else:
        print("Error: filtro invalido.")
        return
    mostrar_lista(encontrados)


# Devuelve una copia de la lista ordenad
def ordenar_lista(paises, campo, descendente):
    ordenados = []
    for pais in paises:
        ordenados.append(pais)
    for i in range(len(ordenados) - 1):
        for j in range(len(ordenados) - 1 - i):
            a = ordenados[j][campo]
            b = ordenados[j + 1][campo]
            if campo == "nombre":
                a = a.lower()
                b = b.lower()
            intercambiar = False
            if descendente:
                if a < b:
                    intercambiar = True
            else:
                if a > b:
                    intercambiar = True
            if intercambiar:
                aux = ordenados[j]
                ordenados[j] = ordenados[j + 1]
                ordenados[j + 1] = aux
    return ordenados


def ordenar_paises(paises):
    if len(paises) == 0:
        print("No hay paises cargados.")
        return
    print("Ordenar por:")
    print("1. Nombre")
    print("2. Poblacion")
    print("3. Superficie")
    opciones = {"1": "nombre", "2": "poblacion", "3": "superficie"}
    orden = input("Elija un orden: ").strip()
    if orden not in opciones:
        print("Error: orden invalido.")
        return
    sentido = input("Ascendente (A) o descendente (D): ").strip().upper()
    if sentido != "A" and sentido != "D":
        print("Error: tiene que ingresar A o D.")
        return
    mostrar_lista(ordenar_lista(paises, opciones[orden], sentido == "D"))


# Muestra mayor/menor poblacion, promedios y cantidad de paises por continente.
def mostrar_estadisticas(paises):
    if len(paises) == 0:
        print("No hay paises cargados.")
        return
    mayor = paises[0]
    menor = paises[0]
    total_poblacion = 0
    total_superficie = 0
    continentes = {}
    for pais in paises:
        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais
        if pais["poblacion"] < menor["poblacion"]:
            menor = pais
        total_poblacion += pais["poblacion"]
        total_superficie += pais["superficie"]
        if pais["continente"] in continentes:
            continentes[pais["continente"]] += 1
        else:
            continentes[pais["continente"]] = 1
    promedio_poblacion = round(total_poblacion / len(paises), 2)
    promedio_superficie = round(total_superficie / len(paises), 2)
    print(f"Pais con mayor poblacion: {mayor['nombre']} ({mayor['poblacion']})")
    print(f"Pais con menor poblacion: {menor['nombre']} ({menor['poblacion']})")
    print(f"Promedio de poblacion: {promedio_poblacion}")
    print(f"Promedio de superficie: {promedio_superficie} km2")
    print("Cantidad de paises por continente:")
    for continente in continentes:
        print(f"  {continente}: {continentes[continente]}")



# Menu principal

# Imprime las opciones del menu.
def mostrar_menu():
    print("\nMenu Paises")
    print("1. Agregar pais")
    print("2. Actualizar poblacion y superficie de un pais")
    print("3. Buscar pais por nombre")
    print("4. Filtrar paises")
    print("5. Ver paises")
    print("6. Ordenar paises")
    print("7. Mostrar estadisticas")
    print("8. Salir")


# Carga los datos del CSV y ejecuta el menu hasta que el usuario salga.
def main():
    paises = cargar_paises(ARCHIVO_CSV)
    while True:
        mostrar_menu()
        opcion = input("Elija una opcion: ").strip()
        if opcion == "1":
            agregar_pais(paises)
        elif opcion == "2":
            actualizar_pais(paises)
        elif opcion == "3":
            buscar_pais(paises)
        elif opcion == "4":
            filtrar_paises(paises)
        elif opcion == "5":
            mostrar_lista(paises)
        elif opcion == "6":
            ordenar_paises(paises)
        elif opcion == "7":
            mostrar_estadisticas(paises)
        elif opcion == "8":
            print("Saliendo del programa.")
            break
        else:
            print("Error: opcion invalida. Elija un numero del 1 al 8.")


main()