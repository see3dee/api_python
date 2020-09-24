class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        print(f"{self.name} is {self.age} years old")

    def __repr__(self):
        print(f"{self.name} is {self.age} years old")


bob = Person("Bob", 35)

bob.__str__()
bob.__repr__()

