
print("Operadors aritmétics")


x = 10
y = 5


print(f"x = {x}, y = {y}")
print(f"Suma: x + y = {x + y}")
print(f"Resta: x - y = {x - y}")
print(f"Multiplicación: x * y = {x * y}")
print(f"División: x / y = {x / y}")
print(f"Módulo: x % y = {x % y}")

print(f"¿x es mayor que y? {x > y}")
print(f"¿x es igual a y? {x == y}")

resultado_logico = (x > y) and (x % 2 == 0)
print(f"¿x es major que y Y el módul de x entre 2 es 0? {resultado_logico}")