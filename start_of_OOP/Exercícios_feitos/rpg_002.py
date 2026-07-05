class Heroi:
    def __init__(self, nome, classe_jogo, vida, energia):
        self.nome = nome
        self.classe_jogo = classe_jogo
        self.vida = vida
        self.energia = energia

    def atacar(self, custo_energia):
        ataque = 5
        if self.energia >= custo_energia:
            print(f"ATACANDO dano dado: {ataque}")
            self.energia -= custo_energia
        else:
            print(f"ENERGIA insuficiente: ")

    def receber_dano(self, dano_inimigo):
        print(f"Dano tomado: {dano_inimigo}")
        if self.vida < 0:
            self.vida = 0
            if self.vida == 0:
                print(f"recalculando rota")
    def status(self):
        print(f"NOME: {self.nome} CLASSE: {self.classe_jogo} VIDA: {self.vida} ENERGIA: {self.energia}")


heroi1 = Heroi("Tuffo", "Guerreiro", 100, 10)
heroi1.atacar(1)
heroi1.receber_dano(10)
heroi1.status()