
print("Area d'un cercle")

def calcular_area_cercle(radi):

    pi = 3.14159
    area = pi * (radi ** 2)
    return area

radi_usuario = float(input("Introdueix el radi del ccercle: "))
area_calculada = calcular_area_cercle(radi_usuario)
print(f"El área del cercle amb radi {radi_usuario} es: {area_calculada:.2f}")