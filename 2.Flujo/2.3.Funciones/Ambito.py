#Una variable es local solo dentro de una funcion y global fuera de cualquier funcion.

frase="El resultado es: " #-->Variable global

if frase != "":
    age =23 #-->Variable global
else:
    age=0

def potencia(b,e):
    c=b**e #--> Variable local
    print(c)

