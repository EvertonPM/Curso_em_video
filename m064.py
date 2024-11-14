x=int(input("Digite um numero para iniciar: "))
r=int(input(("Digite a razão: ")))
c=0
pa=x
b=0
print(x)
while True:
    while c<9:
        pa=pa+r
        c+=1
        print(pa)
    e=int(input("Voce quer ver mais quantos termos: "))
    if e==0:
        break
    h=e
    while h>0:
        pa = pa + r
        print(pa)
        h=h-1
        b=b+1
print("no total foram mostrados {} termos".format(c+1+b))