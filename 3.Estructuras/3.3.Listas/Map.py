#map() te ejecuta una funcion a cada elemento del array/list
numeros=[1,2,3,4,5,6,7]
numeros_3=list(map(lambda n:n*3,numeros))
print(numeros_3)

#limpiar base de datos (normalizarla)-->Quitar espacios por delante y por detras, acentos y pasar a title
clientes=["CArlos Perez","Raúl lópez  ","  maría Pombo "]

def sintildes(n):
    n=n.lower()
    n=n.replace('á',"a")
    n=n.replace('é',"e")
    n=n.replace('í',"i")
    n=n.replace('ó',"o")
    n=n.replace('ú',"u")
    return n


clientes_norm=list(map(lambda nombre: sintildes(nombre).strip().title(),clientes))
print(clientes_norm)
