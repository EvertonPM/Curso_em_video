dic={}
lista=[]
dic['nome']=input("Nome do aluno: ")
dic['media']=int(input("media do aluno: "))
if dic['media']>=70:
    dic['sit']="Aprovado"
elif 50<=dic['media']<=70:
    dic['sit']="Recuperação"
else:
    dic['sit'] = "Reprovado"
lista.append(dic.copy())
for i in lista:
    for k,v in i.items():
        print(k,end=" ")
        print("=",v)
