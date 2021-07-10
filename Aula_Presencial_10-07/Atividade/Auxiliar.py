from Medico import Medico

class Auxiliar(Medico):
    def __init__(self, crm, nome, idade, salario):
        super().__init__(crm, nome, idade, salario)

    def aposenta(self):
        if self.idade >= 60:
            self.aposentado = True
            self.aposentadoria = self.salario * 0.8
            