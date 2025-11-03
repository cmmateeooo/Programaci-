a = [5, 10, 15]
b = 20

if 5 in a:
    b -= 5
elif 10 in a:
    b -= 10
else:
    b -= 15

print(b)

#El codi esta mal fet. 
#Aquest codi primer defineix les variables, on "a" te una llista amb distints valors y "b" soles té el valor 20.
#Despres tenim una estructura de if, elif i else.
#El if comprova si 5 esta en a, si esta fa la operció, en cas que no estaguera pasa a fer el elif i torna a comprovar, i si no esta en el elif tampoc ja pasa a ferse en el else.