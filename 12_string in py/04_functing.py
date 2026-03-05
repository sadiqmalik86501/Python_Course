name="sadiQ,MaliK" # String are immutable 

# name_1=name[0]="Q" # You Can Not Do This 
# print(name_1)

# a=len(name)
# print(a)

# print(name.upper(),name)
# print(name.lower(),name)
# print(name.capitalize(),name)
# print(name.title())

# REmoving Whitespace
print(name.strip())
print(name.lstrip())
print(name.rstrip())

#find And Replace
print(name.find("M"))
print(name.find("K"))
print(name.find(" "))
print(name.replace("s","S"))
print(name.replace("Q","q"))
print(name.replace("K","k"))

# Split And Joining
print(name.split(","))
print(name.split(","))
print(",".join(["sadiQ","MaliK"]))

print(ord("A"))
print(ord("a"))
print(ord("b"))
print(ord("B"))
print(chr(66))
print(chr(101))