valor=int(input("Qual valor você quer sacar: "))
ced50=valor//50

if valor>50:
    print(f"{ced50} cedulas de R$50,00")
if valor%50!=0:
    print(f"{valor%50//20} cedulas de R$20,00")
    if (valor%50//20)!=0:
        print(f"{(valor%50)%20//10} cedulas de R$10,00")
        if (valor % 50) != 0:
            if (valor % 50) % 20 != 0:
                if ((valor % 50) % 20) % 10 != 0:
                    print(f"{(((valor % 50) % 20) % 10) // 1} cedulas de R$1,00")
if valor%50<20:
    print(f"{(valor % 50) % 20 // 10} cedulas de R$10,00")
    #print((valor % 50) % 20 // 10)
    if (valor % 50)!=0:
        if (valor % 50)%20!=0:
            if ((valor % 50)%20)%10!=0:
                print(f"{(((valor % 50) % 20) % 10) // 1} cedulas de R$1,00")
                #print((((valor % 50)%20)%10)//1)
