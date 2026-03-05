# Regular Expressions in Python

# Regular expressions (regex) are powerful tools for pattern matching in strings. Python's re module provides support for regex.

import re 

text="The Quick Brown Jump Over The Lazy dog"

# Search For A Pattern 

match=re.search("brown",text)
print(match)
if match:
    print("Not found!")
    print("Start Index:",match.start())
    print("End Index:",match.end())
# Find All Occurrences Of A Pattern 
matches=re.findall("The",text,re.IGNORECASE) # Case Insensitive Search
print(matches)

#Replace Pattern 
new_text=re.sub("The","This",text)
print(new_text)

# Compile a regex for efficiency (if Used Multiple Time)
pattern=re.compile(r"\b\w+\b")
words=pattern.findall(text)
print(words)