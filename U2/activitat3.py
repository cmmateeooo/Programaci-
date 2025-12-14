num = int(input("Escriu un numero: "))
contador = 0

while num != 0:
    if num % 2 == 0:
        contador += 1
    num = int(input("Un altre numero: "))

print("Tinc " + str(contador) + " numeros parells")

