"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]

    """
    lista = []
    with open('files\\input\\data.csv', 'r') as file:
        for line in file:
            columnas = line.strip(). split ('\t')
            if len(columnas) > 4:
                letra = columnas[0]
                columna_4 = columnas[3]
                columna_5 = columnas[4]

                count_4 = len(columna_4.split(','))
                count_5 = len(columna_5.split(','))
                lista.append((letra, count_4, count_5))
    return lista
print(pregunta_10())