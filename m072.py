total=0
maismil=0
menor=0
barato=" "
contador=0
while True:
    prod=str(input("Qual o produto: "))
    preco=float(input("Qual o valor: "))
    total+=preco
    contador+=1
    if preco>1000:
        maismil+=1
    if contador==1:
        menor=preco
        barato = prod
    if preco < menor:
        menor=preco
        barato=prod
    cont=str(input("Voce quer continuar [S/N]: ")).upper()
    while cont not in "NS":
        cont = str(input("Voce quer continuar [S/N]: ")).upper()
    if cont=="N":
        break
print(f"Voce gastou R${total:.2f}")
print(f"{maismil} produtos foram acima de R$1000.00")
print(f"{barato} foi o produto mais barato, custando {menor}")