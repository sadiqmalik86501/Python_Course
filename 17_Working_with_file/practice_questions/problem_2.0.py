# Write a program that writes three lines of text to a file tasks.txt.
with open("tasks.txt","w",encoding="utf-8") as f:
    f.write("line 1\n")
    f.write("Line 2\n")
    f.write("line 3\n")