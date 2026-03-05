class Animal:

    def __init__(self,name):
        self.name=name

    def speak(self):
        print("Generic animal sound:")
    
class Dog(Animal):
    def speak(self):
        print("Wolf")

class cat(Animal):
    def speak(self):
        print("Meow:")

my_dog=Dog("Rover")
my_dog=cat("fully")

print(my_dog.name)
print(my_dog.name)

my_dog.speak()
my_dog.speak()


class Car:
    location="Australia"
    def __init__(self,name):
        self.name=name
    def Model():
        print("Model Names")

class swift(Car):
    def model(self):
        print("Swift")

class Toyata(Car):
    def model(self):
        print("Fortuner")

my_car=swift("Swift_2026 Model")
my_car=Toyata("Toyata 2026 New Model")
print(my_car.name)
print(my_car.name)

my_car.model()
my_car.model()
print(my_car.location)