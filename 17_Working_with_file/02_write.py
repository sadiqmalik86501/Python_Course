# Write To A File Called SadiK.txt
# It should contain data about sadiK.txt

f=open("sadiK.txt","w") 

content=f.write("Hello Brothers")

print(content)

f.close()