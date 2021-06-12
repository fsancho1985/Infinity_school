class Carro:
    def __init__(self, marca, modelo, ano, ligado = False, automatico = False, velocidade = 0,\
        velocidadeMaxima = 120):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = ligado
        self.automatico = automatico
        self.velocidade = velocidade
        self.velocidadeMaxima = velocidadeMaxima

    
    # Método de ligar o veículo

    def ligar(self):
        self.ligado = True
    
    # Método de desligar o veículo

    def desligar(self):
        if self.ligado:
            self.ligado = False

    # Método de acelerar o veículo

    def acelerar(self, valor):
        if self.ligado and self.velocidadeMaxima > valor:
            self.velocidade += valor
                #return self.velocidade
        else:
            #print("velocidade máxima não pode ser ultrapassada")
            return False
        
    def verificarMarcha(self):
        if(self.velocidade) > 0 and (self.velocidade) <= 19:
            return 1
        elif(self.velocidade) >= 20 and (self.velocidade) <= 29:
            return 2
        elif(self.velocidade) >= 30 and (self.velocidade) <= 44:
            return 3
        elif(self.velocidade) >= 45 and (self.velocidade) <= 59:
            return 4
        elif(self.velocidade) > 59:
            return 5