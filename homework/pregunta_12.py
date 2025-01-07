"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    diccionario = {}
    with open('files\\input\\data.csv', 'r') as file:
        for line in file:
            columnas = line.strip(). split ('\t')
            if len(columnas) > 4:
                letra_columna_1 = columnas[0]
                columna_5 = columnas[4]
                suma_columna_5 = 0

                pares = columna_5.split(',')
                for par in pares:
                    clave, valor = par.split(':')
                    suma_columna_5 += int(valor)
            
                if letra_columna_1 in diccionario:
                    diccionario[letra_columna_1] += suma_columna_5
                else:
                    diccionario[letra_columna_1] = suma_columna_5
    return diccionario

print(pregunta_12())