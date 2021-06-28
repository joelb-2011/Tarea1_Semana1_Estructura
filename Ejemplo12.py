class Ejemplo12:
    def __init__(self):
        pass

    def Whilenum(self):
        suma, prod, num = 0, 0, 0

        suma = 0
        prod = 1

        num = int(input("Ingrese un numero: "))
        while (num > 0):
            suma = suma + num
            prod = prod * num
            num = int(input("Ingrese un numero: "))
            
        print("El total de la suma es: ",format(suma))
        print("El total del producto es: ",format(prod))
        
eje12 = Ejemplo12()
eje12.Whilenum()
