from Classes_RPG import *               #Importaçao de todas as classes
from abc import ABC,abstractmethod      #USADA PARA FAZER A CLASSE E MÉTODO ABSTRATO
from rich import print                  #Personalizar o terminal
import time                             #Simular uma espera no combate
import random                           #Sortear o dano e golpes

guerreiro1 = Guerreiro("Pedro",100)
mago1 = Mago("Timoteo", 30)
forca = 0
dano = 0
while True:
    if guerreiro1.vida <= 0:
        guerreiro1.vida = 0
        print(f"Essa batalha [black]chegou ao fim.[/]")
        print(f"[green]VIDA[/] de {guerreiro1.vida}")
        print(f"[green]VIDA[/] de {mago1.vida}")
        break

    elif mago1.vida <= 0:
        mago1.vida = 0
        print(f"A batalha foi justa, porém você foi devorado.")
        print(f"[green]VIDA[/] de {guerreiro1.vida}")
        print(f"[green]VIDA[/] de {mago1.vida}")
        break
    else:
        guerreiro1.atacar(mago1, forca)   #guerreiro ataque o mago, forca é passada como parametro, calcul feito na funcao
        mago1.curar()
        print("-"*55)
        time.sleep(3)

        mago1.atacar(guerreiro1, forca)   #mesma coisa, porem o mago ataca o guerreiro
        guerreiro1.curar()
        print("-"*55)
        time.sleep(3)

