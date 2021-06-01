from datetime import datetime

data2 = datetime.now()

def calculoData(data1, data2):
    data1 = datetime.strptime(data1, "%d/%m/%Y")
    return abs((data2 - data1).days)

data1 = input("Insira a data desejad no formato Dia / Mês / Ano: ")

print(calculoData(data1, data2))




