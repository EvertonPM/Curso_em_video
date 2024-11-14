def ficha(nome=str('<desconhecido>'),gols=0):
    if nome==" ":
        nome=str('<desconhecido>')
    if gols==():
        gols=0
    print(f"O jogador {nome} fez {gols} gols")

nome=str(input('Digite o nome do jogador: '))
gols=int(input('Quantos gols esse jogador fez: '))
ficha(nome,gols)