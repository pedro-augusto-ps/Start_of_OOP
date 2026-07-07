class Avaliacao:
    def __init__(self, nome, disciplina, nota):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota       #Atributo protegido(#)

    def get_nota(self):         #Método GETTER
        return self._nota

    def set_nota(self, valor):  #Método SETTER
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print("Nota inválida")