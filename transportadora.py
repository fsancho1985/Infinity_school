valorTonelada = float(input("Digite o valor da tonelada: "))
caminhao = input("Vai sair caminhão? ")
totalSoma = 0

while caminhao == "s":
    carga = float(input("Digite a quantidade de carga do caminhão: "))
    valorCarga = valorTonelada * carga
    print("Valor Carga", valorCarga)
    totalSoma += valorCarga
    
    caminhao = input("Vai sair caminhão? ")


print("O valor total é: ", totalSoma)

#valorTonelada = (float(input("Digite o valor da tonelada :"))

#qtdTonelada = int(input("Digite a quantidade de toneladas: "))

#faturament0 = 0

#while qtdTonelada != 0:
    #faturamento += (qtdTonelada * valorTonelada)
    #qtdTonelada = int(input("Digite a quantidade de toneladas: "))
#print("Faturament total: R$",faturamento)
    
