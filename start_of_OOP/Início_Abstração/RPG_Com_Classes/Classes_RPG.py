from abc import ABC,abstractmethod  #USADA PARA FAZER A CLASSE E MÉTODO ABSTRATO
from rich import print              #Personalizar o terminal
import random                       #Fazer o sorteio de dano e golpes

class Personagem(ABC):                      #Criação da classe ABSTRATA PERSONAGEM
    def __init__(self, nome, vida):     #Metodo construtor, nome e vida atributos, 
        self.nome = nome                #golpes lista vazia são adicionados dps
        self.vida = vida
        self.golpes = []

    def atacar(self,alvo, forca):           #ATAQUE: forca foi passada como parametro, é sorteado e tira de (alvo.vida
        forca = random.randint(5,20)        #"OBS:alvo.vida é o alvo que inserimos como parametro no main"))
        alvo.vida -= forca
        print(f"[orange3]ATAQUE[/]: {self.nome} atinge {alvo.nome} com {random.choice(self.golpes)}, causando {forca} de [red]dano[/].")
        print(f"{alvo.nome} [green]VIDA[/]: {alvo.vida}")
        return alvo.vida

    def receber_dano(self, dano, golpe):    #RECEBER DANO: meio redundante nessa ocasião, porém o vídeo pedia mas fiz um pouco diferente
        dano = random.randint(1, 10)        #Dano é passado como parametro no main e tira da vida do objeto o  dano correspóndente
        self.vida -= dano
        print(f"[orange3]ATAQUE[/]: {golpe} Surge devastando a arena, {self.nome} desvia")
        print(f"Porém não impune, o corte atinge suavemente seu corpo.")
        print(f"[red]DANO: {dano}")
        print(f"{self.nome} [green]VIDA[/]: {self.vida}")
        return self.vida

    @abstractmethod         #METODO ABSTRATO, cada  personagem cura da sua forma!
    def curar(self):
        pass

class Guerreiro(Personagem):
    def __init__(self, nome, vida):         #MÉTODO CONSTRUTOR do GUERREIRO
        super().__init__(nome, vida)        #Atributos da classe pai
        self.golpes = ("Fúria Ardente", "Lâmina do caos", "A ultima Opção")  #TUPLA: Golpes que o guerreiro tem

    def curar(self):        
        print(f"{self.nome} Brande sua [red]Lâmina[/] no chão. +10HP")
        self.vida += 10

class Mago(Personagem):
    def __init__(self, nome, vida):         #MÉTODO CONSTRUTOR do MAGO
        super().__init__(nome, vida)        #Atributos da classe pai
        self.golpes = ("Bola de fogo", "Energia Cósmica", "Meteoro Divino")   ##TUPLA:Golpes que o mago tem

    def curar(self):
        print(f"{self.nome}utiliza a [yellow]Sagrada[/] magia de cura. +30HP")
        self.vida += 30