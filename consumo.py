velocidade = float(input("Digite a velocidade média do veiculo: "))
consumo = 12
tempo = float(input("Digite o tempo gasto na viagem: "))
distancia = tempo * velocidade
print("A distância percorrida foi: {:.2f}".format(distancia))
consumoViagem = distancia/consumo
print("O consumo de combustível na viagem foi de: {:.2f}".format(consumoViagem))
