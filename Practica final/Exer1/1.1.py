print ("Calculadora Simple")
num1 = int(input("Introdueix un numero enter: "))
num2 = float(input("Introdueix un numero decimal: "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
division_entera = num1 // num2
modulo = num1 % num2
print(f"\nResultados:")
print(f"Suma: {num1} + {num2} = {suma}")
print(f"Resta: {num1} - {num2} = {resta}")
print(f"Multiplicación: {num1} * {num2} = {multiplicacion}")
print(f"División: {num1} / {num2} = {division}")
print(f"División entera: {num1} // {num2} = {division_entera}")
print(f"Módulo: {num1} % {num2} = {modulo}")
mensaje = "El resultat de sumar " + str(num1) + " y " + str(num2) + " es " + str(suma)
print(f"\nConcatenación: {mensaje}")