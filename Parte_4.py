"""
Etapa 4 - Integración
En esta etapa debemos integrar las funcionalidades resueltas en cada una de las etapas
anteriores, haciendo un uso adecuado de las funciones escritas.
La secuencia del juego debe ser la siguiente:
1. Se deberá comenzar con la generación del diccionario de palabras.
2. Luego se deben seleccionar las 10 letras participantes.
3. El programa elegirá al azar la lista de palabras a adivinar por el jugador.
4. Luego se armará el tablero que visualizará el usuario, y dará comienzo la partida,
implementando así, lo realizado en la etapa 1.
"""

from Parte_3 import *

def datos_rosco(cargar_datos_para_rosco, cargar_letras, cargar_palabras):
    """
    Esta funcion integra las funcionalidades resueltas en cada una de las etapas anteriores.
    """
    diccionario_rosco = cargar_datos_para_rosco()
    lista = cargar_letras()
    palabra, definicion = cargar_palabras(diccionario_rosco, lista)
    return lista, palabra, definicion
#print(datos_rosco(cargar_datos_para_rosco, cargar_letras, cargar_palabras))

def generar_dicc(datos_rosco, cargar_datos_para_rosco, cargar_letras, cargar_palabras):
    """
    Esta funcion genera un diccionario con las palabras y las definiciones.
    """
    dicc_rosco = {}
    lista, palabra, definicion = datos_rosco(cargar_datos_para_rosco, cargar_letras, cargar_palabras)
    for i in range(len(palabra)):
        dicc_rosco[palabra[i]] = definicion[i]
    return dicc_rosco, lista
print(generar_dicc(datos_rosco, cargar_datos_para_rosco, cargar_letras, cargar_palabras))

"""
[[palabra1],[palabra2]]
[[definicion1],[definicion2]]

=

{palabra1:definicion1, palabra2:definicion2}

lista 
dicc
"""