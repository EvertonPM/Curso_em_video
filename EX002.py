while True:
    a=float(input("Digite um numero: "))
    b=float(input("Digite outro numero: "))
    c=input("Digite qual operação deseja fazer (+,-,*,/) ou s para sair ")
    if c=="+":
        print("a soma é {}".format(a+b))
    elif c=="-":
        print("a diferença é {}".format(a-b))
    elif c=="*":
        print("a multiplicação é {}".format(a*b))
    elif c=="/":
        print("a divisão é {}".format(a/b))
    elif c == "s":
        break
    else:
        print("operação invalida ")
print("Encerrando............")


