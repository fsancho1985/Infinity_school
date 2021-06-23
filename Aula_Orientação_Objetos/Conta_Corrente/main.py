from ContaCorrente import ContaCorrente

conta = ContaCorrente("1999", "admin")
print(conta.numero)
print(conta.agencia)

"""if(conta.sacar(int(input("Digite o valor que deseja sacar: ")))):
    print("Saque realizado com sucesso!")
else:
    print("Saldo insuficiente!")
"""
print(conta.saldo)

conta2 = ContaCorrente("1998", "admin2")
print(conta2.numero)
print(conta2.agencia)

"""if(conta.transferir:#(input("Digite a conta para transferência: "), \
    #float(input("Digite o valor a ser transferido: "))):
    print("Transferência realizada!")
else:
    print("Saldo insuficiente para transferência!")"""

if(conta.transferir(conta2, 1000)):
    print("transferencia realizada")
else:
    print("Saldo insuficiente")

print("Saldo conta 1", conta.saldo)
print("Saldo conta 2", conta2.saldo)

conta.depositar(1000)
print("Saldo conta 1", conta.saldo)