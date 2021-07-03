def verificaSemestre(semestre):
    if semestre == "1º" or semestre == "2º" or semestre == "3º" or semestre == "4º":
        return semestre
    else:
        return ""


class Aluno:
    def __init__(self, nome, semestre, matricula, notas):
        self.nome = nome
        self.__semestre = semestre
        self.matricula = matricula
        self.__notas = notas

    # Getters & Setters

    @property
    def semestre(self):
        return self.__semestre
    
    @semestre.setter
    def semestre(self, novoSemestre):
        self.__semestre = verificaSemestre(novoSemestre)

    def media(self):
        total = 0
        c = 0
        for n in self.__notas:
            c += 1
            total += n.valor
            media = total / c
        return media