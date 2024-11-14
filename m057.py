import datetime
h=datetime.date.today().year
cont=0
for i in range(1,8):
    x=int(input("Que ano a {}° pessoa nasceu: ".format(i)))
    if h-x>=18:
        cont=cont+1
print("{} dessas pessoas são maiores de idade".format(cont))

