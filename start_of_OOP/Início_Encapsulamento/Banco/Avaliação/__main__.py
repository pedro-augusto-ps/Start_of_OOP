from rich import print, inspect
from Classes_nota_getters_setters import *

def main():
    avaliacao1 = Avaliacao("Pedro","Programação", 8)
    avaliacao1.set_nota(11111)
    inspect(avaliacao1, private=True)


if __name__ == "__main__":
    main()