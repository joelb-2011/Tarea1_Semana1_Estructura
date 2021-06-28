class Ejemplo5:
    def __init__(self):
        pass

    def nuevosueldo(self):
        sueldo = float(input("Ingrese el sueldo del empleado: "))
        if sueldo < 600:
            newsueldo = sueldo + sueldo*0.1
        else:
            newsueldo = sueldo
        print("El nuevo sueldo es de: ",format(newsueldo))

eje5 = Ejemplo5()
eje5.nuevosueldo()
