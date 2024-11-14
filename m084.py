lista=[]
imp=[]
par=[]
while True:
    x=int(input("Digite um numero: "))
    lista.append(x)
    if x%2==0:
        par.append(x)
    else:
        imp.append(x)
    res=str(input('Quer continuar? [S/N] ')).upper()
    if res=="N":
        break
print(f"A sua lista é {lista}")
print(f"Os pares são {par}")
print(f"Os impares são {imp}")