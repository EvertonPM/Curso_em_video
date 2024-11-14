lista=[]
while True:
    x=int(input("Digite um valor: "))
    if x in lista:
        print("Valor duplicado...")
        continue
    lista.append(x)
    p=input("Deseja continuar (S/N): ").upper()
    if p=="N":
        break
    elif p=="S":
        continue
lista.sort()
print(lista)