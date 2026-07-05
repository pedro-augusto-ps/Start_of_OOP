from Classes import Poligno,Quadrado,Circulo
from abc import ABC,abstractmethod
from rich import print,inspect,panel

###Crindo objetos

quadrado1 = Quadrado(10)
quadrado2 = Quadrado(5)
circulo1 = Circulo(0, 10)
circulo2 = Circulo(0, 4)


#quadrado 1
print("[green]QUADRADO 1[/]")
print(f"PERÍMETRO: {quadrado1.perimetro()}")
print(f"ÁREA: {quadrado1.area()}")
#quadrado2
print("[green]QUADRADO 2[/]")
print(quadrado2.perimetro())
print(quadrado2.area())
#circulo1
print("[green]CIRCULO 1[/]")
print(f"{circulo1.perimetro():.2f}")   #Aqui é a circunferencia
print(circulo1.area())