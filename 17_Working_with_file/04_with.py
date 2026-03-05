# Using with statement (recommended):

# The with statement provides a cleaner way to work with files. It automatically closes the file, even if errors occur.

with open("sa.txt","r",encoding="utf-8") as f: # This is Context Manager 
    content=f.read()
    print(content)
    #No Need to write f.close() Because file is already closed by default when using with syntax