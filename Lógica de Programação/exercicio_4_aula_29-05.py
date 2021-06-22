def somatorio(n1):
    resultado = 0
    for i in range(1, n1+1):
        resultado += i
    return resultado
        
numero = int(input("Digite um número: "))

print(somatorio(numero))
    