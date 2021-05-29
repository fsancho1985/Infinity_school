def ordenar(n1, n2, n3):
    retorno1 = 0
    retorno2 = 0
    retorno3 = 0
    
    if n1 >= n2 and n1 >= n3:
        if n2 > n3:
            retorno1 = n3
            retorno2 = n2
            retorno3 = n1
        else:
            retorno1 = n2
            retorno2 = n3
            retorno3 = n1
    elif n2 >= n1 and n2 >= n3:
        if n1 > n3:
            retorno1 = n3
            retorno2 = n1
            retorno3 = n2
        else:
            retorno1 = n1
            retorno2 = n3
            retorno3 = n2
    if n3 >= n1 and n3 >= n2:
        if n2 > n1:
            retorno1 = n1
            retorno2 = n2 
            retorno3 = n3
        else:
            retorno1 = n2
            retorno2 = n1
            retorno3 = n3
            
    return retorno1, retorno2, retorno3

x = int(input("Digite o número desejado: "))
y = int(input("Digite outro número desejado: "))
z = int(input("Digite outro número: "))

print(ordenar(x,y,z))
