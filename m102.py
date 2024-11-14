from datetime import date
hoje=date.today().year
def voto(x):
    if (hoje-x)<16:
        return 'NÃO VOTA'
    elif 16<=(hoje-x)<18:
        return 'VOTO OPCIONAL'
    elif 18<= (hoje - x) <60:
        return 'VOTO OBRIGATÓRIO'
    elif (hoje-x)>=60:
        return 'VOTO OPCIONAL'


#Programa princial
ano=int(input('Qual ano voce nasceu: '))
idade=hoje-ano
print(f'Sua idade é {idade}: {voto(ano)}')