a=float(input("Digite a medida do lado a "))
b=float(input("Digite a medida do lado b "))
c=float(input("Digite a medida do lado c "))

if a+b<c:
    print("é um triangulo")
    if a == b == c:
        print("triangulo esquilatero")
    elif a == b or a == c or b == c:
        print("triangulo isosceles")
    else:
        print("triangulo escaleno")
elif a+c<b:
    print("é um triangulo")
    if a == b == c:
        print("triangulo esquilatero")
    elif a == b or a == c or b == c:
        print("triangulo isosceles")
    else:
        print("triangulo escaleno")
elif b+c<a:
    print("é um triangulo")
    if a == b == c:
        print("triangulo esquilatero")
    elif a == b or a == c or b == c:
        print("triangulo isosceles")
    else:
        print("triangulo escaleno")
else:
    print(" não é triangulo")
