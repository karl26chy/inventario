# inventario
se creara un inventario utilizando conocimientos basicos de python

Resumen del programa de inventario

Este programa es un sistema de gestión de inventario en consola que permite al usuario administrar productos de manera interactiva. Utiliza una estructura de datos basada en una lista de diccionarios, donde cada producto contiene tres atributos: nombre, precio y cantidad.

El sistema ofrece un menú principal que se ejecuta en un ciclo while, permitiendo al usuario realizar múltiples operaciones sin que el programa se cierre. Entre sus funcionalidades principales se encuentra la opción de agregar productos, donde se solicitan los datos al usuario y se validan mediante estructuras try-except para asegurar que el precio sea un número decimal y la cantidad un número entero.

También permite mostrar el inventario completo, recorriendo la lista de productos con un ciclo for y presentando la información de forma ordenada y legible. Además, el programa incluye la capacidad de buscar productos por nombre, lo que facilita encontrar elementos específicos dentro del inventario.

Otra funcionalidad importante es la actualización de productos, donde se pueden modificar el precio o la cantidad de un producto existente, así como la eliminación de productos del inventario. Esto permite mantener los datos actualizados y organizados.

El sistema también realiza cálculos estadísticos sobre el inventario, como el valor total (precio por cantidad de cada producto), la cantidad total de unidades, el producto más caro y el producto con mayor stock. Estos cálos se realizan mediante acumuladores y comparaciones dentro de ciclos.

Adicionalmente, el programa permite guardar el inventario en un archivo CSV, lo que facilita la persistencia de datos y su posterior uso en herramientas como Excel. También es capaz de cargar información desde un archivo CSV, validando su estructura y manejando errores en caso de datos inválidos.

En términos técnicos, el programa aplica conceptos fundamentales de programación como estructuras de datos (listas y diccionarios), funciones y modularización, manejo de errores, lectura y escritura de archivos, y control de flujo mediante condicionales y ciclos.
