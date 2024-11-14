todos=[]
dados=[]
cont=0
while True:
    n=input("Nome: ")
    p=float(input("Peso: "))
    dados.append(n)
    dados.append(p)
    todos.append(dados[:])
    dados.clear()
    cont+=1
    res=input("Deseja continuar? [S/N]").upper()
    if res == "N":
        break
print(f"Foram cadastradas {cont} pessoas")
maior=0
nmaior=" "
c=0
for p in todos:
    if p[1]>=maior:
        maior=p[1]
        nmaior=p[0]
menor=999999
nmenor=" "
for p in todos:
    if p[1]<=menor:
        menor=p[1]
        nmenor=p[0]
print(f"Os mais pesados são",end=" ")
for p in todos:
    if p[1]==maior:
        print(f"[{p[0]}]",end=" ")
print(f"\nOs mais leves são", end=" ")
for p in todos:
    if p[1]==menor:
        print(f"[{p[0]}]",end=" ")