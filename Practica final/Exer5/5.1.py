
print("Calculadora de IMC")

peso = float(input("Introdueix el pes en kg: "))
altura = float(input("Introdueix la altura en Metres: "))
imc = peso / (altura ** 2)
print(f"\nTu IMC es: {imc:.2f}")
if imc < 18.5:
    print("El teu IMC está per  baix del pes saludable")
elif 18.5 <= imc <= 24.9:
    print("¡Felicitacions! El teu IMC está en un rang saludable.")
else:
    print("El teu IMC esta per dalt del pes saludable.")