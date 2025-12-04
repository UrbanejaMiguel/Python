def main():
    menu ="""####### Elige una frase para hoy ####### 
[1] - Me van a subir el sueldo
[2] - Va a ser un buen dia
[3] - En el gimnasio voy a darlo todo
[4] - Hasta mañana
    """
    print(menu)
    option = input("Selecciona una opción: ")
    if option == "1":
        print("Te han subido el sueldo 300€")
    elif option =="2":
        print("Hoy tienes el guapo subido")
    elif option =="3":
        print("Hoy levantas 140kg en press banca")
    elif option =="4":
        print("Hasta pronto, vuelve cuando quieras")
    else:
        print("Opcion no permitida")
        main()



main()