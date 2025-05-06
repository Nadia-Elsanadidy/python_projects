class Human:
    def eat(self):
        print("Human eats with fork.")

class Mammal:
    def eat(self):
        print("Mammal eats naturally.")

class Employee(Human, Mammal):  # Human comes first
    pass




e = Employee()
e.eat()