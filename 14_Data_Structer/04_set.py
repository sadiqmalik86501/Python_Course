set_1={1,2,3,4,5}
print(set_1,type(set_1))
#print(set_1[0]) you are not allowed to do somethings like this 

set_1.add(6)
print(set_1)
set_1.add(11)
print(set_1)
set_1.remove(2)
print(set_1)
set_1.remove(11)
print(set_1)
set_1.discard(111223)
print(set_1)
set_1.discard(1)
print(set_1)
set_1.pop()
print(set_1)
set_1.pop()
print(set_1)

a={1,2,3,4,5}
b={30,21,23,4,43,2}
c=a.union(b)
print(c)
d=a.intersection(b)
print(d)

dif=a.difference(b)
print(dif)