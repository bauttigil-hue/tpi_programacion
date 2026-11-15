# validaciones.py
# Todo lo que revisa que los datos esten bien.
# Las funciones revisar_...() reciben lo que escribio el usuario y devuelven
# True si esta bien, o un texto con el error si esta mal.
# Esa es la forma que pide la libreria questionary para validar lo que se escribe.

CONTINENTES = ["America", "Europa", "Asia", "Africa", "Oceania"]


# cambia las vocales con tilde por vocales sin tilde, asi "America" y "América" son lo mismo
def quitar_tildes(texto):
    texto = texto.replace("á", "a").replace("é", "e").replace("í", "i")
    texto = texto.replace("ó", "o").replace("ú", "u")
    texto = texto.replace("Á", "A").replace("É", "E").replace("Í", "I")
    texto = texto.replace("Ó", "O").replace("Ú", "U")
    return texto


# se fija si un pais ya esta en la lista (sin importar mayusculas)
def esta_repetido(paises, nombre):
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            return True
    return False


# El nombre no puede estar vacio y solo puede tener letras y espacios
def revisar_nombre(texto):
    texto = texto.strip()
    if texto == "":
        return "El nombre no puede estar vacio"
    if not texto.replace(" ", "").isalpha():
        return "El nombre solo puede tener letras y espacios"
    return True


# Numero entero mayor a 0 (para la poblacion y la superficie)
def revisar_positivo(texto):
    texto = texto.strip()
    if texto == "":
        return "No puede estar vacio"
    if not texto.isdecimal():
        return "Tiene que ser un numero entero, sin puntos ni comas"
    if int(texto) <= 0:
        return "Tiene que ser mayor a 0"
    return True


# Numero entero que puede ser 0 (para el minimo y el maximo de los filtros)
def revisar_entero(texto):
    texto = texto.strip()
    if texto == "":
        return "No puede estar vacio"
    if not texto.isdecimal():
        return "Tiene que ser un numero entero, sin puntos ni comas"
    return True
