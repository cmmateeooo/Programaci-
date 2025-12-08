import json

try:
    with open('dades_exercici.json', 'r') as fitxer:
       dades = json.load(fitxer)

    dades_noves = {"Asignatura:" "Programacio"}
    with open('dades_exercici.json', 'w') as fitxer:
        json.dump(dades_noves, fitxer, indent=4)

except FileNotFoundError:
    print("No s'ha trobat l'arxiu")
