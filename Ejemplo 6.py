class Ejemplo6:
    def __init__(self):
        pass

    def pagohoras(self):
        horat, he, het = 0, 0, 0
        pagohora, phe, pagototal = 0, 0, 0
        horat = int(input("Ingrese las horas trabajadas: "))
        pagohora = float(input("Ingrese el pago por hora normal: "))
        if horat > 40:
            he = horat - 40
            if he > 8:
                het = he - 8
                phe = pagohora * 2 * 8 + pagohora * 3 * het
            else:
                phe = pagohora * 2 * he
            pagototal = pagohora * 40 + phe
        else:
            pagototal = pagohora * horat
        print("El pago total de las horas trabajadas es de: ",format(pagototal))

eje6 = Ejemplo6()
eje6.pagohoras()
