num_1=int(input("Enter A Number:..."))
opr=input("Enter An Operation:..")
num_2=int(input("Enter A NUmber:..."))

try:
    if opr=="+":
        print(f"The Addition of {num_1}+{num_2}={num_1+num_2}")
    elif opr=="-":
        print(f"The Subtraction of {num_1}-{num_2}={num_1-num_2}")
    elif opr=="*":
        print(f"The Multiplication Of {num_1}*{num_2}={num_1*num_2}")
    elif opr=="/":
        print(f"The Division of {num_1}/{num_2}={num_1/num_2}")
    elif opr=="//":
        print(f"The Floor Division Of {num_1}//{num_2}={num_1//num_2}")
    elif opr=="%":
        print(f"The Modulus of {num_1}%{num_2}={num_1%num_2}")
    elif opr=="**":
        print(f"The Exponent of {num_1}**{num_2}={num_1**num_2}")
    else:
        print("Enter Valid Input:")
except ZeroDivisionError as e:
    print(f"ZeroDivisioonError:{e}")