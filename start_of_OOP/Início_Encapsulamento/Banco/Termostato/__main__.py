from rich import print,inspect
from Classes_termostato import *

def main():
    temp1 = Termostato()
    inspect(temp1,private=True,methods=True)
    temp1.temperatura = 1
    temp1.temperatura = 11232
    inspect(temp1,private=True,methods=True)
    temp1.temperatura = 31.2
    temp1.temperatura =25
    temp1.temperatura = 30
    inspect(temp1,private=True,methods=True)

if __name__ ==  "__main__":
    main()