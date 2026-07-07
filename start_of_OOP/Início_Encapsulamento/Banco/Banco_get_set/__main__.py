from start_of_OOP.Início_Encapsulamento.Banco.Banco_get_set.Banco import *


def main():
    user000000000001 = Banco("777","Carlos",2000)
    user000000000001.sacar(500)
    user000000000001.depositar(100)
    user000000000001.__saldo = 0
    user000000000001.nome ="João"      #Nao trocou o nome, criou outro atributo chamado João
    user000000000001._nome = "Pericio" #Troucou o atributo.
    print(user000000000001) 

if __name__ == "__main__":
    main()