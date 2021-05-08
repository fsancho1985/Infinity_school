import random

sorteio = random.randrange(1,10)
print(sorteio)

numAdivinhe = int(input("Digite um valor: "))

while numAdivinhe != sorteio:
    if numAdivinhe > sorteio:
        print("Valor maior")
    else:
        print("valor menor")
    numAdivinhe = int(input("Digite um valor: "))
print("Parabéns")
    
