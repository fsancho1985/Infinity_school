from Carro import Carro

r = "S"

gol = Carro("Volks", "1.0","2015", False, False)

# Verificando se o veículo é manual ou automático

if gol.automatico == True:
    print("Veículo automático")
else:
    print("Veículo manual")

# Ligando o veículo
gol.ligar()

# Verificando se o veículo está ligado
if gol.ligar:
    print("Veículo ligado!")
else:
    print("Veículo desligado")
#print(gol.ligado)

# Acelerando veículo
if(gol.ligado):
    print("Velocidade inicial", gol.velocidade)
    while r == "S":
        gol.acelerar(int(input("Digite a velocidade a ser acelerada: ")))
        print("Velocidade atual", gol.velocidade)
        r = input("Deseja continuar acelerando? ").upper()

# Verificando a marcha do veículo
if gol.verificarMarcha() == 1:
    print("1ª Marcha")
elif gol.verificarMarcha() == 2:
    print("2ª Marcha")
elif gol.verificarMarcha() == 3:
    print("3ª Marcha")
elif gol.verificarMarcha() == 4:
    print("4ª Marcha")
elif gol.verificarMarcha() == 5:
    print("5ª Marcha")
else:
    print("Velocidade máxima atingida!")
