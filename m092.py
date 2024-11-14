import random
import time
dic={}
lista=[]
x=random.randint(1,6)
dic['jogador1'] = x
lista.append(dic.copy())
#dic.clear()
a=random.randint(1,6)
dic['jogador2'] = a
lista.append(dic.copy())
#dic.clear()
b=random.randint(1,6)
dic['jogador3'] = b
lista.append(dic.copy())
c=random.randint(1,6)
#dic.clear()
dic['jogador4'] = c
lista.append(dic.copy())
print(lista)
print("***JOGANDO OS DADOS***")
from time import sleep
sleep(1)
print(f"   JOGADOR 1 = ...{x}")
sleep(1)
print(f"   JOGADOR 2 = ...{a}")
sleep(1)
print(f"   JOGADOR 3 = ...{b}")
sleep(1)
print(f"   JOGADOR 4 = ...{c}")
sleep(1)
print("***VENCEDORES***")
sleep(1)
print(dic)
pri=0
seg=0
ter=0
ult=0
for k,v in dic.items():
    if v>pri:
        pri=v
    elif v>seg and v>ter and v>ult and v<=pri:
        seg=v
    elif v>ter and v>ult and v<=ult and v<pri:
        seg=v 
    else:
        ult=v
    print(f"{k} = ...{v}")
print(pri)
print(seg)
print(ter)
print(ult)