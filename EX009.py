p=0
d=0
i=0
while True:
    if x>0 and x<3:
        print("gratuito")
        i=i+x
        p=p+1
    elif x>=3 and x<=12:
        print("preço R$15,00")
        i = i + x
        p = p + 1
        d=d+15
    elif x>=12:
        print("preço R$30,00")
        i = i + x
        p = p + 1
        d=d+30
    elif x==0:
        break
print(" ")
print("Encerrando...")
print("{} pessoas compraram o ingresso".format(p))
print("foi arrecadado R${}".format(d))
print("media de idade do publico: {} anos ".format(i/p))