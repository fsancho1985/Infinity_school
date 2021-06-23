class Nave:
    def __init__(self, nome, fabricante, modelo, classe, tripulacao):
        self.nome = nome
        self.fabricante = fabricante
        if tripulacao > 120:
            self.novaTripulacao = 120
        else:
            self.__tripulacao = tripulacao
        self.modelo = modelo
        self.classe = classe
        
    @property
    def tripulacao(self):
        return self.__tripulacao

    @tripulacao.setter
    def tripulacao(self, novaTripulacao):
        tripMax = 120
        if novaTripulacao> tripMax:
            return False
        else:
            self.__tripulacao = novaTripulacao
            return True