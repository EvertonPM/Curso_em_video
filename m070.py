import random
cont=0
while True:
    escolha=input("VOCE QUER PAR OU IMPAR [P/I]  ").upper()
    x=int(input("Digite um numero: "))
    y=random.randint(0,9)
    soma=x+y
    print(f"Voce jogou {x} e o pc jogou {y} = {soma}")
    if soma%2==0:
        if escolha=="P":
            print("VOCE VENCEU")
            cont+=1
        else:
            print("VOCE PERDEU")
            break
    if soma%2!=0:
        if escolha=="I":
            print("VOCE VENCEU")
            cont+=1
        else:
            print("VOCE PERDEU")
            break
print(f"Voce venceu {cont} vezes seguidas")