# Input de dados
pista = float(input("Digite o comprimento da pista em metros: "))
voltas = int(input("Digite o número de voltas: "))
reabastecimento = int(input("Digite o numero de reabastecimentos: "))
consumo = float(input("Digite o consumo do veículo: "))

totalKm = (pista * voltas)/1000
print("O percurso total do grand premio é: {:.2f}km".format(totalKm))

qntdVoltasAbastecimento = voltas / reabastecimento
print("Serão {:.0f} voltas por abastecimento.".format(qntdVoltasAbastecimento))
kmPrimeiroAbastecimento = qntdVoltasAbastecimento
primeiroAbatecimentoKm = (pista * kmPrimeiroAbastecimento) / 1000
print("O percurso até o primeiro pit stop será de: {:.2f}km, considerando o número de pit stops programados".format(primeiroAbatecimentoKm))


combustivelAbastecimento = consumo * primeiroAbatecimentoKm
print("O veículo deve iniciar a corrida com {:.2f} litros, isso o levará até o primeiro abastecimento.".format(combustivelAbastecimento))