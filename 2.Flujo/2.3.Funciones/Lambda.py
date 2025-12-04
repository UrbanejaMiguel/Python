#Una funcion lambda es una funcion abrebiada

#Funcion normal (declarativa)
def get_name(n,s,j):
    r=f'{n} {s} - {j}'
    print(r)

#Funcion en lambda (expresiva)
get_name_l= lambda n,s,j: print(f'{n} {s} - {j}')

