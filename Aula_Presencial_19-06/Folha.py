class Folha:
    def __init__(self, funcionarios):
        self.__funcionarios = funcionarios

    def totalFolha(self):
        total = 0
        for f in self.__funcionarios:
            total += f.salario
        return total