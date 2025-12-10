import pandas as pd # type: ignore

class Poliza:
    cartera = "df"
    fichero = "path"


    def __init__(self,archivo,ext):
        self.fichero = f"./data/{archivo}.{ext}"
        if ext == "csv":
            self.cartera = pd.read_csv(self.fichero)
        else:
            self.cartera = pd.read_excel(self.fichero)
    
    def med(self,a,p):
       self.media = a[p].mean()