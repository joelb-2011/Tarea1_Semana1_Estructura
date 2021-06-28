class Ejemplo10:
    def __init__(self):
        pass

    def sumaFor(self):
        i = 1
        suma = 0

        for i in range(5):
            suma = suma + i * i
            i += 1

        print("Suma es: ",format(suma))
        
eje10 = Ejemplo10()
eje10.sumaFor()
