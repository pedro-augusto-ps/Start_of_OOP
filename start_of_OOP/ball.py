class MoldeBola:
    def __init__(self,cor, circunferencia, material):  #atributos
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocar_cor(self, cor):  #metodo de instancia?
        MoldeBola.cor = str(input("Insira a nova cor: "))

    def mostrar_cor(self, cor):         #metodo de instancia?
        print(f"A cor é: {self.mostrar_cor}")
MoldeBola.cor = str(input("Insira a cor: "))
MoldeBola.circunferencia = int(input("Insira a circunferencia: "))
MoldeBola.material = str(input("Insira o mat: "))

print(f"Bola da cor {MoldeBola.cor} da circunferencia {MoldeBola.circunferencia} e material {MoldeBola.material}")
trocar = str(input("trocar de cor?"))
if trocar == "S".lower():
    MoldeBola.trocar_cor(self, cor)
