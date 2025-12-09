import pandas as pd
#Se ha tenido que instalar openpyxl porque pandas la usa pero no lo instala

df = pd.read_excel("../Data/mortalidad_tabla.xlsx",sheet_name="Sheet1")
print(df)

df_dicc=df.to_dict("records")

print(df_dicc[3])
