def area(a,b):
    print('-'*30)
    print("    CONTROLE DE TERRENO")
    print('-' * 30)
    print(f"A area do seu terreno de {a} por {b} é {a*b}m²")


a=float(input("Digite a largura do seu terreno: "))
b=float(input("Digite a comprimento do seu terreno: "))
area(a,b)