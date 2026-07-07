from abc import ABC, abstractmethod
from rich import print

class Funcionario(ABC):
    def __init__(self, nome, salario_bruto):
        self.nome = nome
        self.salario_bruto = salario_bruto
        self.salario_minimo = 1612
        self.inss = 18

    @abstractmethod
    def calc_salario(self):
        pass

    def analisar_salario(self,salario_calculado):
        print(f"O salário mínimo atual é de: {self.salario_minimo}")
        print(f"O salário do(a) {self.nome} já calculado é de: {salario_calculado}")
        print(f"O salário de(a) é {salario_calculado / self.salario_minimo:.2f}Vezes o salário mínimo!")

class Horista(Funcionario):
    def __init__(self,nome, valor_hora, horas_trabalhadas):
        super().__init__(nome, 0)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas

    def calc_salario(self):
        print(f"O calculo de salário de {self.nome} deu: {self.valor_hora * self.horas_trabalhadas}")
        salario_calculado = self.valor_hora * self.horas_trabalhadas 
        return salario_calculado

class Mensalista(Funcionario):
    def __init__(self,nome,salario_bruto):
        super().__init__(nome, salario_bruto)
    def calc_salario(self):
        descontado = self.salario_bruto * (self.inss / 100)
        salario_calculado = self.salario_bruto - descontado
        print(f"Salário mínimo atual: [green]R${self.salario_minimo}[/]")
        print(f"Seu salário bruto: [green]{self.salario_bruto}[/]")
        print(f"Seu salário com o desconto atual do [black]INSS: {self.inss}[/], é de: [green]{salario_calculado:.2f}")
        print(f"Seu sálario é [red]{salario_calculado / self.salario_minimo:.2f}[/] Vezes o salário mínimo atual.")
        return salario_calculado
    
print("-"*40)
mensalista1 = Mensalista("Carlos",3431)
salario_calculado = mensalista1.calc_salario()
mensalista1.analisar_salario(salario_calculado)
