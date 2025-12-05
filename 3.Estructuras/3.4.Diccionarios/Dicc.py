#Un diccionario es un conjunto de datos que no tienen posicion. En otoros lenguajes se llaman arrays asociativos
#Funcioan con el concepto: Clave --> Valor

clientes={
    "Nombre": "Miguel",
    "Edad": 29,
    "Riesgo": 0.30,
    "Activo": True
}

print(clientes)
print(clientes["Riesgo"])

#Modificar un valor del diccionario
clientes["Edad"]=30
print(clientes)

#Recorrer el diccionario
for clave,valor in clientes.items(): #Items te da una lista con clave, valor
    print(clave,valor)

for valor in clientes.values(): #Values te devuelve el valor
    print(valor)

for clave in clientes.keys(): #Keys te da la clave
    print(clave)

#Se puede añadir claves nuevas
clientes["Direccion"]="xxxxx"
print(clientes)

#Se puede eliminar claves
clientes.pop("Edad")
print(clientes)

clientes.clear
clientes = [

    {'id': 1, 'name': 'Juan', 'genero': 'm', 'capital_bruto': '35000', 'age': 30, 'q_ext': 0.2},

    {'id': 2, 'name': 'Maria', 'genero': 'f', 'capital_bruto': '40000', 'age': 23, 'q_ext': 0.1},

    {'id': 3, 'name': 'Pedro', 'genero': 'm', 'capital_bruto': '52000', 'age': 27, 'q_ext': 0.15},

    {'id': 4, 'name': 'Lucia', 'genero': 'f', 'capital_bruto': '46000', 'age': 32, 'q_ext': 0.3},

    {'id': 5, 'name': 'Ana', 'genero': 'f', 'capital_bruto': '38000', 'age': 28, 'q_ext': 0.05},

    {'id': 6, 'name': 'Carlos', 'genero': 'm', 'capital_bruto': '60000', 'age': 40, 'q_ext': 0.25},

    {'id': 7, 'name': 'Luis', 'genero': 'm', 'capital_bruto': '42000', 'age': 35, 'q_ext': 0.12},

    {'id': 8, 'name': 'Sofia', 'genero': 'f', 'capital_bruto': '33000', 'age': 22, 'q_ext': 0.08},

    {'id': 9, 'name': 'Elena', 'genero': 'f', 'capital_bruto': '55000', 'age': 29, 'q_ext': 0.18},

    {'id': 10,'name': 'Miguel','genero': 'm', 'capital_bruto': '48000', 'age': 31, 'q_ext': 0.22}

]

cliente_filt=[]
filt=0.1
for cliente in clientes:
    if cliente["q_ext"]<=filt:
        cliente_filt.append(cliente)

print(cliente_filt)
print("-"*40)
#Resuelto por el profesor
def get_client_by_qext(list,q_min,q_max):
    cliente_filt_2=[]
    for cliente_2 in list:
        if q_min<=cliente_2["q_ext"]<=q_max:
            cliente_filt_2.append(cliente_2)
    return(cliente_filt_2)
print(get_client_by_qext(clientes,0.1,0.1))
print("-"*40)
#Opcion 2
def get_cliente_by_qext_2(lista,q_min,q_max):
    return list(filter(lambda client: q_min<=client["q_ext"]<=q_max,lista))
  
print(get_cliente_by_qext_2(clientes,0.1,0.1))
print("-"*40)
#Obtener clientes con mas de 30 años y un riesgo por encima del 30%
def get_client_by_age(lista,age_min,age_max):
    return list(filter(lambda client: age_min<=client["age"]<=age_max,lista))

print(get_client_by_age(clientes,30,999))
print("-"*40)
