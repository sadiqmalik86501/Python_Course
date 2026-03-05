# while True:
#     try:    
int_1=int(input("Enter A Number:"))
int_2=int(input("Enter A Number:"))
# print(int_1/int_2)
    # except  ZeroDivisionError as e:
    #     print(f"error {e}")
    
    # except ValueError as e:
    #     print("Please Don't Perform Bad Typecasts")

    # except Exception as e:
    #     print(f"Unknown Error:{e}")

if int_2==0:
    raise ValueError("Please Dont divide by 0")
print(int_1/int_2)