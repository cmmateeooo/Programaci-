nom = input("Introdueix el teu nom: ")
edat = int(input("Introdueix la teua edat: "))

try:

    with open('dades_usuari.txt', 'w') as fitxer:
        fitxer.write((nom) + "\n")
        fitxer.write(str(edat) + "\n")

    with open('dades_usuari.txt', 'r') as fitxer:
        contingut = fitxer.read()
        print(contingut)
    
  
    ciutat = input("A on vius? ")
    with open('dades_usuari.txt', 'a') as fitxer:
        fitxer.write(ciutat)
    
except FileNotFoundError:
    print("No se ha trobat el fitxer.")
except PermissionError:
    print("Accés denegat.")

