x = int(input("Digite um número para receber sua tabuada: "))
cont = 0
print("Entrada: {}".format(x))
while cont < 100:
    cont +=1
    tabuada = x*cont
    print("{}".format(x), " . ", "{}".format(cont), " = ", "{}".format(tabuada))


#print("=====================")

#numero = int(input("Digite um número: "))

#print("Tabuada de: {}".format(numero))

for i in range(1, 101):
    print("{} x {} = {}".format(numero, i, numero*1))
