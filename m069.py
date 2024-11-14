print("TABUADA")
while True:
    x=int(input("Digite um numero para ver sua tabuada: "))
    if x<0:
        break
    cont=1
    while cont<11:
        print(f"{x}x{cont}={x*cont}")
        cont+=1
    if x<0:
        break
print("FIM")