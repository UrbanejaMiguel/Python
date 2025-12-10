
from lib.poliza import Poliza


def main():
    menu="""
### Analisis de polizas ###
[1]. Calcular prima media
[2]. Calcular suma asegurada total
[3]. Calcular edad media
[x]. Salir de la app
"""
    print(menu)
    option =input("Selecciona una opción: ")
    if option == "1":
        cartera = Poliza("cartera_polizas","csv")
    elif option=="2":
        cartera = Poliza("cartera_polizas","csv")
    elif option == "3":
        cartera = Poliza("cartera_polizas","csv")
    elif option =="x":
        print("Hasta pronto")
    else:
        print("Opcion no valida")
        main()



if __name__ == "__main__":
    main()