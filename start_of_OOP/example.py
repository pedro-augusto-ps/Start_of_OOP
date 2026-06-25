class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello my name is {carlos.name} and my age is {carlos.age}")

carlos = Person("carlos", 999)

carlos.greet()