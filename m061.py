import random
x=random.randint(1,10)
y=int(input("Digite um numero de 1 a 10 pra ver se vc acerta: "))
tent=0
while x!=y:
    if y<x:
        print("Mais, tenta outro: ")
        tent+=1
    else:
        print("Menos, tenta outro: ")
        tent += 1
    y = int(input("Digite um numero de 1 a 10 pra ver se vc acerta: "))
print("Acertou na {}° tentativa".format(tent+1))
