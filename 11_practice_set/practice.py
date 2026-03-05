#1. If-Else Conditional Statements

#1.Write a program that asks the user for a number and prints whether it is positive, negative, or zero.
from ast import While


try:
    num_1=int(input("Enter A Number:"))
    if num_1>0:
        print("This Number Is Positive:")
    elif num_1<0:
        print("This Number Is Negative:")
    elif num_1==0:
        print("This Number is Zero:")
    else:
        print("Valid Number")
except ValueError:
    print("Please Enter A Valid Input:")


#2.Create a program that checks if a person is eligible to vote (age >= 18).
try:
    age=int(input("Enter Your Age:"))
    if age>=18:
        print("You Are Eligible To Vote:")
    else:
        print("Your Are Not Eligible To Vote:")
except ValueError:
    print("Please Enter A Valid Number:")

#3.Write a program that takes a number from the user and prints "Even" if it is even, otherwise "Odd".\\
try:
    number=int(input("Enter A Number:"))
    if number%2==0:
        print("This Number Is Even:")
    else:
        print("This Number Is Odd:")
except ValueError:
    print("This Input Is Not Valid:")



#3. For Loops Question

#1.Print numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print(i,end=",")
print()

#2.Print the multiplication table of a number (entered by user).
for i in range(1,11):
    print(f"{5}X{i}={i*5}")

#3.Calculate the sum of all numbers from 1 to 100 using a for loop.
num_sum=int(input("Enter A NUmber:"))
sum_1=0
for i in range(1,num_sum+1):
    sum_1+=i
    print(sum_1)

num_1=int(input("Enter A Number:"))
sum_1=num_1*(num_1+1)//2
print(sum_1)


#4.Print the following pattern using a for loop:
for i in range(1,5):
     print("*"*i)


#4. While Loops
#1.Print numbers from 1 to 10 using a while loop.

num=1
while num<11:
    print(num)
    num+=1

#2.Write a program that keeps asking the user to enter a password until they enter the correct one.

pass_1=123
password=int(input("Enter Your Pass:"))
while pass_1:
    if password==123:
        print("Correct Pass:")
        break  
    else:
        print("Incorrect Pass:")
        break

#3.Use a while loop to reverse a given number (e.g., 123 → 321).
num_1=123
while num_1>0:
    rem=num_1%10
    num_1=num_1//10
    print(rem,end="")
print()

# #4.Use a while loop to reverse a given number (e.g., 100 → 001).
num_1=100
while num_1>0:
    rem=num_1%10
    num_1=num_1//10
    print(rem,end="")

print()
#5.3.Use a while loop to reverse a given number (e.g., 99000 → 00099).
num_1=int(input("Enter A Number:"))
while num_1>0:
    ram=num_1%10
    num_1=num_1//10
    print(ram,end="")

# print()
# ## 5.Break, Continue, and Pass Statements

# #1.Use a for loop to print numbers from 1 to 10, but stop the loop if the number is 7
for i in range(1,11):
    if i==7:
        break
    print(i)
print()
# #2.Use a for loop to print numbers from 1 to 100, but stop the loop if the number is 50

# for i in range(1,101):
#     if i==50:
#         break
#     print(i)
print()
#3.Print numbers from 1 to 10, skipping the number 5 (use continue).

for i in range(1,10):
    if i==5:
        continue
    print(i)
print()
#3.Print numbers from 1 to 10, skipping the number 5 (use continue).
for i in range(1,20):
    if i==10:
        continue
    print(i)
print()
#4.Write a loop that goes through numbers 1 to 5, but does nothing for number 3

for i in range(1,5):
    if i==3:
        pass
    print(i)
print()

#5.Write a loop that goes through numbers 1 to 10, but does nothing for number 8

for i in range(1,11):
    if i==8:
        pass
    print(i)
