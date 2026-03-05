# 1-Write a function greet() that prints "Hello, Python Learner!" when called.
def greet():
    return "Hello Python Learner"
print(greet())

#2-Write a function square(num) that returns the square of a given number. Test it with different numbers.

def square(x):
    return x*x
print(square(6))


#3- Write a function full_name(first, last) that takes first name and last name as parameters and returns a single string in the format "First Last".
def full_name(first,last):
    return f"{first} {last}"
print(full_name("John","MaliK"))

#4- Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:
# Both length and width
# Only length (use default width)

def calculate_area(length,width=10):
    return length*width
print(calculate_area(13,20))

#4-Write a lambda function that adds two numbers and test it.
add=lambda x,y:x+y
print(add(10,11))

#5-Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares.

list1=[1,2,3,4,5]
squ=lambda x: x*x
print(list(map(squ,list1)))

list_1=[1,2,3,4,5]
squ=list(map(lambda x:x*x,list_1))
print(squ)


#6- Write a recursive function factorial(n) that returns the factorial of a number.
def factorial(n):
    if n==1:
        return n
    return n*factorial(n-1)
print(factorial(5))

#7-Write a recursive function sum_of_digits(n) that returns the sum of all digits of a given number.

def sum_of_number(n):
    if n==0:
        return 0
    return n%10+sum_of_number(n/10)
print(sum_of_number(101121202))

#8-Find the square root of 144
import math
print(math.sqrt((144)))
print(math.sin(0))
print(math.sin(90))

#9-Install and import the requests module (if available) and use it to fetch data from "https://api.github.com
# import requests
# response=requests.get("https://api.github.com")
# print(response.text)

#10-Write a recursive function fibonacci(n) that prints the first n Fibonacci numbers
def fibonacci(n):
    if (n==0 or n==1):
        return n
    return fibonacci(n-2)+fibonacci(n-1)
print(fibonacci(9))

#11-Write a function safe_divide(a, b) that returns the result of a / b, but returns "Cannot divide by zero" if b is 0
def safe_divide(a,b):
    if b!=0:
        return b
    return a+b
print(safe_divide(10,0))


#12-Write a function increment() that has a local variable counter initialized to 0 and increments it by 1 each time it is called. Observe whether the value persists across function calls.
def increment():
    counter=0
    counter+=1
    print(counter)
increment()
increment()
increment()






#13-Create a small module my_utils.py with a function is_even(n) that returns True if n is even. Import and use it in another Python file.

def is_even(n):
    if n%2==0:
        return "Even"
    return "Odd"
print(is_even(11))