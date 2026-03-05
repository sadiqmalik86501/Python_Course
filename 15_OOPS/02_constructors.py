class Employee:

    def __init__(self,salary,name,bond):
        self.salary=salary # Create An Instance attribute 
        self.name=name
        self.bond=bond 

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f" The Name Of The Employee is {self.name}.\n salary is {self.salary}.\n The Bond is For {self.bond} Years")


obj=Employee(30000,"SadiQ",4)
obj.get_info()