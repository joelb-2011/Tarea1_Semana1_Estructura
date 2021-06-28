class Ejemplo7:
    def __init__(self):
        pass

    def numeromayor(self):
        num1, num2, num3 = 0, 0, 0
        nummayor = 0
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        num3 = int(input("Ingrese el tercer número: "))

        if (num1 > num2) and (num1 > num3):
            nummayor = num1
        else:
            if (num2 > num3):
                nummayor = num2
            else:
                nummayor = num3

        print("El numero mayor es: ",format(nummayor))
        
eje7 = Ejemplo7()
eje7.numeromayor()
