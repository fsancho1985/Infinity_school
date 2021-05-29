numero = int(input("Digite um número: "))
fatorial = 1
print("Fatorial de {}".format(numero),"!")

for i in range(numero, 1, -1):
    fatorial *= i
print("{}! = {}".format(numero, fatorial))

#from math import factorial

#n = int(input('Informe um algarismo:  '))
#print('O fatorial de {} é : {}'.format(n,factorial(n))
