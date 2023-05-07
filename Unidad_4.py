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
def invocar_unidad_3():
    from Unidad_3 import 

def pasapalabra():
    aciertos = 0
    errores = 0
    lista_2 = [" "," "," "," "," "," "," "," "," "," "]
    for clave, valor in dicc.items():
        palabra = clave
        print(palabra)
        longitud = len(palabra)
        definicion = valor
        letra = clave[0]
        lista_ = [" "," "," "," "," "," "," "," "," "," "]
        for letra_1, clave_1 in enumerate(dicc.keys()):
            lista_[letra_1] = clave_1[0]
        print(f"""[{lista_[0]}][{lista_[1]}][{lista_[2]}][{lista_[3]}][{lista_[4]}][{lista_[5]}][{lista_[6]}][{lista_[7]}][{lista_[8]}][{lista_[9]}]""")
        print(f"[{lista_2[0]}][{lista_2[1]}][{lista_2[2]}][{lista_2[3]}][{lista_2[4]}][{lista_2[5]}][{lista_2[6]}][{lista_2[7]}][{lista_2[8]}][{lista_2[9]}]")
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
            #lista_2.append("a")
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

#pasapalabra()
