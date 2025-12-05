#Una excepcion es un condicional internamente
#Se usan los comandos: try/except
def printNum():
    try:
        a =int(input("Dime el primer numero: "))
        b =int(input("Dime el segundo numero: "))
        print(a,b)
    except ValueError:
        print("Has introducido un tipo de dato incorrecto. Deben ser numeros enteros")
        printNum()
            
printNum()