notes = [5,7,9,4,6,3,1,8,2,10]

#Variables de les notes abans del bucle.

aprovats = 0
suspesos = 0

print("Llista de notes:")

#Bucle for per fer recompter de aprovats i suspesos.

for n in notes:
    print(n)

    if n >= 5:
        aprovats = aprovats + 1
    else:
        suspesos = suspesos + 1
print("Total d'aprovats")
print(aprovats)
print("Total de suspeses")
print(suspesos)