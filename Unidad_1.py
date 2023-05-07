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

dicc = {"casa":"lugar donde vives", "perro":"animal domestico", "gato":"animal domestico"}
aciertos = 0
errores = 0
clave = ""
valor = ""
def palabra (dicc):
    for clave, valor in dicc.items():
        palabra = clave
    return palabra

def aciertos_errores (palabra, clave):
    if palabra == clave:
        aciertos = aciertos + 1
        print("aciertos:", aciertos)
    elif palabra != clave :
        errores = errores + 1
        print("errores:", errores)
    return aciertos, errores

longitud = 0

def longotud_palabra (palabra):
    longitud = len(palabra)
    return longitud

definicion = ""

def definicion_palabra (valor):
    definicion = valor
    return definicion

lista = [" "," "," "]

def mostrar_tablero (dicc):
    for letra, clave in enumerate(dicc.keys()):
        lista[letra] = clave[0]
    print(f"""[{lista[0]}][{lista[1]}][{lista[2]}]""")
#mostrar_tablero(dicc)


lista_2 = []

def agregar_lista (lista_2, aciertos):
    for aciertos in lista_2:
        if aciertos + 1:
            lista_2.append("a")
        else:
            lista_2.append("e")
    return lista_2


def mostrar_tablero_3 (acirtos, errores):
    print(f"""
aciertos: {aciertos}
errores: {errores}""")

def turno_letra (dicc, longitud, definicion):
    for clave, valor in dicc.items():
        letra = clave[0]
        print(f"turno letra: {letra}   longitud palabra: {longitud}")
        print(f"definicion: {definicion}")
        return letra, definicion, longitud
#turno_letra(dicc)

def palabra_ingresada (palabra):
    palabra = input()
    return palabra

def pasapalabra():
    aciertos = 0
    errores = 0
    lista_2 = [" "," "," "]
    for clave, valor in dicc.items():
        palabra = clave
        print(palabra)
        longitud = len(palabra)
        definicion = valor
        letra = clave[0]
        lista = [" "," "," "]
        for letra_1, clave_1 in enumerate(dicc.keys()):
            lista[letra_1] = clave_1[0]
        print(f"""[{lista[0]}][{lista[1]}][{lista[2]}]""")
        print(f"[{lista_2[0]}][{lista_2[1]}][{lista_2[2]}]")
        print(f"""
aciertos: {aciertos}
errores: {errores}""")
        print(f"turno letra: {letra}   longitud palabra: {longitud}")
        print(f"definicion: {definicion}")
        palabra = input()
        if palabra == clave:
            aciertos = aciertos + 1
            for i in range(len(lista_2)):
                if lista_2[i] == " ":
                    lista_2[0] = "a"
            #ista_2.append("a")
            #print("aciertos:", aciertos)
        elif palabra != clave :
            errores = errores + 1
            for i in range(len(lista_2)):
                if lista_2[i] == " ":
                    lista_2[0] = "e"
            #lista_2.append("e")
            #print("errores:", errores)
        #print(lista_2)
    return aciertos, errores

pasapalabra()
