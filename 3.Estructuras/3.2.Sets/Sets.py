#Conjunto de datos ordenados(aleatorios) y unicos
lista=[1,1,1,1,1,2,2,2,5,5,56,34,2,22,1]
mi_set={1,1,1,1,1,2,2,2,5,5,56,34,2,22,1}

print(lista,"\n",mi_set) #Los sets están desordenados

frutas ={"Manzana","Naranja","Pera","Platano"}
print(frutas) 


#Ejemplo: lista de comunidades
lista_ci=["Madrid", "Barcelona","Coruña","Sevilla","Madrid","sevilla","oviedo"]

for i in range(len(lista_ci)):
    lista_ci[i]= lista_ci[i].capitalize() #Primera letra en mayuscula

lista_ci_unicas= sorted(list(set(lista_ci)))
print(lista_ci_unicas)


#Los sets son mutables
frutas.add("Melón") #Solo añade un elemento a elemento
print(frutas)
frutas.remove("Naranja") #Si no existe "Naranja" da error
print(frutas)
frutas.discard("Piña") #No da error si no existe el elemento
print(frutas)

#Vaciar un set
frutas.clear

#Eliminar set
del frutas

