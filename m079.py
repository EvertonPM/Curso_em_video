palavras=("ARROZ","FEIJAO","MACARRAO","LEITE")
print(palavras)
for i in range(0,4):
    print(f"A palavra {palavras[i]} tem as vogais: ", end=" ")
    if "A" in palavras[i]:
        print("A", end=" ")
    if "E" in palavras[i]:
        print("E",end=" ")
    if "I" in palavras[i]:
        print("I",end=" ")
    if "O" in palavras[i]:
        print("O",end=" ")
    if "U" in palavras[i]:
        print("U",end=" ")
    print(" ")