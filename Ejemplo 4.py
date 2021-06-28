class Ejemplo4:
    def __init__(self):
        pass

    def calificacion(self):
        cal = float(input("Ingrese la calificacion del alumno: "))
        if cal >= 7:
            print("El alumno ha sido aprobado.")
        else:
            print("El alumno ha sido reprobado.")

eje4 = Ejemplo4()
eje4.calificacion()
