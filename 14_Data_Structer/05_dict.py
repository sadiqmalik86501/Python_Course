marks={"sadiQ":32,"AmaN":40,"AyaN":32}
print(marks,type(marks))

print(marks["sadiQ"])
marks["AyaN"]=90
print(marks)

print(marks.keys())
print(marks.values())
print(marks.items())
marks.pop("sadiQ")
print(marks)

marks.clear()
print(marks)

s={x:x**2 for x in range(7)}
print(s)

table={i:i*5 for i in range(1,11)}
print(table)