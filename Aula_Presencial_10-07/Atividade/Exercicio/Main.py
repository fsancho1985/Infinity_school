from Instrumentos import Instrumentos
from Professor import Professor
from InstrumentoCorda import InstrumentoCorda
from InstrumentoPercussao import InstrumentoPercussao
from InstrumentoSopro import InstrumentoSopro

p1 = Professor("José", 5)
p2 = Professor("Pedro", 10)
p3 = Professor("Paulo", 7)
p4 = Professor("Carlos", 6)
i1 = InstrumentoCorda("violão", 20, p1, "corda", 6, "nylon")
i2 = InstrumentoCorda("Violino", 50, p3, "corda", 3, "aço")
i3 = InstrumentoPercussao("bateria", 18, p3, "percussao", True)
i4 = InstrumentoSopro("Sax", 28, p4, "sopro")

print(i1.dificuldade)
print(i2.dificuldade)
print(i3.dificuldade)
print(i4.dificuldade)




