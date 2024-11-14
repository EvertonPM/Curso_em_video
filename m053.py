soma=0
for c in range (1,7):
    x=int(input("Digite um numero inteiro: "))
    if x%2==0:
        soma=soma+x
print("soma dos numeros pares digitados: {} ".format(soma))
