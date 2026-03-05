import os 

file=os.listdir("dir") # Listdir is a directory
print(file)
print(os.getcwd())
print(os.path.exists("dir"))# it's will return true when file exit otherwise this will return false 
#print(os.remove("SadiK.txt")) # Os.remove only works for deleting file ,not Directories
print(os.rmdir("dir"))