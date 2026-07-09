class Termostato:
    def __init__(self):
        self.__temperatura = 24

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, nova_temperatura):
        if nova_temperatura % 0.5 != 0:
            print(f"Temperatura inválida, ATUAL: {self.__temperatura}")
        elif nova_temperatura < 16:
            print(f"Temperatura inválida, ATUAL: {self.__temperatura}")
        elif nova_temperatura > 30:
            print(f"Temperatura inválida, ATUAL: {self.__temperatura}")
        else:
            self.__temperatura = nova_temperatura
            print(f"Temperatura válida: ATUAL: {self.__temperatura}")