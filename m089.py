import random
print("="*30)
print("          MEGA SENA")
print("="*30)
x=int(input("Você quer quantos jogos? "))
jogo=[]
for i in range (0,x):
    for c in range (0,6):
        n=random.randint(0,60)
        while len(jogo)<6:
            if n not in jogo:
                jogo.append(n)
            else:
                n = random.randint(0, 60)
    jogo.sort()
    print(jogo)
    jogo.clear()
