dia = int(input("Digite o dia de nascimento: "))
mes = input("Digite o mês de nascimento: ")

if dia >= 21 and mes == "março" or dia <= 20 and mes == "abril":
    print(" Seu signo é: Áries")
elif dia >= 21 and mes =="abril" or dia <= 20 and mes == "maio":
    print(" Seu signo é: Touro")
elif dia >= 21 and mes == "maio" or dia <= 20 and mes == "junho":
    print(" Seu signo é: Gêmeos")
elif dia >= 21 and mes == "junho" or dia <=22 and mes == "julho":
        print(" Seu signo é: Câncer")
elif dia >= 23 and mes == "julho" or dia <= 22 and mes == "agosto":
    print(" Seu signo é: Leão")
elif dia >= 23 and mes == "agosto" or dia <= 22 and mes == "setembro":
    print(" Seu signo é: Virgem")
elif dia >= 23 and mes == "setembro" or dia <= 22 and mes == "outubro":
    print(" Seu signo é: Libra")
elif dia >= 23 and mes == "outubro" or dia <= 21 and mes == "novembro":
    print(" Seu signo é: Escorpião")
elif dia >= 22 and mes == "novembro" or dia <= 21 and mes == "dezembro":
    print(" Seu signo é: Sagitário")
elif dia >= 22 and mes == "dezembro" or dia <= 20 and mes == "janeiro":
    print(" Seu signo é: Capricórnio")
elif dia >= 21 and mes == "janeiro" or dia <= 18 and mes == "fevereiro":
    print(" Seu signo é: Aquário")
elif dia > 18 and mes == "fevereiro" or dia <= 20 and mes == "março":
    print(" Seu signo é: Peixes")

