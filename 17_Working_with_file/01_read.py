# Read To A File Called Sa.txt
# It should contain data about sa.txt

f=open("sa.txt","r")

content=f.read()


print(content)

f.close()

try:
    f=open("sad.txt","r") # Open In Read Mode 

    file=f.read() # Read the entire file content

    print(file) #Close The File 

    f.close()
except Exception as e:
    print(f"File not Found:{e}")

# Reding Line By Line
try:
    file=open("sa.txt","r")
    for line in file: # Efficient For Large File
        print(line.strip()) # Remove Newline characters
    f.close() # Close The File
except Exception as e:
    print("File Not Found")