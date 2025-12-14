import json

try:
    # Leer el archivo JSON
    with open('dades_exercici.json', 'r') as fitxer:
        dades = json.load(fitxer)

    # Añadir una nueva asignatura
    dades["assignatures"].append("Programacio")

    # Guardar los cambios en el mismo archivo
    with open('dades_exercici.json', 'w') as fitxer:
        json.dump(dades, fitxer, indent=4)

except FileNotFoundError:
    print("No s'ha trobat l'arxiu")

except json.JSONDecodeError:
    print("El fitxer no conté un JSON vàlid")
