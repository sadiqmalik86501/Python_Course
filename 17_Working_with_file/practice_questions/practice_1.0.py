# Create a text file notes.txt using Python and write "Learning Python is fun!" into it.

file=open("note.txt","w",encoding="utf-8")
string="Learning Python is fun!"
content=file.write(string)
file.close()