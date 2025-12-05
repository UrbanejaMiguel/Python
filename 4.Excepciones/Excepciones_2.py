def calcular():
    try:
        a =int(input("Dime el primer numero: "))
        b =int(input("Dime el segundo numero: "))
        
        c=a/b
        print(c)

    except ValueError:
        print("Has introducido un tipo de dato incorrecto. Deben ser numeros enteros")
        calcular()    
    except ZeroDivisionError:
        print("El divisor no puede ser 0")
        calcular() 
    except:
        print("Error no identificado. Contacte con soporte")

calcular()