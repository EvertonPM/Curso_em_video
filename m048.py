import random
print("[0] PEDRA")
print("[1] PAPEL")
print("[2] TESOURA")
esc=int(input("ESCOLHA: "))
comp=random.randint(0,2)
if esc==0 and comp==1:
    print("VOCÊ ESCOLHEU PEDRA")
    print("O CPU ESCOLHEU PAPEL")
    print("VOCÊ SE FODEU")
elif esc == 0 and comp == 2:
    print("VOCÊ ESCOLHEU PEDRA")
    print("O CPU ESCOLHEU TESOURA")
    print("VOCÊ FODEU COM ELE. ISSO AI")
elif esc == 1 and comp == 0:
    print("VOCÊ ESCOLHEU PAPEL")
    print("O CPU ESCOLHEU PEDRA")
    print("VOCÊ FODEU COM ELE. ISSO AI")
elif esc==1 and comp==2:
    print("VOCÊ ESCOLHEU PAPEL")
    print("O CPU ESCOLHEU TESOURA")
    print("VOCÊ SE FODEU")
elif esc==2 and comp==0:
    print("VOCÊ ESCOLHEU TESOURA")
    print("O CPU ESCOLHEU PEDRA")
    print("VOCÊ SE FODEU")
elif esc==2 and comp==1:
    print("VOCÊ ESCOLHEU TESOURA")
    print("O CPU ESCOLHEU PAPEL")
    print("VOCÊ FODEU COM ELE. ISSO AI")
elif esc==comp:
    print("VOCÊ ESCOLHEU {}".format(esc))
    print("O CPU ESCOLHEU {}".format(comp))
    print("IXI, DEU LUBIZOMI")
else:
    print("JOGA SERIO FIOOO, SEM GRACINHA AI")


