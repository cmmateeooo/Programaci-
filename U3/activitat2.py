try:
    with open ('cuotes.txt', 'w') as fitxer:
        fitxer.write("Cuota carnet: 300€.")

    with open ('practiques.txt', 'w') as fitxer:
        fitxer.write('Practiques necessaries: 5.')

except FileNotFoundError:
    print("Error: No s'ha trobat el arxiu")

try:
    with open ('cuotes.txt', 'r') as fitxer:
        cuotes = fitxer.read()
        print(cuotes)


    with open ('practiques.txt', 'r') as fitxer:
        practiques = fitxer.read()
        print(practiques)


    with open ('concatenació.txt', 'w') as fitxer_nou:
        fitxer_nou.write(cuotes)
        fitxer_nou.write("\n")
        fitxer_nou.write(practiques)

except FileNotFoundError:
    print("Error: No s'ha trobat un dels arxius originals'.")

except PermissionError:
    print("Error: No tens permís per vore el contingut del fitxer.")
