"""
Etapa 1 - Interacción con el Jugador

En esta etapa deberás escribir las funciones que consideres necesarias, y que permitan
una interacción con el jugador, y que sigan los lineamientos que se dan a continuación.
Inicialmente, comenzaremos por mostrar el tablero con las letras participantes, debajo
de cada letra se mostrará el resultado de haber adivinado la palabra de dicha letra,
siendo “a” de acierto, o bien “e” de error.
Al usuario se le debe indicar el turno actual, la cantidad de letras de la palabra a adivinar
y la definición de la misma.
Una vez que el usuario ingrese la palabra se le indicará si fue correcta o no , y en el caso
de ser incorrecta se le muestra la palabra correcta. y luego se pasa al siguiente turno de
letra.
Cuando la palabra es ingresada por el usuario debe validarse que esté
compuesta sólo por letras, no están permitidos los números, espacios ni ningún
carácter especial, y que sea de la longitud correcta para el turno.
"""

"""Importamos el diccionario que necesitamos"""
import diccionario_etapa1

"""
En esta funcion imprimimos lo que el usuario vizualiza(aciertos, errores, indicador de posicion actual, letras a jugar, "a" o "e" depende de lo que ingreso el usuario)
"""
def mostrar_tablero(aciertos, errores, posicion, lista, lista_2):
    print(f"""[{lista[0]}][{lista[1]}][{lista[2]}]\n[{lista_2[0]}][{lista_2[1]}][{lista_2[2]}]
{' ' * (posicion * 3 + 1)}^
Aciertos: {aciertos}
Errores: {errores}""")

"""
En esta funcion lo que hacemos es pedir al usuario que ingrse una palabra, si la palabra esta en mayuscula o algun caracter esta en mayuscula, lo convertimos a
minuscula paara que no haya errores a la hora de igualar la palabra que ingreso con la palabra del diccionario que se esta jugando.
En el While lo que hacemos es fijarnos si el usuario ingreso solo caracteres alfabeticos, si no es asi se le pide ingresar nuevamente una palabra,
asi hasta que el ingreso sea valido.
"""
def ingresar_palabra():
    ingreso_usuario = input("Ingresa palabra: ").lower()
    while not ingreso_usuario.isalpha():
        print("Ingrese solo letras.")
        ingreso_usuario = input("Ingrese palabra: ").lower()
    return ingreso_usuario

"""
Lo que hace esta funcion es evaluar si la palabra ingresada por el usuario es correcta o erronea, devuelve "a" por acierto y "e" por error
"""
def evaluar_palabra(palabra_ingresada, clave):
    return "a" if palabra_ingresada == clave else "e"

"""
Esta funcion recibe 7 parametros (cantidad de aciertos hasta el momento, cant errores hasta el momento, posicion actual en el tablero, una lista con las letras a jugar,
una 2da lista que contiene los aciertos y errores que se van cometiendo, la palabra que el usuario debe adivinar, la definicion que se le da al usuario como pista).
La función muestra el tablero, el turno actual y la longitud de la palabra a adivinar.
Despues solicita al usuario que ingrese una palabra llamando a la funcion Ingresar_palabra()
Despues verifica si la palabra es correcta o incorrecta llamando a la funcion Evaluar_palabra(palabra_ingresada, clave).
Dependiendo lo que devuelva la funcion Evaluar_palabra, se actualizara el tablero y los contadores de aciertos y errores.
La funcion retorna los nuevos valores de aciertos, errores y palabra_ingresada
"""
def jugar_turno(aciertos, errores, posicion, lista, lista_2, clave, definicion):
    letra = clave[0]
    longitud = len(clave)

    mostrar_tablero(aciertos, errores, posicion, lista, lista_2)
    print(f"Turno letra: {letra} Longitud palabra: {longitud}\nDefinicion: {definicion}")

    palabra_ingresada = ingresar_palabra()
    resultado = evaluar_palabra(palabra_ingresada, clave)
    lista_2[posicion] = resultado

    if resultado == "a":
        aciertos += 1
    else:
        errores += 1

    return aciertos, errores, palabra_ingresada

"""
En esta funcion como su nombre lo dice, muestra un resumen de la partida con los parametros que recibe.
Muetsra como encabezado RESUMEN DE LA PARTIDA separado por 50 "-".
Despues iteramos el diccionario con un enumerate para obetener tanto el indice como la clave del diccionario importado.
dentro del for lo que hacemos es (sacar la letra inicial de la palabra, su respectiva longitud, una correccion si en caso el ususario se equivoco en una
de las palabras, igualamos la palabra del jugador a la lista de las palabras que ingreso el jugador, despues en el resultado, devuele "acierto" si 
la lista de aciertos es igual a "a" de lo contrario "error", depsues imprimimos los resultados) Todo esto en cada una de las iteraciones.
"""
def mostrar_resumen(diccionario, lista_palabras_ingresadas, lista_2):
    print("\n--- Resumen de la Partida ---")
    print("-" * 50)
    for i, clave in enumerate(diccionario.keys()):
        letra = clave[0]
        long = len(clave)
        correccion = clave
        palabra_jugador = lista_palabras_ingresadas[i]
        result = "acierto" if lista_2[i] == "a" else "error"
        if result == "error":
            print(f"Turno de la letra: {letra} - Palabra de {long} letras - {palabra_jugador} - {result} - Palabra correcta es : {correccion}")
        else:
            print(f"Turno de la letra: {letra} - Palabra de {long} letras - {palabra_jugador} - {result}")
    print("-" * 50)





"""
En esta funcion multiplicamos la cantidad de aciertos por 10 y retornamos ese valor
"""
def calcular_puntaje(aciertos):
    return aciertos * 10
