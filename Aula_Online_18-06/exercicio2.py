indice = 1
primos = 0

while(indice == 1):
    numero = int(input("Digite um número: "))
    
    if(numero == 1):
        primos += numero
    elif(numero == 2):
        primos += numero
    elif(numero ==3):
        primos += numero
    elif(numero % 3 != 0 and numero % 2 != 0 and numero % 5 != 0):
        primos += numero
    elif(numero == 0):
        indice = 0
print(primos)