salarioHora = float(input("Qual o valor em horas: "))
horasTrabalho = float(input("Quantas horas trabalhadas: "))
salarioBruto = salarioHora * horasTrabalho
print("Salario bruto: R${:.2f}".format(salarioBruto))
IR = salarioBruto * 0.11
print("Imposto de renda: R${:.2f}".format(IR))
INSS = salarioBruto * 0.08
print("INSS: R${:.2f}".format(INSS))
sindicato = salarioBruto * 0.05
print("Desconto sindical: R${:.2f}".format(sindicato))
#descontos = IR + INSS + sindicato
#salarioLiquido = salarioBruto - descontos
salarioLiquido = salarioBruto - IR - INSS - sindicato
print("Salário líquido: R${:.2f}".format(salarioLiquido))