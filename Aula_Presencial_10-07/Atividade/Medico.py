class Medico:
    def __init__(self, crm, nome, idade, salario):
        self.crm = crm
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.aposentado = False
        self.aposentadoria = None

    def aposenta(self):
        if self.idade >= 55:
            self.aposentado = True
            self.aposentadoria = self.salario * 0.8
