import pandas as pd # type: ignore
import numpy as np # type: ignore

class Poliza:
    cartera = "df"
    fichero = "path"


    def __init__(self,archivo,ext):
        self.fichero = f"./data/{archivo}.{ext}"
        if ext == "csv":
            self.cartera = pd.read_csv(self.fichero)
        else:
            self.cartera = pd.read_excel(self.fichero)
    
    def promedio(self,c):
       self.media = self.cartera[c].mean() 
       return self.media
    
    def total_SA(self,c):
        self.total= self.cartera[c].sum()
        return self.total
    
    def df(self):
        edad=int(input("Edad de filtro: "))
        df_edad = self.cartera[self.cartera["edad"]>edad]
        return df_edad

    def va(self):
        años= int(input("¿Cuántos años quieres proyectar? "))
        i = float(input("¿Cúal es el tipo de interés? "))
        spot= (1+i)**np.arange(años)
        primas_va= self.cartera["prima_anual"]
        primas_va = primas_va.to_numpy()
        primas_va = primas_va.reshape(-1,1)
        primas_va=np.tile(primas_va,años)
        primas_va=pd.DataFrame(primas_va)
        primas_va= primas_va/spot
        primas_va=primas_va.sum(axis=1)
        return primas_va