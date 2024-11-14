dia = int(input('QUANTOS DIAS FICOU COM O CARRO? '))
KM = float(input('QUNTOS KM RODOU?'))
VALOR = (dia * 60) + (KM * 0.15)
print('SEU ALUGUEL FICOU R${:.2f}'.format(VALOR))
