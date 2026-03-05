def to_do_list():
    tasks=[]
    while True:
        print("1.Hello")
        print("2.SadiQ")
        print("3.MaliK")
        print("4.How Are You?")
        print("5.Fine") 

        result=int(input("Enter A Number"))

        if result==1:
            task=input("Enter Task:")
            tasks.append(task)
        if result==2:
            task=input("Enter A Task")
            if task in tasks:
                tasks.remove(task)
            else:
                print("Error")
        if result==3:
            print("Task")
            for task in tasks:
                print("__" + task)
        if result==4:
            print("Code Is Completed")
            break
        
to_do_list()

def add_fun():
    files=[]
    while True:
        print("1.Hello ")
        print("2.hii")
        try:    
            files=int(input("Enter A Number:"))

            if files==1:
                file=input("Enter A file:")
                files.append(file)
            if files==2:
                file=input("Enter A file :")
                files.append(file)
            if files==3:
                file=input("Enter A file :")
                files.append(file)
            elif files==4:
                file=input("Enter A file :")
                if file in files:
                    files.remove(file)
                else:
                    print("invalid ")
            elif files==5:
                file=input("Enter A file :")
                if file in files:
                    files.remove(file)
                else:
                    print("invalid :")
            elif files==6:
                file=input("Enter A file :")
                if file in files:
                    files.remove(file)
                else:
                    print("invalid :")
            elif files==7:
                print("Task")
                for file in files:
                    print("_" + file)
            elif files==8:
                print("Exit The Code:")
                break
        except Exception as e:
            print(f"Function Error {e}")

add_fun()
