notes = [5,7,9,4,6,3,1,8,2,10]

for n in notes:
    print(n)

aprovats = 0
suspesos = 0

print("Notes aprovades:")

for n in notes:
    if n >= 5:
        print(f" -{n}")
        aprovats = aprovats + 1
    else:
        suspesos = suspesos + 1

print("Notes aprovades:")
print(aprovats)
print("Notes suspeses:")
print(suspesos)