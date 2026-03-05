class Points:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def sum(self,p):
        return Points((self.x+p.x),(self.y+p.y))
    
    def print_point(self):
        print(f"X is {self.x} an Y is {self.y}")

    def __add__(self, p):
        return Points((self.x+p.x),(self.y+p.y))
        
p1=Points(3,8)
p2=Points(9,10)

# p=p1.sum(p2)

p=p1+p2
p.print_point()