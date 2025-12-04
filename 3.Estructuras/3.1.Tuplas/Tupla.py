#Una tupla es una lista de elementos inmutable

tupla=("Juan",32,True)

print(tupla, len(tupla))

print (tupla[1],tupla[-2])

tupla_2=("Juan", "Pepe", "Maria", "Alba", "Lucia", "Rodrigo")

#Copias de una tupla
tupla_mujeres= tupla_2[2:5]
print(tupla_mujeres)

#Recorrer una tupla
for i in tupla_2:
    print(i)

#Eliminar una tupla
del tupla
