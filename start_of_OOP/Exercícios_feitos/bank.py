class Banco:
    def __init__(self,ide, nome, saldo):
        self.id = ide
        self.nome = nome
        self.saldo = saldo

    def sacar(self, valor):
        print("---SACAR---")
        if valor <= self.saldo:
            self.saldo -= valor    
            print(f"SAQUE no valor de: {valor} realizado, SALDO atual: {self.saldo}")
        else:
            print(f"Operação INVÁLIDA, SAQUE desejado: {valor}, SALDO atual: {self.saldo}")

    def depositar(self, valor):
        print(f"---DEPOSITAR---")
        self.saldo += valor
        print(f"DEPÓSITO de R${valor} realizado, SALDO atual: {self.saldo}")


user000000001 = Banco(777, "Marcos", 100000000)
user000000001.depositar(1)
print("-" * 40)
user000000001.sacar(1)