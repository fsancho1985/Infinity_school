class Processo:
    def __init__(self, candidatos):
        self.candidatos = candidatos

    def aprovados(self):
        aprovados = []
        for c in self.candidatos:
            if c.prova.pontuacao > 8:
                aprovados.append(c)

        for a in aprovados:
            print(a.nome)