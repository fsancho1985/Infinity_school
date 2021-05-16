massa = float(input("Digite o valor do seu peso: "))
altura = float(input("Digite o valor da sua altura: "))
imc = massa / (altura ** 2)
print("Massa (kg) {}".format(massa))
print("Altura (m) {}".format(altura))
print("Seu valor de IMC é: {}".format(imc))

if (imc < 18.5):
    print("Abaixo do peso")
else:
    #elif imc >= 18.5 and imc <= 24.9:
    #print("Peso normal")
    if (imc >= 18.5) and (imc < 25):
        print("Peso normal")
    else:
        if (imc >= 25) and (imc < 30):
              print("Sobrepeso")
        else:
              if (imc >= 30) and (imc < 40):
                    print("Obesidade")
              else:
                   if (imc > 40):
                    print("Obesidade morbida")
                        
              
