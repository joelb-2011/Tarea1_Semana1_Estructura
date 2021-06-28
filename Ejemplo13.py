class Ejemplo13:
    def __init__(self):
        pass

    def factorial(self):
        
        num = int(input("Ingrese cantidad de numeros: "))

        for i in range(num):
            numero = int(input("Ingrese numero: "))
            fact = 1
            for j in range(numero,0,-1):
                fact=fact*j
            print("Factorial del numero: ",format(numero))
            print("Es de: ",format(fact))
        
eje13 = Ejemplo13()
eje13.factorial()
