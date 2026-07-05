class Filme():
    def __init__(self, titulo, descricao, arquivo_video):
        print("Estou criando um filme")

    def assistir_filme(self):
        duracao = self.calcular_duracao_filme()
        print("Dar play no arquivo de video do filme que tem", duracao, "minutos de duração")

    def calcular_duracao_filme(self):
        # varios comandos para calcular a duracao do filme
        return 130

filme1 = Filme("A volta dos que nao foram", "Filme TOP", 1)

filme1.assistir_filme()

