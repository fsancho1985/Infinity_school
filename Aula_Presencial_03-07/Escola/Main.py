from Nota import Nota
from Aluno import Aluno


n1 = Nota("Nota1", "Algoritmo", 8.0)
n2 = Nota("Nota2", "Alogritmo", 6.5)
n3 = Nota("Nota3", "Python", 5.5)
n4 = Nota("Nota4", "Python", 7.5)
notas = [n1, n2, n3, n4]
a1 = Aluno("Francisco", "1º", "001", notas)

print(a1.notas)
print(a1.media())