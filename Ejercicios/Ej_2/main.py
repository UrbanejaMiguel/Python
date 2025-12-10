
from lib.poliza import Poliza


def main():
    menu="""
### Analisis de polizas ###
[1]. Calcular prima media
[2]. Calcular suma asegurada total
[3]. Calcular edad media
[4]. Crear dataset filtrado
[5]. Calcular VA de primas
[x]. Salir de la app
"""
    print(menu)
    option =input("Selecciona una opción: ")
    if option == "1":
        cartera = Poliza("cartera_polizas","csv")
        prima_media= cartera.promedio("prima_anual")
        print(f"La prima anual media de la cartera es {prima_media}") 
    elif option=="2":
        cartera = Poliza("cartera_polizas","csv")
        total_sa= cartera.total_SA("suma_asegurada")
        print(f"La suma asegurada total de la cartera es {total_sa:,}") 
    elif option == "3":
        cartera = Poliza("cartera_polizas","csv")
        edad_media= cartera.promedio("edad")
        print(f"La edad media de la cartera es {edad_media}") 
    elif option == "4":
        cartera = Poliza("cartera_polizas","csv")
        df=cartera.df()
        print(f"La nueva cartera es: \n {df}") 
    elif option == "5":
        cartera = Poliza("cartera_polizas","csv")
        va=cartera.va()
        print(f"El valor actual de las primas es \n {va}") 
    elif option =="x":
        print("Hasta pronto")
    else:
        print("Opcion no valida")
        main()

if __name__ == "__main__":
    main()