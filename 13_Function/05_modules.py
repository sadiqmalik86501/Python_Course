#Two Type Of Modules in Python
#1- Build in modules
#2-External Modules
import math
import os 
import requests
import mymodule
print(math.sqrt(10))
print(mymodule.hell())
r=requests.get("https://api.github.com")
print(r.text)