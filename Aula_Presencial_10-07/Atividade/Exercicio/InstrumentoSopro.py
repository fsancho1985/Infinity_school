from Instrumentos import Instrumentos

class InstrumentoSopro(Instrumentos):
    def __init__(self, nome, professor, dificuldade, tipo):
        super().__init__(nome, professor, dificuldade)
        self.tipo = tipo

    def verificaDificuldade(self):
        self.dificuldade = self.dificuldade - self._professor.pontuacao
        return self.dificuldade