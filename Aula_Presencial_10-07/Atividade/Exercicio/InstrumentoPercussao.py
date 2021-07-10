from Instrumentos import Instrumentos

class InstrumentoPercussao(Instrumentos):
    def __init__(self, nome, professor, dificuldade, tipo, baqueta):
        super().__init__(nome, professor, dificuldade)
        self.tipo = tipo
        self.baqueta = baqueta


    def verificaDificuldade(self):
        self.dificuldade = self.dificuldade - self._professor.pontuacao
        return self.dificuldade