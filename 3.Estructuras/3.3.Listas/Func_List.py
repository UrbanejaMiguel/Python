lista_nombres=["Nacho","Miguel","Igor","David","Miguel","David"]

#Saber cuantos elementos iguale hay
print(lista_nombres.count("David"))

#Invertir una lista
print(lista_nombres[::-1])
#lista_nombres.reverse() tambien lo hace

#Ordebar listas
numeros=[12,33,45,6,47,345,89]
letras=["a","F","D","i","b"]

numeros.sort() #sort() modifica la lista original
print(numeros)

letras.sort(key=str.lower,reverse=False) #Por defecto, primero las mayusculas y luego las minusculas. Despues por orden alfabetico. Con esa key, las valora todas como lower.

#Max y min
print(max(numeros),min(numeros))
