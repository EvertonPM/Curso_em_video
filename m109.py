import moeda


x=float(input('Digite um valor R$:'))
print(f'O dobro de {x:.2f} é {moeda.dobro(x):.2f}')
print(f'A metade de {x:.2f} é {moeda.metade(x):.2f}')
print(f'Aumentando 15% fica R${moeda.aumentar(x,15)}')