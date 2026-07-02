from rich import print

class Funcionarios:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self):
        print(f"Olá, me chamo [white]{self.nome}[/] trabalho no setor de [yellow]{self.setor}[/] com o cargo [green]{self.cargo}[/]")

funcionario00000000000001 = Funcionarios("Tenébrio", "CEO", "Presidente")
funcionario00000000000001.apresentar()