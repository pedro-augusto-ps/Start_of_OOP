class Gamer:
    def __init__(self,nome, nick, jogos_fav):
        self.nome = nome
        self.nick = nick
        self.jogos_fav =  jogos_fav
    def add_game(self,add_jogo):
        self.jogos_fav.append(add_jogo)

    def mostrar_fav(self):
        print(f"JOGOS FAVORITOS DE(O): {self.nome}")
        print(f"LISTA: {sorted(self.jogos_fav)}")


gamer000000000001 = Gamer("Pedro", "PedryZz", ["Outer Wilds","Terraria","Elden Ring","Bloodbone"])
gamer000000000001.mostrar_fav()
gamer000000000001.add_game("COD")
gamer000000000001.mostrar_fav()
