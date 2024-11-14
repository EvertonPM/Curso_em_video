print("SISTEMA DO BANCO")
c=float(input("Qual o valor da casa ? "))
s=float(input("Qual seu salario ? "))
a=float(input("Quantos anos pagando ? "))
if c/(a*12)>((s/100)*30):
    print("SEM CAPACIDADE DE PAGAMENTO")
else:
    print("EMPRESTIMO APROVADO")
    print("{}x de {}".format(a*12,c/(a*12)))
#print(c/(a*12))
#print((s/100)*30)


