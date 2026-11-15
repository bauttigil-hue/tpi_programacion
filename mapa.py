# mapa.py
# Dibuja un mapa del mundo en la consola.
# El mapa es una matriz de letras (igual que las banderas): 28 filas de 64 columnas.
#   espacio = mar
#   letra minuscula = tierra de un continente (a America, e Europa, s Asia, f Africa, o Oceania)
#   letra mayuscula o numero = un pais que esta dibujado entero (ver PAISES_DEL_MAPA)
# Los paises que no estan dibujados enteros (porque son chicos o no entraban) se marcan
# con un punto en el lugar donde quedan (ver PUNTOS_DEL_MAPA).
# La matriz se armo una sola vez a partir de los datos libres de Natural Earth.

from rich.text import Text

from banderas import clave_de


MAPA = [
    "               FFFFFaaaaaaaaa     e                             ",
    "          FFF FFFF    aaaaaaa                  YYYYYY    Y      ",
    "   GGGGFFFFFFFFFFFFF  aaaaaa       7eYY  YYYYYYYYYYYYYYYYYYYYYYY",
    " YGGGGGFFFFFFFFFF  FF  aa   e     77eYYYYYYYYYYYYYYYYYYYYYYYYYYY",
    "   GGGGFFFFFFFFF  FFF            e7 eYYYYYYYYYYYYYYYYYYYYYYYYY  ",
    "         FFFFFFFF FFFF         2 LLeeYYYYYYY8YYYYYYYYYYYY   Y   ",
    "         FFFFFFFFFFFFF         NNLLeeeeYY888888Y999Y9IIYY       ",
    "          GGGGGGGFFGF          MNOOee  YY88888III999IIII H      ",
    "          GGGGGGGGG          ZMM  Oe33335ssssIIIIIIIIIs         ",
    "           GGGGGGG             f66    ss555ssJIIIIIIIIK H       ",
    "            EEGGGG            f666ffPP44s55ssJIIIIIIII          ",
    "            EEE              ff666ffPP44445sJJJJJIIII           ",
    "             EEEE            fff6ffffff444   JJ sss             ",
    "               Ea            ffffffffffss    J   sss            ",
    "                 aV00        fffQQQffffff                       ",
    "                  VV0aa       ff Qfffffff        ss s           ",
    "                 1VVBBBB         fffffff          ssss          ",
    "                  UBBBBBBB        fffff                 so      ",
    "                  UBBBBBBB        fffff                         ",
    "                   UWBBBB         fffff f             SSSS      ",
    "                   CWXBBB         ffff  f            SSSSSS     ",
    "                   CAABB          ffRR              SSSSSSS     ",
    "                   AAABD           RRR              SSSSSSS     ",
    "                   AAA                                  SSS     ",
    "                   AA                                           ",
    "                   A                                          T ",
    "                  CA                                            ",
    "                   C                                            ",
]

ANCHO_MAPA = 64     # columnas de la matriz (y letras que ocupa en la pantalla)
ALTO_MAPA = 14      # renglones que ocupa en la pantalla (28 filas de a 2 por renglon)

# Para cada pais que el mapa conoce: [su letra en la matriz, su continente]
PAISES_DEL_MAPA = {
    "argentina": ["A", "America"],
    "brasil": ["B", "America"],
    "chile": ["C", "America"],
    "uruguay": ["D", "America"],
    "mexico": ["E", "America"],
    "canada": ["F", "America"],
    "estados unidos": ["G", "America"],
    "japon": ["H", "Asia"],
    "china": ["I", "Asia"],
    "india": ["J", "Asia"],
    "corea del sur": ["K", "Asia"],
    "alemania": ["L", "Europa"],
    "espana": ["M", "Europa"],
    "francia": ["N", "Europa"],
    "italia": ["O", "Europa"],
    "egipto": ["P", "Africa"],
    "nigeria": ["Q", "Africa"],
    "sudafrica": ["R", "Africa"],
    "australia": ["S", "Oceania"],
    "nueva zelanda": ["T", "Oceania"],
    "peru": ["U", "America"],
    "colombia": ["V", "America"],
    "bolivia": ["W", "America"],
    "paraguay": ["X", "America"],
    "rusia": ["Y", "Europa"],
    "portugal": ["Z", "Europa"],
    "venezuela": ["0", "America"],
    "ecuador": ["1", "America"],
    "reino unido": ["2", "Europa"],
    "turquia": ["3", "Asia"],
    "arabia saudita": ["4", "Asia"],
    "iran": ["5", "Asia"],
    "argelia": ["6", "Africa"],
    "suecia": ["7", "Europa"],
    "kazajistan": ["8", "Asia"],
    "mongolia": ["9", "Asia"],
}

# Para los demas paises: [fila, columna, continente] del punto donde quedan en la matriz.
# Se calcularon una sola vez con la latitud y la longitud de cada pais (datos libres de world-countries).
PUNTOS_DEL_MAPA = {
    "afganistan": [9, 43, "Asia"],
    "albania": [7, 35, "Europa"],
    "andorra": [7, 32, "Europa"],
    "angola": [19, 35, "Africa"],
    "antigua y barbuda": [12, 20, "America"],
    "armenia": [8, 39, "Asia"],
    "austria": [6, 34, "Europa"],
    "azerbaiyan": [8, 40, "Asia"],
    "bahamas": [11, 18, "America"],
    "bahrein": [11, 40, "Asia"],
    "bangladesh": [11, 47, "Asia"],
    "barbados": [13, 21, "America"],
    "belgica": [5, 32, "Europa"],
    "belice": [12, 15, "America"],
    "benin": [14, 32, "Africa"],
    "bielorrusia": [5, 36, "Europa"],
    "bosnia y herzegovina": [7, 35, "Europa"],
    "botswana": [20, 36, "Africa"],
    "brunei": [15, 52, "Asia"],
    "bulgaria": [7, 36, "Europa"],
    "burkina faso": [13, 31, "Africa"],
    "burundi": [17, 37, "Africa"],
    "butan": [10, 48, "Asia"],
    "cabo verde": [13, 27, "Africa"],
    "camboya": [13, 50, "Asia"],
    "camerun": [15, 34, "Africa"],
    "catar": [11, 41, "Asia"],
    "chad": [13, 35, "Africa"],
    "chipre": [9, 37, "Europa"],
    "comoras": [18, 39, "Africa"],
    "congo": [16, 34, "Africa"],
    "corea del norte": [8, 54, "Asia"],
    "costa de marfil": [14, 30, "Africa"],
    "costa rica": [14, 16, "America"],
    "croacia": [7, 34, "Europa"],
    "cuba": [11, 17, "America"],
    "dinamarca": [4, 33, "Europa"],
    "dominica": [13, 20, "America"],
    "el salvador": [13, 15, "America"],
    "emiratos arabes unidos": [11, 41, "Asia"],
    "eritrea": [13, 38, "Africa"],
    "eslovaquia": [6, 35, "Europa"],
    "eslovenia": [6, 34, "Europa"],
    "estonia": [4, 36, "Europa"],
    "esuatini": [21, 37, "Africa"],
    "etiopia": [14, 38, "Africa"],
    "fiji": [20, 63, "Oceania"],
    "filipinas": [13, 53, "Asia"],
    "finlandia": [3, 36, "Europa"],
    "gabon": [16, 33, "Africa"],
    "gambia": [13, 28, "Africa"],
    "georgia": [7, 39, "Asia"],
    "ghana": [14, 31, "Africa"],
    "gibraltar": [8, 30, "Europa"],
    "granada": [13, 20, "America"],
    "grecia": [8, 35, "Europa"],
    "groenlandia": [1, 24, "America"],
    "guatemala": [13, 15, "America"],
    "guinea": [14, 30, "Africa"],
    "guinea bissau": [13, 29, "Africa"],
    "guinea ecuatorial": [16, 33, "Africa"],
    "guyana": [15, 21, "America"],
    "haiti": [12, 18, "America"],
    "honduras": [13, 16, "America"],
    "hong kong": [11, 52, "Asia"],
    "hungria": [6, 35, "Europa"],
    "indonesia": [17, 53, "Asia"],
    "irak": [9, 39, "Asia"],
    "irlanda": [5, 30, "Europa"],
    "islandia": [3, 28, "Europa"],
    "islas feroe": [3, 30, "Europa"],
    "islas marshall": [14, 61, "Oceania"],
    "islas salomon": [18, 60, "Oceania"],
    "israel": [9, 38, "Asia"],
    "jamaica": [12, 17, "America"],
    "jordania": [10, 38, "Asia"],
    "kenia": [16, 38, "Africa"],
    "kirguistan": [7, 45, "Asia"],
    "kiribati": [16, 62, "Oceania"],
    "kosovo": [7, 35, "Europa"],
    "kuwait": [10, 40, "Asia"],
    "laos": [12, 50, "Asia"],
    "lesoto": [22, 36, "Africa"],
    "letonia": [4, 36, "Europa"],
    "libano": [9, 38, "Asia"],
    "liberia": [15, 30, "Africa"],
    "libia": [11, 34, "Africa"],
    "liechtenstein": [6, 33, "Europa"],
    "lituania": [4, 36, "Europa"],
    "luxemburgo": [6, 32, "Europa"],
    "macedonia del norte": [7, 35, "Europa"],
    "madagascar": [20, 40, "Africa"],
    "malasia": [15, 52, "Asia"],
    "malaui": [19, 37, "Africa"],
    "maldivas": [15, 44, "Asia"],
    "mali": [12, 31, "Africa"],
    "malta": [9, 34, "Europa"],
    "marruecos": [9, 30, "Africa"],
    "mauricio": [20, 42, "Africa"],
    "mauritania": [12, 29, "Africa"],
    "micronesia": [15, 60, "Oceania"],
    "moldavia": [6, 37, "Europa"],
    "monaco": [7, 33, "Europa"],
    "montenegro": [7, 35, "Europa"],
    "mozambique": [20, 38, "Africa"],
    "myanmar": [11, 49, "Asia"],
    "namibia": [20, 34, "Africa"],
    "nauru": [16, 61, "Oceania"],
    "nepal": [10, 46, "Asia"],
    "nicaragua": [13, 16, "America"],
    "niger": [13, 33, "Africa"],
    "noruega": [3, 33, "Europa"],
    "oman": [12, 42, "Asia"],
    "paises bajos": [5, 32, "Europa"],
    "pakistan": [10, 44, "Asia"],
    "palau": [14, 55, "Oceania"],
    "palestina": [9, 38, "Asia"],
    "panama": [14, 17, "America"],
    "papua nueva guinea": [17, 58, "Oceania"],
    "polonia": [5, 35, "Europa"],
    "puerto rico": [12, 19, "America"],
    "republica centroafricana": [14, 35, "Africa"],
    "republica checa": [6, 34, "Europa"],
    "republica democratica del congo": [16, 36, "Africa"],
    "republica dominicana": [12, 19, "America"],
    "ruanda": [16, 37, "Africa"],
    "rumania": [6, 36, "Europa"],
    "sahara occidental": [11, 29, "Africa"],
    "samoa": [19, 0, "Oceania"],
    "san cristobal y nieves": [12, 20, "America"],
    "san marino": [7, 34, "Europa"],
    "san vicente y las granadinas": [13, 20, "America"],
    "santa lucia": [13, 20, "America"],
    "santo tome y principe": [16, 33, "Africa"],
    "senegal": [13, 29, "Africa"],
    "serbia": [7, 35, "Europa"],
    "seychelles": [17, 41, "Africa"],
    "sierra leona": [14, 29, "Africa"],
    "singapur": [16, 50, "Asia"],
    "siria": [9, 38, "Asia"],
    "somalia": [14, 40, "Africa"],
    "sri lanka": [14, 46, "Asia"],
    "sudan": [13, 37, "Africa"],
    "sudan del sur": [14, 37, "Africa"],
    "suiza": [6, 33, "Europa"],
    "suriname": [15, 21, "America"],
    "tailandia": [13, 49, "Asia"],
    "taiwan": [11, 53, "Asia"],
    "tanzania": [17, 38, "Africa"],
    "tayikistan": [8, 44, "Asia"],
    "timor oriental": [18, 54, "Asia"],
    "togo": [14, 32, "Africa"],
    "tonga": [20, 0, "Oceania"],
    "trinidad y tobago": [14, 20, "America"],
    "tunez": [9, 33, "Africa"],
    "turkmenistan": [8, 42, "Asia"],
    "tuvalu": [18, 63, "Oceania"],
    "ucrania": [6, 37, "Europa"],
    "uganda": [16, 37, "Africa"],
    "uzbekistan": [7, 43, "Asia"],
    "vanuatu": [19, 61, "Oceania"],
    "vaticano": [7, 34, "Europa"],
    "vietnam": [13, 51, "Asia"],
    "yemen": [13, 40, "Asia"],
    "yibuti": [14, 39, "Africa"],
    "zambia": [19, 37, "Africa"],
    "zimbabue": [20, 37, "Africa"],
    "inglaterra": [5, 31, "Europa"],
    "escocia": [4, 31, "Europa"],
    "gales": [5, 30, "Europa"],
}

# Para saber de que continente es cada letra de la matriz
CONTINENTE_DE_LETRA = {"a": "America", "e": "Europa", "s": "Asia", "f": "Africa", "o": "Oceania"}
for nombre in PAISES_DEL_MAPA:
    CONTINENTE_DE_LETRA[PAISES_DEL_MAPA[nombre][0]] = PAISES_DEL_MAPA[nombre][1]

# Colores [rojo, verde, azul]
MAR = [16, 22, 38]
TIERRA = [50, 56, 70]
ELEGIDO = [255, 255, 255]
COLOR_MAPA = {"America": [70, 200, 115], "Europa": [95, 145, 255], "Asia": [245, 205, 70],
              "Africa": [245, 105, 95], "Oceania": [80, 215, 215]}


# Devuelve la letra que tiene un pais en el mapa, o "" si no esta dibujado entero
def letra_de(nombre):
    clave = clave_de(nombre)
    if clave in PAISES_DEL_MAPA:
        return PAISES_DEL_MAPA[clave][0]
    return ""


# Devuelve [fila, columna, continente] del punto de un pais, o una lista vacia si no tiene
def punto_de(nombre):
    clave = clave_de(nombre)
    if clave in PUNTOS_DEL_MAPA:
        return PUNTOS_DEL_MAPA[clave]
    return []


# True si el pais se puede mostrar en el mapa (dibujado entero o con un punto)
def esta_en_mapa(nombre):
    return letra_de(nombre) != "" or len(punto_de(nombre)) > 0


# Devuelve el continente de un pais segun el mapa, o "" si el mapa no lo conoce
def continente_segun_mapa(nombre):
    clave = clave_de(nombre)
    if clave in PAISES_DEL_MAPA:
        return PAISES_DEL_MAPA[clave][1]
    if clave in PUNTOS_DEL_MAPA:
        return PUNTOS_DEL_MAPA[clave][2]
    return ""


# Devuelve un color mas oscuro: se multiplica cada parte por un numero entre 0 y 1
def oscurecer(rgb, cuanto):
    return [int(rgb[0] * cuanto), int(rgb[1] * cuanto), int(rgb[2] * cuanto)]


# Decide de que color va un cuadradito del mapa
def color_de_celda(letra, encendidas, letra_elegida, continente):
    if letra == " ":
        return MAR
    continente_celda = CONTINENTE_DE_LETRA[letra]
    color = COLOR_MAPA[continente_celda]
    if letra == letra_elegida:
        return ELEGIDO
    if continente_celda == continente:
        # continente resaltado: los paises cargados bien fuertes y el resto mas suave
        if letra in encendidas:
            return color
        return oscurecer(color, 0.5)
    if letra in encendidas:
        return oscurecer(color, 0.68)
    return TIERRA


# Devuelve el mapa dibujado, como un Text de rich.
#   nombres    lista con los nombres de los paises que van "encendidos" (con color)
#   elegido    nombre del pais que va resaltado en blanco ("" si ninguno)
#   continente continente que va resaltado ("" si ninguno)
#   hasta      cuantas columnas se dibujan (se usa en la animacion del principio)
# Cada renglon de la pantalla muestra DOS filas de la matriz: se usa el simbolo ▀
# (medio bloque de arriba). El color de la letra pinta la fila de arriba y el
# color de fondo pinta la fila de abajo.
def dibujar_mapa(nombres, elegido="", continente="", hasta=ANCHO_MAPA):
    encendidas = []
    for nombre in nombres:
        letra = letra_de(nombre)
        if letra != "":
            encendidas.append(letra)
    letra_elegida = letra_de(elegido)

    # los paises que van como punto se anotan en un diccionario: (fila, columna) -> color
    puntos = {}
    for nombre in nombres:
        punto = punto_de(nombre)
        if len(punto) > 0:
            puntos[(punto[0], punto[1])] = COLOR_MAPA[punto[2]]
    # el punto del pais elegido se dibuja como una crucecita blanca, para que se vea bien
    punto = punto_de(elegido)
    if len(punto) > 0:
        for corrida in [[0, 0], [0, -1], [0, 1], [-1, 0], [1, 0]]:
            puntos[(punto[0] + corrida[0], punto[1] + corrida[1])] = ELEGIDO

    texto = Text()
    for renglon in range(ALTO_MAPA):
        arriba = MAPA[renglon * 2]
        abajo = MAPA[renglon * 2 + 1]
        for x in range(ANCHO_MAPA):
            if x < hasta:
                color_arriba = color_de_celda(arriba[x], encendidas, letra_elegida, continente)
                color_abajo = color_de_celda(abajo[x], encendidas, letra_elegida, continente)
                # si en ese lugar hay un punto, gana el color del punto
                if (renglon * 2, x) in puntos:
                    color_arriba = puntos[(renglon * 2, x)]
                if (renglon * 2 + 1, x) in puntos:
                    color_abajo = puntos[(renglon * 2 + 1, x)]
            else:
                color_arriba = MAR
                color_abajo = MAR
            texto.append("▀", style=f"rgb({color_arriba[0]},{color_arriba[1]},{color_arriba[2]}) "
                                    f"on rgb({color_abajo[0]},{color_abajo[1]},{color_abajo[2]})")
        if renglon < ALTO_MAPA - 1:
            texto.append("\n")
    return texto
