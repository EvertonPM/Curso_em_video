x=int(input("Digite um numero inteiro: "))
y=int(input('''ESCOLHA UMA OPÇÃO DE CONVERSÃO:
1 - BINARIO
2 - HEXADECIMAL
3 - OCTADECIMAL
: '''))
if y==1:
    print("{}".format(bin(x)[2:]))
elif y==2:
    print("{}".format(hex(x)[2:]))
elif y==3:
    print("{}".format(oct(x)[2:]))
else:
    print("valor invalido")