# for i in range(1,9):
#     print(i,end=",")# Range Function Goes From 1 to (9-1) ie 8 in this case 
# print()
# numbers=[]
# for i in range(1,11):
#     numbers.append(i)
#     numbers.remove(i)
# print(numbers)



for i in range(1,11):
    print(f"{2}x{i}={i*2}")

for i in range(1,11):
    print(f"{i}X{i}={i*i}")

for i in range(1,11):
    if i%2==0:
        print(f"{i} is Even")
        
    else:
        print(f"{i} is odd")