class Prova():
    """Classe prova"""

    propietat1 = 10

    def __init__(self, param1="123"):   #no permet N constructors, però assignar valor per defecte
        '''Constructor'''
        self.valor = param1
        print("Inici classe. Valor = " + self.valor)

    def met1(self):
        '''Mètode 1'''
        print("m1")
        print(self.propietat1)

    def met2(self, param1):
        '''Mètode 2'''
        print(param1)

pro = Prova()
pro.met1()
pro.met2("***")
print(pro.propietat1)

pro = Prova("333")
