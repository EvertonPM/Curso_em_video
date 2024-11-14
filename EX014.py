print("Bem-Vindo a loja do Everton Pereira Medeiros")
valor=float(input("Digite o valor do produto: "))
quant=int(input("Digite a quantidade do produto: "))
preco=valor * quant
#compras entre 200 e 1000 itens
if quant >= 200 and quant <1000:
    print("O valor sem desconto: R${}".format(preco))
    print("O valor com desconto: R${}".format(preco-(preco*5/100)))
#compras entre 1000 e 2000 itens
elif quant >= 1000 and quant <2000:
    print("O valor sem desconto: R${}".format(preco))
    print("O valor com desconto: R${}".format(preco - (preco * 10 / 100)))
#compras acima de 2000 itens
elif quant >= 2000:
    print("O valor sem desconto: R${}".format(preco))
    print("O valor com desconto: R${}".format(preco - (preco * 15 / 100)))
#compras abaixo de 200 itens (SEM DESCONTO)
else:
    print("O valor sem desconto: R${}".format(preco))
    print("Não possui desconto, compre acima de 200 unidades")