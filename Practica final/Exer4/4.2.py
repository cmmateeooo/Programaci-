print("Operador en IN i NOT IN")


frutas = ["pera", "fresa", "banana", "taronja", "meló d'alger"]
print(f"Lista de frutas: {frutas}")

fruta_buscar = input("\nIntrodueix el nom d'una fruta: ").lower()

if fruta_buscar in frutas:
    print(f"¡Sí! {fruta_buscar} está en la llista.")
else:
    print(f"No, {fruta_buscar} no está en la llista.")