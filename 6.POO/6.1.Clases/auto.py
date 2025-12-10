class Auto:
    #Propiedades(Atributos) --> Variables globales accesibles dentro de su propia clase
    marca = ""
    color = ""
    combustible = ""
    asientos = ""
    ruedas = ""
    encendido=False

    #Metodos --> Funciones que puede realizar mi auto

    #Funcion constructor --> Inicializa el objeto
    #todas las funciones dentro de una clase recibe como primer parameto el propio objeto con la palabra self
    def __init__(self,marca, color,combustible,ruedas): 
                #Recibe todos los parametros que tiene que inicializar (asientos no tiene por que tener valor desde el principio)
        self.marca=marca
        self.color=color
        self.combustible=combustible
        self.ruedas=ruedas

    def arrancar(self):
        self.encendido=True
        print("Vehiculo arrancado")

    def cambiar_color(self,color): #Seter: Funcion que cambia una propiedad
        self.color = color


ferrari = Auto("Ferrari","rojo","Gasolina",4) #Cuando llamamos a Auto() se ejecuta la funcion __init__
topolino=Auto("Fiat","vino","Diesel",4)

print(ferrari.combustible)
print(topolino.marca)
print(ferrari.encendido)
ferrari.arrancar()
print(ferrari.encendido)
ferrari.cambiar_color("Amarillo")
print(ferrari.color)
