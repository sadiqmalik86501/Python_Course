files=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
tasks=[]
def files():
    for file in files:
        try:
            if file==1:
                task=int(input("Enter A Number:"))
                tasks.append(task)
            if file==2:
                task=int(input("Enter A Number:"))
                tasks.append(task)
            if file==3:
                task=int(input("Enter A Number:"))
                tasks.append(task)
            if file ==4:
                task=int(input("Enter A Number:"))
                tasks.append(task)
            if file==5:
                task=int(input("Enter A Number:"))
                tasks.append(task)
            if file==6:
                task=int(input("Enter A Number:"))
                tasks.append(task)
            if file==31:
                continue
            if file==7:
                task=int(input("Enter A Number:"))
                tasks.append(task)
            if file==8:
                task=int(input("Enter A Number:"))
                tasks.append(task)
            if file==9:
                task=int(input("Enter A Number:"))
                tasks.append(task)
            if file==10:
                task=int(input("Enter A Number:"))
                tasks.append(task)
            if file==11:
                task=int(input("Enter A Number:"))
                tasks.append(task)
            if file==12:
                task=int(input("Enter A Number:"))
                tasks.append(task)
            if file==13:
                task=int(input("Enter A Number:"))
                tasks.append(task)
            if file==14:
                task=int(input("Enter A Number:"))
                tasks.append(task)
            if file==15:
                task=int(input("Enter  A Number:"))
                tasks.append(task)
            if file==16:
                task=int(input("Enter A Number:"))
                tasks.append(task)
            if file==17:
                task=int(input("Enter A Number:"))
                tasks.append(task)
            if file==18:
                task=int(input("Enter A Number:"))
                tasks.append(task)
            elif file==19:
                task=int(input("Enter A Number:"))
                tasks.append(task)
            elif file==20:
                task=int(input("Enter A Number:"))
                tasks.append(task)
            elif file==21:
                task=int(input("Enter A Number:"))
                tasks.append(task)
            elif file==22:
                task=int(input("Enter A Number:"))
                tasks.append(task)
            elif file==23:
                task=int(input("Enter A Number:"))
                tasks.append(task)
            elif file==24:
                task=int(input("Enter A NUmber:"))
                tasks.append(task)
            elif file==25:
                task=int(input("Enter A Number:"))
                tasks.append(task)
            elif file==26:
                task=int(input("Enter A Number:"))
                tasks.append(task)
            elif file==27:
                task=int(input("Enter A Number:"))
                tasks.append(task)
            elif file==28:
                task=int(input("Enter A Number:"))
                tasks.append(task)
            elif file==29:
                task=int(input("Enter A Number:"))
                tasks.append(task)
            elif file==30:
                task=int(input("Enter A NUmber:"))
                tasks.append(task)
            elif file==31:
                print("Compleat Your Code:")
            break
        except Exception as e:
            print(f"Error of {e}")
    print(files)
    print(tasks)
files()


def do_list():
    tasks=[]
    while True:
        print("1.Hello")
        print("2.How Are You?")
        print("3.I am Good")
        print("4.And You?")

        num_1=int(input("Enter A Number:"))

        if num_1==1:
            task=input("Enter A Task:")
            tasks.append(task)
        if num_1==2:
            task=input("Enter A Task:")
            tasks.append(task)
        if num_1==3:
            task=input("Enter A Task:")
            tasks.append(task)
        if num_1==4:
            task=input("Enter A Task:")
            tasks.append(task)
        if num_1==5:
            task=input("Enter A Task:")
            tasks.append(task)
        if num_1==6:
            task=input("Enter A Task:")
            tasks.append(task)
        if num_1==7:
            task=input("Enter A Task:")
            tasks.append(task)
        if num_1==8:
            task=input("Enter A Task:")
            tasks.append(task)
        if num_1==9:
            task=input("Enter A Task:")
            tasks.append(task)
        if num_1==10:
            task=input("Enter A Task:")
            tasks.append(task)
        if num_1==11:
            task=input("Enter A Task:")
            if task in tasks:
                tasks.remove(task)
            else:
                print("Error")
        if num_1==12:
            task=input("Enter A Task:")
            if task in tasks:
                tasks.remove(task)
            else:
                print("Invalid!")
        if num_1==13:
            task=input("Enter A Task:")
            if task in tasks:
                tasks.remove(task)
            else:
                print("Invalid_1!")
        if num_1==14:
            task=input("Enter A Task:")
            if task in tasks:
                tasks.append(task)
            else:
                print("invalid_2")
        if num_1==15:
            task=input("Enter A Task:")
            if task in tasks:
                tasks.remove(task)
            else:
                print("Invalid_3")
        if num_1==16:
            task=input("Enter A Task:")
            if task in tasks:
                tasks.remove(task)
            else:
                print("Invalid_4")
        if num_1==17:
            task=input("Enter A Task:")
            if task in tasks:
                tasks.remove(task)
            else:
                print("Invalid_5")
        if num_1==18:
            task=input("Enter A Task:")
            if task in tasks:
                tasks.remove(task)
            else:
                print("Invalid_6")
        if num_1==19:
            task=input("Enter A Task:")
            if task in tasks:
                tasks.remove(task)
            else:
                print("Invalid_7")
        if num_1==20:
            task=input("Enter A Task:")
            if task in tasks:
                tasks.remove(task)
            else:
                print("Invalid_8")
        if num_1==21:
            print("Task!")
            for task in tasks:
                print("_"+task)
        if num_1==22:
            print("Compleat Your Code:")
            break
do_list()