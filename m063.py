x=int(input("Digite um numero inteiro: "))
y=x-1
m=x*y
y=x-2
while y>0:
    m=m*y
    y-=1
print("{}! = {}".format(x,m))
