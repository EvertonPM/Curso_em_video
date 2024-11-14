peso=float(input("Qual seu peso: "))
alt=float(input("Qual sua altura em metros: "))
imc= peso/alt**2
if imc<18.5:
    print("Você está abaixo da média ideal")
elif 18.5<=imc<25:
    print("Você está no peso ideal")
elif 25<=imc>30:
    print("Você está no sobrepeso")
elif 30<=imc>40:
    print("Você está obeso, seu baleia")
else:
    print("Você está em Obesidade morbida, ou seja gordão")