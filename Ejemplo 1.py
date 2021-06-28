class Ejemplo1:
    def __init__(self):
        pass

    def pagototal(self):
        tc = float(input("Ingrese el total de compra: "))
        des = tc*0.15
        pago = tc - des
        print("El total de compra es: ",format(tc))
        print("El descuento es de: ",format(des))
        print("El valor a pagar es de: ",format(pago))

eje1 = Ejemplo1()
eje1.pagototal()
