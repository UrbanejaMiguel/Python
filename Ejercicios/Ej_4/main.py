import pandas as pd
import numpy as np
import openpyxl
import time

def get_data(file_name):
    df = pd.read_excel(f"./data/{file_name}")
    return df

curvas = get_data("curvas_descuento.xlsx")

#Crear una funcion que me saque el vector de pago por año en funcion del fichero de curvas
def get_cf(df_curvas,cf_anual):
    años= len(df_curvas)
    cf =np.full(años,cf_anual) #[cf,cf,cf,...,cf] con dimension años x 1
    return{"años": años, "anual": cf_anual, "vector":cf}

dict_cf = get_cf(curvas,1000.00)
tasas = curvas["tasa"].values

#Metodo tradicional con bucles
start=time.time()
vp_bucle =0.0
for t in range(0,dict_cf["años"]):
    tasa=tasas[t]
    vp_bucle+= dict_cf["anual"]/((1+tasa)**t)

print(vp_bucle)
end=time.time()
tiempo=end-start
print(f"El tiempo usado con bucles ha sido {tiempo}s")

#Metodo numpy
start=time.time()
periodos = np.arange(0,dict_cf["años"])
vp_vector= np.sum(dict_cf["anual"]/((1+tasas)**periodos))
end=time.time()
tiempo=end -start
print(vp_vector)
print(f"El tiempo usado con vectores ha sido {tiempo}s")