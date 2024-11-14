x=float(input("quantos km é sua viagem? "))
if x<=200:
    print("sua passagem custa: R${}".format(x*0.50))
else:
    print("sua passagem custa: R${}".format(x * 0.45))