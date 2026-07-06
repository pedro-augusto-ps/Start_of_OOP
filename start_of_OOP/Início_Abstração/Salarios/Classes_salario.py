from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, salario_bruto, salario_minimo, inss):
        self.nome = nome
        self.salario_bruto = salario_bruto
        self.salario_minimo = 1612
        self.inss = 7.5

    @abstractmethod
    def calc_salario(self):
        pass

    def analisar_salario(self):
        print(f"O salário mínimo atual é de: {self.salario_minimo}")
        print(f"O salário do(a) é de: {self.calc_salario()}")
        print(f"O salário d0(a) é {self.calc_salario()/self.salario_minimo}Vezes o salário mínimo!")

class Horista(Funcionario):
    def __init__(self,nome, valor_hora, horas_trabalhadas):
        super().__init__(nome, 0, 1612, 7.5)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas

    def calc_salario(self):
        print(f"O calculo de salário de {self.nome} deu: {self.valor_hora * self.horas_trabalhadas}")
        return self.valor_hora * self.horas_trabalhadas

horista1 = Horista("Pedro",100000000,1)
horista1.calc_salario()