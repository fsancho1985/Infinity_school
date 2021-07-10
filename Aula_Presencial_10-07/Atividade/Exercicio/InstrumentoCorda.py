from Instrumentos import Instrumentos

class InstrumentoCorda(Instrumentos):
    def __init__(self, nome, dificuldade, professor, tipo, qtd_corda, tipo_corda):
        super().__init__(nome, professor, dificuldade)
        self.tipo = tipo
        self.qtd_corda = qtd_corda
        self.tipo_corda = tipo_corda

    def verificaDificuldade(self):
        if self.tipo_corda == "aço":
            self.dificuldade = (self.dificuldade - self._professor.pontuacao) * self.qtd_corda
        else:
            self.dificuldade = self.dificuldade - self._professor.pontuacao
        return self.dificuldade 
