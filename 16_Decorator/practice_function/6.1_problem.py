# Use map() to convert [1, 2, 3, 4, 5] into their cubes.
num = [1, 2, 3, 4, 5]
cube=list(map(lambda x:x*3,num))
print(cube)

# Use filter() to get only even numbers from [10, 11, 12, 13, 14].

num_1=[10, 11, 12, 13, 14]
even=list(filter(lambda x:x%2==0,num_1))
print(even)

# Use reduce() from functools to find the product of all elements in [1, 2, 3, 4].

from functools import reduce
l=[1,2,3,4]
num_3=reduce(lambda x,y: x*y,l)
print(num_3)