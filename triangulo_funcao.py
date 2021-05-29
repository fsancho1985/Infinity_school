def calcula_triangulo(n1, n2):
    return (n1*n2)/2

p =input("Deseja calcular um triangulo? S/N: " )

while p.upper() == "S":
    base = float(input("Digite o valor da base: "))
    altura = float(input("Digite o valor da altura: "))
    print(calcula_triangulo(base, altura))

    p =input("Deseja calcular outro triangulo? S/N: " )
    if p.upper() == "N":
        print("Tchau obrigado!")
