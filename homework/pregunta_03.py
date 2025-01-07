"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    suma_letra = {}
    with open('files/input/data.csv', 'r') as file:
        for line in file:
            columnas = line.strip(). split ('\t')
            if len(columnas) > 1:
                letra = columnas[0].strip()
                valor = int(columnas[1].strip())
                if letra in suma_letra:
                    suma_letra[letra] += valor
                else:
                    suma_letra[letra] = valor
    resultado = sorted(suma_letra.items())
    return (resultado)
print(pregunta_03())
