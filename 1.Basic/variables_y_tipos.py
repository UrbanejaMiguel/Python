"""
Así se escribe un texto sin poner siempre comillas
"""
#Comentario de una sola linea

#Tipos de datos --> Python es debilmente tipados
name_student ="Juan"
name_student=3
print(name_student,"Tipo:", type(name_student))
#No linkea tipos a una variable

age = 29
print(age, type(age))

#String
text ="En un lugar de la mancha"
text_2= 'Hola como estas?'
print(text,text_2)

text_multiline= """
Aqui puedo escribir varias lineas de texto.
Valen tambien las comillas simples.
"""
print(text_multiline)

#Funcion fprint
name="Miguel"
surname= "Urbaneja"
name_complete= name + " " + surname
print(name_complete)

name_complete_fprint = f"{name} {surname} tiene {age} años"
print(name_complete_fprint)

#Numerics --> int, float
age_student = 34 #int
grades = -24 #int
price = 39.90 #float
print(age_student,type(age_student),grades,type(grades),price,type(price))

#Booleano
status_order = True
order = False
