# #4. Sets and Set Methods
# Create a set my_set = {1, 2, 3, 3, 4} and print it. (What happens to duplicate 3?)

# Add 5 to the set, remove 2, and check if 4 is in the set.

# Create two sets:

# a = {1, 2, 3}

# b = {3, 4, 5}
# Find their:

# Union

# Intersection

# Difference (a - b)

my_set={1,2,3,3,4,5}
print(my_set)
my_set.add(6)
my_set.remove(2)
print(my_set)

if 4 in my_set:
    print("Yes")
else:
    print("No")

a={1,2,3}
b={3,2,1}
print(a,b)
c=a.union(b)
print(c)
d=a.intersection(b)
print(d)

e=a.difference(b)
print(e)