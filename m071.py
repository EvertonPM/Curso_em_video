maior=0
homem=0
mulher=0
while True:
    i=(input("Qual a idade:   "))
    s=str(input(("sexo [M/F]: "))).upper()
    while s not in "MF":
        s = str(input(("sexo [M/F]: "))).upper()
    if i>18:
        maior+=1
    if s=="M":
        homem+=1
    if s=="F" and i<20:
        mulher+=1
    c=str(input("Você quer continuar: [S/N] ")).upper()
    while c not in "SN":
        c = str(input("Você quer continuar: [S/N] ")).upper()
    if c=='N':
        break
print(f"{maior} pessoas maiores de 18 anos")
print(f"{homem} homens foram cadastrados")
print(f"{mulher} mulheres abaixo de 20 anos")