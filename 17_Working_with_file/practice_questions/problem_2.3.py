# Read the file and print all lines as a list using readlines().
try:
    file=open("tasks.txt","r",encoding="utf-8") 
    for line in file.readline():
        print(line)
except Exception as e:
    print(f"Error Of {e}")