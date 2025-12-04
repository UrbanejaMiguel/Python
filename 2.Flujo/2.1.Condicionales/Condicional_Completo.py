mark = float(input("Dime tu nota: "))

#Condicional anidado
if 5<=mark<=10:
    print("Estudiante aprobado")
elif 0<=mark<=10:
    print("Estudiante suspenso")
else:
    print("ERROR")


#Condicional abreviado --> Condiconal simple con secuencia de escape (Binario)
light_status= False
msg=""

if not light_status:
    msg="No está encendida"
else:
    msg="Está apaada"

print(msg)

#Operador ternario --> Una variable cambia su valor dependiendo de que condicion cumpla
light_status_2= False
msg_2 = "Apagado" if not light_status_2 else "Encendido"
print(msg_2)