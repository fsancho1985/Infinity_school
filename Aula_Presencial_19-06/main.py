from Funcionario import Funcionario
from Folha import Folha

funcionario1 = Funcionario("Francisco", 5000, "0001", "Dev")
print("Salário do funcionário: ", funcionario1.nome, " R$",funcionario1.salario)

funcionario2 = Funcionario("João", 4000, "002", "Web-Designer")
print("Salário do funcionário: ", funcionario2.nome, " R$",funcionario2.salario)

funcionario3 = Funcionario("Paulo", 7000, "003", "Java-Dev")
print("Salário do funcionário: ", funcionario3.nome, " R$",funcionario3.salario)

#funcionario1.salario = 6100
#print("Aumento realizado no salário do funcionário: ",funcionario1.nome," foi de:", "R$",funcionario1.salario)
#funcionario2.salario = 4400
#print("Aumento realizado no salário do funcionário: ", funcionario2.nome, " foi de:", "R$", funcionario2.salario)

funcionarios = [funcionario1, funcionario2, funcionario3]
folha = Folha(funcionarios)

print("O total da folha é: R$",folha.totalFolha())