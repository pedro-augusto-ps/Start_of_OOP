###Criacao da clase

class Tartarugas:
    def __init__(self, nome, tipo, genero, casco):   #atributos
        self.nome = nome   #self.nome significa oque? 
        self.tipo = tipo    #o objeto tipo recebe tipo?
        self.genero = genero
        self.casco = casco

    def __str__(self):   #pra que serve isso? e porque recebe self como parametro?
        print(f"Tartaruga {self.nome} do gênero {self.genero} do tipo {self.tipo} e casco {self.casco}")

Tartarugas.nome = (str(input("Insira o nome da Tartaruga")))
Tartarugas.tipo = (str(input("Insira o tipo da Tartaruga")))
Tartarugas.genero = (str(input("Insira o genero da Tartaruga")))
Tartarugas.casco = (str(input("Insira o casco da Tartaruga")))

print(f"Tartaruga {Tartarugas.nome} do gênero {Tartarugas.genero} do tipo {Tartarugas.tipo} e casco {Tartarugas.casco}")