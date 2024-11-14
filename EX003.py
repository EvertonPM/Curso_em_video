a=float(input("Quantos kWh vc usa? "))
b=input("qual seu tipo de instalação: R - Residencial / C- Comercial / I - Industrial  ")
if b=="R" and a<=500:
    print("vc deve pagar R${} ".format(0.4*a))
elif b=="R" and a>500:
    print("vc deve pagar R${} ".format(0.65*a))
elif b=="C" and a<=1000:
    print("vc deve pagar R${} ".format(0.55*a))
elif b=="C" and a>1000:
    print("vc deve pagar R${} ".format(0.60*a))
elif b=="I" and a<=5000:
    print("vc deve pagar R${} ".format(0.55*a))
elif b=="I" and a>5000:
    print("vc deve pagar R${} ".format(0.60*a))
else:
    print("Digito invalido")