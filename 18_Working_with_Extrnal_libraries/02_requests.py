import requests 

r=requests.get('https://api.github.com/users/sadiqmalik86501')
print(r.text)

with open("sadiqmalik86501.txt","w",encoding="utf-8") as f:
    content=f.write(r.text)
    print(content)