print("Bem-vindos ao pet shop do Everton Pereira Medeiros")

try:
    p = float(input("Qual o peso do cachorro? "))
    while p >= 50:
        print("Digite um peso valido")
        p = float(input("Qual o peso do cachorro? "))
    print(p, "  OK")
except ValueError as error:
    print("Digite um peso valido")
    p = float(input("Qual o peso do cachorro? "))
p1=0
if p<3:
    p1=40
elif p>=3 and p<10:
    p1=50
elif p>=10 and p<30:
    p1=60
elif p>=30 and p<50:
    p1=70




print(" ")
print("pelo curto: C")
print("pelo medio: M")
print("pelo longo: L")
x = input("Digite a letra correspondente ao pelo do cachorro: ")
while x != "C" and x != "M" and x != "L" and x != "c" and x != "m" and x != "l":
        print("Letra invalida")
        x = input("Digite a letra correspondente ao pelo do cachorro: ")
print(x, "  OK")

m1=0
if x=="c" or x=="C":
    m1=1
if x=="m" or x=="M":
    m1=1.5
if x=="l" or x=="L":
    m1=2

s=0
while True:
    print(" ")
    print("1 - Corte de unha - R$10,00")
    print("2 - Escovar os dentes - R$12,00")
    print("3 - Limpeza de orelha - R$15,00")
    print("0 - Não desejo mais nada")
    a=int(input("Deseja adicionar mais algum serviço?  "))
    if a ==1:
        s=s+10
    if a ==2:
        s=s+12
    if a ==3:
        s=s+15
    elif a==0:
        break
print("Total a pagar R${} (peso:{} * pelo:{} + adicional(is):{})".format((p1*m1+s),p1,m1,s))