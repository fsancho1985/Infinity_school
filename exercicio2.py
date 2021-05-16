area = float(input("Digite o valor da área a ser pintada: "))

# 1 lata = R$80,00
# 1 lata = 18 litros = 54m²
# 1 litro = 3 m²

litros = area/3

latas = litros/18

valorTotal = latas * 80

print("latas usadas: {:.2f} e o valor final: R${:.2f}".format(round(latas), valorTotal))