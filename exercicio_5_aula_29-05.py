def fatorial(n1):
    resultado = 1
    for i in range(1, n1+1):
        resultado *= i
    return resultado
        
numero = int(input("Digite um número: "))

print(fatorial(numero))
