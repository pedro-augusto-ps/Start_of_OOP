import time
class Biblioteca:
    '''Essa clase cria uma biblioteca, na qual podemos consultar a disponibilidade de livros e retiralos'''
    def __init__(self, titulo, autor, disponivel):      #Método construtor
        self.titulo = titulo               #Atributos BIBLIOTECA
        self.autor = autor                 #Atributos BIBLIOTECA
        self.disponivel = disponivel       #Atributos BIBLIOTECA

    def __str__(self):                          
        return f"Bem vindo a biblioteca"

    def retirar(self):
        if self.disponivel == True:                             #Método da BIBLIOTECA no qual podemos retirar os livros
            print(f"Retirado com SUCESSO: {self.titulo}")       
            self.disponivel = False
            return True                                         #Retorna TRUE para ser usado depois
        else:
            print(f"Esse livro não está disponível para retirada!")
            return False

    def devolver(self):                                        #Método da BIBLIOTECA no qual podemos devolver os livros
        if self.disponivel == False:
            print(f"Devolvido com SUCESSO {self.titulo}")
        else:
            print(f"Esse livro não está disponível para devolver, ja em ESTOQUE!")
        self.disponivel = True

class Membro:                                       #Criação da classe Membro
    def __init__(self,nome, historico):             #Método construtor
        historico = []                              #Histórico não utilizado até o momento
        self.nome = nome                            #Atributos MEMBRO
        self.historico = historico                  #Atributos MEMBRO

    def solicitar_livro(self, livro_alvo):          #Método que o membro solicita os livros, livro alvo chama o método "solicitar da biblioteca"
        print("Verificando disponibilidade")
        for i in range(3):                #Faz 3 pontinhos em sequência
            print(f".", end=' ')          #Faz 3 pontinhos em sequência
            time.sleep(1)                 #Faz 3 pontinhos em sequência
        if livro_alvo.retirar() == True:    #se o livro que desejamos, no método retirar recebe True, ou seja está disponível, retirado com sucesso
            return f"Livro retirado com SUCESSO"
        else:
            return f"Livro não retirado"

m1 = Membro("Carlos", 0)                   #Instancia, membro 1
l1 = Biblioteca("Poeira em alto mar", "Machado de Assís", True)  #Instancia, livro 1
m1.solicitar_livro(l1)

print(Biblioteca.__doc__)