class Nota:
    def __init__(self, nome, disciplina, valor):
        self.nome = nome
        self.disciplina = disciplina
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, novoValor):
        self.__valor = novoValor

    