
print("Funció en valor per defecte")


def sumar(a, b=10):
    """Funció que suma dos numeros. El segon te valor per defecte 10"""
    return a + b

num1 = float(input("Introdueix el primer numero: "))
respuesta = input("¿Vols introduïr un segon numero? (s/n): ").lower()
if respuesta == 's':
    num2 = float(input("Introdueix el segon numero: "))
    resultado = sumar(num1, num2)
    print(f"Suma de {num1} + {num2} = {resultado}")
else:
    resultado = sumar(num1)
    print(f"Suma de {num1} + 10.0 (valor por defecto) = {resultado}")