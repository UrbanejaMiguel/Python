a=6
b=12

def sumar(n,m):
    c=n+m
    return c

print(sumar(a,b))
print(sumar(2,3))

def saludar(n, a="Rodriguez"): #Al darle valor al parametro lo convierto en opcional.
    print(f'Hola me llamo {a}, {n} {a}.')

saludar("Miguel","Urbaneja")
saludar("David","Morato")
saludar("Miguel")