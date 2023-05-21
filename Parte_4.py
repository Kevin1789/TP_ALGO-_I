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
    Esta función integra las funcionalidades resueltas en cada una de las etapas anteriores.
    """
    diccionario_rosco = cargar_datos_para_rosco()
    lista = cargar_letras()
    palabra, definicion = cargar_palabras(diccionario_rosco, lista)
    return lista, palabra, definicion


def generar_dicc(datos_rosco, cargar_datos_para_rosco, cargar_letras, cargar_palabras):
    """
    Esta función genera un diccionario con las palabras y las definiciones.
    """
    dicc_rosco = {}
    lista, palabra, definicion = datos_rosco(cargar_datos_para_rosco, cargar_letras, cargar_palabras)
    for i in range(len(palabra)):
        dicc_rosco[palabra[i]] = definicion[i]
    return dicc_rosco, lista


def mostrar_tablero(le, ae, posicion, aciertos, errores, turno, clave, definicion):
    print(f"""
    [{le[0]}][{le[1]}][{le[2]}][{le[3]}][{le[4]}][{le[5]}][{le[6]}][{le[7]}][{le[8]}][{le[9]}]
    [{ae[0]}][{ae[1]}][{ae[2]}][{ae[3]}][{ae[4]}][{ae[5]}][{ae[6]}][{ae[7]}][{ae[8]}][{ae[9]}]
    {' ' * (posicion * 3 + 1)}^
    Aciertos: {aciertos}
    Errores: {errores}
    """)


def ingresar_palabra():
    ingreso_usuario = input("Ingresa palabra: ").lower()
    while not ingreso_usuario.isalpha():
        print("Ingrese solo letras.")
        ingreso_usuario = input("Ingrese palabra: ").lower()
    return ingreso_usuario


def evaluar_palabra(palabra_ingresada, clave):
    return "a" if palabra_ingresada == clave else "e"


def jugar_turno(aciertos, errores, posicion, le, ae, turno, clave, definicion):
    letra = clave[0]
    longitud = len(clave)
    mostrar_tablero(le, ae, posicion, aciertos, errores, turno, clave, definicion)
    print(f"Turno letra: {letra} Longitud palabra: {longitud}\nDefinicion: {definicion}")
    palabra_ingresada = ingresar_palabra()
    resultado = evaluar_palabra(palabra_ingresada, clave)
    ae[posicion] = resultado

    if resultado == "a":
        aciertos += 1
        puntos = 10
    else:
        errores += 1
        puntos = -3

    return aciertos, errores, palabra_ingresada, puntos


def mostrar_resumen(dicc_rosco, lista_palabras_ingresadas, ae):
    print("\n--- Resumen de la Partida ---")
    print("-" * 90)
    for i, clave in enumerate(dicc_rosco.keys()):
        letra = clave[0]
        long = len(clave)
        correccion = clave
        palabra_jugador = lista_palabras_ingresadas[i]
        result = "acierto" if ae[i] == "a" else "error"
        if result == "error":
            print(f"Turno de la letra: {letra} - Palabra de {long} letras - {palabra_jugador} - {result} - Palabra correcta es : {correccion}")
        else:
            print(f"Turno de la letra: {letra} - Palabra de {long} letras - {palabra_jugador} - {result}")
    print("-" * 90)


def jugar_rosco(dicc_rosco, lista, ae):
    aciertos = 0
    errores = 0
    puntos_totales = 0
    lista_palabras_ingresadas = []
    for i, clave in enumerate(dicc_rosco.keys()):
        print(clave)
        posicion = i
        turno = i + 1
        definicion = dicc_rosco[clave]
        aciertos, errores, palabra_ingresada, puntos = jugar_turno(aciertos, errores, posicion, lista, ae, turno, clave, definicion)
        puntos_totales += puntos
        lista_palabras_ingresadas.append(palabra_ingresada)
    mostrar_resumen(dicc_rosco, lista_palabras_ingresadas, ae)
    return puntos_totales


def jugar():
    ae = [' ' for i in range(10)]
    continuar_jugando = True
    puntaje_total = 0

    while continuar_jugando:
        dicc_rosco, lista = generar_dicc(datos_rosco, cargar_datos_para_rosco, cargar_letras, cargar_palabras)
        puntaje_partida = jugar_rosco(dicc_rosco, lista, ae)
        puntaje_total += puntaje_partida
        print(f"\nPuntaje de la partida: {puntaje_partida}")
        respuesta = input("¿Deseas seguir jugando? (si/no): ").lower()
        while respuesta != "si" and respuesta != "no":
            respuesta = input("Por favor, ingresa 'si' o 'no': ").lower()
        if respuesta == "no":
            continuar_jugando = False

    print(f"\nPuntaje total: {puntaje_total}")
jugar()