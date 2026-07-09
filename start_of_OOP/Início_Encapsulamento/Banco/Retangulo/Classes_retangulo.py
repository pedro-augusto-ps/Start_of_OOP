from rich import print, inspect

class Retangulo:
    def __init__(self):
        self._altura = 0
        self._base = 0

    @property
    def base(self):
        return self._base 

    @base.setter
    def base(self, nova_b):
        if nova_b <= 0:
            print(f"Invalida")
        else:
            self._base = nova_b

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, nova_a):
        if nova_a <=0:
            print(f"INVALIDO!")
        else:
            self._altura = nova_a

    @property
    def area(self):
        return self._altura * self._base

    @property
    def medidas(self):
        return [self._altura, self._base]
    
b1 = Retangulo()
b1.base = 10
inspect(b1)
b1.altura = 10
inspect(b1)
b1.base = -10
inspect(b1)
