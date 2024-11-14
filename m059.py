t_idade=0
m_idade= []
f_idade=0
velho=0

for c in range(1,5):
    nome=input("Qual o nome da {}° pessoa: ".format(c))
    idade =float(input("Qual a idade da {}° pessoa: ".format(c)))
    t_idade=t_idade + idade
    sexo = input("Qual o sexo da {}° pessoa [F/M]: ".format(c)).upper()

    if sexo=="M":
        m_idade.append(idade)

    if sexo=="M" and idade==max(m_idade):
        velho=nome

    if sexo=='F' and idade<20:
        f_idade+=1

media=t_idade/4
print("A media das idades é {} anos".format(media))
print("o nome do homem mais velho é {}".format(velho))
print("{} mulheres tem menos de 20 anos".format(f_idade))



