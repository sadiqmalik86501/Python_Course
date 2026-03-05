class Employee:
    company="Hp"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    #String Representation
    def __str__(self):
        return f"Person({self.name},{self.salary})" #User Friendly
    def __repr__(self):
        return f"person(name={self.name},age={self.salary})" # Unambiguous for debugging 
    def __len__(self):
        return len(self.name)
    
p=Employee("Sadiq",300000000)
print(str(p))
print(repr(p))
print(p)
print(p.company)
print(len(p))


class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self, other):
                return Vector(self.x+other.x,self.y+other.y)
    def __sub__(self, other):
         return Vector(self.x-other.x,self.y-other.y)
    def __mul__(self, scalar):
         return Vector(self.x*scalar.x,self.y*scalar.y)
    def __str__(self):
         return f"Vector({self.x},{self.y})"
        
v1=Vector(4,10)
v2=Vector(10,4)
v3=v1.__add__(v2)# You Can  Call This(v1+v2)
print(v3)

v4=v1.__sub__(v2)# you can Call This(v1-v2)
print(v4)

v5=v1.__mul__(v2)# You Can Call This(v1*v1)
print(v5)


# Vector of 3 Variable
class Vector_3:
    def __init__(self,num_1,num_2):
        self.num_1=num_1
        self.num_2=num_2

    def __add__(self,adding):
         return Vector_3(self.num_1+adding.num_1,self.num_2+adding.num_2)
    
    def __sub__(self, sub):
            return Vector_3(self.num_1-sum.num_1,self.num_2-sub.num_2)         
    
    def __mul__(self, other):
         return Vector_3(self.num_1*other.num_1,self.num_2*other.num_2)
    
    def __eq__(self,number):
            return Vector_3(self.num_1==number.num_1,self.num_2==number.num_2)
    
    def __pow__(self, other):
         return Vector_3(self.num_1**other.num_2,self.num_2**other.num_2)
    
    def __str__(self):
         return f"(Vector_3={self.num_1},{self.num_2})"

v_1=Vector_3(100,122)
v_2=Vector_3(122,100)
v_3=v_1.__add__(v_2)
print(v_3)
v_4=v1.__sub__(v2)
print(v_4)
v_5=v1.__mul__(v2)
print(v_5)
v_6=v1.__eq__(v_2)
print(v_6)
v_7=v1**(v2)
print(v_7) 