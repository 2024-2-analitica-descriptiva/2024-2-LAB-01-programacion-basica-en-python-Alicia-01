"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}
    """
    diccionario = {}
    with open('files\\input\\data.csv', 'r') as file:
        for line in file:
            columnas = line.strip(). split ('\t')
            if len(columnas) > 4:
                valor_columna_2 = int(columnas[1]) 
                columna_4 = columnas[3]
               
                for letra in columna_4.split(','):
                    if letra in diccionario:
                        diccionario[letra] += valor_columna_2 
                    else:
                        diccionario[letra] = valor_columna_2 
    return dict(sorted(diccionario.items()))
print(pregunta_11())
