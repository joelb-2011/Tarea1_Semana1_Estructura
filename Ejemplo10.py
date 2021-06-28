class Ejemplo10:
    def __init__(self):
        pass

    def sumaFor(self):
        suma = 0

        for i in [1,100,1]:
            suma = suma + i * i

        print("Suma es: ",format(suma))
        
eje10 = Ejemplo10()
eje10.sumaFor()
