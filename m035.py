a=float(input("Digite a medida de uma reta"))
b=float(input("Digite a medida de outra reta"))
c=float(input("Digite a medida de outra reta"))
if a+b>c and a+c>b and b+c>a:
    print("forma um triangulo")
    if a==b==c:
        print("Triangulo Equilatero")
    elif a!=b and a!=c and b!=c:
        print("Triangulo Escaleno")
    else:
        print("Triangulo Isoscelos")
else:
    print("não forma um triangulo")