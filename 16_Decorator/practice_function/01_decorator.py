# Decorator is a Function that Take a Function , it create a new function inside its body(wrapper).then it return that new function 
def my_decorator(func):
    def wrapper():
        print("Something is Before The Function is Called!")
        func()
        print("Something is  After The Function Is Called!")
    return wrapper
@my_decorator
def say_hello():
    print("Hello!!")
say_hello()

def decorator(func):
    def fun():
        print("This will before the Function is called!")
        func()
        print("this will after the function will called!")
    return fun
@decorator
def say_hii():
    print("Hello!!")
say_hii()