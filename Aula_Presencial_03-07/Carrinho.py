class Carrinho:
    def __init__(self, produtos):
        self.__produtos = produtos

    # Métodos

    def valorTotal(self):
        valorTotal = 0
        for p in self.__produtos:
            valorTotal += p.preco

        print("O valor total é: R$", valorTotal)
    
    # getters & setters

    @property
    def produtos(self):
        for p in self.__produtos:
            print(p.descricao)
        #return True

    @produtos.setter
    def produtos(self, novoProduto):
        self.__produtos.append(novoProduto)