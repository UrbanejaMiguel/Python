import math

class Calculadora:
    marca = ""
    bateria = False
    cientifica = False

    def __init__(self,marca:str,bateria:bool,cientifica=False):
        self.marca = marca
        self.bateria = bateria
        self.cientifica = cientifica

    def sumar(self,lista: list[float]) -> float:
        return sum(lista)
    
    def redondeo(self,num:float,cantidad:int)->float:
        return round(num,cantidad)
    
    def raiz(self,numero: float)->float:
        if self.cientifica:
            return math.sqrt(numero)
        else:
            print("La calculadora no es cientifica")
    
    def pi(self):
        return math.pi
    