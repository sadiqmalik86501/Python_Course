# 1.Create a string variable name with your full name. Print:

# The first character
# The last character
# The length of the string
name="SadiQ"
print(name[0])
print(name[-1])
print(len(name))

var="hello \nWorld"
print(var)

#2.Concatenate two strings: "Hello" and "World" with a space in between.
str_1="Hello"
str_2="World"
print(str_1+str_2)

#3.Given text = "Python Programming", do the following:

# Print the first 6 characters
# Print the last 6 characters
# Print every second character from the string
text="python Programming"
print(text[0:6])
print(text[6:-6])
print(text[1::2])
print(text[::-1])

#4. Take the string "  i love python programming  " and:

# Remove extra spaces from both ends
# Convert it to title case
# Count how many times "o" appears

str_2=" i love python programming "
print(str_2.strip())
print(str_2.rstrip())
print(str_2.lstrip())
print(str_2.title())
print(str_1.count("o"))

#5.Check if the string "123abc" is alphanumeric.
var_1="123abc"
if str_1.isalpha():
    print("yes this is string:")
else:
    print("False")

#6.Using format(), create a sentence:
# "My name is John and I am 25 years old."
# by passing "John" and 25 as variables.
name="sadiQ"
Age=18
print(f"My Name Is {name} MaliK and I am {Age} Year Old")

#5. String Manipulation Challenges
# Given sentence = "Coding in Python is fun", replace "fun" with "awesome" and print it.
# Find the index of the word "Python" in sentence.
# Convert the entire sentence to uppercase and print it.

sentence="Coding In Python is fun"
print(sentence.replace("fun","Awesome"))
print(sentence.find("Python"))
print(sentence.upper())

# Write a program that counts how many vowels are in a given string.
sent="coding in python is fun"
sum=0
vowels=["a","e","i","o","u"]

for char in sent:
    print(char)
    if char in vowels:
        sum+=1
print(f"Total Vowels of {sum}:")

# Take a user input string and check if it is a palindrome (same forwards and backwards).

str_5="1234"
if str_5==str_5[::-1]:
    print(f"String Is palindrome :")
else:
    print("This is Not palindrome")