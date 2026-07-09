class Diario:
    def __init__(self):
        self.__segredos = []
        self.__senha = 6767

    def escrever(self, msg):
        self.__segredos.append(msg)

    def ler(self, senha):
        if senha != self.__senha:
            print(f"Não vai ler!")
        else:
            print(self.__segredos)
    @property
    def senha(self):
        raise PermissionError("Nao pode LER!!!")
    
    @senha.setter
    def senha(self,nova_senha):
        self.__senha = nova_senha
        print("Mudei a senha")
        
a1 = Diario()
a1.escrever("Fala bacanao")
a1.escrever("Se ta doido motorista")
a1.escrever("08 do 07 de 2026")
a1.ler(5454)
a1.ler(6767)
a1.senha = 1
a1.ler(6767)
a1.ler(1)