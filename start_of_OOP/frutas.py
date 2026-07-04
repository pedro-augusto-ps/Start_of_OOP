class Frutas:
    def __init__(self,nome, cor, preco):
        self.nome = nome
        self.cor = cor
        self.preco = preco

    def aumentar(self):
        qual = str(input("Qual fruta aumentará de valor? "))
        quanto = float(input("Quanto vai aumentar? "))
        for frutas in Frutas:
            if frutas == self.nome:
                return self.preco + quanto
            else:
                print("Nao deu")
                return self.preco
        
morango = Frutas("Morango", "Vermelho", 10)
morango.aumentar()