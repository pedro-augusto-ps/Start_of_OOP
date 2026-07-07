class Banco:
    """Cria um sistema bancário"""
    def __init__(self,ide, nome, saldo):
        self.ide = ide          #Atributo público(+)
        self._nome = nome       #Atributo protegido(#)
        self.__saldo = saldo    #Atributo privado(-)

    def sacar(self, valor):
        print("---SACAR---")
        if valor <= self.__saldo:
            self.__saldo -= valor    
            print(f"{self._nome}, SAQUE no valor de: {valor} realizado, saldo atual: {self.__saldo}")
        else:
            print(f"Operação INVÁLIDA, SAQUE desejado: {valor}, saldo atual: {self.__saldo}")

    def __str__(self):
        return f"Status: {self.__dict__}"
    def depositar(self, valor):
        print(f"---DEPOSITAR---")
        self.__saldo += valor
        print(f"DEPÓSITO de R${valor} realizado, saldo atual: {self.__saldo}")


