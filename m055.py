x=int(input("digite um numero inteiro: "))
cont=0
for c in range(1,x+1):
    if x%c==0:
        print("\033[33m", end=' ')
        cont += 1
    else:
        print("\033[31m", end=' ')
    d = c
    print(d,end=' ')

if cont==2:
    print("\n\033[0mnumero primo")
else:
    print("\n\033[0mnão é numero primo")