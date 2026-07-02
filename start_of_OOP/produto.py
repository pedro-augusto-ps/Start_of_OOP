class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        print(f"PRODUTO: {self.nome} PREÇO: {self.preco}")

produto0000001 = Produto("Banana", 3.5)
produto0000001.etiqueta()