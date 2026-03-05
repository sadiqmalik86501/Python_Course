# 2. Constructor and Attributes
# Create a class Person with a constructor (__init__) that accepts name and age as arguments and stores them as instance attributes.
# Create an object and print the person’s name and age.

class Employee:
    def __init__(self,Name,Salary,Bond):
        self.Name=Name
        self.Salary=Salary
        self.Bond=Bond

    def get_salary(self):
        return 30000
    def get_info(self):
        print(f"Your Name is {self.Name} and Your Salary is {self.Salary} and your Bond {self.Bond} Years")

e=Employee(300000,"SadiK",5)
e.get_info()