# # Write a decorator logger that prints "Function is being called" before the function runs. Use it to decorate a function say_hello() that prints "Hello!".

# def logger(func):
#     def wrapper():
#         print("Function is being called:")
#         func()
#     return wrapper()
# @logger
# def say_hello():
#     print("Hello")
# print()

def logger_1(func_1):
    def wrapper():
        print("Hello Guys How Are You \ni am fine\nand you \ni am too good\nwhat are you doing right now ")
        func_1()
    return wrapper()
@logger_1
def say_hello():
    print("Hello!!!")