def verificaTurno(turno):
    if turno == "matutino" or turno == "vespertino" or turno == "noturno":
        return turno
    else:
        print("Turno inválido!")
        return ""

class Atendentes:
    # Construtor
    def __init__(self, codigo, nome, dataNascimento, salario, turno):
        self.codigo = codigo
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.__salario = salario
        self.__turno = verificaTurno(turno)

    @property
    def salario(self):
        return "O salário do Atendente é: " + str(self.__salario)

    @salario.setter
    def salario(self, novoSalario):
        print("Não é possível atribuir um novo salário")
        return

    @property
    def turno(self):
        return "O turno do atendente é: " + self.__turno

    @turno.setter
    def turno(self, novoTurno):
        self.__turno = verificaTurno(novoTurno)