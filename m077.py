
x=(int(input("Digite um numero: ")),int(input("Digite um numero: ")),int(input("Digite um numero: ")),int(input("Digite um numero: ")))

print(x)
if x.count(9)==1:
    print(f"o 9 apareceu {x.count(9)} vez")
elif 9 in x:
    print(f"o 9 apareceu {x.count(9)} vezes")
else:
    print("não tem 9")



if 3 in x:
    print(f"o 3 aparece na posição {x.index(3)+1}")
else:
    print("não tem 3")

for i in range(0,4):
    if x[i] % 2 == 0:
        print(f"os numeros pares foram {x[i]}")

