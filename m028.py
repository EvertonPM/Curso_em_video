import random
x=random.randint(1,5)
y=int(input("Digite um numero de 1 a 5 pra ver se vc acerta: "))
if y==x:
    print("voce acertou")
else:
    print("voce errou :( o numero era {}".format(x))