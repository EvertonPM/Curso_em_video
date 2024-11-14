a=int(input("digite um numero: "))
b=int(input("digite outro numero: "))
c=int(input("digite outro numero: "))
if a>b and a>c:
    print("0 maior é {}".format(a))
if b > a and b > c:
    print("0 maior é {}".format(b))
if c > a and c > b:
    print("0 maior é {}".format(c))
if a<b and a<c:
    print("0 menor é {}".format(a))
if b < a and b < c:
    print("0 menor é {}".format(b))
if c < a and c < b:
    print("0 menor é {}".format(c))