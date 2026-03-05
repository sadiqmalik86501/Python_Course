# Create The List Containing the table of 10
n=10
table=[]
for i in range(1,11):
    table.append(10*i)
print(table)

for i in range(1,11):
    print(f"{10}x{i}-->{10*i}")

table=[5*i for i in range(1,11)]
print(table)