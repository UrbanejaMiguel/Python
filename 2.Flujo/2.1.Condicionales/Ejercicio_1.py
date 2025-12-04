#Le preguntamos la edad a la persona(input) y le dejamos entrar simpre y cuando sea mayor de edad. (Mayor de edad cambia segun el pais)
#Plantear como resolverlo y la mejor forma de hacerlo. Hay varias posibilidades.

edad = int(input("¿Cúal es tu edad? "))

if  edad >= 21:
    print("Puedes pasar")
elif 18 <= edad < 21:
    pais =input("¿En qué país estas? ").strip().lower()
    print(pais)
    if (pais == "eeuu" or pais == "estados unidos"):
        print("No puedes pasar")
    else:
        print("Puedes pasar")
else:
    print("No puedes pasar")