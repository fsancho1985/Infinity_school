from Medico import Medico

class Cirurgiao(Medico):
    def __init__(self, crm, nome, idade, salario):
        super().__init__(crm, nome, idade, salario)

    def aposenta(self):
        if self.idade >= 50:
            self.aposentado = True
            self.aposentadoria = (self.salario * 0.8) + 2000
            
