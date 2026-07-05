from abc import ABC,abstractmethod
from rich import print,inspect

class Poligno(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Quadrado(Poligno):
    def  __init__(self, lado):
        super().__init__(4)
        self.lado = lado

    def perimetro(self):
        total_perimetro = 0
        for i in range(self.qtd_lados):
            total_perimetro += self.lado
        return total_perimetro

    def area(self):
        total_area = self.lado**2
        return total_area

class Circulo(Poligno):
    def __init__(self, qtd_lados, raio):
        super().__init__(qtd_lados)
        self.raio = raio

    def perimetro(self):
        total_perimetro = 2 * 3.14 * self.raio
        return total_perimetro

    def area(self):
        total_area = 3.14*(self.raio**2)
        return total_area

