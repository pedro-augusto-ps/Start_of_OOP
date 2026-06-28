class Bear:
    species = "Ursus"
    def __init__(self, name, age, color, weight): #atributos
        
        self.name = name
        self.age = age
        self.color = color
        self.weight = weight

    def __str__(self):
        return f"Name:{self.name}\nAge: {self.age}\nColor: {self.color}\nWeight: {self.weight}"
    
    def comer(self):
        self.weight += 10
        

bear1 = Bear("Polar", 10, "White", 200)  #Instancia, criação do objeto
print(f"Bear 1: {bear1}")
print(bear1.name)
print(bear1.age)    #print o objeto bear1 e nao a classe Bear
print(bear1.weight)
print(bear1.color)
print(Bear.species)
print(bear1.species)
