marks=[10,12,322,33,23,323,23]
# print(marks[::-1])
print(marks)
marks.append(10)
print(marks)
marks.append(1000)
print(marks)

marks.insert(4,99)
print(marks)
marks.insert(1,0)
print(marks)


marks.remove(1000)
print(marks)
marks.remove(10)
print(marks)


marks.pop()
print(marks)
marks.pop(2)
print(marks)

marks.sort()
print(marks)


marks.reverse()
print(marks)
marks.clear()
print(marks)

extra_list=[10,12,12,13]
marks.extend(extra_list)
print(marks)