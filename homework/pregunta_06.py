"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    diccionario_valores = {}
    with open('files/input/data.csv', 'r') as file:
        for line in file:
            columnas = line.strip(). split ('\t')
            if len(columnas) > 4:
                 diccionario_str = columnas[4].strip()
                 claves_valores = diccionario_str.split(',')
                 
                 for clave_valor in claves_valores:
                     clave, valor = clave_valor.split(':')
                     valor = int(valor.strip())
                     if clave not in diccionario_valores:
                        diccionario_valores[clave] = [valor, valor]
                     else:
                        diccionario_valores[clave][0] = min(diccionario_valores[clave][0], valor)
                        diccionario_valores[clave][1] = max(diccionario_valores[clave][1], valor)
    resultado = [(clave, valores[0], valores[1]) for clave, valores in diccionario_valores.items()]
    resultado.sort()

    return resultado
print(pregunta_06())