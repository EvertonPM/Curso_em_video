import random
from random import randint

def sorteia(x,y):
    for i in range(0,x):
        x=random.randint(0,9)
        y.append(x)
def somapar(y):
    soma=0
    for i in y:
        if i%2==0:
            soma+=i
    return soma


#Programa principal
lista=[]
soma=0
sorteia(5,lista)
print(f"Os numeros sorteados foram {lista}. ")
x=somapar(lista)
print(f"A soma dos pares da lista é {x}")