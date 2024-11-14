num=[[],[]]
for i in range(0,7):
    x=int(input(f"Digite o {i+1}° valor: "))
    if x%2==0:
        num[0].append(x)
    elif x%2==1:
        num[1].append(x)
print(num)