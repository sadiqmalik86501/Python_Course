# Open notes.txt, read its content, and print it to the console.

file=open("note.txt","r",encoding="utf-8")
content=file.read()
print(content)
file.close()

#Second Type
with open("note.txt","r",encoding="utf-8") as f:
    content=f.read()
    print(content)
    