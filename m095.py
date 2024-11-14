lista=[]
dic={}
while True:
    dic['Nome']=str(input("Nome: "))
    dic['Sexo']=str(input("Sexo: ")).upper().strip().split()[0]
    while dic['Sexo']!='F' and dic['Sexo']!='M':
        print("Opção invalida digite [F ou M]: ")
        dic['Sexo'] = str(input("Sexo: ")).upper()
    dic['Idade']=int(input("Idade: "))
    lista.append(dic.copy())
    res=input('Quer continuar? [S/N]: ').upper().strip().split()[0]
    while res!='S' and res!="N":
        res = input('Quer continuar? [S/N]: ').upper()
    if res=="N":
        break
print("-="*40)
print(f"A)  Foram cadastradas {len(lista)} pessoas")
somai=0
for a,b in enumerate(lista):
    for k,v in b.items():
        if k=='Idade':
            somai+=v
media=somai/len(lista)
print(f"B)  A média de idade é {media:.2f} anos")
print(f"C)  As mulheres são:",end=" ")
for a,b in enumerate(lista):
    for k,v in b.items():
        if k=='Sexo':
            if v=='F':
                for k, v in b.items():
                    if k=='Nome':
                        print(f'{v}',end=' ')
print(f"\nD)  As idade que estão acima da média são:")
for a,b in enumerate(lista):
    for k,v in b.items():
        if k=='Idade':
            if v>media:
                for k, v in b.items():
                    if k=='Nome':
                        print()
                    print(f'   {k} = {v}', end=';')
print(" ")
print("ENCERRANDO... ")
