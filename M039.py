from datetime import date
i=int(input("Em que ano voce nasceu? "))
a=date.today().year
if a-i>18:
    print("VOCE DEVERIA TER SE ALISTADO EM {}, JA SE PASSARAM {} ANOS".format(i+18,a-(i+18)))
if a-i<18:
    print("VOCE DEVE SE ALISTAR EM {}, AINDA FALTA {} ANOS".format(i+18,(i+18)-a))
if a-i==18:
    print("VOCE DEVE SE ALISTAR AGORA")


