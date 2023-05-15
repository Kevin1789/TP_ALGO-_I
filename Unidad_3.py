"""
Etapa 3 - Elección de las palabras candidatas para formar el “rosco”
En esta variante del juego, se seleccionarán al azar 10 letras de todo el conjunto de
letras para formar el rosco.
Ahora que tenemos nuestro diccionario, podremos utilizarlo para obtener una palabra
candidata de cada letra a adivinar.
Escribí una función, que reciba como primer parámetro el diccionario y como segundo la
lista de letras participantes. La función deberá devolver aleatoriamente una palabra que
empiece con cada letra participante de entre todas las posibles, esto será retornado
como una lista de palabras ordenadas alfabéticamente.
Para probar tu función, utiliza un ciclo que la invoque al menos 100 veces, y analiza lo
que obtienes como palabras a adivinar. Repite el proceso varias veces.
Además de la función principal de esta etapa, puedes escribir todas las que consideres
necesarias, teniendo en cuenta los conceptos aprendidos en clase sobre programación
estructurada y programación modular.
Lista de letras que deben procesar:
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
'x', 'y', 'z']
"""

def palabras_participantes():
    from Unidad_2 import invocar_lista, generar_diccionario, dicc_candidatas
    lista_palabras = dicc_candidatas(generar_diccionario(invocar_lista()))
    return lista_palabras
#print(palabras_participantes())

def seleccionar_palabras(palabras_participantes):
    """
    Esta función selecciona las palabras candidatas para formar el rosco.
    >>> seleccionar_palabras({"palabra1": "definición1", "palabra2": "definición2"})
    {'p': 'palabra1'}

    """
    palabras_seleccionadas = {}
    letras = []
    for clave, valor in palabras_participantes.items():
        letras.append(clave[0])
    letras = list(set(letras))
    letras.sort()
    for i in letras:
        palabras_seleccionadas[i] = []
    for clave, valor in palabras_participantes.items():
        palabras_seleccionadas[clave[0]].append(clave)
    for clave, valor in palabras_seleccionadas.items():
        palabras_seleccionadas[clave] = valor[0]
    return palabras_seleccionadas
#print("prueba1",seleccionar_palabras(palabras_participantes()))

def palabras_a_jugar(palabraS_seleccionada):
    """
    Esta función selecciona las palabras candidatas para formar el rosco.
    >>> palabras_a_jugar({"p": "palabra1"})
    ['palabra1']

    """
    palabras = []
    for clave, valor in palabraS_seleccionada.items():
        palabras.append(valor)
    return palabras
#print("prueba2",palabras_a_jugar(seleccionar_palabras(palabras_participantes())))

#crea una funcion que eliga al azar 10 palabras de la lista de palabras a jugar 
def diez(palabras):
    import random
    diez_palabras = []
    for i in range(10):
        palabra = random.choice(palabras)
        diez_palabras.append(palabra)
        palabras.remove(palabra)
    diez_palabras.sort()
    return diez_palabras
#print("prueba3",diez(palabras_a_jugar(seleccionar_palabras(palabras_participantes()))))

def inicial_de_las_diez (diez_palabras):
    """
    Esta función selecciona las palabras candidatas para formar el rosco.
    >>> inicial_de_las_diez(["palabra1", "palabra2", "palabra3", "palabra4", "palabra5", "palabra6", "palabra7", "palabra8", "palabra9", "palabra10"])
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p']

    """
    iniciales = []
    for i in diez_palabras:
        iniciales.append(i[0])
    return iniciales
#print("prueba4",inicial_de_las_diez(diez(palabras_a_jugar(seleccionar_palabras(palabras_participantes())))))

#import doctest
#doctest.testmod()