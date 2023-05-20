import random
from Parte_2 import filtrar_palabras, sin_acentos, invocar_diccionario


#Funcion que retorna 10 letras aleatorias 
def lista_letras():
    """
    Esta función retorna 10 letras aleatorias.
    """
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lista_aleatoria_letras = random.sample(letras, k=10)
    return sorted(lista_aleatoria_letras)
#print(lista_letras())

#Funcion que arma un diccionario de las palabras que empiezan con las letras que se filtraron en la anterior funcion
def armar_dicc(diccionario, lista_aleatoria_letras):
    """
    Esta función arma un diccionario de las palabras que empiezan con las letras que se filtraron en la anterior funcion
    """
    dicc = {}
    LETRA_INICIAL = 0
    for palabra in diccionario.keys():
        if palabra[LETRA_INICIAL] in lista_aleatoria_letras:
            if palabra[LETRA_INICIAL] not in dicc:
                dicc[palabra[LETRA_INICIAL]] = [palabra]
            else:
                dicc[palabra[LETRA_INICIAL]].append(palabra)
    return dicc
#print(armar_dicc(filtrar_palabras(sin_acentos(invocar_diccionario())), lista_letras()))

#Funcion que devuleve una lista ordenada alfabeticamente con 10 palabras al azar que empiezan con las 10 letras al azar de la 1ra funcion 
def palabras_resultantes(resultado):
    """
    Esta función devuleve una lista ordenada alfabeticamente con 10 palabras al azar que empiezan con las 10 letras al azar de la 1ra funcion
    """
    new_list = []
    for palabras in resultado.values():
        palabra = random.sample(palabras, k=1)
        new_list.append(palabra)
    return sorted(new_list)
#print(palabras_resultantes(armar_dicc(filtrar_palabras(sin_acentos(invocar_diccionario())), lista_letras())))

#Imprimo los resultados
def imprimir_resultados():
    letras_aleatorias = lista_letras()
    print(letras_aleatorias)
    diccionario = filtrar_palabras(sin_acentos(invocar_diccionario()))
    resultado = armar_dicc(diccionario, letras_aleatorias)
    print(palabras_resultantes(resultado))

imprimir_resultados()