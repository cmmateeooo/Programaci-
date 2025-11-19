suma = 0
comptador_parells = 0

for i in range (1, 4):
    if i % 2 == 0:
        suma = suma + i
        comptador_parells = comptador_parells + 1
    else:
        suma = suma - 1

print("i"+str (i))        
print("suma"+str(suma))
print("comptador_parells"+str(comptador_parells))


print("Resultat final")
print("suma =", suma)
print("comptador_parells =", comptador_parells)

#Iteració(i) | Condició i % 2 == 0 | Valor de suma | Valor de comptador parells |
#1           | False               | -1            | 0                          |
#2           | True                |  1            | 1                          |
#3           | False               |  0            | 1                          |
#4           | True                |  4            | 2                          |
#5           | False               |  3            | 2                          |
#6           | True                |  9            | 3                          |