from rich import print

class Churrasco:
    def __init__(self, titulo, quantia_pessoas):
        self.titulo = titulo 
        self.quantia_pessoas = quantia_pessoas

    def quantos_kg(self):  #400 gm por cabeça
        quantia_de_carne = self.quantia_pessoas * 400
        quantia_de_carne = quantia_de_carne / 1000   #divide por mil pois esta em gramas
        print(f"A quantia de [red]CARNE[/] é de [orange]{quantia_de_carne}KG[/]")
        return quantia_de_carne
    
    def preço(self, quantia_de_carne):
        print(f"O [green]PREÇO[/] por KG é de: [green]82.48[/]")
        print(f"TOTAL a pagar: [green]{quantia_de_carne * 82.48}R$[/]")
        return quantia_de_carne * 82.48   #preço por kilo
    
    def preco_pessoa(self, preco_total_churrasco):
        print(f"O [green]PREÇO[/] por [yellow]PESSOA[/] é de: [green]{preco_total_churrasco/self.quantia_pessoas}R$[/]")

churas1 = Churrasco("Churas dos guri", 20) #20 pessoas
carne_necessaria = churas1.quantos_kg()
preco_total_churrasco = churas1.preço(carne_necessaria)
churas1.preco_pessoa(preco_total_churrasco)