def sumar(*num):
    c=0
    for n in num:
        c+=n
    print(c)

sumar(1,2)
sumar(1,4,6,7)

#Calcular media
def media(*num):
    c=0
    for n in num:
        c+=n
    media=c/len(num)
    print("La media es",media)
    
media(1,2,3,4,5)
media(0,10)