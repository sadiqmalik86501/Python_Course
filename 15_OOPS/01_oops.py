# Class is a Blue Print or a template . e.g from for an exam that contains name,age,electives,father's name etc

# Object: Specific instance create from teh template (class) eg. from which contains the data for John Doe

class Employee: # We define a class called "Dog"
    company="HP"

    def get_salary(self):# Self Is Important hre self Because self is a way to reference the object of the Class which is being created 
        return 30000
    
e = Employee() # An Object of class employee is created here 
print(e.get_salary()) # Employee e's get salary method is called
print(e.company)

e1=Employee()
print(e1.get_salary())
print(e1.company)