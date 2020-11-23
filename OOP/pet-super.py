#SUPER
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I dont know what i say")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self. color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and i am {self.age} years old and i am {self.color}")
class Dog(Pet):
    def speak(self):
        print("Bark")

p = Pet("TIm", 19)
p.speak()
c = Cat("Bill", 34, "Brown")
c.show()
c.speak()
d = Dog("Jill", 25)
d.speak()