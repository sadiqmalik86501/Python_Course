def sum(a,b):
    # a And b Local Variables
    c=a+b
    z=1# it creates a local variable called z which is destroyed after this function returns
    print(f"This Is local variable {z}")
    return c

z=8 # Z is A Global function
print(f"This Is Global function:{z}")
sum_1=sum(10,12)
print(f"This Is Sum Of Local variable {sum_1}")