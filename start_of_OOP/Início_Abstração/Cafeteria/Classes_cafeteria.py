from abc import ABC,abstractmethod

class Bebida_quente(ABC):
    def preparar(self):
        print("Preparando...")
        self.ferver_agua()
        self.misturar()
        self.servir()

    def ferver_agua(self):
        print(f"Estou fervendo água!")

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

class Cafe(Bebida_quente):
    def misturar(self):
        print(f"Estou misturando o CAFÉ!")

    def servir(self):
        print(f"Estou servindo o CAFÉ")

class Cha(Bebida_quente):
    def misturar(self):
        print("Estou misturando o CHÁ!")

    def servir(self):
        print("Servindo o CHÁ!")

class Leite(Bebida_quente):
    def misturar(self):
        print("Estou misturando o LEITE!")

    def servir(self):
        print("Servindo o LEITE!")

bebida = Leite()
bebida.preparar() 