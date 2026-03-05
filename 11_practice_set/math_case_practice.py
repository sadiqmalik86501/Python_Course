#Write a program using match case that simulates a simple calculator.Ask the user for two numbers and an operation (+, -, *, /).
num_1=int(input("Enter a Number:"))
opr=input("Enter  A Opr:")
num_2=int(input("Enter A Number:"))

match opr:
        case "+":
            print(num_1+num_2)
        case "-":
            print(num_1-num_2)
        case "*":
            print(num_1*num_2)
        case "/":
            print(num_1/num_2)
        case "//":
            print(num_1//num_2)
        case _:
            print("Enter valid Number:")   


#Ask the user to enter a day number (1–7) and print the corresponding day of the week using match case.
day=input("Enter A day:")
match day:
        case "Sunday":
          print("Today is Sunday:")
        case "Monday":
          print("Today is Monday:")
        case "Tuesday":
          print("Today is tuesday:")
        case "Wednesday":
            print("Today is Wednesday:")
        case "Friday":
            print("Today is Friday:")
        case "Sunday":
            print("Today is Sunday")
        case _:
                print("Enter Valid Input")