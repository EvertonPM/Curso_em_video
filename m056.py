x=str(input("Digite uma frase: "))
y=(x.replace(" ",""))
h=y[::-1]
print("se voce escrever {} ao contrario fica {}".format(y,h))
if y==h:
    print("por isso é um polindromo")
else:
    print("por isso não é um polindromo")
