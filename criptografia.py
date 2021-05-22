#opcao = input("Deseja codificar ou decodificar? (C/D): ")

frase = input("Digite um texto: ")

novoTexto = ""

alfabeto1 = "abcdefghijklm "
alfabeto2 = "nopqrstuvwxyz "


indice = 0

for letra in frase.lower():
    indice = 0
    for i in alfabeto1:
        if letra == i:
            novoTexto += alfabeto2[indice]
            break
        else:
            indice += 1
    indice = 0
    for i in alfabeto2:
        if letra == i:
            novoTexto += alfabeto1[indice]
            break
        else:
            indice += 1

print(novoTexto)

