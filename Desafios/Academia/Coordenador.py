from Desafios.Academia.Instrutores import Instrutores


def verificaTurno(turno):
    if turno == "matutino" or turno == "vespertino" or turno == "noturno":
        return turno
    else:
        print("Turno inválido!")
        return ""

def verificaCategoria(categoria):
    if categoria == "musculação" or categoria == "crossfit" or categoria == "spinning":
        return categoria
    else:
        print("Categoria inválida!")
        return ""

class Coordenador:
    def __init__(self, codigo, nome, dataNascimento, salario, turno, cref, categoria):
        self.codigo = codigo
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.__salario = salario
        self.__turno = verificaTurno(turno)
        self.cref = cref
        self.__categoria = verificaCategoria(categoria)
        self.__instrutores = []

    @property
    def salario(self):
        return "O salário do Instrutor é: " + str(self.__salario)

    @salario.setter
    def salario(self, novoSalario):
        print("Não é possível atribuir um novo salário")
        return

    @property
    def turno(self):
        return "O turno do Instrutor é: " + self.__turno

    @turno.setter
    def turno(self, novoTurno):
        self.__turno = verificaTurno(novoTurno)

    @property
    def categoria(self):
        return "A categoria do instrutor é: " + self.__categoria

    @categoria.setter
    def categoria(self, novaCategoria):
        print("Categoria inválida!")
        return

    @property
    def instrutores(self):
        for i in self.__instrutores:
            print(i.nome)

    @Instrutores.setter
    def instrutores(self, novoInstrutor):
        if self.__categoria == novoInstrutor:
            self.__instrutores.append(novoInstrutor)
        else:
            print("Erro: Catergoria Inválida")