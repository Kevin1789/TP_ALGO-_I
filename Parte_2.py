def invocar_diccionario():
    from datos import obtener_lista_definiciones
    lista = obtener_lista_definiciones()
    return lista

def sin_acentos(lista):
    """
    Esta función reemplaza las vocales con acentos por vocales sin acentos.
    >>> sin_acentos([["víveres","1.  m. pl. Provisiones de boca de un ejército plaza o buque"],["unificación","1.  f. Acción y efecto de unificar"]])
    [['viveres', '1.  m. pl. Provisiones de boca de un ejército plaza o buque'], ['unificacion', '1.  f. Acción y efecto de unificar']]
    """
    vocales_con_acentos = "áéíóú"
    vocales_sin_acentos = "aeiou"
    for i in range(len(lista)):
        palabra = lista[i][0]
        for j in range(len(vocales_con_acentos)):
            palabra = palabra.replace(vocales_con_acentos[j], vocales_sin_acentos[j])
        lista[i][0] = palabra
    return lista
#print(sin_acentos(invocar_diccionario()))

def filtrar_palabras(lista_filtra):
    """
    Esta funcion filtra las palabras que tienen mas de 5 letras
    >>> filtrar_palabras([["palabra1", "definición1"], ["palabra2", "definición2"]])
    {'palabra1': 'definición1', 'palabra2': 'definición2'}
    """
    diccionario_rosco = {}
    LONG_MIN = 5
    for sublistas in lista_filtra:
        if len(sublistas[0]) >= LONG_MIN:
            diccionario_rosco[sublistas[0]] = sublistas[1]
    return diccionario_rosco
#print(filtrar_palabras(sin_acentos(invocar_diccionario())))

#D 
def contar_letras_de_palabras(diccionario_rosco):
    """
    Esta funcion cuenta la cantidad de palabras que hay en el diccionario por letra inicial
    >>> contar_letras_de_palabras({'palabra1': 'definición1', 'palabra2': 'definición2'})
    {'p': 2}
    """
    dicc_candidatas_letra = {}
    for clave, valor in diccionario_rosco.items():
        if clave[0] not in dicc_candidatas_letra:
            dicc_candidatas_letra[clave[0]] = 1
        else:
            dicc_candidatas_letra[clave[0]] += 1
    return dicc_candidatas_letra
#print(contar_letras_de_palabras(filtrar_palabras(sin_acentos(invocar_diccionario()))))

def ordenar_contar_letras(dicc_candidatas_letra):
    """
    Esta función ordena el diccionario de palabras candidatas a adivinar por letra.
    >>> ordenar_contar_letras({"p": 2})
    letra: p - cantidad: 2
    """
    for clave, valor in sorted(dicc_candidatas_letra.items()):
        print("letra:", clave, "-", "cantidad:", valor)
    return
#print(ordenar_contar_letras(contar_letras_de_palabras(filtrar_palabras(sin_acentos(invocar_diccionario())))))

def contar_palabras(diccionario_rosco):
    """
    Esta funcion cuenta la cantidad de palabras que hay en el diccionario
    >>> contar_palabras({'palabra1': 'definición1', 'palabra2': 'definición2'})
    Total de palabras:  2
    """
    total_palabras = 0
    for clave, valor in diccionario_rosco.items():
        total_palabras += 1
    return print("Total de palabras: ", total_palabras)
#print(contar_palabras(filtrar_palabras(sin_acentos(invocar_diccionario()))))

#import doctest
#print(doctest.testmod())
