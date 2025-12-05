# - filtrar por tipo de siniestro
# - Sacar el pago maximo por fallecimiento

from lib.func import get_data,filter_by_sin,max_paid,types


def main():
    data=get_data()

    menu="""
### Simulador de caidas ###
[1]. Filtrar por tipo de siniestro
[2]. Sacar el pago maximo por fallecimiento
[x]. Salir de la app
"""
    print(menu)
    option =input("Selecciona una opción: ")
    if option == "1":
        s=types(data)
        s_type=input(f"Diga el tipo de siniestro ({s}): ")
        if s_type in s:
            print(f"Datos de los siniestros '{s_type}': ")
            print(filter_by_sin(data,s_type))
        else:
            print("Tipo de siniestro no valido")
            main()
    elif option =="2":
        print(f"Pago maximo: {max_paid(data)}")  
    elif option =="3":
        print("Adiós")
    else:
        print("Opción no permitida.")
        main()




if __name__ == "__main__":
    main()