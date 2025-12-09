import pandas as pd

#Cargar un fichero con pandas
df = pd.read_csv("C:\\Users\\miguel.urbanejaferna\\Desktop\\Py\\Curso Milliman\\Python\\Ejercicios\\Ej_1\\data\\siniestros.csv")
#print(df)

print(df["tipo_siniestro"][1])
print("-"*40)

#Para filtrar:
tipo_siniestro=df["tipo_siniestro"].unique()
filtro = df[df["tipo_siniestro"]=="Fallecimiento"]
print(filtro)
