# Create a class MathUtils with:

# A @staticmethod called add(a, b) that returns a + b.
# A @classmethod called description(cls) that prints "This is a utility class for math operations."

class Add:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    @staticmethod
    def sum(a,b):
        return a+b
    @classmethod
    def des(cls):

        print("This Is Unitaly class For Math Opr")
# a=Add
# print(a.sum(3,4))
# a.des()
Add.des()
print(Add.sum(10,11))