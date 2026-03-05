class Employee:
    company="Asus"

    def __init__(self,name,salary,bond,company):
        self.name=name
        self.salary=salary
        self.bond=bond
        self.company=company
       
    
    def get_salary(self):
        return self.name
    def get_info(self):
        print(f"The name Of The employee is {self.name} .and salary is {self.salary} The Bond is for{self.bond} years and company name:{self.company}")
e=Employee(300000,"Sadik",4,"Tesla")
print(e.company)
print(Employee.company)

#Object introspection 
print(dir(e))