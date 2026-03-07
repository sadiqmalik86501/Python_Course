import requests

messages=[]

def Ai_Chat_Bot(message):
    global messages

    messages.append({
        "role":"user",
        "content":message
    })

    r=requests.post("http://localhost:11434/api/chat",
                    json={
                        "model":"gemma3",
                        "messages":messages,
                        "stream":False
                    })
    response=r.json()["message"]["content"]

    message={
        "role":"assistant",
        "content":response,
        "images":"null"
    }

    messages.append(message)
    print(f"Jarvis:{response}")

if __name__=="__main__":
    print("Hello I am Jarvis: Can I  Help With You:")

    while True:
        question_query=input()
        if question_query=="":
            continue
        Ai_Chat_Bot(question_query)
        