op = input("Digite a operação: ")
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if op == '+':
    print("{} + {} = {}".format(numero1,numero2,numero1+numero2))
elif op == '-':
    print("{} - {} = {}".format(numero1,numero2,numero1-numero2))
elif op == '*':
    print("{} * {} = {}".format(numero1,numero2,numero1*numero2))
elif op == '/':
    print("{} / {} = {}".format(numero1,numero2,numero1/numero2))
elif op == '%':
    print("{} % {} = {}".format(numero1,numero2,numero1%numero2))
elif op == '^':
    print("{} ^ {} = {}".format(numero1,numero2,numero1**numero2))
else:
    print("Operação inválida!")