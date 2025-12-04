#For
#Quiero imprimer 100 numeros
cantidad = 100
for i in range(cantidad): #Desde 0 a 99
    print(i)

for i in range(1,cantidad+1): #Desde 1 a 100
    print(i)

for i in range(0, cantidad+1,2):
    print(i)

#Los bucles tambien tienen else. Se ejecuta el else cuando se ha ejecutado TODO(de 0 a n) el bucle
for i in range(1,10):
    print(f'Valor: {i}')
else:
    print("El bucle ha terminado")

for i in range(1,10,2):
    if i % 2 == 0:
        break
        print(f'Valor par encontrado: {i}')
else:
    print("Valor par no encontrado")

texto= "Solo sé que no se nada"
print(len(texto))

for i in texto:
    print(i)

for i in range(len(texto)):
    if not texto[i]==" ":
        print(texto[i])

#While
i = 1

while i<=10:
    print(i)
    i+=1


#Break --> Para el bucle
#Continue --> Cambia de iteracion sin completar el bucle

for i in range(1, 10):
    if i %2==0:
        print(i)

for i in range(1,10):
    if i %2!=0:
        continue
    print(i)

for i in range(1,10):
    if i % 5==0:
        print(i)
        break
