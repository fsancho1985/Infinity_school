class Endereco:
    def __init__(self, cep, rua, numero, bairro, cidade, estado, pais, complemento = None):
        self.cep = cep
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.pais = pais
        self.complemento = complemento