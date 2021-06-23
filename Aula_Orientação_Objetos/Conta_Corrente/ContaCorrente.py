<<<<<<< HEAD
class ContaCorrente:
    def __init__(self, numero, senha, banco = "010", agencia = "515", saldo = 1500.00):
        self.numero = numero
        self.senha = senha
        self.banco = banco
        self.agencia = agencia
        self.saldo = saldo
        

    # Método de saque

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor # self.saldo = self.saldo - valor
            return True
        else:
            return False

    # Método de transferência

    def transferir(self, contaDestino, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            contaDestino.saldo += valor
            return True
        else:
            return False

    # Método de depositar

    def depositar(self, valor):
=======
class ContaCorrente:
    def __init__(self, numero, senha, banco = "010", agencia = "515", saldo = 1500.00):
        self.numero = numero
        self.senha = senha
        self.banco = banco
        self.agencia = agencia
        self.saldo = saldo
        

    # Método de saque

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor # self.saldo = self.saldo - valor
            return True
        else:
            return False

    # Método de transferência

    def transferir(self, contaDestino, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            contaDestino.saldo += valor
            return True
        else:
            return False

    # Método de depositar

    def depositar(self, valor):
>>>>>>> 525c9be650c00ce336742307918a19c40163cd01
        self.saldo += valor