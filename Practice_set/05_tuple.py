# 3. Tuples and Operations on Tuples
# Create a tuple coordinates = (10, 20) and print both elements.

# Try to modify the tuple by setting coordinates[0] = 50 — note what happens.

# Convert the tuple to a list, change its first element to 50, and convert it back to a tuple.

tup_1=(10,20)
print(tup_1[0:])
print(type(tup_1))

# tup_1[0]=50
# print(tup_1)

tup_2=list(tup_1)
print(tup_2)
tup_2[0]=50
print(tup_2)
tup_3=tuple(tup_2)
print(tup_3)