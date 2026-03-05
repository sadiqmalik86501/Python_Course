class Employee:
    company="HP"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary


    def print_info(self):
        return f"The Name Is {self.name} And The Salary is {self.salary}"
    
    @staticmethod
    def sum(a,b):
        return a+b
    
    @classmethod
    def print_class(cls):
        print(cls.company)

    @classmethod
    def change_company(cls,new_company):
        cls.company=new_company

    

e1=Employee("Jack",30000000)
e2=Employee("Jill",200000000)



print(e1.print_info())

print(e2.print_info())
print(e2.sum(10,12))

e1.change_company("Cisco")
print(Employee.company)