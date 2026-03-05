x=10
def sum():
    global x
    x=5 # Modifies The Global x

sum()
print(x)

def sum(a,b):
    print("hey I Am SadiQ")
    c=a+b
    global z #This Is The Modify global z
    z=0
    return c
z=9
print(sum(10,23))
print(z)
