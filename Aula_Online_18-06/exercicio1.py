# variaveis

indice = 1
media = 0
multiplosDeTres = 0

while(indice == 1):
    numero = int(input("digite seu número: "))
    
    if(numero ==0):
        indice = 0
        
    if(numero % 3 == 0 and numero != 0):
        media += numero
        multiplosDeTres += 1
        
print("A médida dos números é: ", multiplosDeTres)