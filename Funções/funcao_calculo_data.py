from datetime import datetime

# Variável que identifica a data atual
data2 = datetime.now()

# Função para cálculo da data
def calculoData(data1, data2):
    data1 = datetime.strptime(data1, "%d/%m/%Y")
    return abs((data2 - data1).days)

data1 = input("Insira a data desejad no formato Dia / Mês / Ano: ")

print("A data inserida ocorreu há ",(calculoData(data1, data2)), "dia(s) atrás.")