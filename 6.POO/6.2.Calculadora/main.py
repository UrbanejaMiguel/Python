from calculadora import Calculadora

casio = Calculadora("Casio",True,cientifica=True)
sum_result=casio.sumar([1.35435,2.235,3.457647,4.65754,5.3543])
red_num=casio.redondeo(sum_result,4)
print(sum_result)
print(red_num)
print(casio.raiz(256))
print(casio.pi())