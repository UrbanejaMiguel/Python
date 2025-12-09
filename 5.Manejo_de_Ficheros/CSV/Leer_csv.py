import csv #Importacion de datos csv interna de Python
import pandas as pd

df = pd.read_csv("../Data/siniestros.csv")

#Convertir mi dataframe en una lista de listas
df_list = df.values.tolist()
print(df_list[0])

#Convertir una sola columna en una lista
df_column = df["tipo_siniestro"].unique().tolist()
print(df_column)

#Convertir a lista de diccionarios (Lista JSON o APIs)
df_dicc=df.to_dict(orient="records") #Para tener una lista de diccionarios por filas
print(df_dicc[3]["anio"])

#Convertir cada fila en una tupla
df_tuplas=list(df.itertuples(index=False,name=None))
print(df_tuplas[3])