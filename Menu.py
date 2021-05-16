valorTotal = 0

while True:
    codigo = input("Digite o codigo do produto: ")
    if codigo == "encerrar":
        break
    qtd = int(input("Digite a quantidade: "))
    
    if codigo == "100":
        valorTotal += 2.20 * qtd
        print("Cachorro quente {}x = R${:.2f}".format(qtd, qtd*2.20))
    elif codigo == "101":
        valorTotal += 2.50 * qtd
        print("Bauru Simples {}x = R${:.2f}".format(qtd, qtd*2.50))
    elif codigo == "102":
        valorTotal += 3.00 * qtd
        print("Bauru com ovo {}x = R${:.2f}".format(qtd, qtd*3.00))
    elif codigo == "103":
        valorTotal += 2.20 * qtd
        print("Hambúrguer {}x = R${:.2f}".format(qtd, qtd*2.20))
    elif codigo == "104":
        valorTotal += 3.30 * qtd
        print("Cheeseburguer {}x = R${:.2f}".format(qtd, qtd*3.30))
    elif codigo == "105":
        valorTotal += 3.00 * qtd
        print("Refrigerante {}x = R${:.2f}".format(qtd, qtd*3.00))

print("Valor total: R${:.2f}".format(valorTotal))
