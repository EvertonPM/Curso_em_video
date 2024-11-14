soma=0
cont=0
while True:
    x = int(input("Digite um numero:  "))
    if x==999:
        break
    soma += x
    cont += 1
print(f"foram digitados {cont} numeros e a soma é {soma}")