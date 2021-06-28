class Ejemplo8:
    def __init__(self):
        pass

    def calificacionand(self):
        c1, c2 = 0, 0
        c1 = int(input("Ingrese la primera calificacion: "))
        c2 = int(input("Ingrese la segunda calificacion: "))

        if (c1 >= 80) and (c2 >= 80):
            print("Ha sido aceptado.")
        else:
            print("Ha sido rechazado.")
        
eje8 = Ejemplo8()
eje8.calificacionand()
