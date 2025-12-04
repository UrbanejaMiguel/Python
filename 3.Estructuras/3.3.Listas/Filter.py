numeros=[1,4,7,12,67,23,97,34,67,34]

impares=[]
for n in numeros: #Manera bruta
    if n%2!=0:
        impares.append(n)
print(impares)

pares=list(filter(lambda numero: numero%2==0,numeros)) #Filter es una clase que es un objeto por tanto lo convierto en lista
print(pares)

animales=["Leon","gato","perro","Cuervo","Aguila","Colibri","hipopotamo","TIGRE"]
animales_sort=list(filter(lambda animal:animal[0].isupper(),animales))
print(animales_sort)

animales_sort2=list(filter(lambda animal:animal.istitle(),animales))
print(animales_sort2)