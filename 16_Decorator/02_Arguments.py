def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator

@repeat(3)
def greet(a):
    print(f"Hello,{a}")
greet("Sadiq")

print()
def repeat(n):
    def decorator(func):
        def fun(a):
            for i in range(n):
                func(a)
        return fun
    return decorator
@repeat(7)
def say_hello(name):
    print(f"Hello!!,{name}")
say_hello("World")
 