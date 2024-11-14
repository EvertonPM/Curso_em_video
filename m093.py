from datetime import date

dic={'Nome':input("Nome: ")}

dic['Nascimento']=int(input("Ano de nascimento: "))
dic['CTPS']=int(input("CTPS (0 se não possui): "))
if dic['CTPS']==0:
    for k,v in dic.items():
        if v==0:
            print(f'Não possui {k}')
        else:
            print(f'{k} é {v}')
else:
    dic['Contratação']=int(input("Ano de contratação: "))
    dic['Salario'] = int(input("Salario: "))

print('-='*30)
for k,v in dic.items():
    print(f' -{k} = {v}')
idade=(date.today().year)-dic['Nascimento']
print(f' -Idade: {idade}')
if (date.today().year)-dic['Contratação']>=40:
    pos="Aposentado"
    print(f' -INSS: {pos}')
else:
    falta =40-((date.today().year) - dic['Contratação'])
    pos=f'Falta {falta} anos para aposentadoria'
    print(f' -INSS: {pos}')