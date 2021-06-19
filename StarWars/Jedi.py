class Jedi:
    def __init__(self, nome, especie, sabre, nomeDaNave = "", grau = "Padawan"):
        self.nome = nome
        self.__grau = grau
        self.especie = especie
        self.sabre = sabre
        self.nomeDaNave = nomeDaNave

    @property
    def grau(self):
        return self.__grau

    @grau.setter
    def grau(self, novoGrau):
        if novoGrau == "Padawan":
            self.__grau = novoGrau
            return True
        elif novoGrau == "Cavaleiro":
            self.__grau = novoGrau
        elif novoGrau == "Mestre":
            self.__grau = novoGrau
            return True
        else:
            return False