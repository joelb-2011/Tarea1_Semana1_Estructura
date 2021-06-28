class Ejemplo2:
    def __init__(self):
        pass

    def cantidadtotal(self):
        sb = float(input("Ingrese el sueldo base: "))
        v1 = float(input("Ingrese la cantidad de venta 1: "))
        v2 = float(input("Ingrese la cantidad de venta 2: "))
        v3 = float(input("Ingrese la cantidad de venta 3: "))
        tv = v1+v2+v3
        com = tv*0.1
        trec = sb + com
        print("El total a recibir es de: ",format(trec))

eje2 = Ejemplo2()
eje2.cantidadtotal()
