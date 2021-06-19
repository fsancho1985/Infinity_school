from Funcionario import Funcionario

funcionario1 = Funcionario("Francisco", 5000, "0001", "Dev")
print("Salário do funcionário: ", funcionario1.nome, " R$",funcionario1.salario)

funcionario2 = Funcionario("João", 4000, "002", "Web-Designer")
print("Salário do funcionário: ", funcionario2.nome, " R$",funcionario2.salario)

# funcionario1.salario = 6100
# print("Aumento realizado no salário do funcionário: ",funcionario1.nome," foi de:", "R$",funcionario1.salario)
funcionario2.salario = 4400
print("Aumento realizado no salário do funcionário: ", funcionario2.nome, " foi de:", "R$", funcionario2.salario)