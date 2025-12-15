# Opcion 1: import lib.func as fn
from lib.func import sumar, potencia

def main():
    suma = sumar(1,2)
    exp = potencia(2,3)
    print(suma,exp)


if __name__ == '__main__':
    main()
