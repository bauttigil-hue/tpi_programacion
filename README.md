# Gestion de Datos de Paises - TPI Programacion 1

Trabajo Practico Integrador - Programacion 1 - 

## Descripcion

Programa de consola hecho en Python para manejar datos de paises (nombre, poblacion, superficie y continente). Los datos se leen de un archivo CSV y se manejan con las flechas del teclado.

Con el programa se puede:

- Agregar un pais nuevo (no se permiten campos vacios ni repetidos)
- Actualizar la poblacion y la superficie de un pais
- Buscar paises por nombre (parcial o exacto)
- Filtrar por continente, rango de poblacion o rango de superficie
- Ordenar por nombre, poblacion o superficie (ascendente o descendente)
- Ver estadisticas: mayor y menor poblacion, promedios y cantidad de paises por continente

Cada vez que se agrega o se actualiza un pais, los cambios se guardan en el CSV.

## Que tiene de distinto

- **Mapa del mundo dibujado en la consola.** Los paises cargados en el CSV aparecen en color y el pais elegido se marca en blanco. Al abrir el programa se ve como se van encendiendo a medida que se lee el archivo.
- **Banderas dibujadas con cuadraditos de colores**, al lado de cada pais. Estan las de todos los paises del mundo (206), asi que un pais nuevo ya tiene su bandera y su lugar en el mapa.
- **Menu con flechas**: no hay que escribir numeros.
- **Buscador en vivo**: la lista se achica con cada letra que se escribe y la parte que coincide queda resaltada.
- **Formularios con ayuda**: al escribir el nombre sugiere los paises que conoce, y si un dato esta mal avisa y lo vuelve a pedir.
- **Ordenamiento animado**: se ve como trabaja el metodo burbuja, con una barra por pais y el contador de comparaciones e intercambios.

## Librerias que usa

| Libreria | Para que la usamos |
|---|---|
| rich | Colores, tablas, barras y las pantallas que se actualizan sin parpadear |
| readchar | Leer las flechas del teclado sin apretar Enter |
| questionary | Las preguntas de los formularios, con validacion y sugerencias |

## Integrantes

- Bautista Gil
- Agustin Tomadin

## Links

- Video demostrativo: https://youtu.be/J233eETXkP4
- Documentacion en PDF: disponible en el repo

## Como usarlo

Requisitos: Python 3.

```
git clone https://github.com/bauttigil-hue/tpi_programacion
cd tpi_programacion
pip install -r requirements.txt
python main.py
```

- El `pip install` se hace una sola vez. Si falta alguna libreria, el programa avisa cual es.
- Todos los archivos .py y paises.csv tienen que estar en la misma carpeta, y la consola tiene que estar parada en esa carpeta.
- Hay que ejecutarlo en una consola de verdad (la terminal de VS Code, Windows Terminal, CMD o PowerShell). No funciona en IDLE.
- Para ver el mapa y la animacion del ordenamiento la ventana tiene que tener al menos 114 columnas y 22 renglones. Si es mas chica el programa funciona igual, pero sin el mapa.

Teclas: flechas para moverse, Enter para elegir, Esc para volver. En los formularios, Ctrl+C cancela.

## Archivos del proyecto

| Archivo | Que tiene |
|---|---|
| main.py | El menu principal. Es el archivo que se ejecuta |
| paises.py | Agregar, actualizar, buscar, filtrar y ordenar (burbuja) |
| estadisticas.py | Calculo y muestra de estadisticas |
| archivo.py | Lectura y guardado del CSV |
| validaciones.py | Revisar los datos que se escriben |
| formularios.py | Las preguntas que se contestan escribiendo (questionary) |
| vistas.py | Menu con flechas, lista con buscador y ficha (rich) |
| animaciones.py | Presentacion y ordenamiento animado (rich) |
| mapa.py | Dibujo del mapa del mundo |
| banderas.py | Dibujo de las banderas |
| teclado.py | Lee una tecla (readchar) |
| consola.py | Colores, titulos y barras (rich) |
| requirements.txt | La lista de librerias para instalar |
| paises.csv | Los datos de los paises |

## Formato del CSV

La primera linea es el encabezado. Cada linea siguiente es un pais con sus datos separados por comas, sin tildes:

```
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,America
Japon,125800000,377975,Asia
```

La poblacion y la superficie tienen que ser numeros enteros mayores a 0. Si una linea tiene algun error, el programa avisa cual es y la saltea.

## Ejemplos de uso

- **Agregar:** elegir "Agregar pais", escribir Peru, 34352719 y 1285216, elegir el continente y Enter. Aparece la ficha con el mensaje "Agregado y guardado en paises.csv".
- **Buscar:** elegir "Buscar pais" y escribir "an". Quedan Canada, Alemania, Espana, Francia y Nueva Zelanda.
- **Ordenar:** elegir "Ordenar paises", "Por poblacion", "Descendente". Se ve la animacion y despues la lista, con China primero.
- **Errores:** si en "Agregar pais" se escribe un pais que ya existe, avisa "Peru ya existe en la lista". Si en la poblacion se escribe "abc", avisa "Tiene que ser un numero entero". Si en un filtro el minimo es mas grande que el maximo, avisa "El minimo no puede ser mayor al maximo".

## Validaciones

- No se permiten campos vacios ni paises repetidos
- Los nombres solo aceptan letras y espacios
- La poblacion y la superficie tienen que ser numeros enteros mayores a 0
- El continente se elige de una lista, asi no se puede escribir mal
- En los filtros por rango, el minimo no puede ser mayor al maximo
- Las lineas del CSV con errores se avisan y se ignoran
- Si el CSV no existe, el programa arranca con la lista vacia
- No importan las mayusculas ni las tildes al buscar
