x=int(input("Digite um numero: "))
y=int(input("Digite outro numero: "))
while True:
    print("[1] somar")
    print("[2] multiplicar")
    print("[3] maior")
    print("[4] novos numeros")
    print("[5] sair do programa")
    o=int(input("Escolha uma opção: "))
    if o==1:
        print("A soma de {} + {} é {}".format(x,y,x+y))
    elif o==2:
        print("A multiplicação de {} * {} é {}".format(x, y, x * y))
    elif o==3:
        if x>y:
            print("o maior é {}".format(x))
        else:
            print("o maior é {}".format(y))
    elif o==4:
        x = int(input("Digite um numero: "))
        y = int(input("Digite outro numero: "))
    elif o==5:
        break
    else:
        print("opção invalida")
print("Programa encerrado")
