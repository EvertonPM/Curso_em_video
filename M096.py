dick={}
lista=[]
time=[]
while True:

    dick['nome']=str(input("Digite o nome do craque: "))
    dick['part']=int(input('Quantas partidas esse craque foi escalado: '))
    soma=0

    for i in range(1,dick['part']+1):
        x=int(input(f"Quantos gols o craque fez na partida {i}: "))
        lista.append(x)
        soma=soma+x
    res=input("Quer continuar: [S/N]: ").upper().strip().split()[0]
    dick['gols'] = lista[:]
    dick['tot'] = soma
    time.append(dick.copy())
    lista.clear()
    if res=="S":
        continue
    if res=='N':
        break


print("-="*30)
print(f"{'cod':<4}{'nome':<10}{'gols':<15}{'total':<26}")
cont=0
for i in time:
    print(f'{cont:<4}{i["nome"]:<10}{str(i["gols"]):<15}{i["tot"]:<26}')
    cont += 1
print("-"*30)
while True:
    y=int(input("Mostrar dados de qual jogador? (999 para parar): "))
    if y == 999:
        break
    if y>=len(time):
        continue
    print(F" -- LEVANTAMENTO DO JOGADOS {time[y]['nome']}:")
    for i in range (0,(time[y]['part'])):
        print(f"   => Na partida {i+1}, fez {time[y]['gols'][i]} gols. ")

print("ENCERRANDO...")




#for k,v in dick.items():
#    print(f"{k} = {v}")
#print("-=" * 40)
#print(f"O jogados {dick['nome']} jogou {dick['part']} partidas'")
#print()
#for k,v in dick.items():
#    if k=='gols':
#        for i in range (0,dick['part']):
#           print(f"  => Na partida {i}, fez {v[i]} gols. ")
#print('')
#print(f"O total de gols foram {dick['tot']}")
#print("-=" * 40)