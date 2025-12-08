with open('prueba.txt', 'w') as fitxer:
    fitxer.write("Primera linia")
    fitxer.write("\n")

fitxer = open('prueba.txt', 'w')
fitxer.write("Segona linia")
fitxer.write("\n")
#Lo que passa así es que estem diguent ficant un 'w', que lo que fa es escriure o sobre escriure si hi ha algo ja escrit
#Si lo que volem es que s'escriga baix tindriem que gastar el 'a' per a crear una nova linia i que no se sobreescriga.

fitxer = open('prueba.txt', 'a')
fitxer.write("Tercera linia")
fitxer.write("\n")
#El que pasa es que estem diguent en la 'x' que cree un fitxer que no existix, i en este cas com existeix mos fica la excepció
#Si borrem el fitxer i tornem a provar el que passa es que mos ix el mateix error perque ja l'hem creat abans el fitxer, concretament
#Quan fem el with open prueba.txt 'w' as fitxer.
#Ara he editat la 'x' per una 'a' per a que vaja agreganse i no done errors.

fitxer = open('prueba.txt', 'a')
fitxer.write("Quarta linia")
fitxer.write("\n")

fitxer = open('prueba.txt', 'a')
fitxer.write("Quinta linia")
fitxer.write("\n")

fitxer = open('prueba.txt', 'a')
fitxer.write("Sisena linia")
fitxer.write("\n")


fitxer = open('prueba.txt', 'r')
contingut = fitxer.read()
print(contingut)

fitxer = open('prueba.txt', 'r')
contingut = fitxer.read()

fitxer.close()

fitxer = open('pruebita.txt', 'r')
contingut = fitxer.read()
#El error que ix es el de FileNotFoundError, ja que estem diguent que llisga un arxiu que no existeix.