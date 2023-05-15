"""
Etapa 2 - Construcción de un Diccionario de Palabras candidatas
Ahora el objetivo será generar un diccionario de palabras candidatas a adivinar.
Para ello se proveerá una función que retorna un texto en formato:
[
[“palabra1”, “definición1”],
[“palabra2”, “definición2”],
…
]
Se les proveerá de una función que devolverá un texto del cual extraerán las palabras
con sus definiciones para formar el diccionario. Las palabras seleccionadas deberán tener
un mínimo de 5 letras.
Una vez generado el diccionario de palabras, se debe mostrar por pantalla el total de
palabras que hay por cada letra, y el total que hay en el diccionario.
"""

def invocar_lista():
    from datos import obtener_lista_definiciones
    lista = obtener_lista_definiciones()
    #quitamos los acentos de las palabras
    for i in range(len(lista)):
        lista[i][0] = lista[i][0].replace("á", "a")
        lista[i][0] = lista[i][0].replace("é", "e")
        lista[i][0] = lista[i][0].replace("í", "i")
        lista[i][0] = lista[i][0].replace("ó", "o")
        lista[i][0] = lista[i][0].replace("ú", "u")
    return lista
#print(invocar_lista())

def generar_diccionario(lista):
    """
    Esta función genera un diccionario a partir de una lista de listas.
    >>> generar_diccionario([["palabra1", "definición1"], ["palabra2", "definición2"]])
    {'palabra1': 'definición1', 'palabra2': 'definición2'}
    """
    dicc = {}
    for i in lista:
        dicc[i[0]] = i[1]
    return dicc
#print(generar_diccionario(invocar_lista()))

def dicc_candidatas(dicc):
    """
    Esta función genera un diccionario con las palabras candidatas a adivinar.
    >>> dicc_candidatas({"palabra1": "definición1", "palabra2": "definición2"})
    {'palabra1': 'definición1', 'palabra2': 'definición2'}
    """
    dicc_candidatas = {}
    for clave, valor in dicc.items():
        if len(clave) >= 5:
            dicc_candidatas[clave] = valor
    return dicc_candidatas
#print(dicc_candidatas(generar_diccionario(invocar_lista())))

def palabras_candidatas(dicc_candidatas):
    """
    Esta función genera una lista con las palabras y descripciones de las palabras candidatas a adivinar.
    >>> palabras_candidatas({"palabra1": "definición1", "palabra2": "definición2"})
    (['palabra1', 'palabra2'], ['definición1', 'definición2'])
    """
    palabras_candidatas = []
    descripcion_de_palabras_candidatas = []
    for clave, valor in dicc_candidatas.items():
        palabras_candidatas.append(clave)
        descripcion_de_palabras_candidatas.append(valor)
    return palabras_candidatas, descripcion_de_palabras_candidatas
#print(palabras_candidatas(dicc_candidatas(generar_diccionario(invocar_lista()))))

def dicc_candidatas_letra(dicc_candidatas):
    """
    Esta función genera un diccionario con la cantidad de palabras candidatas a adivinar por letra.
    >>> dicc_candidatas_letra({"palabra1": "definición1", "palabra2": "definición2"})
    {'p': 2}
    """
    dicc_candidatas_letra = {}
    for clave, valor in dicc_candidatas.items():
        if clave[0] not in dicc_candidatas_letra:
            dicc_candidatas_letra[clave[0]] = 1
        else:
            dicc_candidatas_letra[clave[0]] += 1
    return dicc_candidatas_letra
#print(dicc_candidatas_letra(dicc_candidatas(generar_diccionario(invocar_lista()))))

def ordenar_dicc_candidatas_letra(dicc_candidatas_letra):
    """
    Esta función ordena el diccionario de palabras candidatas a adivinar por letra.
    >>> ordenar_dicc_candidatas_letra({"p": 2})
    letra: p - cantidad: 2
    """
    for clave, valor in sorted(dicc_candidatas_letra.items()):
        print("letra:", clave, "-", "cantidad:", valor)
    return
#print(ordenar_dicc_candidatas_letra(dicc_candidatas_letra(dicc_candidatas(generar_diccionario(invocar_lista())))))

def total_palabras(dicc_candidatas_letra):
    """
    Esta función genera la cantidad total de palabras candidatas a adivinar.
    >>> total_palabras({"p": 2})
    Total de palabras:  2
    """
    total_palabras = 0
    for clave, valor in dicc_candidatas_letra.items():
        total_palabras += valor
    return print("Total de palabras: ", total_palabras)
#print(total_palabras(dicc_candidatas_letra(dicc_candidatas(generar_diccionario(invocar_lista())))))

#import doctest
#print(doctest.testmod())