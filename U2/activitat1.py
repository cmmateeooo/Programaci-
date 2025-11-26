temperatura= float(input("Passam la temperatura"))
nuvolat= input("Esta nuvolat? (si/no): ").strip().lower()

if temperatura < 0:
    print("Fa un fred polar!")
elif 0 <= temperatura <= 15:
    if nuvolat == "si":
        print("Fa fred i el dia esta trist.")
    elif nuvolat == "no":
        print("Fa fresqueta però el sol alegra el dia")
    else:
        print("Resposta no valida per a nuvolat.")
elif 16 <= temperatura <= 25
if nuvolat=="si":
    print("Temperatura agradable, però potser ploga.")
    elif nuvolat =="si":
        print("Dia perfecte per a ixir a passejar.")
        else:
            print("Resposta no vàlida per a nuvolat.")
elif 26 <= temperatura <= 35:
    print("Fa calor, millor busca ombra.")
else: # temperatura > 35
     if nuvolat =="si":
        print("Calor i humitat...una combinació")
     elif nuvolat =="no":
        print("Fa un calor que fon les pedres!")
     else:
        print("Resposta no valida.")