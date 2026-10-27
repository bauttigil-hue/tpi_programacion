# tpi_programacion
Trabajo Integrador Programacion
Gestion de Datos de Paises en Python

Trabajo Practico Integrador - Programacion 1 Tecnicatura Universitaria en Programacion - UTN
Descripcion

Programa de consola hecho en Python que permite manejar informacion de paises (nombre, poblacion, superficie y continente). Los datos se leen desde un archivo CSV y se trabaja con ellos desde un menu de opciones.

Con el programa se puede:

Agregar un pais nuevo (no se permiten campos vacios)
Actualizar la poblacion y la superficie de un pais
Buscar paises por nombre (coincidencia parcial o exacta)
Filtrar paises por continente, rango de poblacion o rango de superficie
Ordenar paises por nombre, poblacion o superficie (ascendente o descendente)
Ver estadisticas: pais con mayor y menor poblacion, promedio de poblacion, promedio de superficie y cantidad de paises por continente

Cada vez que se agrega o se actualiza un pais, los cambios se guardan en el CSV.

Integrantes
Integrante	
Bautista Gil	
Agustin Tomadin
Links
Video demostrativo: [completar]
Documentacion en PDF: Disponible en repo
Requisitos
Python 3.x
No hace falta instalar ninguna libreria
Como usarlo
Descargar o clonar el repositorio:
git clone https://github.com/bauttigil-hue/tpi_programacion
cd tpi_programacion
Ejecutar el programa (el archivo paises.csv tiene que estar en la misma carpeta):
python tpi2_programacion.py

Elegir una opcion del menu escribiendo el numero y apretando Enter:
Menu Paises
1. Agregar pais
2. Actualizar poblacion y superficie de un pais
3. Buscar pais por nombre
4. Filtrar paises
5. Ver paises
6. Ordenar paises
7. Mostrar estadisticas
8. Salir
Archivos del proyecto
tpi2_programacion.py                 codigo del programa
paises.csv                      datos de los paises
README.md                       este archivo
TPI_Programacion1_Informe.pdf   documentacion del trabajo
Formato del CSV

La primera linea es el encabezado. Cada linea siguiente es un pais con sus datos separados por comas, sin tildes:

nombre,poblacion,superficie,continente
Argentina,45376763,2780400,America
Japon,125800000,377975,Asia

La poblacion y la superficie tienen que ser numeros enteros mayores a 0. Si una linea tiene algun error, el programa avisa cual es y la saltea.

Ejemplos de entradas y salidas

Agregar un pais

Elija una opcion: 1
Ingresa el nombre del pais: Peru
Ingresa la poblacion del pais: 34352719
Ingresa la superficie del pais (km2): 1285216
Ingresa el continente del pais: America
Pais 'Peru' agregado correctamente.

Buscar por parte del nombre

Elija una opcion: 3
Ingresa el nombre (o parte del nombre) del pais: ar
Nombre: Argentina, Poblacion: 45376763, Superficie: 2780400 km2, Continente: America

Ordenar por superficie de mayor a menor

Elija una opcion: 6
Ordenar por:
1. Nombre
2. Poblacion
3. Superficie
Elija un orden: 3
Ascendente (A) o descendente (D): D
Nombre: Canada, Poblacion: 38246108, Superficie: 9984670 km2, Continente: America
Nombre: Estados Unidos, Poblacion: 331893745, Superficie: 9833520 km2, Continente: America
Nombre: China, Poblacion: 1412360000, Superficie: 9596961 km2, Continente: Asia
...

Estadisticas

Elija una opcion: 7
Pais con mayor poblacion: China (1412360000)
Pais con menor poblacion: Uruguay (3426260)
Promedio de poblacion: 222095364.5
Promedio de superficie: 3009790.25 km2
Cantidad de paises por continente:
  America: 7
  Asia: 4
  Europa: 4
  Africa: 3
  Oceania: 2

Errores

Elija una opcion: 9
Error: opcion invalida. Elija un numero del 1 al 8.

Elija una opcion: 1
Ingresa el nombre del pais: peru
Error: el pais ya existe.

Elija una opcion: 3
Ingresa el nombre (o parte del nombre) del pais: xyz
No se encontraron paises.
Validaciones
No se permiten campos vacios ni paises repetidos
Los nombres y continentes solo aceptan letras
La poblacion y la superficie tienen que ser numeros enteros mayores a 0
En los filtros por rango, el minimo no puede ser mayor al maximo
Las lineas del CSV con errores se avisan y se ignoran
Si el CSV no existe, el programa arranca con la lista vacia
No importan las mayusculas ni las tildes al buscar o filtrar
