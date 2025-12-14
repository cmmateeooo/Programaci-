try:
     num1 = int(input("Introdueix el primer numero:"))
     num2 = int(input("Introdueix el segon numero:"))
     res = num1/num2
     print(f"El resultat de la divisió és: {res}")
except ZeroDivisionError:
     print("Error: No es pot divir entre zero.")