elements = ["poma", "pera", "taronja", "plàtan"]
selecció = None
try:
     pos = int(input("Introdueix una posició (0-3):"))
     assert 0 <= pos <= 3,print("Error: la posició ha d'estar entre 0 i 3")
     selecció = elements[pos]
     print(f"L'element en la posició {pos} és {selecció}")
except AssertionError:
     print("Error en l'asserció")
finally:
     print("Comprovació finalitzada")
     print(f"La longitud de la llista es: {len(elements)}")
     selecció = None
     print(f"Selecció reiniciada a:  {selecció}.")