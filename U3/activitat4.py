import shutil
import os

try:
    shutil.move('../directori_original/proba.txt', '../directori_nou')
    print("L'arxiu s'ha menejat correctament.")
    fitxers = os.listdir('../directori_nou')

except FileNotFoundError:
    print("Error: No s'ha trobat l'arxiu.")
#Este error ix si no es troba l'arxiu o si no esta en la ruta correcta

except shutil.Error as e:
    print("Error: No s'ha pogut moure l'arxiu.")
#Este error el que fa es mostrar si l'arxiu no s'ha pogut menejar d'un directori a un altre.
