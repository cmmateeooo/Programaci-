elements = ["poma", "pera", "taronja", "plàtan"]
selecció = None
try:
    pos = int(input("Fica un numero del 0-3:"))
    selecció = elements[pos]
    print(f"L'element en la posició {pos} és: {selecció}")
except ValueError:
    print("Has d'introduïr un número enter:")
except IndexError:
    print("La posicició es incorrecta")
finally:
    print("Intent completat.")
