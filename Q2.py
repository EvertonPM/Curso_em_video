print("                 BEM-VINDOS A SORVETERIA DO EVERTON PEREIRA MEDEIROS")
print("                                       CARDAPIO")
print("N° DE BOLAS         SABOR TRADICIONAL           SABOR PREMIUM            SABOR ESPECIAL")
print("     1                    R$6,00                   R$7,00                    R$8,00  ")
print("     2                    R$11,00                  R$13,00                   R$15,00  ")
print("     3                    R$15,00                  R$18,00                   R$21,00  ")

print(" ")
print("TRADICIONAL - tr")
print("PREMIUM - pr")
print("ESPECIAL - es")
print(" ")
sabor=input("Escolha um SABOR de sorvete: ")
while sabor != "tr" and sabor != "pr" and sabor != "es":
    print("SABOR INVALIDO")
    sabor = input("Escolha um sabor de sorvete: ")
    if sabor != "tr" and sabor != "pr" and sabor != "es":
        continue
    bolas=int(input("Quantas BOLAS desse sabor: "))
  #  elif bolas != 1 and bolas != 2 and bolas != 3:

    print("QUANTIDADES DE BOLAS DE SORVETE INVALIDA")
    bolas=int(input("Quantas BOLAS desse sabor: "))
