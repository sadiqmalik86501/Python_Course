Physics=int(input("Enter your physics Number:"))
chemistry=int(input("Enter Chemistry Marks: "))
opr=input("Enter Your Opr:")
math=int(input("Enter Your Math Marks:"))
english=int(input("Enter Your English Marks:"))



def marks():
    try:
        if opr== "+":
            total_marks=chemistry+Physics+math+english
            print(f"Your Present is {total_marks/4}")
            if total_marks>90:
                print("You are Great:")
            elif total_marks>70:
                print("good Marks:")
            elif total_marks>50:
                print("I Think You Wan to Study:")
            elif total_marks==23:
                print("Final you are pass:")
            else:
                print("Your Are Fail")
    except Exception as e:
        print(f"Error Of {e}")        
marks()


#500 Rs. Fees Per Subject

def physics_fees():
    try:
        Physics_1=int(input("Do You Want Add Your  Fees of Physics:"))
        if Physics_1==500:
            print("your Fees Is Done Because Your Are Good Boy:")
        elif Physics_1==400:
                print("due 100Rs. Of Physics \n Please Fill Your Total Fees:")
        elif  Physics_1==300:
                print("Due 200 Rs. of Physics \n Please Fill Your Total Fees")
        else:
                print("Your Total Fee Due \n please Fill Your Total Fees;")
    except Exception as e:
        print(f"error Of{e}")
physics_fees()



def chemistry_fees():
    try:
        chemistry_fees=int(input("Do You Want Add Your Fees of Chemistry:"))
        if chemistry_fees==500:
                print("Your Total Fees Complected ")
        elif chemistry_fees==400:
              print("Due 100 Rs. fees of Chemistry\n Please Submit Your Total Fees:")
        elif chemistry_fees==300:
              print("Due 200 Rs. fees of Chemistry\n Please Submit Your Total Fees:")
        elif chemistry_fees==200:
              print("Due 300 Rs. fees of Chemistry\n Please Submit Your Total Fees:")
        else:
              print("Due Total  fees of Chemistry\n Please Submit Your Total Fees:")
    except Exception as e:
          print(f"Error of {e}")
chemistry_fees()

def math_fees():
    try:
        math_fees=int(input("Do Your Want Add Your Fees of Math:"))
        if math_fees==500:
            print("Your Total Fees Complected:")
        elif math_fees==400:
            print("Due 100 Rs. fees of Chemistry\n Please Submit Your Total Fees:")
        elif math_fees==300:
             print("Due 200 Rs. fees of Chemistry\n Please Submit Your Total Fees:")
        elif math_fees==200:
             print("Due 300 Rs. fees of Chemistry\n Please Submit Your Total Fees:")
        else:
             print("Due Total  fees of Chemistry\n Please Submit Your Total Fees:")
    except Exception as e:
         print(f"Error Of {e}")
math_fees()


def English_Fees():
    try:
        English_Fees=int(input("Wholud you like to  Add Your Fees of English:"))
        if English_Fees==500:
            print("Your Total Fees Complected:")
        elif English_Fees==400:
             print("Due 100 Rs. fees of Chemistry\n Please Submit Your Total Fees:")  
        elif English_Fees==300:
             print("Due 200 Rs. fees of Chemistry\n Please Submit Your Total Fees:")
        elif English_Fees==200:
             print("Due 300 Rs. fees of Chemistry\n Please Submit Your Total Fees:")
        else:
             print("Due Total  fees of Chemistry\n Please Submit Your Total Fees:")
    except Exception as e:
         print("Error Of {e}")
English_Fees()


