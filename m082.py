
lista=[]

for i in range(0,5):
    x=int(input("Digite um valor: "))
    if i==0 or x>lista[-1]:
        lista.append(x)
        print("Adionado no final da lista")
    else:
        pos=0
        while pos<len(lista):
            if x<=lista[pos]:
                lista.insert(pos,x)
                print(f"Adicionado na posição {pos}")
                break
            pos+=1

print(lista)