x=float(input("Qual seu salario? "))
if x>=1250:
    print("seu nome salario será: {}".format(x+(x/100)*10))
else:
    print("seu nome salario será: {}".format(x + (x / 100) * 15))