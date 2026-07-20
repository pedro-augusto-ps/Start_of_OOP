from abc import ABC, abstractmethod

class Fruta(ABC):
    def __init__(self, nome, cor, preco):
        self.nome = nome
        self.cor = cor
        self.preco = preco

    @abstractmethod
    def mudar_preco(self):
        pass

class Banana(Fruta):
    def __init__(self, nome, cor, preco):
        super().__init__(nome, cor, preco)

    def mudar_preco(self, novo_preco):
        if novo_preco <= 3:
            return
        else:
            self.preco = novo_preco

class Maça(Fruta):
    def __init__(self, nome, cor, preco):
        super().__init__(nome, cor, preco)

    def mudar_preco(self, novo_preco):
        if novo_preco <= 4:
            return
        else:
            self.preco = novo_preco

class Mercado:
    def __init__(self, nome, fruta, fruta2):
        self.nome = nome
        self.fruta = fruta
        self.fruta2 = fruta2

    def frutas(self):
        print(self.fruta)
        print(self.fruta2)


m = [[0 for j in range(2)]for i in range(2)]

for i in range(2):
    for j in range(2):
        m[i][j] = int(input("Insira: "))

for i in range(2):
    for j in range(2):
        print(m[i][j], end='')
    print()


l1 = []


for i in range(3):
    l1.append(int(input("Insira: ")))

print(l1)
for i in range(3):
    for j in range(i+1, 3):
        if l1[i] > l1[j]:
            aux = l1[i]
            l1[i] = l1[j]
            l1[j] = aux
print(l1)