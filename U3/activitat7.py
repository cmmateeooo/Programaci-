import csv

with open('dades_exercici.csv', 'r') as fitxer:
    lector_csv = csv.reader(fitxer)
    for fila in lector_csv:
             print(fila)

dades =  [["Nom:", "Edat:", "Curs"],["Mateo", "17", "2nSMX-A"]]
with open('dades_exercici.csv', 'a', newline='') as fitxer:
    escriptor_csv = csv.writer(fitxer)
    escriptor_csv.writerows(dades)