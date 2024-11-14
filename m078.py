prod=('geladeira',"2000.00","fogão","990.00","pia","389.90","copos","80.00")
for i in range(0,8,2):
    print(prod[i],"-"*(40-len(prod[i])),"R$"," "*(1+(7-len(prod[i+1]))-1),prod[i+1])
