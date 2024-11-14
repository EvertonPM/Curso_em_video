matriz=[]
linha=[]
par=0
soma=0
m=0
for a in range (0,3):
    for b in range (0,3):
        x=int(input(f"Digite o valor para [{a}][{b}]: "))
        linha.append(x)
        matriz.append(linha[:])
        linha.clear()
        if x%2==0:
            par+=x
        if b==2:
            soma+=x
        if a==1:
            if x>m:
                m=x
print("",matriz[0],end=" ")
print(matriz[1],end=" ")
print(matriz[2],end=" ")
print("\n",matriz[3],end=" ")
print(matriz[4],end=" ")
print(matriz[5],end=" ")
print("\n",matriz[6],end=" ")
print(matriz[7],end=" ")
print(matriz[8],end=" ")
print("+"*30)
print(f"A soma dos pares é {par}")
print(f"A soma da 3° coluna é {soma}")
print(f"O maior valor da 2° linha é {m}")