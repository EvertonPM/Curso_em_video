print("=====BOCA DE DROGA DO JHONATHAN=====")
valor=float(input("Quando deu sua droga: "))
print("====OPÇÕES DE PAGAMENTO====")
print("[1] - dinheiro/pix")
print("[2] - a vista no cartão")
print("[3] - até 2x no crédito")
print("[4] - de 3x a 12x no crédito")
pag=int(input("Escolha um opção de pagamento: "))
if pag==1:
    print("o valor da sua é R${:.2f} você receberá 10% de desconto, valor final R${:.2f}".format(valor,(valor-(valor/100*10))))
elif pag==2:
    print("o valor da sua é R${:.2f} você receberá 5% de desconto, valor final R${:.2f}".format(valor,(valor-(valor/100*5))))
elif pag==3:
    prc=int(input("1x ou 2x: "))
    if prc==1:
        print("sua droga custou R${}". format(valor))
    elif prc==2:
        print("sua droga custou R${}, 2 parcelas de R${}". format(valor,valor/2))
    else:
        print("seu idiota essa não é uma opção")
elif pag==4:
    prc = int(input("de 3x a 12x: "))
    ju=( valor + (valor / 100 * 20))/prc
    print("o valor da sua droga é R${:.2f} juros de 20% da maquinhinha meu patrão, valor final R${:.2f}".format(valor, (valor + (valor / 100 * 20))))
    print("{}x de R${:.2f} ".format(prc,ju))
else:
    print("seu idiota essa não é uma opção")