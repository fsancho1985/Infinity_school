from Candidato import Candidato
from Processo import Processo
from Prova import Prova

p1 = Prova("02/06/2021", 9)

c1 = Candidato("João", "Rua K", 5, "Estudante", p1)

candidatos = [c1]

processo = Processo(candidatos)
processo.aprovados()
