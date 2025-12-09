import shutil

try:
    shutil.copytree("prova_copiarfeta", "prova_copiar")
    print("Còpia completada!")
except Exception as e:
    print("Error:", e)

#preguntar a Alberto