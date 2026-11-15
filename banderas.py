# banderas.py
# Dibuja las banderas en la consola.
# Cada bandera es una matriz de 3 filas y 6 columnas, donde cada letra es un color.
# Estan simplificadas: son un dibujo chico, no la bandera exacta.
# Las funciones devuelven un Text de la libreria rich, que es un texto con colores.

from rich.text import Text

# Cada letra es un color, guardado como [rojo, verde, azul] de 0 a 255
COLORES = {
    "R": [206, 17, 38],     # rojo
    "B": [245, 245, 245],   # blanco
    "A": [0, 56, 168],      # azul
    "L": [0, 110, 200],     # azul claro
    "C": [116, 172, 223],   # celeste
    "T": [0, 170, 180],     # turquesa
    "I": [36, 38, 84],      # azul oscuro
    "V": [0, 135, 81],      # verde
    "K": [0, 84, 40],       # verde oscuro
    "Y": [252, 209, 22],    # amarillo
    "O": [255, 140, 26],    # naranja
    "D": [122, 16, 40],     # bordo
    "M": [120, 80, 40],     # marron
    "N": [20, 20, 20],      # negro
    "G": [110, 110, 110],   # gris
}

# Las banderas de todos los paises. Las matrices se armaron una sola vez achicando
# las banderas reales (del paquete libre flag-icons) a 3 filas por 6 columnas,
# y las que no se entendian se corrigieron a mano.
BANDERAS = {
    "afganistan": ["NNRRVV", "NNRRVV", "NNRRVV"],
    "albania": ["RRRRRR", "RRNNRR", "RRRRRR"],
    "alemania": ["NNNNNN", "RRRRRR", "YYYYYY"],
    "andorra": ["AAYYRR", "AAOORR", "AAYYRR"],
    "angola": ["RRRRRR", "RRNRRR", "NNNNNN"],
    "antigua y barbuda": ["RNNNNR", "RRLLRR", "RRRRRR"],
    "arabia saudita": ["VVVVVV", "VBBBBV", "VVVVVV"],
    "argelia": ["KKKBBB", "KKRRBB", "KKKBBB"],
    "argentina": ["CCCCCC", "BBYYBB", "CCCCCC"],
    "armenia": ["RRRRRR", "AAAAAA", "OOOOOO"],
    "australia": ["RAAABA", "AAAAAA", "ABAABA"],
    "austria": ["RRRRRR", "BBBBBB", "RRRRRR"],
    "azerbaiyan": ["TTTTTT", "RRRRRR", "VVVVVV"],
    "bahamas": ["NTTTTT", "NNNYYY", "NTTTTT"],
    "bahrein": ["BBRRRR", "BBRRRR", "BBRRRR"],
    "bangladesh": ["VVVVVV", "VRRRVV", "VVVVVV"],
    "barbados": ["AAYYAA", "AAYYAA", "AAYYAA"],
    "belgica": ["NNYYRR", "NNYYRR", "NNYYRR"],
    "belice": ["AAAAAA", "AABBAA", "AAAAAA"],
    "benin": ["VVYYYY", "VVVYYY", "VVRRRR"],
    "bielorrusia": ["RRRRRR", "RRRRRR", "RVVVVV"],
    "bolivia": ["RRRRRR", "YYYYYY", "VVVVVV"],
    "bosnia y herzegovina": ["AAYYYY", "AAAYYY", "AAAAAY"],
    "botswana": ["TTTTTT", "NNNNNN", "TTTTTT"],
    "brasil": ["VVYYVV", "VYAAYV", "VVYYVV"],
    "brunei": ["BYYYYY", "NNNBBB", "YYYYNN"],
    "bulgaria": ["BBBBBB", "VVVVVV", "RRRRRR"],
    "burkina faso": ["RRRRRR", "RRRRRR", "VVVVVV"],
    "burundi": ["BRRRRB", "VVBBVV", "BRRRRB"],
    "butan": ["YYYYYO", "YYBBOO", "YOOOOO"],
    "cabo verde": ["AAAAAA", "BBRRBB", "AAAAAA"],
    "camboya": ["AAAAAA", "RRCCRR", "AAAAAA"],
    "camerun": ["VVRRYY", "VVRRYY", "VVRRYY"],
    "canada": ["RBBBBR", "RBRRBR", "RBBBBR"],
    "catar": ["BBDDDD", "BBDDDD", "BBDDDD"],
    "chad": ["IIYYRR", "IIYYRR", "IIYYRR"],
    "chile": ["AABBBB", "AABBBB", "RRRRRR"],
    "china": ["YRRRRR", "RRRRRR", "RRRRRR"],
    "chipre": ["BBBBBB", "BBOBBB", "BBBBBB"],
    "colombia": ["YYYYYY", "AAAAAA", "RRRRRR"],
    "comoras": ["VYYYYY", "VVVBBB", "VAAAAA"],
    "congo": ["VVVYYY", "VVYYRR", "VYYRRR"],
    "corea del norte": ["AAAAAA", "RBBRRR", "CAAAAC"],
    "corea del sur": ["BBBBBB", "BBRABB", "BBBBBB"],
    "costa de marfil": ["OOBBVV", "OOBBVV", "OOBBVV"],
    "costa rica": ["AAAAAA", "RRRRRR", "AAAAAA"],
    "croacia": ["RRRRRR", "BBRRBB", "AAAAAA"],
    "cuba": ["RAAAAA", "RRBBBB", "RAAAAA"],
    "dinamarca": ["RRBRRR", "BBBBBB", "RRBRRR"],
    "dominica": ["KKKBKK", "CNRRNN", "KKKBKK"],
    "ecuador": ["YYYYYY", "AAMMAA", "RRRRRR"],
    "egipto": ["RRRRRR", "BBYYBB", "NNNNNN"],
    "el salvador": ["AAAAAA", "BBYYBB", "AAAAAA"],
    "emiratos arabes unidos": ["RRKKKK", "RRBBBB", "RRNNNN"],
    "eritrea": ["RRVVVV", "RRRRRV", "RRBBBB"],
    "escocia": ["BAAAAB", "AABBAA", "BAAAAB"],
    "eslovaquia": ["BBBBBB", "ARRAAA", "RRRRRR"],
    "eslovenia": ["BABBBB", "AAAAAA", "RRRRRR"],
    "espana": ["RRRRRR", "YYYYYY", "RRRRRR"],
    "estados unidos": ["AAARRR", "AAABBB", "RRRRRR"],
    "estonia": ["LLLLLL", "NNNNNN", "BBBBBB"],
    "esuatini": ["LLLLLL", "RRNBRR", "LLLLLL"],
    "etiopia": ["KKKKKK", "YYLLYY", "RRRRRR"],
    "fiji": ["RRRCCC", "CCCCRC", "CCCCCC"],
    "filipinas": ["BAAAAA", "BYBAAA", "BBRRRR"],
    "finlandia": ["BABBBB", "AAAAAA", "BABBBB"],
    "francia": ["AABBRR", "AABBRR", "AABBRR"],
    "gabon": ["VVVVVV", "YYYYYY", "LLLLLL"],
    "gales": ["BBBBBB", "BBRRBB", "VVVVVV"],
    "gambia": ["RRRRRR", "AAAAAA", "VVVVVV"],
    "georgia": ["BBBBBB", "RRRRRR", "BBBBBB"],
    "ghana": ["RRRRRR", "YYYYYY", "KKKKKK"],
    "gibraltar": ["BBBBBB", "BBRRBB", "RRRRRR"],
    "granada": ["RRYYYR", "RVVVVR", "RYYYYR"],
    "grecia": ["ABAAAA", "BBBBBB", "AAAAAA"],
    "groenlandia": ["BBBBBB", "BRRBBB", "RRRRRR"],
    "guatemala": ["CCBBCC", "CCBBCC", "CCBBCC"],
    "guinea": ["RRYYVV", "RRYYVV", "RRYYVV"],
    "guinea bissau": ["RRYYYY", "RNVYYV", "RRVVVV"],
    "guinea ecuatorial": ["LVVVVV", "LLBBBB", "LRRRRR"],
    "guyana": ["RYVVVV", "RRYYYV", "RYVVVV"],
    "haiti": ["AAAAAA", "AABBAA", "RRRRRR"],
    "honduras": ["LLLLLL", "BBLLBB", "LLLLLL"],
    "hong kong": ["RRRRRR", "RRBBRR", "RRRRRR"],
    "hungria": ["RRRRRR", "BBBBBB", "KKKKKK"],
    "india": ["OOOOOO", "BBAABB", "VVVVVV"],
    "indonesia": ["RRRRRR", "RRRRRR", "BBBBBB"],
    "inglaterra": ["BBRRBB", "RRRRRR", "BBRRBB"],
    "irak": ["RRRRRR", "BBBBBB", "NNNNNN"],
    "iran": ["VVVVVV", "BBRRBB", "RRRRRR"],
    "irlanda": ["VVBBOO", "VVBBOO", "VVBBOO"],
    "islandia": ["AARAAA", "CBRBBB", "AARAAA"],
    "islas feroe": ["BBRBBB", "CARAAC", "BBRBBB"],
    "islas marshall": ["AAAAAO", "ABAOBA", "AAAAAA"],
    "islas salomon": ["AAAAAA", "AAAAYK", "AYKKKK"],
    "israel": ["AAAAAA", "BBAABB", "AAAAAA"],
    "italia": ["VVBBRR", "VVBBRR", "VVBBRR"],
    "jamaica": ["NYVVYN", "NNYYNN", "NYVVYN"],
    "japon": ["BBBBBB", "BBRRBB", "BBBBBB"],
    "jordania": ["RRNNNN", "RRRRBB", "RRVVVV"],
    "kazajistan": ["TTTTTT", "TTYYTT", "TTTTTT"],
    "kenia": ["NNNNNN", "RRBBRR", "VVVVVV"],
    "kirguistan": ["RRRRRR", "RRYYRR", "RRRRRR"],
    "kiribati": ["RRRRRR", "RRYYRR", "BBAABB"],
    "kosovo": ["AAAAAA", "AAOOAA", "AAAAAA"],
    "kuwait": ["NVVVVV", "NNBBBB", "NRRRRR"],
    "laos": ["RRRRRR", "IIBBII", "RRRRRR"],
    "lesoto": ["AAAAAA", "BBBBBB", "VVVVVV"],
    "letonia": ["DDDDDD", "BBBBBB", "DDDDDD"],
    "libano": ["RRRRRR", "BBVVBB", "RRRRRR"],
    "liberia": ["ABRRRR", "BBBBBB", "RRRRRR"],
    "libia": ["RRRRRR", "NNBBNN", "VVVVVV"],
    "liechtenstein": ["AAAAAA", "ARRAAA", "RRRRRR"],
    "lituania": ["YYYYYY", "VVVVVV", "RRRRRR"],
    "luxemburgo": ["RRRRRR", "BBBBBB", "TTTTTT"],
    "macedonia del norte": ["RYRRYR", "YRYYRY", "RRRRRR"],
    "madagascar": ["BBRRRR", "BBRRRV", "BBVVVV"],
    "malasia": ["IIYRRR", "IIYBBB", "RRRRRR"],
    "malaui": ["NNNNNN", "RRRRRR", "VVVVVV"],
    "maldivas": ["RRRRRR", "RVVVVR", "RRRRRR"],
    "mali": ["VVYYRR", "VVYYRR", "VVYYRR"],
    "malta": ["BBBRRR", "BBBRRR", "BBBRRR"],
    "marruecos": ["RRRRRR", "RRVVRR", "RRRRRR"],
    "mauricio": ["RRRRRR", "IIIIII", "VVVVVV"],
    "mauritania": ["RRRRRR", "KKYYKK", "RRRRRR"],
    "mexico": ["VVBBRR", "VVMMRR", "VVBBRR"],
    "micronesia": ["CCBCCC", "CBCBCC", "CCBCCC"],
    "moldavia": ["AAYYRR", "AADORR", "AAYYRR"],
    "monaco": ["RRRRRR", "RRRRRR", "BBBBBB"],
    "mongolia": ["RRAARR", "RYAARR", "RRAARR"],
    "montenegro": ["RRRRRR", "RROORR", "RRRRRR"],
    "mozambique": ["RVVVVV", "RRRNNN", "RYYYYY"],
    "myanmar": ["YYYYYY", "VVBBVV", "RRRRRR"],
    "namibia": ["LLLLRR", "LLRRVV", "RRVVVV"],
    "nauru": ["IIIIII", "YYYYYY", "IBIIII"],
    "nepal": ["RCCCCC", "RRCCCC", "RRRCCC"],
    "nicaragua": ["LLLLLL", "BBYYBB", "LLLLLL"],
    "niger": ["OOOOOO", "BBBBBB", "VVVVVV"],
    "nigeria": ["VVBBVV", "VVBBVV", "VVBBVV"],
    "noruega": ["RRIRRR", "BBIBBB", "RRIRRR"],
    "nueva zelanda": ["RAAAAA", "AAAARA", "AAARAA"],
    "oman": ["RRBBBB", "RRRRRR", "RRVVVV"],
    "paises bajos": ["RRRRRR", "BBBBBB", "AAAAAA"],
    "pakistan": ["BKKKKK", "BKKBKK", "BKKKKK"],
    "palau": ["CCCCCC", "CCYYCC", "CCCCCC"],
    "palestina": ["RNNNNN", "RRRBBB", "RVVVVV"],
    "panama": ["BBBRRR", "BABRRR", "AAABRB"],
    "papua nueva guinea": ["NRRRRR", "NNNRRR", "NNNNNR"],
    "paraguay": ["RRRRRR", "BBBBBB", "AAAAAA"],
    "peru": ["RRBBRR", "RRBBRR", "RRBBRR"],
    "polonia": ["BBBBBB", "BBBBBB", "RRRRRR"],
    "portugal": ["VVRRRR", "VYRRRR", "VVRRRR"],
    "puerto rico": ["ARRRRR", "AABBBB", "ARRRRR"],
    "reino unido": ["ABRRBA", "RRRRRR", "ABRRBA"],
    "republica centroafricana": ["AAARAA", "BBRRBB", "YYYRYY"],
    "republica checa": ["ABBBBB", "AAABBB", "ARRRRR"],
    "republica democratica del congo": ["LLLLRR", "LLRRLL", "RRLLLL"],
    "republica dominicana": ["IIIRRR", "BBBBBB", "RRRIII"],
    "ruanda": ["TTTTTT", "TTTTTT", "KKKKKK"],
    "rumania": ["AAYYRR", "AAYYRR", "AAYYRR"],
    "rusia": ["BBBBBB", "AAAAAA", "RRRRRR"],
    "sahara occidental": ["RNNNNN", "RRRBBB", "RVVVVV"],
    "samoa": ["AAARRR", "ARARRR", "RRRRRR"],
    "san cristobal y nieves": ["VVVVNN", "VVNNRR", "NNRRRR"],
    "san marino": ["BBBBBB", "BBKVBB", "TTTTTT"],
    "san vicente y las granadinas": ["AAYYVV", "AAVVVV", "AAYYVV"],
    "santa lucia": ["CCCCCC", "CCNNCC", "CCYYCC"],
    "santo tome y principe": ["RVVVVV", "RRYYYY", "RVVVVV"],
    "senegal": ["KKYYRR", "KKYYRR", "KKYYRR"],
    "serbia": ["RRRRRR", "AAAAAA", "BBBBBB"],
    "seychelles": ["AAYRRR", "AYRRBB", "ARBVVV"],
    "sierra leona": ["VVVVVV", "BBBBBB", "AAAAAA"],
    "singapur": ["RRRRRR", "RBRRRR", "BBBBBB"],
    "siria": ["VVVVVV", "BBBBBB", "NNNNNN"],
    "somalia": ["CCCCCC", "CCBBCC", "CCCCCC"],
    "sri lanka": ["KODDDO", "KODYYD", "KODDDO"],
    "sudafrica": ["NRRRRR", "YVVVVV", "NAAAAA"],
    "sudan": ["VRRRRR", "VVVBBB", "VNNNNN"],
    "sudan del sur": ["ANNNNN", "AYARRR", "AAVVVV"],
    "suecia": ["LLYLLL", "YYYYYY", "LLYLLL"],
    "suiza": ["RRRRRR", "RRBBRR", "RRRRRR"],
    "suriname": ["VVVVVV", "RRRRRR", "VVVVVV"],
    "tailandia": ["RRRRRR", "IIIIII", "RRRRRR"],
    "taiwan": ["AAARRR", "ARRRRR", "RRRRRR"],
    "tanzania": ["VVVVNN", "VVNNLL", "NNLLLL"],
    "tayikistan": ["RRRRRR", "BBBBBB", "KKKKKK"],
    "timor oriental": ["NRRRRR", "NNNYRR", "NRRRRR"],
    "togo": ["RRRKKK", "RRRKKK", "KKKKKK"],
    "tonga": ["BRRRRR", "RRRRRR", "RRRRRR"],
    "trinidad y tobago": ["RNRRRR", "RRNNRR", "RRRRNR"],
    "tunez": ["RRRRRR", "RRRBRR", "RRRRRR"],
    "turkmenistan": ["VRVVVV", "VRVVVV", "VRVVVV"],
    "turquia": ["RRRRRR", "RBBRRR", "RRRRRR"],
    "tuvalu": ["RRRTTT", "TTTTTT", "TTTTTT"],
    "ucrania": ["LLLLLL", "LLLLLL", "YYYYYY"],
    "uganda": ["NNNNNN", "RRBBRR", "YYYYYY"],
    "uruguay": ["YYBBBB", "AAAAAA", "BBBBBB"],
    "uzbekistan": ["TTTTTT", "BBBBBB", "VVVVVV"],
    "vanuatu": ["NRRRRR", "NNNNNN", "NVVVVV"],
    "vaticano": ["YYYBBB", "YYYBBB", "YYYBBB"],
    "venezuela": ["YYYYYY", "AABBAA", "RRRRRR"],
    "vietnam": ["RRRRRR", "RRYYRR", "RRRRRR"],
    "yemen": ["RRRRRR", "BBBBBB", "NNNNNN"],
    "yibuti": ["BCCCCC", "BBBCCC", "BVVVVV"],
    "zambia": ["KKKKKK", "KKKKNO", "KKKKNO"],
    "zimbabue": ["BKYYYY", "BOBNNN", "BKYYYY"],
}

# Otros nombres con los que se puede escribir un pais: [como se escribe] -> [nombre que esta en BANDERAS]
OTROS_NOMBRES = {
    "antigua": "antigua y barbuda",
    "arabia saudi": "arabia saudita",
    "barein": "bahrein",
    "belarus": "bielorrusia",
    "birmania": "myanmar",
    "birmania myanmar": "myanmar",
    "bosnia": "bosnia y herzegovina",
    "botsuana": "botswana",
    "brunei darussalam": "brunei",
    "centroafrica": "republica centroafricana",
    "chequia": "republica checa",
    "ciudad del vaticano": "vaticano",
    "congo democratico": "republica democratica del congo",
    "corea": "corea del sur",
    "djibouti": "yibuti",
    "eeuu": "estados unidos",
    "emiratos arabes": "emiratos arabes unidos",
    "estados unidos de america": "estados unidos",
    "fiyi": "fiji",
    "gran bretana": "reino unido",
    "guinea bisau": "guinea bissau",
    "holanda": "paises bajos",
    "holland": "paises bajos",
    "iraq": "irak",
    "kazajstan": "kazajistan",
    "kazakhstan": "kazajistan",
    "kenya": "kenia",
    "kirguizistan": "kirguistan",
    "lesotho": "lesoto",
    "macedonia": "macedonia del norte",
    "malawi": "malaui",
    "moldova": "moldavia",
    "nueva zelandia": "nueva zelanda",
    "papua": "papua nueva guinea",
    "qatar": "catar",
    "rd congo": "republica democratica del congo",
    "rep dominicana": "republica dominicana",
    "republica arabe siria": "siria",
    "republica de corea": "corea del sur",
    "republica del congo": "congo",
    "republica democratica popular de lao": "laos",
    "republica islamica de iran": "iran",
    "republica popular democratica de corea": "corea del norte",
    "rwanda": "ruanda",
    "saint kitts y nevis": "san cristobal y nieves",
    "san vicente": "san vicente y las granadinas",
    "santa sede": "vaticano",
    "santo tome": "santo tome y principe",
    "suazilandia": "esuatini",
    "surinam": "suriname",
    "swazilandia": "esuatini",
    "timor leste": "timor oriental",
    "trinidad": "trinidad y tobago",
    "turkiye": "turquia",
    "usa": "estados unidos",
    "zimbabwe": "zimbabue",
}

# bandera gris para los paises que no tenemos dibujados
SIN_BANDERA = ["GGGGGG", "GGGGGG", "GGGGGG"]


# Deja el nombre como estan escritas las claves de BANDERAS: en minuscula y sin enie.
# Si el pais se escribio con otro nombre (por ejemplo Holanda) lo cambia por el que esta en BANDERAS.
def clave_de(nombre):
    clave = nombre.lower().strip().replace("ñ", "n")
    if clave in OTROS_NOMBRES:
        clave = OTROS_NOMBRES[clave]
    return clave


# True si tenemos dibujada la bandera de ese pais
def tiene_bandera(nombre):
    return clave_de(nombre) in BANDERAS


# Devuelve la matriz de la bandera de un pais (gris si no la tenemos)
def buscar_bandera(nombre):
    clave = clave_de(nombre)
    if clave in BANDERAS:
        return BANDERAS[clave]
    return SIN_BANDERA


# Devuelve el color de una letra escrito como lo entiende rich: "rgb(206,17,38)"
def color_rich(letra):
    rgb = COLORES[letra]
    return f"rgb({rgb[0]},{rgb[1]},{rgb[2]})"


# Bandera GRANDE: 3 renglones. Cada cuadradito son 2 espacios con color de fondo.
def bandera_grande(nombre):
    bandera = buscar_bandera(nombre)
    texto = Text()
    for i in range(3):
        for letra in bandera[i]:
            texto.append("  ", style="on " + color_rich(letra))
        if i < 2:
            texto.append("\n")
    return texto


# Arma una bandera de 2 renglones usando solo las columnas que se piden.
# El truco: las 3 filas de la bandera se meten en 2 renglones de la consola.
# Se usa un simbolo que es un bloque que solo llena la parte de abajo de la letra.
# El bloque se pinta de un color y el fondo de otro, asi en un renglon entran dos colores.
#   renglon 1: fondo = fila 0, bloque bajito (▃) = fila 1
#   renglon 2: fondo = fila 1, bloque alto  (▅) = fila 2
def bandera_en_dos_renglones(nombre, columnas):
    bandera = buscar_bandera(nombre)
    texto = Text()
    for columna in columnas:
        texto.append("▃", style=color_rich(bandera[1][columna]) + " on " + color_rich(bandera[0][columna]))
    texto.append("\n")
    for columna in columnas:
        texto.append("▅", style=color_rich(bandera[2][columna]) + " on " + color_rich(bandera[1][columna]))
    return texto


# Bandera CHICA: 2 renglones de 6 letras de ancho (se usa en las listas)
def bandera_chica(nombre):
    return bandera_en_dos_renglones(nombre, [0, 1, 2, 3, 4, 5])


# Bandera ANGOSTA: 2 renglones de 3 letras de ancho (se usa abajo de las barras del ordenamiento)
def bandera_angosta(nombre):
    return bandera_en_dos_renglones(nombre, [0, 2, 5])


# Devuelve la lista de todos los paises que tienen bandera, con mayuscula (para sugerir nombres)
def nombres_conocidos():
    nombres = []
    for clave in BANDERAS:
        nombres.append(clave.title())
    return nombres
