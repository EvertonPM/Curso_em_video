import datetime
a=datetime.date.today().year
y=int(input("Que ano voce nasceu: "))
x=a-y
print("voce tem {} anos".format(x))
if x<=9:
    print("atleta MIRIM")
elif x<=14:
    print("atleta INFANTIL")
elif x<=19:
    print("atleta JUNIOR")
elif x<=25:
    print("atleta SENIOR")
else:
    print("atleta MASTER")