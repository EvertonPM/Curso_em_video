lista=[]
for i in range(0,5):
    add=int(input(f"Digite um valor para a posição {i}: "))
    lista.append(add)
print(lista)
menor=(min(lista))
maior=(max(lista))
print(f"o menor valor foi {menor}, nas posições {lista.index(menor)}",end=' ')

cont = (lista.count(menor))-1

while cont >0:
    print("..",lista.index(menor,lista.index(menor)+(cont)),end=" ")
    cont-=1
#print(f"o maior valor foi {maior}, nas posições {lista.index(maior)}")

