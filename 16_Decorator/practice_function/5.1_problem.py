# Write a program that asks the user to enter a number and handles:

# ValueError if the input is not a number
# ZeroDivisionError if you try to divide by zero
try:
    num_1=int(input("Enter A Number:"))
    num_2=int(input("Enter A Number:"))
    print(num_1/num_2)
    if num_2==0:
        print("Ok")
except ValueError as e:
    print("This is Not  a Number")

except ZeroDivisionError :
    print("Zero division Error:")



    
class NegativeNumberError(Exception):
      pass

try:

    num_3=int(input("Enter A Number:"))
    if num_3<0:
            raise NegativeNumberError("Number Can Not Be Negative")
    else:
          print(num_3)
except Exception as e:
      print(e)
        