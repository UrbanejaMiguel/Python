import pandas as pd
import numpy as np


class Poliza:
    fichero=""
    path=""
    df=""
    def get_data(self,file1):
        self.path="./data/"
        self.fichero=file1
        self.df= pd.read_csv(f"{self.path}{self.fichero}")
        return self
    def join(self, other_poliza):
        filtro=self.df["id_poliza"].isin(other_poliza.df["id_poliza"]) 
        df_join=self.df[filtro.to_numpy()]
        df_join=pd.merge(df_join,other_poliza.df,"inner","id_poliza")
        return df_join
    def total(self,c):
        return self.df[c].sum()
    def siniestralidad(self):
        return self.df.set_index("id_poliza")["pago"]/self.df.set_index("id_poliza")["suma_asegurada"]