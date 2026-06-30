class MoldeBola:
    def __init__(self, cor, circunferencia, material):  
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocar_cor(self):  
        self.cor = str(input("Insira a nova cor: "))
        print(f"Nova cor: {self.cor}")
    def mostrar_cor(self):         
        print(f"A cor é: {self.cor}")

bola1 = MoldeBola("Azul", 2.0, "Metal")

print(f"Bola da cor {bola1.cor} da circunferencia {bola1.circunferencia} e material {bola1.material}")

trocar = str(input("trocar de cor?"))

if trocar == "S".lower():
    bola1.trocar_cor()
    print(f"Bola atualizado!")
    print(f"Bola NOVA: {bola1.cor} circunferencia: {bola1.circunferencia} material {bola1.material}")
else:
    print("Blz cara, n vm mudar nada")

