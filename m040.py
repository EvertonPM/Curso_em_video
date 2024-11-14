nota1=float(input("qual a nota na prova 1: "))
nota2=float(input("qual a nota na prova 2: "))
if (nota1+nota2)/2<50:
    print("\033[0;31mREPROVADO")
elif (nota1+nota2)/2>=50 and (nota1+nota2)/2<=69 :
    print("\033[0;33mRECUPERAÇÃO")
else:
    print("\033[0;32mAPROVADO")