import requests
import json

query=input("What Type Of News Are You Interested in today:")
api_key="32adac173c414afeb553719e546d96c4"

url=f"https://newsapi.org/v2/everything?q={query}&from=2026-02-05&sortBy=publishedAt&apiKey={api_key}"

print(url)
r=requests.get(url)
data=r.json()
articles=data['articles']
# print(articles) 


for index,article in enumerate(articles):
    print(index+1,article["title"],article["url"])
    print("\n***********************************\n")


with open("news.json","w",encoding="utf-8") as f:
    data_1=json.dump(data,f,ensure_ascii=False,indent=4)
    print(data_1)

