def notas(*num,sit=False):
    dic={}
    soma=0
    for k in num:
        soma+=k
        dic['total']=len(num)
        dic['maior']=max(num)
        dic['menor']=min(num)
        media=soma/len(num)
        dic['media']=media
    if sit:
        media = soma / len(num)
        if media>=7:
            dic['sit']='BOA'
        elif 4<=media<7:
            dic['sit'] = 'RAZOAVEL'
        elif media<4:
            dic['sit'] = 'RUIM'
    print(dic)


notas(2,3,5,sit=True)