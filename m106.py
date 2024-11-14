def leiaint(msg):
    ok=False
    valor=0
    while True:
        y = str(input(msg))
        if y.isnumeric():
            valor=int(y)
            ok = True
        else:
            print('\033[;31mERRO! DIGITE UM NUMERO VALIDO\033[m')
            continue
        if ok:
            break
    return valor


def leiareal(msg):
    while True:
        try:
            y = float(input(msg))
        except:
            print('\033[;31mERRO! DIGITE UM NUMERO REAL VALIDO\033[m')
            continue
        else:
            return y


n = leiaint('Digite um valor inteiro: ')
nr = leiareal('Digite um valor real: ')

print(f'Voce digitou o valor inteiro {n} e o valor real {nr}')
