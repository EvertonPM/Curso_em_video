lista=[]
a='Fizz'
b='Buzz'
c='FizzBuzz'
for i in range (1,101):
    if i % 3 == 0:
        if i % 3 == 0 and i % 5 == 0:
            lista.append(c)
        else:
            lista.append(a)
    elif i%5==0:
        if i % 3 == 0 and i % 5 == 0:
            lista.append(c)
        else:
            lista.append(b)
    else:
        lista.append(i)
for i in range (0,100):
    print(lista[i])