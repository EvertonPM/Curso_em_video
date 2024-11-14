class Moeda():
    def __init__(self,Euro,Dolar,Real):
        self.Euro= Euro
        self.Dolar = Dolar
        self.Real = Real

    def converter(self):
        self.total = (self.Euro * 5.56) + (self.Dolar * 5.16) + self.Real



class Cofrinho(Moeda):
    def __init__(self,total):
        super().__init__(self,total)
        self.total = total



    def menu(self):
        print('      COFRINHO')
        print(" ")
        print('1 - Adicionar moeda')
        print('2 - Remover moeda')
        print('3 - Listar moeda')
        print('4 - Total convertido')

    def add(self):
        print('QUAL MOEDA ?')
        print(" ")
        print('1 - Real')
        print('2 - Dolar')
        print('3 - Euro')

    def update(self):
        




