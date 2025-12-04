#La recursividad es una funcion que se llama a sí misma

#Crear una funcion que me pida un numero de telefono. Este numero tiene que ser un str. Si meto un numero me volverá a pedir el telefono

def get_phone():
    tef=input("Dime tu numero de lelefono: ")
    if tef.isdigit() == False:
        get_phone()
    else:
        print(tef)

get_phone()
