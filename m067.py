x=0
contador=0
soma=0
maior=0
menor=999999
while x!="N":
    num=int(input("Digite um numero: "))
    x=input("Quer mais numeros [S/N]").upper()
    contador+=1
    soma+=num
    if num>maior:
        maior=num
    elif num<menor:
        menor=num


print("A média dos numeros é {}".format(soma/contador))
print("o maior é {} e o menor é {}".format(maior,menor))

