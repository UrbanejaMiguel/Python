import csv

def get_data():
    b=[]
    try:
        with open ("C:\\Users\\miguel.urbanejaferna\\Desktop\\Py\\Curso Milliman\\Python\\Ejercicios\\Ej_1\\data\\siniestros.csv","r") as siniestros:
            r= csv.DictReader(siniestros)
            for row in r:
               b.append(row)
        return b
    except:
        print("Error en la importacion de datos")

def types(lista):
    tipos=[]
    for c in lista:
        tipos.append(c["tipo_siniestro"])
    return list(set(tipos))

def filter_by_sin(lista,s_type):
        return list(filter(lambda siniestro: siniestro["tipo_siniestro"] == s_type,lista))

def max_paid(lista):
    return max(siniestro['pago'] for siniestro in lista)
