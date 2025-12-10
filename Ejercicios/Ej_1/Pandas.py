import pandas as pd # type: ignore

#Cargar un fichero con pandas
df = pd.read_csv("C:\\Users\\miguel.urbanejaferna\\Desktop\\Py\\Curso Milliman\\Python\\Ejercicios\\Ej_1\\data\\siniestros.csv")
#print(df)

print(df["tipo_siniestro"][1])
print("-"*40)

#Para filtrar:
tipo_siniestro=df["tipo_siniestro"].unique()
filtro = df[df["tipo_siniestro"]=="Fallecimiento"]
print(filtro)

#Pago maximo por fallecimiento
max_paid =df[df["tipo_siniestro"]=="Fallecimiento"]["pago"].max()
id_max_paid =df[df["tipo_siniestro"]=="Fallecimiento"]["pago"].idxmax()
print(id_max_paid, max_paid)
print(df.loc[id_max_paid])
print(df.loc[[id_max_paid]])
diccionario = df.loc[id_max_paid].to_dict()
print(diccionario["anio"])