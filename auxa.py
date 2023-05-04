"""
crea una funcion en python de adivinar las palabras de un diccionario
el diccionario tiene como clave la palabra y como valor la definicion
el juego consiste que el usuario adivine la palabra
el juego termina cuando el usuario adivine las 3 palabras
dicc = {"casa":"lugar donde vives", "perro":"animal domestico", "gato":"animal domestico"}
ejemplo de salida:
ingrese la palabra que empieza con la letra c: casa
ingrese la palabra que empieza con la letra p: perro
ingrese la palabra que empieza con la letra g: gato
ganaste 
"""
dicc = {"casa":"lugar donde vives", "perro":"animal domestico", "gato":"animal domestico"}
def adivinar_palabras (dicc):
    for clave, valor in dicc.items():
        print("ingrese la palabra que empieza con la letra", clave[0],":")
        print(valor)
        palabra = input()
        if palabra == clave:
            print("correcto")
        else:
            print("incorrecto")
    print("ganaste")

adivinar_palabras(dicc)

