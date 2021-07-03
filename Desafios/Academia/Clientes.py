def verificaPlano(plano):
    if plano == "economico" or plano == "estudantil" or plano == "platinum":
        return plano
    else:
        print("Plano inválido!")
        return ""

class Clientes:
    # Construtor
    def __init__(self, matricula, nome, dataNasc, plano):
        self.matricula = matricula
        self.nome = nome
        self.dataNasc = dataNasc
        self.__plano = verificaPlano(plano)

    # getters & setters

    @property
    def plano(self):
        return "O plano selecionado é: " + self.__plano

    @plano.setter
    def plano(self, novoPlano):
        self.__plano = verificaPlano(novoPlano)