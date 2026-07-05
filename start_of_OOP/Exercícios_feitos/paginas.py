
class Livro:
    def __init__(self,nome, autor, qtd_paginas, pg_atual):
        self.nome = nome
        self.autor = autor
        self.qtd_paginas = qtd_paginas
        self.pg_atual = pg_atual
    def passar_pagina(self):
        if self.pg_atual < self.qtd_paginas:
            self.pg_atual += 1
            print(f"Página atual: {self.pg_atual}")
            return self.pg_atual
        else:
            print(f"Sem páginas para passar!")
            return self.pg_atual
    def  voltar_pagina(self):
        if self.pg_atual > 0:
            self.pg_atual -= 1
            print(f"Pagina atual:  {self.pg_atual}")
            return self.pg_atual
        else:
            print(f"Não pode voltar")
            return self.pg_atual

l1 = Livro("Clarissa", "Erico Verssimo", 5 ,0)

l1.passar_pagina()

for  i in range(7):
    l1.voltar_pagina()