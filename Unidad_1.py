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

#ayuddaaaaa
#no se que estoy haciendo TT

#recibe un lista con posicion, palabra y su informacion
def palabras_a_jugar ():
    #import unidad 3
    #palabras_elegidas = [[1, "entropecer", "info"],[2, "unicornio_paranoico", "uni"],[3,"Krussu", "info"]]
    palabras_elegidas = {1: ["cuarteto de nos", "la mejor banda de rock papa"], 2: ["unicornio_paranoico", "uni"], 3:["kryssu", "yo"]}
    #print(palabras_elegidas)
    return palabras_elegidas

def letras_palabras(palabras_elegidas):
    letras = []
    palabras = []
    claves = []
    for clave, valor in palabras_elegidas.items():
        letras.append(valor[0][0])
        palabras.append(valor[0])
        claves.append(clave)
    #print(letras)
    #print(palabras)
    #print(claves)
    return letras, palabras, claves

#letras_palabras(palabras_a_jugar())

j1 = letras_palabras(palabras_a_jugar())[0][0]
j2 = letras_palabras(palabras_a_jugar())[0][1]
j3 = letras_palabras(palabras_a_jugar())[0][2]

def descripcion(palabras_elegidas):
    for clave, valor in palabras_elegidas.items():
        valor[1]
        #print (valor[1])
    return valor[1]


d1 = descripcion(palabras_a_jugar())



def turno_letra (letras):
    for inicial in letras:
        inicial
        #print(inicial)
    return inicial

i1 = turno_letra(letras_palabras(palabras_a_jugar())[0][0])




#turno_letra(letras_palabras(palabras_a_jugar())[0])



def juego (palabras_elegidas):
    for clave, valor in palabras_elegidas.items():
        print("ingrese la palabra que empieza con la letra", valor[0][0],":")
        print(valor[1])
        palabra = input()
        if palabra == valor[0]:
            print("correcto")
        else:
            print("incorrecto")
    return palabra, valor[0][0], valor[1], clave #palabra, letra, definicion, clave

#juego(palabras_a_jugar())


def juego_ok(palabra_elegidas):
    dicc = palabra_elegidas
    n1 = " "
    aciertos = 0
    errores = 0
    j1 = letras_palabras(palabras_a_jugar())[0][0]
    turno_letra = letras_palabras(palabras_a_jugar())[0][0]
    longitud_palabra = len(palabra_elegidas[1][0])
    definicion = palabra_elegidas[1][1]
    tablero
    print(f"""
[{j1}][2][3][4][5][6][7][8][9][0]
[{n1}][2][3][4][5][6][7][8][9][0]
Aciertos: {aciertos}
Errores: {errores}
Turno letra {turno_letra} - palabra de {longitud_palabra} letras
Definicion: {definicion}""")
    palabra = input()
    for clave, valor in palabra_elegidas.items():
            if palabra == valor[0]:
                print("correcto")
                n1 = "a"
                aciertos = aciertos + 1
            else:
                print("incorrecto")
                n1 = "e"
                errores = errores + 1
            

    return palabra, valor[0][0], valor[1], clave #palabra, letra, definicion, clave

juego_ok(palabras_a_jugar())

            


#juego_ok(palabras_a_jugar())



#funciones para cada juego
def juego_1 (palabras_elegidas):
    palabra = palabras_elegidas[1][0]
    definicion = palabras_elegidas[1][1]
    letra = palabra[0]
    #print( 1, palabra, definicion, letra)
    return palabra, definicion, letra

#juego_1(palabras_a_jugar())

def juego_2 (palabras_elegidas):
    palabra = palabras_elegidas[2][0]
    definicion = palabras_elegidas[2][1]
    letra2 = palabra[0]
    #print( 2, palabra, definicion)
    return palabra, definicion, letra2

#juego_2(palabras_a_jugar())

def juego_3 (palabras_elegidas):
    palabra = palabras_elegidas[3][0]
    definicion = palabras_elegidas[3][1]
    letra3 = palabra[0]
    #print( 3, palabra, definicion)
    return palabra, definicion, letra3

#juego_3(palabras_a_jugar())


#mostrar_tablero(juego_1(palabras_a_jugar()), juego_2(palabras_a_jugar()), juego_3(palabras_a_jugar()))

#pruebas

j1 = juego_1(palabras_a_jugar())[2]
j2 = juego_2(palabras_a_jugar())[2]
j3 = juego_3(palabras_a_jugar())[2]
d1 = juego_1(palabras_a_jugar())[1]
d2 = juego_2(palabras_a_jugar())[1]
d3 = juego_3(palabras_a_jugar())[1]
n1 = ""


#funsion que permite ver los errores y aciertos
def aciertos_errores ():
    acierto = 0
    error = 0
    return acierto, error

#ingreso de la palabra y verificacion de la misma
def ingreso_palabra(juego_1, acierto, error):
    palabra = juego_1[0]
    print(palabra)
    valido = False
    palabra_ingresada = input("Ingrese la palabra: ")
    print(palabra_ingresada)
    if palabra_ingresada == palabra:
        acierto += 1
        valido = True
        print("acerto",acierto)
    elif palabra_ingresada != palabra:
        error += 1
        valido = False
        print("error",error)
    return palabra_ingresada, acierto, error, valido

#ingreso_palabra(juego_1(palabras_a_jugar()), aciertos_errores()[0], aciertos_errores()[1])

#mostar el el historial de errores y aciertos
def segunda_linea (valido, n1):
    if valido == True:
        n1 = "a"
        #print(n1)
    elif valido == False:
        n1 = "e"
        #print(n1)
    return n1
#segunda_linea(ingreso_palabra(juego_1(palabras_a_jugar()), aciertos_errores()[0], aciertos_errores()[1])[3], n1)

def longitud_palabra (palabra):
    longitud = len(palabra)
    #print(longitud)
    return longitud
l_palabra = longitud_palabra(juego_1(palabras_a_jugar())[0])
#longitud_palabra(juego_1(palabras_a_jugar())[0])


#funcion que muestra el tablero
def tablero ():
    print(f"""
[{j1}][{j2}][{j3}][4][5][6][7][8][9][0]
[{n1}][{n1}][{n1}][4][5][6][7][8][9][0]

Aciertos: {aciertos_errores()[0]}
Errores: {aciertos_errores()[1]}
Turno letra {i1} - palabra de {l_palabra} letras
Definicion: {d1}""")
#tablero()
#segunda_linea(ingreso_palabra(juego_1(palabras_a_jugar()), aciertos_errores()[0], aciertos_errores()[1])[3], n1)
