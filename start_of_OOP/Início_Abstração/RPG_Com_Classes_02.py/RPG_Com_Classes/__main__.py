from Classes_RPG import *               #Importaçao de todas as classes
from abc import ABC,abstractmethod      #USADA PARA FAZER A CLASSE E MÉTODO ABSTRATO
from rich import print                  #Personalizar o terminal
import time                             #Simular uma espera no combate
import random                           #Sortear o dano e golpes

guerreiro1 = Guerreiro("Pedro",100)
mago1 = Mago("Timoteo", 30)
while True:
    if guerreiro1.vida <= 0:                                #Testes para ver se os combatentes estão vivos
        guerreiro1.vida = 0                                 
        print(f"Essa batalha [black]chegou ao fim.[/]")
        print(f"[green]VIDA[/] de {guerreiro1.vida}")
        print(f"[green]VIDA[/] de {mago1.vida}")
        break

    elif mago1.vida <= 0:                                   #Testes para ver se os combatentes estão vivos
        mago1.vida = 0
        print(f"A batalha foi justa, porém você foi devorado.")
        print(f"[green]VIDA[/] de {guerreiro1.vida}")
        print(f"[green]VIDA[/] de {mago1.vida}")
        break

    else:                                     #SE ambos estão vivos, ENTÃO continue o combate
        guerreiro1.atacar(mago1)              #Guerreiro ataca mago1
        if mago1.vida <= 0:                   #TESTE para vida do mago1 não aparecer negativa
            mago1.vida = 0                    #TESTE para vida do mago1 não aparecer negativa
            continue                                         
        print("-"*55)
        time.sleep(3)

        mago1.atacar(guerreiro1) 
        if guerreiro1.vida <=0:                #TESTE para vida do guerreiro não aparecer negativa
            guerreiro1.vida = 0                #TESTE para vida do guerreiro não aparecer negativa
            continue                
        guerreiro1.curar()
        print("-"*55)
        time.sleep(3)

