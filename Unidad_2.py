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
    return lista

#print(invocar_lista())

def generar_diccionario(lista):
    dicc = {}
    for i in lista:
        dicc[i[0]] = i[1]
    return dicc

#print(generar_diccionario(invocar_lista()))

def dicc_candidatas(dicc):
    dicc_candidatas = {}
    for clave, valor in dicc.items():
        if len(clave) >= 5:
            dicc_candidatas[clave] = valor
    return dicc_candidatas

#print(dicc_candidatas(generar_diccionario(invocar_lista())))

def palabras_candidatas(dicc_candidatas):
    palabras_candidatas = []
    for clave, valor in dicc_candidatas.items():
        palabras_candidatas.append(clave)
    return palabras_candidatas

#print(palabras_candidatas(dicc_candidatas(generar_diccionario(invocar_lista()))))

def definiciones_candidatas(dicc_candidatas):
    definiciones_candidatas = []
    for clave, valor in dicc_candidatas.items():
        definiciones_candidatas.append(valor)
    return definiciones_candidatas

#print(definiciones_candidatas(dicc_candidatas(generar_diccionario(invocar_lista()))))

def dicc_candidatas_letra(dicc_candidatas):
    dicc_candidatas_letra = {}
    for clave, valor in dicc_candidatas.items():
        if clave[0] not in dicc_candidatas_letra:
            dicc_candidatas_letra[clave[0]] = 1
        else:
            dicc_candidatas_letra[clave[0]] += 1
    return dicc_candidatas_letra

#print(dicc_candidatas_letra(dicc_candidatas(generar_diccionario(invocar_lista()))))

def ordenar_dicc_candidatas_letra(dicc_candidatas_letra):
    dicc_candidatas_letra_ordenado = {}
    for clave, valor in sorted(dicc_candidatas_letra.items()):
        dicc_candidatas_letra_ordenado[clave] = valor
        #print(f"letra: {clave} - cantidad: {valor}")
    return dicc_candidatas_letra_ordenado

#print(ordenar_dicc_candidatas_letra(dicc_candidatas_letra(dicc_candidatas(generar_diccionario(invocar_lista())))))


#dicc_candidatas_a= {"casa","palo","combate","comer","com"}
def total_palabras(dicc_candidatas):
    total_palabras = len(dicc_candidatas)
    #print(f"Total de palabras: {total_palabras}")
    return total_palabras

#total_palabras(dicc_candidatas_a)
#print(total_palabras(dicc_candidatas(generar_diccionario(invocar_lista()))))

#ordenar_dicc_candidatas_letra(dicc_candidatas_letra(dicc_candidatas(generar_diccionario(invocar_lista()))))
#total_palabras(dicc_candidatas(generar_diccionario(invocar_lista())))