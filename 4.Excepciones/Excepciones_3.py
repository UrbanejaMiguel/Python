def get_number_by_index(lista):
    try:
        indice=int(input(f"Ingresa un indice (valor entre {(0,len(lista)-1)}): "))
        print(lista[indice])
    except ValueError:
        print("Has introducido un tipo de dato incorrecto. Deben ser numeros enteros")
        
    except IndexError:
        print(f"La lista no tiene tantos numeros. El maximo es {len(lista)-1}")
        
    except:
        print("Error no identificado. Contacte con soporte")    

    finally:
        #Ocurre simpre al final hayamos fallado o no
        print("El acceso ha terminado. Ejecutalo de nuevo si quieres hacer otro")

list_num=[1,2,3,4,5,56,743,32,34,546,456,2,6,8,9,0,6,4,43]

get_number_by_index(list_num)