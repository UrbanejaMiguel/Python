def sumar(a,b): return a+b

def sust(a,b): return a-b

def mult(a,b): return a*b

def div(a,b): return a/b


def mostar_resultado(c,a,b,oper,error):
    if error==False:
        print(f'{a}{oper}{b}={c}')
    else:
        print("Error: Calculo no valido")


def calcular(a,b,oper):
    c=0
    error=False

    if oper == "+":
        c=sumar(a,b)
    elif oper == "-":
        c=sust(a,b)
    elif oper == "*":
        c=mult(a,b)
    elif oper == "/":
        c=div(a,b)
    else:
        error=True

    mostar_resultado(c,a,b,oper,error)