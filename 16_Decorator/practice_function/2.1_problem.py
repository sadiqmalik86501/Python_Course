# Create a class Employee with a private attribute _salary.

# Use @property to define a getter for salary.
# Use @salary.setter to prevent setting negative values (print a warning instead).
# Create an object and test by setting positive and negative salaries.

class Employee:
    def __init__(self,salary):
        self._salary=salary
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self,value):
        if value<0:
            print("Hey Do Not Set a Negative Value for salary")     
        else:
            self._salary=value
        return value
        
e=Employee(3)
e.salary=9090898
print(e.salary) 
