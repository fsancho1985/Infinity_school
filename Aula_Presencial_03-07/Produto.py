class Produto:
    def __init__(self, nome, preco, descricao):
        self.nome = nome
        self.__preco = preco
        self.descricao = descricao

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, preco):
        preco_min = self.__preco*0.10
        preco_min = self.__preco - preco_min
        if preco_min >= self.__preco:
            self.__preco = preco
            return True
        else:
            return False