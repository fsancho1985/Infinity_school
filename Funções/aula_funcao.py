"""def calculadora(n1, n2):
    return n1 * n2
y = 0
x = int(input("Digite o 1º número: "))
while y < 10:
    y = y+1
    print(calculadora(x,y))"""

limite = int(input("Digite um valor para o limite: "))
def calculadora(n1, limite):
    y = 0
    while y < limite:
        y += 1
        print(n1 * y)

x = int(input("Digite o 1º número: "))
print(calculadora(x, limite))


