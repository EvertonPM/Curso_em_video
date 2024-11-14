import time
print('\033[1;;42m~'*27)
print('  SISTEMA DE AJUDA PyHELP')
print('~\033[1;;42m'*27)
print('\033[m',end='')

def ajuda(x):
    print('\033[1;;44m~'*(36 + len(x)))
    print(F'  ACESSANDO O MANUAL DO COMANDO ({x}) ')
    print('\033[1;;44m~' * (36 + len(x)))
    print('\033[m',end='')
    print('\033[7;38m')
    help(x)
    print('\033[m',end='')



while True:
    time.sleep(1)
    x=input('Função ou Biclioteca > ').lower()
    if x =='fim':
        print('\033[1;;41m~' * 12)
        print('  ATÉ LOGO')
        print('~\033[1;;41m' * 12)
        break
    else:
        ajuda(x)
