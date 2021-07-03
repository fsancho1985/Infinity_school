class Cliente:
    def __init__(self, nome, email, senha, endereco):
        self.nome = nome
        self.email = email
        self.__senha = senha
        self.endereco = endereco

    # getters & setters

    @property
    def senha(self):
        return "**********"
    
    @senha.setter
    def senha(self, novaSenha):
        return 