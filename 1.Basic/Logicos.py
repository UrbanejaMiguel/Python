#Operadores logicos: AND, OR, NOT

#Quiero un numero que sea par y divisible entre 5
a=23
print(f"¿{a} es par y divisible entre 5?", a%2==0 and a%5==0)

#Quiero 1 producto de mas de 40 euros o de menos de 10 euros
price = 30
print(f"¿{price} es mayor que 40 o menor que 10?", price>40 or price<10)
print(f"¿{price} está entre 10 y 40 ?", 10 < price < 40)

#Negacion
print(f"¿{price} es mayor que 40 o menor que 10?", not(10 < price < 40))
