ab=[]
fe=[]
to=[]
x=input("Digite um expressão matematica: ")
to.append(x)
for item in to:
    for digito in item:
        if digito=="(":
            ab.append(x)
        elif digito==")":
            fe.append(x)
if len(ab)==len(fe):
    print("expressão valida")
else:
    print("expressão invalida")

 