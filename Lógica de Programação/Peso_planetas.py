peso = float(input("Digite o seu peso: "))
planeta = int(input("Digite o número do planeta: "))

if planeta == 1:
    peso *= 0.37
    print("Mercúrio")
elif planeta == 2:
    peso *= 0.88
    print("Vênus")
elif planeta == 3:
    peso *= 0.38
    print("Marte")
elif planeta == 4:
    peso *= 2.64
    print("Júpiter")
elif planeta == 5:
    peso *= 1.15
    print("Saturno")
else:
    peso *= 1.17
    print("Urano")

print("Seu peso no planeta escolhido: ", peso)


