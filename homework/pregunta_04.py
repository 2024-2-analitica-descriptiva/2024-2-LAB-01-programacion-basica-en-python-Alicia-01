"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    registro_mes = {}
    with open('files\input\data.csv', 'r') as file:
        for line in file:
            columnas = line.strip(). split ('\t')
            if len(columnas) > 2:
                fecha = columnas[2].strip()
                mes = fecha.split('-')[1]
                if mes in registro_mes:
                    registro_mes[mes] += 1
                else:
                    registro_mes[mes] = 1
    resultado = sorted(registro_mes.items())
    return resultado
print(pregunta_04())