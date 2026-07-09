import hashlib

#texto = "Alo"
#codificado = texto.encode('utf-8')
#has = hashlib.sha384(codificado).hexdigest()

#print(has)

class Credencial:
    def __init__(self):
        self.__hash = None

    def validar(self, chave):
        chave = hashlib.sha256(chave.encode('utf-8')).hexdigest()
        if chave == self.__hash:
            print(f"Correto")
        else:
            print("INVALIDO!")

    @property
    def chave(self):
        return self.__hash

    @chave.setter
    def chave(self, chave):
        codificado = chave.encode('utf-8')
        texto = hashlib.sha256(codificado).hexdigest()
        self.__hash = texto

a1 = Credencial()
a1.chave = str(input("Insira a sua senha: "))
print(a1.chave)
a1.validar(str(input("Insira a senha, tentativa: ")))
