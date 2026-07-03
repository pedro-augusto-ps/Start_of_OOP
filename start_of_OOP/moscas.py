class Fro:
    def __init__(self, tipo, tamanho):
        self.tipo = tipo
        self.tamanho = tamanho
          

    def __str__(self):
        return f"Sou uma fro do tipo: {self.tipo} meu tamanho é {self.tamanho}"

    def voar(self):
        print("Estou voando!")
        return 0


fro1 = Fro("verde", "Enorme")
fro2 = Fro("azul", "Pequena")

print(fro1)
print(fro2)
fro1.voar()
fro2.voar()
