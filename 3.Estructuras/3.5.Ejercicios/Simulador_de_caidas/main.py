#Si trabajamos con modulos tiene que haber uno que sea el inicial. Paea marcarlo tenemos que poner el condicional y siempre se pone al final del script
# if __name__ == "__main__":
#     main()

from lib.func import perc_g, get_data, get_client_by_tramo

def main():
    data=get_data()

    menu="""
### Simulador de caidas ###
[1]. Porcentaje global de caidas
[2]. Porcentaje por edad
[x]. Salir de la app
"""
    print(menu)
    option =input("Selecciona una opción: ")
    if option == "1":
        print("Porcentaje global de caidas:",perc_g(data))
    elif option =="2":
        tramo =int(input("Longitud del tramo: "))
        filter_clients = get_client_by_tramo(data,tramo)
        for i in range(len(filter_clients)):
            print(f'Caida {i+1} tramo: {perc_g(filter_clients[i])}')
            print(f'{i+1} tramo: {filter_clients[i]}',"\n")
            
    elif option =="3":
        print("Adiós")
    else:
        print("Opción no permitida.")
        main()




if __name__ == "__main__":
    main()
