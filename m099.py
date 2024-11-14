def cont(a,b,c):
    print(f'\nContagem de {a} a {b} de {c} em {c}:')
    if a<b:
        for i in range(a, b+1, c):
            print(i, end=' ')
            sleep(0.3)
    else:
        for i in range(a, b -1, c):
            print(i, end=' ')
            sleep(0.3)



from time import sleep
print('Contagem de 0 a 10:')
for i in range(0,11):
    print(i,end=' ')
    sleep(0.3)
sleep(0.4)
print('\nContagem de 10 a 0 de 2 em 2:')
for i in range(10,-1,-2):
    print(i,end=' ')
    sleep(0.3)

a=int(input('\nDigite o numero que inicia a contagem: '))
b=int(input('Digite o numero que finaliza a contagem: '))
c=int(input('Digite o intervalo da contagem: '))
if c < 0:
    c = c+(2*(-c))
if a>b:
    c=-c

cont(a,b,c)