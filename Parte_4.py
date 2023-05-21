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
#print(generar_dicc(datos_rosco, cargar_datos_para_rosco, cargar_letras, cargar_palabras))

le = generar_dicc(datos_rosco, cargar_datos_para_rosco, cargar_letras, cargar_palabras)[1]
ae = [' ' for i in range(10)]

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
    else:
        errores += 1
    return aciertos, errores, palabra_ingresada

def mostrar_resumen(dicc_rosco, lista_palabras_ingresadas, ae):
    print("\n--- Resumen de la Partida ---")
    print("-" * 50)
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
    print("-" * 50)

def jugar_rosco(dicc_rosco, lista, ae):
    aciertos = 0
    errores = 0
    lista_palabras_ingresadas = []
    for i, clave in enumerate(dicc_rosco.keys()):
        posicion = i
        turno = i + 1
        definicion = dicc_rosco[clave]
        aciertos, errores, palabra_ingresada = jugar_turno(aciertos, errores, posicion, lista, ae, turno, clave, definicion)
        lista_palabras_ingresadas.append(palabra_ingresada)
    mostrar_resumen(dicc_rosco, lista_palabras_ingresadas, ae)

jugar_rosco(generar_dicc(datos_rosco, cargar_datos_para_rosco, cargar_letras, cargar_palabras)[0], generar_dicc(datos_rosco, cargar_datos_para_rosco, cargar_letras, cargar_palabras)[1], ae)