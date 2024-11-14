num=int(input("Digite quantos numeros vc quer ver na sequencia de F: "))
contador=0
pri=0
seg=1
if num==0:
    print("0 termos da sequencia")
elif num==1:
    print(pri)
else:
    print(pri)
    print(seg)
while contador<num-2:
    fib=pri+seg
    print(fib)
    contador+=1
    pri=seg
    seg=fib

