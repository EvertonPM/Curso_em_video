lista=[]
cont=0
while True:
    x=int(input("Digite um valor: "))
    lista.append(x)
    cont+=1
    r=input("Quer continuar (S/N): ").upper()
    if r=="N":
        break
print(f"sua lista possui {cont} elementos")
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print("A lista possui o numero 5")
else:
    print("A lista NÃO possui o numero 5")