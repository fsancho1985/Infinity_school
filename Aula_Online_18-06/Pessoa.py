class Pessoa:
    def __init__(self, nome, dataNasc, altura):
        self.nome = nome
        self.dataNasc = dataNasc
        self.altura = altura
        
    def imprime(self):
        return("nome: " + self.nome + "\n" + "data de nascimento: " + str(self.dataNasc) + "\n" + "altura: " + str(self.altura))
    
    def idade(self, anoAtual):
        return anoAtual - self.dataNasc