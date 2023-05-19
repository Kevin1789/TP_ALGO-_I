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
dicc = {"casa": "lugar donde vives", "perro": "animal domestico", "gato": "animal domestico"}

def agregar_lista(lista_2,aciertos,errores):
    #aciertos, errores
    for i in range(len(lista_2)):
        if i < aciertos:
            if lista_2[i] == " ":
                lista_2[i] = "c"
        elif i < aciertos + errores:
            if lista_2[i] == " ":
                lista_2[i] = "e"
        else:
            if lista_2[i] == " ":
                lista_2[i] = " "
    return lista_2

def mostrar_tablero_3(aciertos, errores, posicion, lista, lista_2):
    print(f"[{lista[0]}][{lista[1]}][{lista[2]}]")
    print(f"[{lista_2[0]}][{lista_2[1]}][{lista_2[2]}]")
    print(" " * (posicion * 3 + 1) + "^")
    print(f"Aciertos: {aciertos}")
    print(f"Errores: {errores}")

def ingresar_palabra():
    ingreso_usuario = input("Ingresa palabra: ").lower()
    while not ingreso_usuario.isalpha():
        print("Ingrese solo letras.")
        ingreso_usuario = input("Ingrese palabra: ").lower()
    return ingreso_usuario

def puntaje(aciertos):
    return aciertos

def pasapalabra():
    puntaje_total = 0 
    aciertos = 0
    errores = 0
    lista_2 = [" ", " ", " "]
    posicion = 0
    lista_palabras_ingresadas = [] # nueva variable para almacenar las palabras ingresadas por el usuario

    for clave, valor in dicc.items():
        palabra = clave
        longitud = len(palabra)
        definicion = valor
        letra = clave[0]
        lista = [" ", " ", " "]

        for letra_1, clave_1 in enumerate(dicc.keys()):
            lista[letra_1] = clave_1[0]

        mostrar_tablero_3(aciertos, errores, posicion, lista, lista_2)
        print(f"Turno letra: {letra} Longitud palabra: {longitud}")
        print(f"Definicion: {definicion}")

        if posicion == 0:
            palabra_ingresada_1 = ingresar_palabra() # Cambio de nombre para evitar conflicto con la función
            lista_palabras_ingresadas.append(palabra_ingresada_1) # agregar la palabra ingresada a la lista de palabras ingresadas
            if palabra_ingresada_1 == clave:
                aciertos += 1
                lista_2[posicion] = "a"
                posicion += 1
                print(f"Turno letra: {letra} - Palabra de {longitud} - {palabra_ingresada_1} - acierto")
            else:
                errores += 1
                lista_2[posicion] = "e"
                posicion += 1
                print(f"Turno letra: {letra} - Palabra de {longitud} - {palabra_ingresada_1} - error - Palabra correcta: {clave}")
        else:
            palabra_ingresada_2 = ingresar_palabra() # Cambio de nombre para evitar conflicto con la función
            lista_palabras_ingresadas.append(palabra_ingresada_2) # agregar la palabra ingresada a la lista de palabras ingresadas
            if palabra_ingresada_2 == clave:
                aciertos += 1
                lista_2[posicion] = "a"
                posicion += 1
                print(f"Turno letra: {letra} - Palabra de {longitud} - {palabra_ingresada_2} - acierto")
            else:
                errores += 1
                lista_2[posicion] = "e"
                posicion += 1
                print(f"Turno letra: {letra} - Palabra de {longitud} - {palabra_ingresada_2} - error")

    # Resumen de la partida
    print("\n--- Resumen de la Partida ---")
    print("-" * 50)
    for i, (clave, valor) in enumerate(dicc.items()):
        letra = clave[0]
        longitud = len(clave)
        palabra_correcta = clave
        palabra_ingresada = lista_palabras_ingresadas[i] # nueva variable para almacenar la palabra ingresada por el usuario
        resultado = "acierto" if lista_2[i] == "a" else "error"
        if resultado == "error":
            print(f"Turno de la letra: {letra} - Palabra de {longitud} letras - {palabra_ingresada} - {resultado} - Palabra correcta es : {palabra_correcta}")
        else:
            print(f"Turno de la letra: {letra} - Palabra de {longitud} letras - {palabra_ingresada} - {resultado}")
    print("-" * 50)

    puntaje_total = puntaje(aciertos)
    print(f"\nPuntaje total: {puntaje_total}")

pasapalabra()