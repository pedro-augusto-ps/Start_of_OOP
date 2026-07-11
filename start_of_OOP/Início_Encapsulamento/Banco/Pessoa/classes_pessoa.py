from abc import ABC,abstractmethod
from rich import print, inspect

class Pessoa(ABC):
    def __init__(self, nome, nascimento):
        self._nome = nome
        self._nascimento = nascimento

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, novo_nascimento):
        if novo_nascimento == self._nascimento or novo_nascimento > 2026:
            print(f"Data inválida!")
        else:
            self._nascimento = novo_nascimento
            
    @property
    def idade(self):
        return 2026 - self._nascimento

class Aluno(Pessoa):
    def __init__(self, nome, nascimento, curso):
        super().__init__(nome, nascimento)
        self.cursos_oficiais = ["ADM", "ENG", "BIO", "CC"]
        self._curso = curso

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, novo_curso):
        if novo_curso in self.cursos_oficiais:
            self._curso = novo_curso
        else:
            print(f"Este curso não consta na lista oficial, porfavor adicione ele primeiro!")
            return None

    def add_curso(self, curso):
        if len(curso) > 5:
            print(f"Use abreviaturas.")
        else:
            self.cursos_oficiais.append(curso)


a1 = Aluno("Miguel", 2000, "CC")
inspect(a1, private=True, methods=True)
a1.nascimento = 1999
inspect(a1, private=True, methods=True)
a1.curso = "Senior Programmer"
inspect(a1, private=True, methods=True)
a1.curso = "ADM"
inspect(a1, private=True, methods=True)
a1.add_curso("CONTA")
inspect(a1, private=True, methods=True)


