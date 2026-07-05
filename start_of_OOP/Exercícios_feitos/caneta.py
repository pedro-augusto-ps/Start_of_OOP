from rich import print

class Caneta:
    def __init__(self,cor):
        self.cor = cor

    def escrever(self):
        texto = str(input("Insira:"))
        print(f"[{self.cor}]{texto}[/]")

caneta1 = Caneta("blue")
caneta2 = Caneta("red")
caneta3 = Caneta("black")
caneta1.escrever()
caneta2.escrever()
caneta3.escrever()