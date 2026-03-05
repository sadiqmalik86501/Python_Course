def very_slow_fun():
    print("Something.......")
    print("Something.......")
    print("Something.......")
    print("Something.......")
    print("Something.......")
    print("Something.......")
    print("Something.......")
    print("Something.......")
    return 70

if ((a:=very_slow_fun())>10):
    print(a)
else:
    print("its Not Greater The 10")


while (data:=input("Enter The Value:")):
    print(data)
    if data=="b":
        break