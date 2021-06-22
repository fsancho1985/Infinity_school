# Função soma
def soma(n1, n2):
    return n1 + n2

# Função subtração
def sub(n1, n2):
    return n1 - n2

# Função multiplicação
def mult(n1, n2):
    return n1 * n2

# Função divisão
def div(n1, n2):
    if n2 == 0:
        return "erro"
    else:    
        return n1 / n2

x = float(input("Digite um valor: "))
y = float(input("Digite outro valor: "))
op = input("Digite a operação desejada: ")

if op == "+":
    print(soma(x,y))
elif op == "-":
    print(sub(x,y))
elif op == "*":
    print(mult(x,y))
elif op == "/":
    print(div(x,y))
else:
    print("erro")

