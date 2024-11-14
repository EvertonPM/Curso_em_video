lista=[]
for c in range(1,6):
    peso=float(input("qual o peso da {}° pessoa: ".format(c)))
    lista.append(peso)
print("o mais gordo pesa {} e o mais magro pesa {}".format(max(lista),min(lista)))
