lista=[[],[],[],[]]

cont=0
while True:
    nome=input("Digite o nome: ")
    nota1=int(input("Qual a nota da prova 1: "))
    nota2=int(input("Qual a nota da prova 2: "))
    media=(nota1+nota2)/2
    lista[0].append(nome)
    lista[1].append(nota1)
    lista[2].append(nota2)
    lista[3].append(media)
    cont+=1
    res=input("Quer continuar? [S/N]").upper()
    if res=='N':
        break

print("-="*11)
print("       BOLETIM")
print("-="*11)
print(f'{"N°":<4}  {"NOME":<10}     {"MÉDIA":>8}')
for i in range(0,cont):
    print(f'{i:<4}   {lista[0][i]:<10}',end="")
    print(f'{lista[3][i]:>8}')
while True:
    y=int(input("Mostrar notas de qual aluno? (999-SAIR)"))
    print(f"Nota de {lista[0][y]} são {lista[1][y]} e {lista[2][y]}")
    if y==999:
        break
print("FINALIZANDO")