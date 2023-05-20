def cambiar(palabra):
    voales = "aeiou"
    vocales_acentuadas = "áéíóú"
    for caracter in range(len(vocales_acentuadas)):
        palabra = palabra.replace(vocales_acentuadas[caracter], voales[caracter])
    return palabra

print(cambiar("café"))