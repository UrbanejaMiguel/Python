#La calculadora pedirá dos numeros por pantalla y un tipo de calculo(+,-,*) e imprimirá el resultado

# import Lib.functions as fun
from Lib.functions import calcular #Solo me hace falta la funcion calcular porque las demas se ejecutan internamente

def main():
    a=float(input("Primer numero: "))
    b=float(input("Segundo numero: "))
    oper=input("Operador (+,-,*,/): ")
    calcular(a,b,oper)

if __name__=="__main__": #Solo ejecuta si este .py es el modulo principal.
    main()
