# 3. Simple Inheritance
# Create a base class Animal with a method sound() that prints "Some sound".
# Create a derived class Dog that overrides sound() to print "Bark!".
# Create an object of Dog and call sound().


class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
       print("Hello")
class Dog(Animal):
    def speak(self):
        print("woof")
class Cat(Animal):
    def speak(self):
       print("Meow")

c=Dog("Buleow")
d=Cat("Ladli")
print(c.name)
print(d.name)
c.speak()
d.speak()
        