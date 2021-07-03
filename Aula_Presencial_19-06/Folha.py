class Folha:
    def __init__(self, funcionarios):
        self.__funcionarios = funcionarios

    # getters

    @property
    def funcionarios(self):
        for f in self.__funcionarios:
            print("Funcionário: ", f.nome, "Salário: ", str(f.salario))

    # Setters

    @funcionarios.setter
    def funcionarios(self, novoFuncionario):
         self.__funcionarios.append(novoFuncionario)

    # Método

    def totalFolha(self):
        total = 0
        for f in self.__funcionarios:
            total += f.salario
        return total