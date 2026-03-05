# number=[1,2,3,4,5,6,7,8,9,10]
# add_1=list(map(lambda x:x+2 ,number))
# print(add_1)

# num_1=[1,2,3,4,5,6,7,8,9,10]
# num_2=[10,9,8,7,6,5,4,3,2,1]
# add_2=list(map(lambda x,y:x+y,num_1,num_2))
# print(add_2)

# for_1=[x**2 for x in number]
# print(for_1)



# numbers = [1, 2, 3, 4, 5, 6]

# # Get even numbers using filter
# even_numbers = filter(lambda x: x % 2 == 0, numbers)
# print(list(even_numbers))  # Output: [2, 4, 6]

# # Equivalent list comprehension:
# even_numbers_lc = [x for x in numbers if x % 2 == 0]
# print(even_numbers_lc) # Output: [2, 4, 6]

# # Example with None as function
# values = [0, 1, [], "hello", "", None, True, False]
# truthy_values = filter(None, values)
# # print(list(truthy_values)) # Output: [1, 'hello', True]




# from functools import reduce

# numbers = [1, 2, 3, 4, 5]

# # Calculate the sum of all numbers using reduce
# sum_of_numbers = reduce(lambda x, y: x + y, numbers)
# print(sum_of_numbers)  # Output: 15

# # Calculate the product of all numbers using reduce
# product_of_numbers = reduce(lambda x, y: x * y, numbers)
# print(product_of_numbers)  # Output: 120

# #reduce with initializer
# empty_list_sum = reduce(lambda x,y: x+y, [], 0)
# print(empty_list_sum) # 0

# # Without the initializer:
# # empty_list_sum = reduce(lambda x,y: x+y, []) # raises TypeError

# # Equivalent using a loop (for sum):
# total = 0
# for x in numbers:
#     total += x
# print(total)  # 15




def squ(x):
    return x*x
number=[1,1,2,3,4,5,6,7,8,9,10]
nwe=list(map(squ,number))
print(nwe)


def is_greater_then_9(x):
    if x>9:
        return True
    else:
        return False
num_1=[10,22,1,12,133,4,5,649,4]
new=list(filter(is_greater_then_9,num_1))
print(new)


from functools import reduce
num_1=[1,2,3,4,5,6,7,8,9]
def sum(a,b):
    return a+b
c=reduce(sum,num_1)
print(c)