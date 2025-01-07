"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    letras = {}
    with open('files/input/data.csv', 'r') as file:
        for line in file:
            columnas = line.strip(). split ('\t')
            if len(columnas) > 1:
                letra = columnas[0].strip()
                valor = int(columnas[1].strip())
                if letra in letras:
                    letras[letra].append(valor)
                else:
                    letras[letra] = [valor]
    resultado = []
    for letra, valores in letras.items():
        maximo = max(valores)
        minimo = min(valores)
        resultado.append((letra, maximo, minimo))
    resultado.sort()

    return resultado
print(pregunta_05())

