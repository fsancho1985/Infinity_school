class Funcionario:
    def __init__(self, nome, salario, matricula, funcao):
        self.nome = nome
        self.__salario = salario
        self.matricula = matricula
        self.funcao = funcao

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novoSalario):
        aumento = self.__salario * 0.20
        aumento = self.__salario + aumento
        if novoSalario > aumento:
            return False
        elif novoSalario < self.__salario:
            return False
        else:
            self.__salario = novoSalario
            return True