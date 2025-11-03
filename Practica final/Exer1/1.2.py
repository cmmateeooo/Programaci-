print("Comparar numeros")
num_a = float(input("Introdueix el primer numero:  "))
num_b = float(input("Introdueix el segon numero: "))
if num_a > num_b:
    print(f"{num_a} es major que {num_b}")
elif num_a == num_b:
    print(f"{num_a} es igual a {num_b}")
else:
    print(f"{num_a} es menor que {num_b}")