#Son conjuntos ordenados y mutables
list_nom=["Nacho","Miguel","Igor","David"]

#Longitud
print(len(list_nom))

#Acceder a un elemento concreto list[0:n-1]
print(list_nom[0])

for n in list_nom:
    print(n)

#Se puede modificar
list_nom[1]="Anais"
print(list_nom)

#Añadir al final
list_nom.append("Juan")
print(list_nom)

#Añadir en alguna posicion
list_nom.insert(3,"Marika")
print(list_nom)

#Añadir varios elementos a la vez
list_nom.extend(["Miguel","Javier"])
print(list_nom)


#Borrar elementos-->.pop(x) donde x es la posicon (predeterminado x=-1, es decir, borra la ultima)
elem_elmi=list_nom.pop() #Puedo almacenar el elemento eliminado en alguna otra variable--> Basicamente lo que hace es sacarlo de la lista
print(list_nom,elem_elmi)
