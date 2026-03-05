class Employee:
    def __init__(self,name,salary,age):
        self.name=name
        self.salary=salary
        self.age=age
    @property
    def first_name(self):
        l=self.name.split(" ")
        print(l)
        return l[0]
    
    def set_first_name(self,first):
        l=self.name.split(" ")
        new_name=f"{first} {l[1]}"
        self.name=new_name

e=Employee("Jack MaliQ",300000,29)
# print(e.first_name())
# e.set_first_name("Sadiq")
# print(e.name)

print(e.first_name)
e.set_first_name="SadiQ"
print(e.name)