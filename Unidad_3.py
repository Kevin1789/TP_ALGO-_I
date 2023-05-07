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

#print(descripcion_palabras())

#el rosco es una lista de 10 palabras, una por cada letra del abecedario que no se repiten
#lista_palabras2 = {"casa": "donde vives", "cama": "donde duermes", "perro": "animal", "gato": "animal", "raton": "animal", "pajaro": "animal", "pato": "animal", "caballo": "animal", "vaca": "animal", "oveja": "pastor"}
list_rosco = []
descp_palabras = []
def generar_rosco(lista_palabras, list_rosco, descp_palabras):
    letras_utilizadas = set()
    palabras_seleccionadas = 0
    for palabra in lista_palabras:
        if palabras_seleccionadas == 10:
            return list_rosco
        if palabra[0] not in letras_utilizadas:
            list_rosco.append(palabra)
            letras_utilizadas.add(palabra[0])
            palabras_seleccionadas += 1
        descp_palabras.append(lista_palabras[palabra])
    if palabras_seleccionadas < 10:
        list_rosco = None
    return list_rosco , descp_palabras


lista_palabras2 = {"casa": "donde vives", "cama": "donde duermes", "perro": "animal", "gato": "animal", "raton": "animal", "pajaro": "animal", "pato": "animal", "caballo": "animal", "vaca": "animal", "oveja": "pastor"}

dicc_rosco2 = {}
descp_palabras2 = {}

def generar_rosco(lista_palabras2, dicc_rosco2, dicc_descripciones2):
    letras_utilizadas = set()
    palabras_seleccionadas = 0
    for palabra, descripcion in lista_palabras2.items():
        if palabras_seleccionadas == 10:
            return dicc_rosco2, dicc_descripciones2
        if palabra[0] not in letras_utilizadas:
            dicc_rosco2[palabra] = None
            dicc_descripciones2[palabra] = descripcion
            letras_utilizadas.add(palabra[0])
            palabras_seleccionadas += 1
    if palabras_seleccionadas < 10:
        dicc_rosco2 = None
    return dicc_rosco2, dicc_descripciones2
rosco, descripciones = generar_rosco(lista_palabras2, dicc_rosco2, descp_palabras2)
print(rosco)
print(descripciones)

#casa


def ordenar_rosco(list_rosco):
    list_rosco.sort()
    return list_rosco

#print(ordenar_rosco(generar_rosco(palabras_participantes(), list_rosco)))

def rosco_2(list_rosco):
    rosco_2 = []
    for i in list_rosco:
        rosco_2.append(i[0])
    return rosco_2

#print(rosco_2(list_rosco))