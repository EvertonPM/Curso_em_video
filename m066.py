num=int(input("digite um numero: (999-PARAR)  "))
contador=0
soma=0
while num!=999:
    print(num)
    soma+=num
    contador+=1
    num = int(input("digite um numero: (999-PARAR)   "))
print("Voce pediu {} numeros e a soma deles é {}".format(contador,soma))