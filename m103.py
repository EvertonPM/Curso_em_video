def fatorial(x,show=False):
    f=1
    #for i in range(x,0,-1):
    #    f*=i
    for i in range(x, 0, -1):
        f *= i
        if i==0:
            print(f'{x}',end='')
        elif x>1:
            print(f' x {x-1}',end=' ')
        elif i==x:
            print(f'= {f}')


fatorial(5)