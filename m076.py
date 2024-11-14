import random
tupla=[]
for i in range(1,6):
    x=(random.randint(0,9))
    tupla.append(x)
print(tupla)
print(f"maior = {max(tupla)}")
print(f"menor = {min(tupla)}")