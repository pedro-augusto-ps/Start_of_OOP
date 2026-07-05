from rich import print,inspect
from Classes import Pessoa, Aluno, Professor, Funcionario

p1 = Pessoa("Carlos", 29)     #antes de ver abstração fiz isso kkkkkkkk
a1 = Aluno("Carlos", 20, "CC", "Primeira")
a1.fazer_aniversario()
print(a1)
print(a1.__dict__)
#inspect(a1,methods=True) 
