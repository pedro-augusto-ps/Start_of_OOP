from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0

    @abstractmethod
    def calc_frete(self):
        pass

class Moto(Transporte):
    fator = 0.50
    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        self.frete = self.distancia * self.fator
        print(f"O frete para moto em {self.distancia} é de: {self.frete}")
        return self.distancia * self.fator

class Caminhao(Transporte):
    fator = 1.20
    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        if self.distancia < 50:
            print("Distância precisa ultrapassar 50KM!")
        else:
            self.frete = self.distancia * self.fator
            print(f"O frete para CAMINHAO em {self.distancia} é de: {self.frete}")
            return f"O frete para CAMINHAO em {self.distancia} é de: {self.frete}"

class Drone(Transporte):
    fator = 9.5
    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        if self.distancia > 10:
            print("O drone infelizmente só póde ir até 10KM")
        else:
            self.frete = self.distancia * self.fator
            print(f"O frete para CAMINHAO em {self.distancia} é de: {self.frete}")            
            return self.distancia * self.fator

dist  =  50
fretes = [Moto(dist), Caminhao(dist),  Drone(dist)]
for frete in fretes:
    frete.calc_frete()