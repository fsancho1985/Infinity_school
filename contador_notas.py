qtdNotas = int(input("Digite a quantidade de notas desejadas: "))
soma = 0

for i in range(qtdNotas):
    nota = float(input("Digite a nota: "))
    soma += nota
    #print(soma)
    media = soma/qtdNotas
print("A média do aluno foi: ", media)
