def marks(**kwargs):
    for item in kwargs.keys():
        print(f"The Marks of {item} is {kwargs[item]}")

marks(Sadiq=70,aman=20,ayan=30,saniya=90)