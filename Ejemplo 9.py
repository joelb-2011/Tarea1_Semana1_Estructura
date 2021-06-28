class Ejemplo9:
    def __init__(self):
        pass

    def calificacionor(self):
        c1, c2 = 0, 0
        c1 = int(input("Ingrese la primera calificacion: "))
        c2 = int(input("Ingrese la segunda calificacion: "))

        if (c1 >= 90) or (c2 >= 90):
            print("Ha sido aceptado.")
        else:
            print("Ha sido rechazado.")
        
eje9 = Ejemplo9()
eje9.calificacionor()
